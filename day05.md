### day05

###### 考题

range（10，0，-1）-->10 9 8 7 6 5 4 3 2 1 

v1=1     ---->type int

v2=(1)  ---->type int

v3=(1,)  ---->type tuple

v4=()   -----> type tuple

###### 回顾

数据类型：

- int 

  - py2/py3 范围有区别

  - 除法，py2会丢失小数点部分

  - 强制转换

    - int（‘字符串') 【重要】
    - int （布尔值）

    

- bool

  - 强制转换

    - bool（整数） -->bool(1)   T        bool(0)   F

    - bool（字符串）-->bool('x')  T     bool('')   F  空字符串

    - bool（列表）  --->bool([1,2,])  T bool([])  F  空列表

    - bool（元组）--->boil((1,2,))   T    bool(())  F  空元组

      

- str

  - 独有功能：upper/lower/split/strip/replace/isdigit/startswith/endswith/format/encode/jion
  - 公共功能：
    - len
    - 索引
    - 切片
    - 步长
    - for循环
    - 删除【无】
    - 更新【无】

- list

  - 独有功能：append/insert/remove('元素')/pop(’索引‘，删除值可赋值)/clear/extend（循环加到原来列表之后）
  - 公共功能
    - len
    - 索引
    - 切片
    - 步长
    - for循环
    - 删除
    - 更新
  - 强制转换：
    - str('999')='999'
    - str(True)='True'
    - str(['taoting’，‘luwei’])=‘’['taoting’，‘luwei’]‘’，‘‘.jion(['taoting’，‘luwei’]‘)=taotingluwei

- tuple

  - 独有功能（无）

  - 公共功能

    - len

    - 索引

    - 切片

    - 步长

    - for循环

    - 删除【无】

    - 更新【无】

      
    
  - 强制转换：
  
    - tuple('adfadfasdfasdfasdfafd')
  
      ```
      v1 = tuple('adfadfasdfasdfasdfafd')
      print(v1)
      ```
  
      
  
  - tuple([11,22,33,44])
  
    ```
    v1 = tuple([11,22,33,44])
    print(v1)
    -->((11,22,33,44)
    ```
  
    
  
    ​	

###### 总结

- 常见的类型转换

  ```
  # 字符串转数字
  
  # 数字转字符串
  
  # 列表转元组
  
  # 元组转列表
  
  # 其他转bool时，只有：0 “”  []  () 
  ```

  ```
  # 练习题
  nums = [11,22,33,44]
  for i in range(0,len(nums)):
      nums[i] = str(nums[i])
  resutl = '_'.join(nums)
  print(resutl)
  
  # 1. "".jon([元素必须是字符串,元素必须是字符串,])
  ```

  

##### 1.字典

帮助用户去表示一个事物的信息（事物是有多个属性）。

```python
info = {"name":'刘伟达','age':18,'gender':'男','hobby':'同桌'} # 键值

# 请输出：我今天点%s,他的年龄是%s,性别是%s，他喜欢他的%s;
```

基本格式，并且是无序的

```
data = {键:值,键:值,键:值,键:值,键:值,键:值,}
```

1. 独有功能

   ```python
   info = {"name":'刘伟达','age':18,'gender':'男','hobby':'同桌'}
   ```

   - keys，获取字典中所有的键。     ['name','age','gender','hobby']

     ```python
     # for item in info.keys():
     #     print(item)
     ```

   - values，获取字典中所有的值。  ['刘伟达','18','男','同桌']

     ```python
     # for item in info.values():
     #     print(item)
     ```

   - items，获取字典中的所有键值对。

     ```python
     # for v1,v2 in info.items():
     #     print(v1,v2)
     ```

   公共功能

   - len

     ```
     info = {"name":'刘伟达','age':18,'gender':'男','hobby':'同桌'}
     print(len(info))
     ```

   - 索引

     ```
     info = {"name":'刘伟达','age':18,'gender':'男','hobby':'同桌'}
     info['name']
     info['age']
     ```

   - 切片【无】

   - 步长【无】

   - for

     ```
     info = {"name":'刘伟达','age':18,'gender':'男','hobby':'同桌'}
     
     for item in info.keys():
         print(item)
     
     for item in info.values():
         print(item)
     
     for k,v in info.items():
         print(k,v)
     ```

   - 修改（存在就修改/不存在就增加）

     ```
     #改值
     userinfo={'username':'luwei','age':'25','gender':'boy','hobby':'movie'}
     userinfo['age']='10'
     print(userinfo)
     #字典是无序的
     --->{'age': '10', 'hobby': 'movie', 'username': 'luwei', 'gender': 'boy'}
     ```

   - 删除

     ```
     userinfo={'username':'luwei','age':'25','gender':'boy','hobby':'movie'}
     del userinfo['username']
     print(userinfo)
     -->{'gender': 'boy', 'age': '25', 'hobby': 'movie'}
     ```

2. 字典Key-Values，key不可以为列表和字典

   Key在python中通过Hash算法生成一段数字，由于Key是不允许变化，而列表和字典是允许可以变的。所以Key不能是列表与字典。

   ```
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
     #  [1,2]:1, 列表可以变
      # {1,2}:1, 字典可以变
   }
   print(dict1)
   ```

   

###### 重点：

- int
- bool
- str
- list
- tuple
- dict

