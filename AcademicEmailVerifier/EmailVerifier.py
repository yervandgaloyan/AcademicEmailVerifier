import re
from os.path import exists
from os import getcwd

class EmailVerifier:
    
    def isEmailValid(self, email):
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
                
        return re.fullmatch(regex, email)
        
    def domainToUrl(self, domain):
        url = domain.split('.')
        url[0] += '.txt'
        url.reverse()
        url = '/'.join(url)
        
        return url
    
    def isAcademic(self, email):
        if not self.isEmailValid(email):
            return -1
        domain = email.split('@')[-1]
        url = self.domainToUrl(domain)
        path = getcwd() + '/domains/' + url
        return exists(path)
