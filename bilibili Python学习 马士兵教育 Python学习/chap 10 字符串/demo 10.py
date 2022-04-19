# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/2/7 21:34
#字符串的编码转换
# str 在内存中 以 unicode 表示
# 编码 与解码 的方式
'''编码 将字符串 转化为二进制数据 bytes
    解码 将bytes类型的数据 转化成字符串类型
    '''
# 编码
s='天涯共此时'
print(s.encode(encoding='GBK'))  #一个中文占两个字节
print(s.encode(encoding='UTF-8')) #一个中文占 三个字节
# 解码
byte=s.encode(encoding='GBK')
print(byte.decode(encoding='GBK'))

# 编码格式  是啥 对应解码 格式就是啥
byte=s.encode(encoding='UTF-8')
print(byte.decode(encoding='UTF-8'))
