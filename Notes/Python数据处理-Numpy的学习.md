#### Numpy 的学习

##### Numpy中Ndarray对象-创建对象  
    1. 创建格式: 直接创建数组
    创建数组: numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
    相关说明: 
    object: 数组或者数列(列表/元组)
    dtype: 元素的数据类型
    copy: 对象是否需要复制
    order: 创建数组的样式
            C:行方向
            F:列方向
            A:任意方向
    ...
    
    2. 创建格式: 通过库中的方法创建ndarray数组 
        1.创建空数组: numpy.empty(shape, dtype = float, order = 'C')
          相关说明:  
          shape: 数组形状
          dtype: 数据类型  
          order: C 代表行优先, F代表列优先, 均为在内存中存储元素的顺序
          注意: 若未对其中的元素赋值,则获得的数组元素均为随机值
        
        2.创建o数组:numpy.zeros(shape, dtype = float, order = 'C')
          相关说明: 
          shape: 数组形状
          dtype: 数据类型
          order: C: 行数组
                 F: 列数组
        
        3.创建单位矩阵:numpy.ones(shape, dtype = None, order = 'C')
          shape: 数组形状
          dtype: 数据类型
          order: C: 行数组
                 F: 列数组   
            
    3.  创建格式: 从已有的数组创建数组
        1.使用numpy.asarray(a, dtype = None, order = None)
        相关说明: 可以从列表 元素 其他数组转化而来
        a: 可可以使列表和元素的组合搭配 多维数组
        dtype: 数据类型
        order: C F
        
        2.使用numpy.fromiter(iterable, dtype, count=-1)
        相关说明: 可以从可迭代对象中建立ndarray对象,返回一维数组
        iterable: 可迭代对象
        dtype:  返回数组的数据类型
        count: 读取的数据数量, 默认为-1, 读取所有数据
        
        3. 使用numpy.arange(start, stop, step, dtype)
        相关说明:  创建数值范围并返回ndarray对象 /==
        start: 起始值
        stop: 终止值(不包含)
        step: 步长, 默认为1
        dtype: 返回ndarray的数据类型,如果没有提供,则会使用输入数据的类型
        
        4. 使用np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
        相关说明: 构造一个数组并且数组的表示形式为等差数列
        start: 起始值
        stop: 终止值
        num=50: 样本数量
        endpoint=True: 
        retstep=False,
        dtype=None: 数组的数据类型
        
        5. 使用np.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None)
        相关说明: 构造一个数组并且数组的表现形式为等比数列
        start: 序列的起始值为：base ** start
        stop: 序列的终止值为：base ** stop。如果endpoint为true，该值包含于数列中
        num: 要生成的等步长的样本数量，默认为50
        endpoint: 该值为 ture 时，数列中中包含stop值，反之不包含，默认是True。
        base: 对数 log 的底数。
        dtype: ndarray 的数据类型
     
    
##### Numpy中Ndarray对象-对象分析       
    1. Numpy 数据类型: 略  
    2. Numpy 数组属性: 
        1. ndim : 秩
        2. shape : 维度    
        3. size : 数组元素的个数    
        4. dtype : 对象的元素类型    
        5. itemsize : ndarray 对象中每个元素的大小
        6. itemsize : ndarray 对象的内存信息
        7. itemsize : ndarray 元素的实部
        8. itemsize : ndarray 元素的虚部
        ...  
        
##### Numpy中Ndarray对象-索引和切片
    1. 索引: 找到具体的符合某个条件的数组元素  
        * 索引可以通过数组的下标进行索引,例如: a[2:7:2]/a[2,7,2]表示从数组a的下标2到下标7之间, 步长为2的元素
        注意: 多维数组同样可以使用这一方式进行索引
        * 高级索引方式
            1. 整数数组索引:  
            2. 布尔索引:  
            3. 花式索引:  
    2. 切片: 利用已存在的数组,得到一个新的数组
        切片对象可以通过内置的 slice 函数，并设置 start, stop 及 step 参数进行，从原数组中切割出一个新数组  
        
        
##### Numpy迭代数组
    1. 使用numpy.nditer()方法,可以返回数组元素的迭代结果
```python
import numpy as np
 
a = np.arange(6).reshape(2,3)
for x in np.nditer(a.T):
    print (x, end=", " )
print ('\n')
 
for x in np.nditer(a.T.copy(order='C')):
    print (x, end=", " )
print ('\n')
```  
    结果为:
```shell script
0, 1, 2, 3, 4, 5, 

0, 3, 1, 4, 2, 5, 
```  

    2. 控制遍历顺序
* for x in np.nditer(a, order='F'):Fortran order，即是列序优先；
* for x in np.nditer(a.T, order='C'):C order，即是行序优先；
```python
import numpy as np
 
a = np.arange(0,60,5) 
a = a.reshape(3,4)  
print ('原始数组是：') 
print (a) 
print ('\n') 
print ('原始数组的转置是：') 
b = a.T 
print (b) 
print ('\n') 
print ('以 C 风格顺序排序：') 
c = b.copy(order='C')  
print (c)
for x in np.nditer(c):  
    print (x, end=", " )
print  ('\n') 
print  ('以 F 风格顺序排序：')
c = b.copy(order='F')  
print (c)
for x in np.nditer(c):  
    print (x, end=", " )
```
    结果为:
```shell script
原始数组是
[[ 0  5 10 15]
 [20 25 30 35]
 [40 45 50 55]]


原始数组的转置是
[[ 0 20 40]
 [ 5 25 45]
 [10 30 50]
 [15 35 55]]


以 C 风格顺序排序
[[ 0 20 40]
 [ 5 25 45]
 [10 30 50]
 [15 35 55]]
0, 20, 40, 5, 25, 45, 10, 30, 50, 15, 35, 55, 

以 F 风格顺序排序
[[ 0 20 40]
 [ 5 25 45]
 [10 30 50]
 [15 35 55]]
0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55,
```
    
    3.  修改数组中元素的值
    注意: 
    nditer 对象有另一个可选参数 op_flags。 
    默认情况下，nditer 将视待迭代遍历的数组为只读对象（read-only）;
    为了在遍历数组的同时，实现对数组元素值得修改，必须指定 read-write 或者 write-only 的模式

##### Numpy 数组操作  
* 修改数组形状
    1. numpy.reshape()
    numpy.reshape 函数可以在不改变数据的条件下修改形状，格式如下： numpy.reshape(arr, newshape, order='C')
    2. numpy.ndarray.flat()
    3. numpy.flatten()
    4. numpy.ravel()
    
* 翻转数组
    1. numpy.transpose()  
    numpy.transpose() 函数用于兑换函数的维度,格式如下: numpy.transpose(arr, axes)
    注意, 该函数的作用于numpy.ndarray.T作用相似,均实现了数组的转置
    其中: arr为执行操作的数组, axes为整数数组,用于指定格式, 举例如下: 
```python
import numpy as np
 
a = np.arange(12).reshape(3,4)
 
print ('原数组：')
print (a )
print ('\n')
 
print ('对换数组：')
print (np.transpose(a))
```
.....等等其他函数

