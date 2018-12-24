# coding=utf-8
"""再老的版本用下面这个utf-8设置，很bug"""
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

import  json
import requests

data ={"登陆接口":
           {"method": "post",
                    "url": "https://pv.csdn.net/csdnbi",
                    "data": [{"headers":{"component":"enterprise","datatype":"re","version":"v1"},"body":"{\"re\":\"ref=https%3A%2F%2Fpassport.csdn.net%2Faccount%2Fverify&mtp=2&mod=ad_popu_282&con=ad_content_3743%2Cad_order_719&uid=chen498858336&ck=-\"}"}],
       "header": {"Content-Type": "text/plain;charset=UTF-8"},
        "cookie": {"dc_session_id": "10_1541690279946.617154"},
        "author": "JackChen",
        "bug": "我想吐槽"
    }
 }

class JsonTransfer(object):
    """2.7-3.0以下的版本json文件读取中文乱码用这种可以解决，transefer函数转换json.load()中文编码乱码问题"""
    def transfer(self,obj):
        if isinstance(obj, dict):
            return {self.transfer(key):self.transfer(value) for key,value in obj.iteritems()}
        elif isinstance(obj, list):
            return [self.transfer(element) for element in obj]
        elif isinstance(obj, unicode):
            return obj.encode('utf-8')
        else:
            return obj

    """3.x以上的json文件读取中文乱码用这个解决"""
    def write_read_json(self):
        with open('./ReadJson.json', 'w')as f:
            json.dump(data,f,ensure_ascii=False,separators=(',',':'),sort_keys=True,indent=2,encoding='utf-8')
        f= open('./ReadJson.json','r')
        dt =json.load(f) # 2.x读取出来都是Unicode
        dict =self.transfer(dt) # unicode转换utf-8
        print dict
        print dict['登陆接口']['bug']
        """如果你是要输出报告请用下面转换,请求请用上面"""
        """------------------"""
        results = json.dumps(dict,ensure_ascii=False,encoding='utf-8',indent=3,separators=(',', ':'))
        print(results)
        """-------------------"""
        cookie=dict['登陆接口']['cookie']
        js =dict['登陆接口']['data']
        # print dict['登陆接口']['bug']
        url=dict['登陆接口']['url']
        header =dict['登陆接口']['header']
        rep =requests.post(url=url,headers=header,json=js,cookies=cookie)
        print rep.content  #2.x这里content也可以，3.x不可以只能text

if __name__ == "__main__":
    JsonTransfer().write_read_json()

