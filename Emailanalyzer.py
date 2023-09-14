import re
def matchre(data,*args):
    for regstr in args:
        matchObj = re.search( regstr+'.*', data, re.M|re.I)
        if matchObj:
            print(matchObj.group(0).lstrip().rstrip())
        else:
            print("No ",regstr,"found")
        
print("Email Header Program ")

fo = open("sample.eml", "r")
data=fo.read()
matchre(data,"MIME-version","Date:","Subject:","delivered-to:","From:","^to:")
fo.close()


