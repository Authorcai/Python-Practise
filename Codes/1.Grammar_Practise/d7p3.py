"""
设计一个函数返回给定文件名的后缀名
思路:
    将给定的文件名是为你一个字符串,通过rfind()函数找到最后一个'.',再通过对字符串的截取即可获得文件的后缀名
"""
def getHzm(filename='.py'):
    code = ''
    pos = filename.rfind('.')
    for x in range(pos+1,len(filename)):
        code = code + filename[x]
    return code
name = str(input('请输入文件名: '))
print(getHzm(name))