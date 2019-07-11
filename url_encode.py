import urllib
query1 = "&"
query2 = "#"
f = {'urlencode' : query1, 'password':query2}

print urllib.urlencode(f)