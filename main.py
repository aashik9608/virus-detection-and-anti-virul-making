fp= open('/content/eicar.txt','r')
fbuf= fp.read()
fp.close()
print(fbuf[0:3])

if (fbuf[0:3]=='X5O'):
    print('virus')
    os.remove('/content/eicar.txt')
else:
    print('No virus')
import os
import hashlib as hashlib

fp= open('/content/eicar.txt','r')
fbuf= fp.read()
fp.close()
# anti virul production
fbuf.encode(encoding='utf-8', errors='strict')
m = hashlib.md5()
m.update(b'X5O!P%@AP[4\\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*')
fmd5= m.hexdigest()
if fmd5 == '44d88612fea8a8f36de82e1278abb02f' :
    print ('Virus')
    os.remove('eicar.txt')
else :
    print('No Virus')
VirusDB = ['44d88612fea8a8f36de82e1278abb02f:EICAR TEST','77bff0b143e4840ae73d4582a8914a43:Dummy Test']
vdb = []
def MakeVirusDB() :
    for pattern in VirusDB :
        t = []
        v = pattern.split(':')
        t.append(v[0])
        t.append(v[1])
        vdb.append(t)
 VirusDB = ['68:44d88612fea8a8f36de82e1278abb02f:EICAR Test','65:77bff0b143e4840ae73d4582a8914a43:Dummy Test'
]
def LoadVirusDB() :
    fp = open('virus.db', 'rb')
    while True :
        line = fp.readline()
        if not line : break
        line = line.strip()
        Virus.append(line)
        fp.close()
