"""
Copyright 2022 Yervand Galoyan
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

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
        print(path)
        return exists(path)

if __name__ == "__main__":
    verifier = EmailVerifier()