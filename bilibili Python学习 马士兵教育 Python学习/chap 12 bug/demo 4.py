# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/2/9 19:19
'''python 中 常见的 异常类型'''


'''异常处理 模块  
traceback 模块'''

#print(10/0)

import traceback
try:
    print('-----------')
    print(1/0)
except:
      traceback.print_exc()


