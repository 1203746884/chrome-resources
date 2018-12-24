# coding=utf-8
import xlrd
import sys
import inspect


class Excel(object):

    def __init__(self,excel_path,sheet_name):
        self.excel_file=xlrd.open_workbook(excel_path)
        # excel_sheet_names =self.excel_file.sheet_names()
        # sheet1 =excel_sheet_names[0]
        self.sheet =self.excel_file.sheet_by_name(sheet_name)
        self.sheet_name =self.sheet.name
        self.rows = self.sheet.nrows
        self.cols = self.sheet.ncols

    """返回单元格,计数（0,0）表示第一行，第一列的单元格"""
    def get_sheet_data(self,row,col):
            test_data = self.sheet.cell(row ,col).value #.encode('utf-8')
            print test_data

    """读取excel,并处理数据返回格式"""
    def read_excel(self):
            list=[]
            for row in range(1,self.rows):
                lists=self.sheet.row_values(row)[:self.cols]
                list1=[]
                dict={}
                for j in range(self.cols):

                    list1.append(lists[j].encode('utf-8'))

                dict['test_name']=list1[0]
                dict['method']=list1[1]
                dict['url']=list1[2]
                dict['data']=list1[3]
                dict['header']=list1[4]
                dict['param']=list1[5]
                dict['type']=list1[6]
                # print dict
                list.append(dict)
            return  list
    """返回数组"""
    def get_test_data(self):
            array= self.read_excel()
            return  array

    """
    拓展写一个一个方法用来获取当前所在函数的名称：
    sys._getframe().f_code.co_name 等价于 inspect.stack()[0][3]  都可以获取当前函数名称
    """
    def test_foo(self):
            print "类名称为：{}，函数名称为：{}".format(self.__class__.__name__,sys._getframe().f_code.co_name)
            fn_name ='test_foo'
            print type(sys._getframe().f_code.co_name),(sys._getframe().f_code.co_name) # str equal str
            try:
                assert  fn_name == sys._getframe().f_code.co_name
            except NameError as e:
                print e
            else:
                print "当前函数名称为:{}".format(inspect.stack()[0][3])

# if __name__ =="__main__":
#     path=r"f://myexcel.xlsx"
#     st_name='Sheet1'
#     test_data= Excel(path,st_name).read_excel()
#     print test_data