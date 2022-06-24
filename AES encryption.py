from Crypto.Cipher import AES
import hashlib, optparse

PARSER = optparse.OptionParser()
PARSER.add_option('--msg', metavar = 'Text you want to crypt', dest = 'TEXT', help = '')
OPT, ARG = PARSER.parse_args()

if not OPT.TEXT:
    print('\nPlease type "--help" or "-h" for informations about this program.\n')
    exit()

# Generating key ...
KEY = hashlib.sha256('EZG0m8LO6Q?L8ss(PTI?Fhznx?ig#iNGS17x#63PLlPFMRWICtBwANXYEkFra??Oirg?SHU383bgF!r#zZ2yfrj4jzf!OWNC6lRQNqfh(v4KSpQ1bB1xyb7OAz?1ehIH)LqQ6GKJiDhqrUnzth7?!gb(jbMPjUZqGGn6af3YgXoV1YulCrV!(h)dvEJsn(A?TbJPJ?Hsr9qCQ#x)b5kJyxy!cr7Wixgyz)x7bafeQjLzIyY!RfeEI?B)6oDVDmR8tSjjXFJ3mtUPiM#LOOuEOi7XyLCTZuOlWiAn4Ux7?mo0(UsFI)za#l91n6dzV3y81GEw3iJKwfXezocg0gnAAXTajGwRbQQM)wikUw!mjwGkaAZTT62cUdstAq)OQnjBd77Qg9TgUKI0C4OqW2qIPuQMSLgY5QvRR0ncwHvm(XWDVP?DWDQNZiPTimDs0oKXLoAUlnwEiJcz4DXbNLvTRLIUqoNm2bcDcpAWOaJy4y#(3wkwHMfzsar1AXuLAtA)9FzctyYM8YVaSH)?egiKWEvfyM(xCp!egmvCs69awDdRBKw0g!HT583gUhh1IMuGApZ)cXl4ChVaT5eKEAtEpYOpfM0rdF6?Q9ydouYvWc(avKbzBQEWqmhs?R55e1Y4DZ8AkWJmYTSSmGwgVboSi!Vf(oR6aTxONNlMbO9)eD0DHUh?XgVCJ!hWwHdmsK!A!8ZC0S1d5H14dC4hj4AnC(RXq8pBJJQc2BBXku7C)q(#C4CB8menp)sBEcZm8WyPF7pB0ESh82KPvjLOS7V?a#F(zor?Cm69I0egGiM5vEJTjMo9ZyBBd#yzp4YyNjUmT!o8uGMzCKPB#lypd7FMyCMuE6nc3UKFj48sLsz28#sBVXe4dnFqXEwKd6G?sjtJ)2KZgZiu!(9KgzOHXU!mIHxJ#W5l4)ULFOzB95MaHEkJQg7xMH0ZPgrhCGd0MFSEXufMQ5GulJIEvpL76mKdSyXjum1f8vM1G8p97BFU'.encode()).digest()

# Specifying Initialization Vector ...
IV = '!eTquJDexC3)(?0r'.encode()

# Assembling cipher ...
CIPHER = AES.new(KEY, AES.MODE_CBC, IV)
MSG = OPT.TEXT

# Adding bytes to the message before encryption ...
while not len(MSG) % 16 == 0:
    MSG += ' '

cMSG = CIPHER.encrypt(MSG.encode())

print('\n ENCRYPTED MESSAGE >  '+str(cMSG)+'\n')

# REMEMBER TO SPECIFY ANOTHER CIPHER FOR OTHER FUNCTION (enc > dec / dec > enc) !
CIPHER = AES.new(KEY, AES.MODE_CBC, IV)
dMSG = CIPHER.decrypt(cMSG)
print(' DECRYPTED MESSAGE >  '+str(dMSG),'\n')
