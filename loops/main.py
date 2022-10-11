
# user=input('enter a word');
# while user!='done':
#     user=input('enter a word');
# print('user is '+user);

# user=input('enter a number');
# count=0
# total=0;
# avarageT=0;
#
# while user!='done':
#     try:
#         value=int(user);
#         count+=1
#         total+=value
#         avarageT=total/count
#         user = input('enter a value');
#     except:
#         user = input('pelase enter a number');
# print(count,total,avarageT)

#   for loop
# person=[]
# 
# lis=['sara','retta','abagelan','gezimu']
# for a in lis:
#     if a=='retta':
#         person.append(a)
#         break
# print(person)

largest = None
smallest = None

user = input('enter a number');
no = []
maxx = 0;
minn = None

while user != 'done':
    try:
        x = int(user);
        no.append(x);
        user = input("Enter a number: ")

    except:
        print('Invalid input')
        user = input("Enter a number: ")
for n in no:
    if (n > maxx):
        maxx = n;
for n in no:
    if (minn is None or minn > n):
        minn = n;

print('Maximum is', maxx);
print('Minimum is', minn);
