# coding=utf=8

import yaml
import json
"""写入 yaml"""
with open('./dump.yaml','w') as f:
     data ={
             {'测试登陆接口':
                        {'url':'aa',
                        'method': 'post',
                        'param': {"key1": "value1"},
                        'header': {"Content-Type": "application/json"},
                        'data':{
                            'ball':'volleyball',
                            'book':'Python'
                               }
                        }
            }
                # {'保存用户接口':
                #         {
                #         'url': 'bb',
                #         'method': 'get',
                #          'header': '{"Content-Type": "application/json"}',
                #         'param': '{"key2": "value2"}'
                #         }
                # }
            }
     yaml.dump(data,f)

#"""读取yaml内容"""
with open("./dump.yaml", 'r') as f:
    d=yaml.load(f)
    print d


