# coding = utf-8

import os
import ConfigParser
config_dir = os.path.split(os.path.realpath(__file__))[0]
config_path = os.path.join(config_dir, "config.ini")


def get_config_value(section, option):
    config = ConfigParser.SafeConfigParser()
    config.read(config_path)
    value = config.get(section='config', option='ip')
    print type(value)
    print config.options("config")
    print config.items("mysqlconf")
    print config.sections()  # 名字
    # return value


def has_config():
    config = ConfigParser.SafeConfigParser()
    config.read(config_path)
    print config.has_option("config", "port")
    print config.has_section("config")

    print config.options("config")
    config.set("config","host","192.168.110.2")
    print config.items("config")
    # config.remove_option('config', 'host')
    config.add_section('new_sect')
    print config.sections()


def allow_no_value():
    config = ConfigParser.SafeConfigParser(allow_no_value=True)
    config.read(config_path)
    print config.get("config","name")

get_config_value("config", "db_name")
# has_config()
# allow_no_value()
