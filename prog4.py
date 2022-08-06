pt = input().lower()
key = input().lower()
pt = [ord(a)-97 for a in pt]
key = [ord(a)-97 for a in key]

i=0
while(len(key)!=len(pt)):
    key.append(key[i])
    i+=1
    if(i==len(key)):
        i=0
res = []
for i,j in zip(pt,key):
	 a = (i+j)%26
    res.append(a)
    print(chr(a+97),end="")
print()
print("Decrypted text is ")
for i,j in zip(res,key):
	print(chr((i-j)%26+97),end="")
