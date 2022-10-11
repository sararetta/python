# sx=open('../sasa.txt');
# a=''
# for a in sx:
#     print(a.rstrip())
# print('////////////////////////////////////')
# cou = 0
# for line in sx:
#     cou+=1
# print(cou)

# z=sx.read()
# x=sx.read()
# print(len(z))
# print(len(x))

cc=[]
#
# for s in sx:
#     if s.lower().startswith('from'):
#         x=s.find('/');
#         cc.append(s[:x])
# print(cc)

# for s in sx:
#     if s.find('@')==-1:
#         x=s.find('/');
#         print(x)
#         cc.append(s[:x])
# print(cc)


# the write method of the file handle object puts data into the file, returning the
# number of characters written. The default write mode is text for writing (and
# reading) strings

# c=open('../sasa.txt', 'a');
# print(c)
# x="This here's the wattle,\n"
#
#
# c.write(x)

# xx=open('../sasa.txt')
# v=xx.read()
# print(v)
# # cc='sara retta\n hhhh'
# # print(cc)
# print(repr(v))


cap=open('../sasa.txt')

for i in cap:
    print(i.strip().lower())









