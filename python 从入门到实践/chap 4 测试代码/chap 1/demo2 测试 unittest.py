# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/3/27 15:02
import unittest
from name_function import  get_formatted_name

class NamesTestCase(unittest.TestCase):   #创建这个类 用于包含一系列针对 get_formatted_name()的单元测试
    '''测试name_function，py'''

    def test_first_0last_name(self):
        '''能够正确处理 像 janis joplin 这样的姓名吗'''
        formatted_name =get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name,'jains joplin')

unittest.main()