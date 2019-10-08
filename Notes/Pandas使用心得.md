#### Pandas使用教程

* 在Pandas库中一般会使用Series 和 DataFrame

##### Series使用教程

* 构造方法:
    基本格式: obj = pd.Series(sdata,index=sindex)
    sdata 为 列表
    sindex 为 列表

* 相关操作:
    转置
    
    
##### DataFrame使用教程

* 构造方法:
    基本格式: obj = pd.DataFrame(sdata,columns=[],index=sindex)
    sdata 为字典, 格式为 {'clown1': [], 'clown2': [] }
    columns 为列表
    sindex 为 列表
    需要一一对应
    
* 相关操作
    转置
    修改DataFrame的相关属性: 修改index和列: obj.index.name, obj.columns.name
    转换为narray
    索引: 包括排序
    选取一行或一组行
    选组一列或一组列
    

