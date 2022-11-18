
import requests
import json
from socket import socket
from OpenSSL import SSL
from OpenSSL.crypto import load_certificate
import idna
import os
import urllib
import ssl


def get_ssl_info(hostname):

    try:
        hostname_idna = idna.encode(hostname)
    except:
        return("unvalid_host_err")    

    sock = socket()
    sock.settimeout(10)
    port = 443
    
    try:
        sock.connect((hostname_idna, port))
    except:
        return "unvalid_url_err"    
    
    sock.settimeout(None)
    
    try:
        peername = sock.getpeername()
        ctx = SSL.Context(SSL.SSLv23_METHOD)
        ctx.check_hostname = False
        ctx.verify_mode = SSL.VERIFY_NONE

        sock_ssl = SSL.Connection(ctx, sock)
        sock_ssl.set_connect_state()
        sock_ssl.set_tlsext_host_name(hostname_idna)
        sock_ssl.do_handshake()
        cert = sock_ssl.get_peer_certificate()
        crypto_cert_chain = cert.to_cryptography()
        sock_ssl.close()
        sock.close() 
    except:    
        return("chain_err")    

    #  non decrypted certificate instance
    
    try: 
        conn = ssl.create_connection((hostname, port))
        context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
        sock0 = context.wrap_socket(conn, server_hostname=hostname)
        certificate = ssl.DER_cert_to_PEM_cert(sock0.getpeercert(True))
    except:
        return ("certificate_err")    

         # Date checker for extra information, currently in development
    # cert_query = 'openssl s_client -servername ' + hostname + ' -connect ' + hostname + ':' + str(443)  + ' 2> /dev/null | openssl x509 -noout -dates'
    # hostplusport = hostname + ":" + str(443)
    # try: 
    #     chain = os.popen(cert_query).read()
    # except: 
    #     print("certificate problem occured")
    #     return "outdated_certificate_err"

    return (crypto_cert_chain)


