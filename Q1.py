x = int(input("Input a number between 1 to 99 to convert to words : "))
a = ['','one','two','three','four','five','six','seven','eight','nine']
b = ['','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
c = ['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

i = x%10 #to get ones place digit
j = x//10 #to get tens place digit

if x==0:
    print('zero')
elif x>0 and x<10: #Printing from 1-9
    print(a[x])
elif x>9 and x<20: #Printing from 10-19
    print(b[x-9])
elif x>20 and x<100: #Printing from 20-99
    print(c[j],a[i])