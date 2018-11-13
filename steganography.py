import skimage.io as pp
from skimage import color as c
import matplotlib.pyplot as plt
import numpy as np
import math


file_name="/home/sudhanshu/scikit-image/lena.jpg"
img = pp.imread(file_name)
#print(img)
print(type(img))
print(img.shape)
#converting colored image to grayscale
q=img[:,:,0]
w=img[:,:,1]
e=img[:,:,2]
t=np.floor(0.2989*q+0.5870*w+0.1140*e)
#t=np.floor(t/128)
print(t)
print(t.shape)
#t1=np.copy(t)
text="This is encoded text."
st=[]
#storing bits of each character in a list after ignoring starting two bits("0b")
for i in range(0,len(text)):
    k=ord(text[i])
    q=str(bin(k))[2:]
    print(q)
    #if the binary number is not of length 8, then we wre making it 8.
    if(len(q)==8):
        st.append(q)
    if(len(q)==7):
        st.append("0"+q)
    if(len(q)==6):
        st.append("00"+q)
    if(len(q)==5):
        st.append("000"+q)
    if(len(q)==4):
        st.append("0000"+q)
    if(len(q)==3):
        st.append("00000"+q)
    if(len(q)==2):
        st.append("000000"+q)
    if(len(q)==1):
        st.append("0000000"+q)

#counting the number of bits in whole string
cv=0
for i in range(0, len(st)):
    cv+=1
    print(cv)
cv*=8
print(cv)
p=0
y=0
check=0
print(st)

for i in range(0, t.shape[0]):
    #if y index has reached the end of  st.

    if(y==(len(st))):
        break
    for j in range(0, t.shape[1]):
        l=len(st[y])
        #converting particular pixel to binary form.
        a=bin(int(t[i][j]))
        #checking if we have not exceeded the length of a a particular st[y].
        if(p<l):

            #a[2]=st[p]
            print(st[y][p])

            #we are making a of 8 bits because we are appending our bit(to be encoded) to first bit of pixel bit.
            #But if number is not of 8 bits then we will end up encoding some other bit of pixel and since it is not of 8 bits
            # then we will consider first bit as 0 while retrieving the information which is wrong.


            if(len(a[2:])==7):
                a=a[0:2]+"0"+a[2:8]
            if(len(a[2:])==6):
                a=a[0:2]+"00"+a[2:7]
            if(len(a[2:])==5):
                a=a[0:2]+"000"+a[2:6]
            if(len(a[2:])==4):
                a=a[0:2]+"0000"+a[2:5]
            if(len(a[2:])==3):
                a=a[0:2]+"00000"+a[2:4]
            if(len(a[2:])==2):
                a=a[0:2]+"000000"+a[2:3]
            if(len(a[2:])==1):
                a=a[0:2]+"0000000"+a[2:2]
            #sandwitching bit of text inside image's starting bit
            a=a[0:2]+st[y][p]+a[3:10]

            print(a)
            #here p counts the number of bits sandwitched of a particular character.
            p+=1


        if((p)<l):
            print(st[y][p])
            #Here we are checking if length of particular image pixel is 7 or 8. In case of 7, we will append the bit and
            #in case of 8 we will replace the bit.

            if(len(a)!=10):
                a=a[0:len(a)]+st[y][p]

            else:
                a=a[0:len(a)-1]+st[y][p]

            print(a)
            p+=1


        #if current st[y] has been covered then move to next st[y] and intialize previous p to 0, so that bits are counted from 0.
        if(p==(len(st[y]))):
            y=y+1
            p=0
        #Storing the decimal form of a in image pixel.
        t[i][j]=int(a,2)
        #In case where st[y] is finished, break the loop.
        if(y==(len(st))):
            break

#Assigning total length of text in binary form in last pixel of image.
i1=(t.shape[0]-1)
j1= (t.shape[1]-1)
t[i1][j1] = cv

print(t)
print(cv)
plt.imshow(t, cmap="gray")
plt.show()




#fetching information out of image




#p for counting the number of bits retrieved.
p=0
#r for counting the number of bits of a particular character.
r=0
#s for storing each ascii value's binary code.
s=""
#st1 for storing the binary forms of all the ascii values in one place.
st1=[]
j1=t.shape[0]-1
j2=t.shape[1]-1
#retrieving the last pixel value which is the number of bits encoded.
k=t[j1][j2]

for i in range(0, t.shape[0]):
    #when all 32 bits are retrived then break.
    if(p==k):
        break
    for j in range(0, t.shape[1]):
        #when all 32 bits are not retrieved then go into the condition.
        if(p<=k):
            #if 8 bits of  a character are retrieved then start from new s where first two bits will represent the binary form.
            if(r%8==0):
                s=s+"0b"
            #converting the pixel value into binary digits and storing them into a.
            a=bin(int(t[i][j]))
            #if length of a is not 10(including 0b) then first number would have been 0 so retrieve 0 as the encoded bit.
            if(len(str(a))!=10):
                s=s+str(0)
                print(a)
                p+=1
                r+=1
            #if the length is 10 then retrieve the 3rd bit which in this case is encoded bit.
            else:
                s=s+str(a[2])
                print("hello",a[2])
                p+=1
                r+=1
        # while retrieving the next bit simply retrive the last bit of the binary form.
        if(p<=k):

            s=s+a[len(str(a))-1]
            p+=1
            r+=1
        #if 8 bits of a particular character are retrieved then store s in st1 list and again make s as null so that it can store
        #next character's bit from starting. Also makr r=0 because we have counted 8 bits of one character.
        if(r==8):
            st1.append(s)
            s=""
            r=0
        #when all 32 bits are retrived then break.
        if(p==k):
            break

print(st1)
#Here, we are converting the binary digits stored in st1 into integer value(ascii value) then we are converting those ascii values
#back into character and displaying it.
for i in range(0,len(st1)):

    v=int(st1[i],2)
    print(chr(v),)
