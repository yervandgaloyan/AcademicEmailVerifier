import re
import os

def isEmailValid(email):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
            
    return True if re.fullmatch(regex, email) else False
    
def domainToUrl(domain):
    url = domain.split('.')
    url[0] += '.txt'
    url.reverse()
    url = '/'.join(url)
    
    return url

def isAcademic(email):
    this_dir = os.path.split(__file__)[0]
    DATA_PATH = os.path.join(this_dir, "domains/")
    domain = email.split('@')[-1]
    url = domainToUrl(domain)
    path = DATA_PATH + url
    return os.path.exists(path)
