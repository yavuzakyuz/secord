import searchexploits
import pscans as portscan
import getssl
import bs as drinksoup


def extract_arg(arg):
    return arg.split()[1:]


def searchsploit(message):
    try:
        result = []
        query=" ".join(message)
        info=searchexploits.searchsploit(query)
        count = 0
        for exploit in info:
            #print(message, exploit+": "+info[exploit]) !no need to involve! 
            result.append((message, exploit+": "+info[exploit]))
            count = count + 1
        return result     
    except:
        print(message, " error on searchsploit")



def scan_port(url):
    try:
        openedports= portscan.scan_ports_of(url)
        result = "\n".join(str(port) for port in openedports)
        if not result:
            return "can't find any open ports between the range 1 - 65535 (ipv4 max)"
        else: 
            return result    
    except:
        print("error on scan port")

def check_ssl(url):
    response = getssl.get_ssl_info(url)
    if (response == "unvalid_host_err" or response == "unvalid_url_err" or response == "chain_err" or response == "certificate_err"  ):
        print(response)
        return "err"
    else:
        return response

def fetch_webpage(url):    
    if(drinksoup.get_code(url) == "error"):
        return("error")
    else: 
        return("success")    



#scan_port("google.com")        