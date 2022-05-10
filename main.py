def sum(a,b):
    return a+b

def div(a,b):
    return a/b

def sub(a,b):
    return a-b  

def mul(a,b):
    return a*b          

a = float(input('First: '))
b = float(input('Second: '))
op = input('Operation (sum/sub/div/mul): ')

if op== 'sum':
    print(f'a+b = {a+b}')
elif op=='div':
    print(f'a+b = {a+b}')
elif op =='sub':
    print(f'a+b = {a+b}')
elif op=='mul':
    print(f'a+b = {a+b}')
else:
    print("Invalid Choice")
    

#sentence = "the quick brown fox jumped over the lazy dog"
#record = {}

#for letter in sentence:
 #   if letter in record:
  #      record[letter] +=1
   # else:
    #    record[letter] =1
#print (record)           
