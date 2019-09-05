#### Numpy 的学习

##### Array的创建

* 利用List或Tuple创建Array  
```python
import numpy as np

list_1 = [1,2,3,4]
list_2 = [5,6,7,8]
list_3 = [5.0,6,7,8]

array_1 = np.array(list_1)
array_2 = np.array([list_1,list_2])
array_3 = np.array([list_1,list_3])

print(array_1)
print(array_2)
print(array_3)

print(array_2.dtype)
print(array_2.shape)
print(array_3.dtype)
```
可得输出结果为:  
```text
[1 2 3 4]
[[1 2 3 4]
 [5 6 7 8]]
[[1. 2. 3. 4.]
 [5. 6. 7. 8.]]
int64
(2, 4)  
float64
```

* 创建全0矩阵 : 使用np.zeros()
* 创建单位矩阵 : 使用np.eye(5)
* 创建爱你矩阵 : 使用np.arrage(m,n)
* 总结 
    1. 使用array.size查看矩阵中元素的个数
    2. 使用array.dtype查看矩阵中元素的类型(向上)
    3. 使用array.查看矩阵中元素的类型(向上) 
   
##### Array的计算

* array和标量之间的计算
* array和array之间的计算(广播)

##### Array的切片
##### Array的索引