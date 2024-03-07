###PRINT FIRST HALF OF THE STRING IN UPPERCASE AND THE NEXT HALF IN LOWERCASE
#a=>
'''ls='jIlLPaTel'
uc=len(ls)//2
for i in ls[:uc]:
    x=i.capitalize()
    print(x,end='')
for i in ls[uc:]:
    y=i.casefold()
    print(y,end='')'''
#b=>
'''ls='jIlLPaTel'
uc=len(ls)//2
str=''
res=map(lambda i:i.capitalize(),ls[:uc])
res2=map(lambda i:i.casefold(),ls[uc:])
x=(list(res)+(list(res2)))
y=str.join(x)
print(y)'''


###Capitalize the Alternative Characters of the String
#a=>
'''ls='jillpatel'
res="".join([ls[i].upper() if i%2==0 else ls[i].lower() for i in range(len(ls))])
print(res)'''

#b=>
'''ls='jillpatel'
str=''
for i in range(len(ls)):
    if i%2==0:
        x=ls[i].upper()
    else:
        y=ls[i].lower()
        print(str.join(x),end='')
        print(str.join(y),end='')'''


###First and Last Characters of Each Word in a String
#a=>
'''str1='Jill'
for i in str1:
    y=str1[0]
    x=str1[-1]
print(y,end='')
print(x)'''

#b=>
'''str1='Jill'
res=map(lambda i:i,str1[0]+str1[-1])
print(list(res))'''


###Count the Number of Digits, Alphabets, and Other Characters in a String
#a=>
'''ls='kn348203$%^#@^8658hvkjh'
num=[]
al=[]
for i in ls:
    if i.isnumeric() :
        num.append(i)
    if i.isalpha():
        al.append(i)
ot=len(ls)-(len(num)+len(al))
print(ls)
print(f"Number of digits: {(len(num))}")
print(f"Number of alphabets: {(len(al))}")
print(f"Number of other chars: {ot}")'''

#b=>
'''ls='kn348203$%^#@^8658hvkjh'
digits=filter(lambda i:i.isnumeric(),ls)
al=filter(lambda i:i.isalpha(),ls)
ot=len(ls)-(len(digits)+len(al))
d=len(ls)-(len(al+len(ot)))
print(list(digits))
print(list(al))
print(ot)'''


###Check if a String Starts With the Alphabet and Has Digits
#a=>
'''ls='kn$%^#@986098^hvkjh'
digits=False
if ls[0].isalpha():
    print("The string starts with an an alphabet")
else:
    print("String does not start with an alphabet")
for i in ls:
    if i.isdigit():
        digits=True
print(f"Digits present: {digits}")'''

#b=>
'''ls='kn$%^#@986098^hvkjh'
res=map(lambda i: i.isalpha(),ls[0])
res2=map(lambda ls:ls.isdigit(),ls)
print(f"The string starts with alphabet: {list(res)}")
print(f"The String has digits: {list(res2)}")'''


####Count the Number of Vowels in a String
#a=>
'''str1='oeuhnmioAUO'
v='aeiouAEIOU'
c=sum(str1.count(vowel) for vowel in v)
print(c)'''

#b=>
'''str1='oeuhnmioAUO'
v='aeiouAEIOU'
res=filter(lambda i:v.count(i),str1)
x=list(res)
print(len(x))'''


####Remove All Duplicate Words From a Given String
#a=>
'''ls='apple pies apple banana banana'
x=ls.split()
for i in x:
    if x.count(i)>1:
       y=x.remove(i)
print(x)'''

#b=>
'''ls='apple pies apple banana banana'
p=ls.split()
print(p)
g = p[:]
res=filter(lambda x: g.remove(x) is None and g.count(x) == 0, p)
print(list(res))'''


####Print the Character with Maximum Frequency in a String
#a=>
'''ls='aaaeeeeeeuiey36'
print(ls)
freq={}
for i in ls:
    if i in freq:
        freq[i]=freq[i]+1
    else:
        freq[i]=1
res=max(freq,key=freq.get)
print(f"Char with maximum frequency: {res}")'''

#b=>*********
'''ls='aaaeeeeeeuiey36'
res = max(ls,key=lambda i: ls.count(i))
print(res)'''



####Print the Frequency of Each Character in String
#a=>
'''s='resources'
freq={}
for i in s:
    freq[i]=s.count(i)
print(freq)'''

#b=>
'''from collections import Counter
str1='resources'
res=Counter(str1)
print(res)'''



####*****Create Random Strings Until a Given String is Generated
  





####Find the words that are greater than given length k
#a=>
'''length=int(input("Enter a number to get words greater than:"))
s='apples','bananas','dictionary','games','tomatoes','gamingpc'
for i in s:
    if len(i)>length:
        print(i)'''

#b=>
'''length=int(input("Enter a number to get words greater than:"))
s='apples','bananas','dictionary','games','tomatoes','gamingpc'
res=filter(lambda i:len(i)>length,s)
print(list(res))'''



#####Remove i’th Character From String in Python
#a=>
'''k='Jill Patel'
p=list(k)
n=int(input("Enter a char position to remove:"))
z=p.pop(n)
y=''.join(p)
print(y)'''

#b=>
'''k=list('Jill Patel')
print(k)
n=int(input("Enter a char position to remove:"))
res=filter(lambda n:n,k.pop(n))
z=''.join(k)
print(z)'''
