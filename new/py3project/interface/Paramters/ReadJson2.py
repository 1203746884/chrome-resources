# coding=utf-8
import  json
import requests
data ={"登陆接口":
           {"method": "post",
                    "url": "https://pv.csdn.net/csdnbi",
                    "data": [{"headers":{"component":"enterprise","datatype":"re","version":"v1"},"body":"{\"re\":\"ref=https%3A%2F%2Fpassport.csdn.net%2Faccount%2Fverify&mtp=2&mod=ad_popu_282&con=ad_content_3743%2Cad_order_719&uid=chen498858336&ck=-\"}"}],
       "header": {"Content-Type": "text/plain;charset=UTF-8"},
        "cookie": {"dc_session_id": "10_1541690279946.617154"},
        "author": "JackChen"
    }
 }

class JsonTransfer(object):
    """3.x以上的json文件读取中文乱码用这个解决,3.x默认utf-8,dump你再加异常很bug"""
    def write_read_json(self):
        with open('./ReadJson.json', 'w')as f:
            json.dump(data,f,ensure_ascii=False,separators=(',',':'),sort_keys=True,indent=3)
        f= open('./ReadJson.json','r')
        dict =json.load(f)
        # print(dict)
        """如果有人还有问题请用以下输出,注意3.x默认encoding=utf-8,你再加就异常了dumps里面"""
        """------------------"""
        report_show = json.dumps(dict,ensure_ascii=False,indent=3,separators=(',', ':'))
        print(report_show)
        """--------------------"""

        cookie=dict['登陆接口']['cookie']
        js =dict['登陆接口']['data']

        url=dict['登陆接口']['url']
        header =dict['登陆接口']['header']
        rep =requests.post(url=url,headers=header,json=js,cookies=cookie)
        return rep.text  #在2.x这里是content也可以的3.x，我都不想吐槽了

if __name__ == "__main__":
   print(JsonTransfer().write_read_json())
