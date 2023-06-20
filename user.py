'''
import sys

if len(sys.argv)<2 :
    print(' too less argument')
elif len(sys.argv)>2:
    print('too many argument')
else:
    print("hello your name is " ,sys.argv[1])



if 5>2:
    print('five is grater than two')

x=5
print(type(x))
print(bool(-1))
'''


'''

if __name__ == '__main__':
    n = int(input())
if n%2==0:
    print("Weird")
else:
    print("even")
    if n in range(2,5):
        print("Not Weird")
    elif n in range(6,20):
        print("Weird")
    elif n < 20:
        print("Not Weird")
'''
'''
n = int(input())
new_list= list(range(0,n))
for i in new_list:
    print(i*i,end='\n')
'''
'''
year = int(input())
if year%4==0:
    print("leap year")
else:
    print('not leap year')
'''
'''
car= ['toyota','hyundai','tata']
car.sort(reverse=True)
print(car,end="\n")
'''
'''
def desimal_to_binary(num):
    if num>=1:
        desimal_to_binary(num//2)
        print (num%2 , end="") 
if __name__ == '__main__':
    dec_val = int(input())

    desimal_to_binary(dec_val)

'''
'''
string = input("write anything: ")
vowels=0
for ch in string:
    if (ch=='a' or ch =='e'or ch=='i'or ch=='o'or ch=='u'):
        vowels+=1
print(f'there is {vowels} vowels')
'''
'''
total_price = int(input('product price: '))
discount = int(input('total discount: '))
discount_value= (total_price/ 100)*discount
print(f"after discout price is {total_price-discount_value}")
'''
'''
list_1= [1,2,3,7,-1,-3,-5,"sayantan"]

def xtract_int(list):
    return[x for x in list if isinstance(x,int)and x>=0]
interger_list= xtract_int(list_1)
print(interger_list)
'''
'''
def double_string(string):
    double_string=''
    for chat in string:
        double_string+=chat*2
    return double_string
print(double_string("123oo"))
'''
"""
num= int(input("how many number: "))
total_sum= 0

for i in range(num):
    number= float(input('enter any number: '))
    total_sum+=number
average = total_sum/num
print(average)
"""
'''
time_hours=int(input())
time_dayes=time_hours/24
print(time_dayes)
'''
def binary_search(arr,k,n):#binary serch funct
    low = 0
    upper = len(arr)
    while low <= upper:
        mid = (low+upper)//2
        if arr[mid]== k:
            return mid
        elif arr[mid]<k :
            low = mid +1 
        else:
            upper= mid -1 
    return -1
#enter all input
i =  input("Enter: ")
arr= [int(x) for x in i.split(" ") ] 
arr.sort()
n = len (arr)
#printing all the value

print(arr)
print(n)

k = int(input("Target: "))
result = binary_search(arr,k,n)
print(result)

