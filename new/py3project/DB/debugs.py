# coding=utf-8
import os
import ConfigParser
config_dir = os.path.split(os.path.realpath(__file__))[0]
config_path = os.path.join(config_dir, "config.ini")
config = ConfigParser.SafeConfigParser()
config.read(config_path)
name=config.get('数据库测试接口', "name")
