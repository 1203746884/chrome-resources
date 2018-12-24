# coding=utf-8
import json
import os
login = {"url": "http://192.168.229.128:8080/cms/manage/loginJump.do",
         "data": "{'userAccount': 'admin', 'loginPwd': '123456'}"}
save_user = {"url": "http://192.168.229.128:8080/cms/manage/saveSysUser.do",
             "data": "{'userName': 'zhangsan', 'userEmail': '1932390299@qq.com',"
                    "'userMobile': '18871027706', 'userSex': '1','userAccount': 'dev',"
                    " 'confirmPwd': '123456', 'loginPwd': '123456', 'id': ''}"}
json_str = json.dumps(login)  # dict to str
json_str1 = json.dumps(save_user)  # dict to str
str_json = json.loads(json_str)  # str to dict
str1_json = json.loads(json_str1)  # str to dict
# 文件数据类型dict作为字符串存储入json文件
json_file_path = os.path.join(os.getcwd(), 'utils.json')
json_to_str= json.dump(str_json,open(json_file_path, 'w'))

print "文件写入完成"
json_dict = json.load(open(json_file_path))
print json.dumps(json_dict)


# import json
# import re
# import sys
# import os
# s="愿你合上笔盖的刹那，有着侠客收剑入鞘的骄傲"
# s=re.sub(r"(.{16})","\\1\n",s)
# print(s)