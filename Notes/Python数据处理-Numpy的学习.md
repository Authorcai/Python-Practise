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

##### Numpy 位运算
Numpy 的位运算使用的是numpy.bitwise来开头的函数
分别为:
    bitwise_and: 对数组元素执行位与操作
    bitwise_or:	对数组元素执行位或操作
    invert:	按位取反
    left_shift:	向左移动二进制表示的位(())
    right_shift: 向右移动二进制表示的位
    
##### Numpy字符串函数
注意: 在numpy.char.*中定义,举例说明:  
    add()	        对两个数组的逐个字符串元素进行连接
    multiply()	    返回按元素多重连接后的字符串
    
    center()	    居中字符串
    capitalize()	将字符串第一个字母转换为大写
    title()	        将字符串的每个单词的第一个字母转换为大写
    lower()	        数组元素转换为小写
    upper()	        数组元素转换为大写
    
    split()	        指定分隔符对字符串进行分割，并返回数组列表
    splitlines()	返回元素中的行列表，以换行符分割
    strip()	        移除元素开头或者结尾处的特定字符
    
    join()	        通过指定分隔符来连接数组中的元素
    replace()	    使用新字符串替换字符串中的所有子字符串
    
    decode()	    数组元素依次调用str.decode
    encode()	    数组元素依次调用str.encode

##### Numpy数学函数 : 三角函数 算数运算函数 复数处理函数  
* 三角函数: 
    np.sin() np.cos() np.tan()  
    np.arcsin() np.arccos() np.arctan()
    
* 算数运算函数: 
    舍入函数: numpy.around()
    下舍函数: numpy.floor()
    上入函数: numpy.ceil()
    加: numpy.add()
    减: numpy.subtract()
    乘: numpy.multiply()
    除: numpy.divide()
    求倒数: numpy.reciprocal()
    幂函数: numpy.power()
    取余: numpy.mod()

* 统计函数: 一般用于统计本函数
    求最大值: numpy.amin(a) , 可指定axis
    求最小值: numpy.amax(a) , 可指定axis
    求最大值和最小值的差: 
    求小于某个值的观察值的百分比: numpy.percentile(a, q, axis)
    计算的中位数: numpy.median(), 可指定轴
    求平均值(加权平均值): numpy.average() 
    求标准差和方差: ...
    
##### NumPy 排序、条件刷选函数: 快速排序 归并排序 堆排序
    相关说明: numpy.sort(a, axis, kind, order)
    a: 要排序的数组
    axis: 沿着它排序数组的轴，如果没有数组会被展开，沿着最后的轴排序， axis=0 按列排序，axis=1 按行排序
    kind: 默认为'quicksort'（快速排序）
    order: 如果数组包含字段，则是要排序的字段
    
##### Numpy字节交换  

##### Numpy 副本和视图

* 副本: 为数组的拷贝结果,对副本的修改不影响原数组的内容;
    1. Python 序列的切片操作，调用deepCopy()函数。
    2. 调用 ndarray 的 copy() 函数产生一个副本。
* 视图: 为数组的引用,对视图的修改将会影响原数组的内容;
    1. numpy 的切片操作返回原数据的视图。
    2. 调用 ndarray 的 view() 函数产生一个视图。

    