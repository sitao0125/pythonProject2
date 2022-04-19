# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/2/6 19:10
# 集合的 相关操作
# 判断  in not in
s={10,20,30,40,50,60}
print(10 in s)
print(100 in s)
print(10 not in s)
print(100 not in s)
# 新增
'''
1.调用add（）  一次添加 一个 
2.调用update  一次至少添加一个

'''
'''
删除
1.remove（） 一次删除一个指定元素
2.discard（） 一次删除一个指定元素  若不存在 不抛出异常
3. pop() 一次删除一个人一元素
4.clear() 清空集合
'''
# 添加
s.add(80)
print(s)

s.update({200,400,300})
print(s)
s.update([100,99,8])
s.update((78,64,56))
print(s)

'''删除'''
s.remove(100)
#s.remove(500)
s.discard(500)
s.pop()
print(s)

s.clear()
print(s)