# coding=utf-8
import requests
cookie={"dc_session_id": "10_1541690279946.617154"}
js =[{"headers":{"component":"enterprise","datatype":"re","version":"v1"},
      "body":"{\"re\":\"ref=https%3A%2F%2Fpassport.csdn.net%2Faccount%2Fverify&mtp=2&mod=ad_popu_282&con=ad_content_3743%2Cad_order_719&uid=chen498858336&ck=-\"}"}]

url="https://pv.csdn.net/csdnbi"
header ={"Content-Type": "text/plain;charset=UTF-8"}
rep =requests.post(url=url,headers=header,json=js,cookies=cookie)
print rep.content