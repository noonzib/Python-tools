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

text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
for i in range(1,40):
    print str(i) + ","+"=>"+decoding(text,i)+" Key="+str(i)