x = input('Enter:  ')
# x = 'oggy buggy oggy'
p=x.split(' ')
list=[]
for i in range(len(p)):
        if i == 0 and len(p) >= 2 :
        	temp=p[i]+'+'
        	list.append(temp)
        elif i != (len(p)-1):
                temp=p[i]+'%20'
                list.append(temp)
        else:
                list.append(p[i])
print(p,list)
x=''.join(list)
print(x)
# url  = 'https://yts.mx/browse-movies/'+x+'/all/all/0/latest/0/all'
# x = 'oggy buggy oggy'
# p=x.split(' ')
# list=[]
# for i in range(len(p)):
#         if i != (len(p)-1):
#                 temp=p[i]+'%20'
#                 list.append(temp)
#         else:
#                 list.append(p[i])
# print(p,list)
# x=''.join(list)
# print(x)