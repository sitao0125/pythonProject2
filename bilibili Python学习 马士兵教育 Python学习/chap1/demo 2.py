# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/1/30 14:20
#转义字符
print('hello\nworld') #\  +转义功能首字母
print('hello\tworld')
print('helloooo\tworld')
print('hello\rworld')#world 将hello 覆盖
print('hello\bworld')# \b是退格把o给退没了
print('http:\\www.baidu.com')
print('老师说：\'da jia hao\'')
#原字符 ，不希望字符串的转义字符起作用，就使用原字符，就是在字符串之前加上r或R
print(r'hello\nworld') #如果使用原字符，则最后一个字符不能是反斜线
print(r'hello\nworld\\')
#二进制与字符编码
#8bit =1 byte  1024byte=1kb 1024kb=1mb 1024GB=1TB
#GB2312 简体中文 80后  GBK 不仅可以表示简体中文还有繁体中文 90  GB18030 不仅可以表示简体繁体 维吾尔 藏文 规定每个字符可以由一个两个 或四个组成
#Unicode 几乎包含了全世界的字符