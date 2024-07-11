import random

def gcd(x,y):
    if(y <  x):
        x,y = y,x
    while (y):
        x,y = y, x%y
    return abs(x)

def power(a,b):
    return a**b

p = int(input(" Enter 1st prime number : "))
q = int(input(" Enter 2nd prime number : "))

n  = p*q

phi = (p-1)*(q-1)


e = random.randint(2,phi-1)

while(gcd(e,phi)!=1):
    e = random.randint(2,phi-1)

k=0

while(True):
    d = (1+k*phi)//e
    if ((1+k*phi)%e==0 and d!=e):
        break
    k+=1

private_key = {d,n}
public_key = {e,n}
print("private key : ",private_key)
print("private key : ",public_key)


msg = int(input(" Enter msg to be shared : "))

cipher = (msg**e)%n

print(" ciphet_text : ",cipher)

#decrption

plain = (cipher**d)%n

print(" plain text : ",plain)
    
