#-*-coding:utf-8-*-
# Author:Lu Wei
'''
v1=list('LUWEI')
print(v1)
v2=list((1,2,3,))
print(v2)

v1=tuple('LUWEI')
print(v1)
v2=tuple([1,2,3,])
print(v2)


nums=[11,22,33,44]
for i in range(0,len(nums)):
    nums[i]=str(nums[i])
resutl='_'.join(nums)
print(resutl)

userinfo={'username':'luwei','age':'25','gender':'boy','hobby':'movie'}
del userinfo['username']
print(userinfo)

userinfo['age']='10'
print(userinfo)


print(userinfo.keys())#获取字典中所有键'username', 'age', 'gender', 'hobby'
print(userinfo.values())#获取字典中所有的值'luwei', '25', 'boy', 'movie'
for v1,v2 in userinfo.items():
    print(v1,v2)

while True:
    userinfo={'username':'luwei','age':'25','gender':'boy','hobby':'movie'}
    for a,b in userinfo.items():
        print(a,b)
    key_choice=input('key_message:')
    print(userinfo[key_choice])

info = {}
while True:
    k=input('KEY:')
    if k == 'n':
        break
    v=input('value:')
    info[k]=v
    print(info)
print(info)



message='k1|v1,k2|v2,k3|v3'
mess_sp1=message.split(',')
list={}
for i in mess_sp1:
    a,b=i.split('|')
    list[a]=b
    print(list)




dict1={
    'k1':1,
    'k2':'a',
    'k3':True,
    'k4':[1,2],
    'k5':(1,2),
    'k6':{1,2},
    1:1,
    True:1,
    (1,2):1,
  #  [1,2]:1,
   # {1,2}:1,
}
print(dict1)


user_list=[]
while True:
    u=input("username:")
    if u=='n':
        break
    p=input('password:')
    dict1={}
    dict1['user']=u
    dict1['pwd']=p
    user_list.append(dict1)
print(user_list)
print('请登录')

a=True

while a:
    u1 = input('username1:')
    p1 = input('password2:')
    for item in user_list:
        if u1==item['user'] and p1==item['pwd']:
            print('pass')
            a=False
            break
    if a:
        print('重来')
'''

v=[1,3,4]
l='12e'
v.extend(l)
print(v)
































