import xlrd
import sys
import inspect
import requests
import json

class Excel(object):

    def __init__(self,excel_path,sheet_name):
        self.excel_file=xlrd.open_workbook(excel_path)
        # excel_sheet_names =self.excel_file.sheet_names()
        # sheet1 =excel_sheet_names[0]
        self.sheet =self. excel_file.sheet_by_name(sheet_name)
        self.rows = self.sheet.nrows
        self.cols = self.sheet.ncols
        self.sheet_name =self. sheet.name
        def get_sheet_data(self,row,col):
            test_data = self.sheet.cell(row ,col).value #.encode('utf-8')
            return test_data

        def read_excel(self):
            list =[]
            for rowx in self.rows:
                if self.sheet.row_values(rowx)[0] != u'Test_case_name':
                    list.append(self.sheet.row_values(rowx,start_colx=0,end_colx=5))
            return list
        #[('case_name,method,url,header, data',type),]

        def get_requests_dict(self):
            dicts = self.read_excel()
            return  dicts

        def test_foo(self):
            print "class name is{},fn name is {}".format(self.__class__.__name__,sys._getframe().f_code.co_name)
            str = 'test_foo'
            fn_name = eval('str')
            print type(fn_name),type(sys._getframe().f_code.co_name) # str equal str
            try:
                assert  fn_name == sys._getframe().f_code.co_name
                print "yes!!!"
            except NameError as e:
                print e
            print "fn name is {}".format(inspect.stack()[0][3])
        def ensure_fn_name(self,fn):
            array = self.get_requests_dict()
            fn_name = array[0][0] # case_name
            type =eval(array[0][5])
            body =eval(array[0][4])
            method =eval(array[0][1])
            url = eval(array[0][2])
            header =eval(array[0][3])
            for tuple in array:
                if array[0][0] == fn :
                    if type == "data":
                        data = body
                    elif type == "json":
                        data = json.dumps(body)
                    else:
                        data =body
                    if method =='post':
                        response = session.request(method=method,headers=header,url=url,data=data,verify=False,)
                        txt = response.json()
                        return json.dumps(txt,encoding="UTF-8", ensure_ascii=False, sort_keys=True, indent=2, separators=(',', ': '))

                    elif method =='get':
                        response =session.request(method=method,url=url,params=data)
                        txt = response.json()
                        return json.dumps(txt,encoding="UTF-8", ensure_ascii=False, sort_keys=True, indent=2, separators=(',', ': '))
                        #times =response.elapsed.total_seconds()
                        # text =response.content.decode('utf-8')
if __name__ =="__main__":
    session = requests.session()