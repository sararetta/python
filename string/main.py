#
#Getting the length of a string using len

# x='banana'
#
# count=1
# while count<=len(x):
#     print(x[-count]);
#     count+=1



# A segment of a string is called a slice. Selecting a slice is similar to selecting a
# character:

# print(x[0:3])
# coun=0
# for a in x:
#     if(a=='a'):
#         coun+=1
# print(coun)

def count(letter):
    count = 0
    for a in letter:
        if(a=='a'):
            count+=1
    return count

x=count('nananananaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
print(x)
# The in operator
xx='banana'
print('ana' in xx);
print(xx.upper())
print(xx.lower())
print(xx.find('na'))
print(xx.startswith('bg'))
a=''
print(a)
print(len(a))
print(dir(xx))
help(str.replace)