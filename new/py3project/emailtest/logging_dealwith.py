# coding=utf-8
import logging
import os
import time
import logging.handlers


class TestLogger(object):
    def __init__(self, log_dir_path):
        # logs 文件父目录
        self.log_dir_path = log_dir_path
        if os.path.exists(log_dir_path) and os.path.isdir(log_dir_path):
            pass
        else:
            os.mkdir(log_dir_path)
        time_stamp_name = time.strftime("%Y-%m-%d-%a", time.localtime())
        log_name = time_stamp_name + ".log"
        # logs 文件路径
        self.log_path = os.path.join(log_dir_path, log_name)
        # logs 文件输出格式
        self.log_format = "[%(asctime)s] log output from:%(pathname)s \n" \
            "module named:[%(funcName)s],The specific number of lines " \
            " is line %(lineno)d\nLog level[%(levelname)s]:%(message)s"
        self.date_format = "%Y-%m-%d %H:%M:%S %a"

        """logs在文件输出格式控制"""
        logging.basicConfig(level=logging.DEBUG,
                            format=self.log_format,
                            datefmt=self.date_format,
                            filename=self.log_path)

        """  logs文件内容转换控制台输出，文件处理器处理when：是一个字符串，用于描述滚动周期的基本单位，字符串的值及意义如下：
            “S”: Seconds
            “M”: Minutes
            “H”: Hours
            “D”: Days
            “W”: Week day (0=Monday)
            “midnight”: Roll over at midnight
            interval: 滚动周期，单位有when指定，比如：when=’D’,interval=1，表示每天产生一个日志文件；
            backupCount: 表示日志文件的保留个数；
        """

        # rotating_file_handler = logging.handlers.RotatingFileHandler(filename=self.log_path,
        #                                                              maxBytes=1024 * 1024 * 50,
        #                                                              backupCount=2)
        rotating_file_handler = logging.handlers.TimedRotatingFileHandler(filename=self.log_path,
                                                                     interval=1,
                                                                     backupCount=3,when='M')

        rotating_file_handler.setFormatter(self.log_format)

        """python控制台句柄设置输出日志格式"""
        self.console = logging.StreamHandler()
        self.console.setLevel(logging.NOTSET)
        self.console_format = logging.Formatter(self.log_format)
        self.console.setFormatter(self.console_format)

    """添加日志content到句柄并返回添加完成的句柄 """
    def console_log(self):
        logger = logging.getLogger()
        logger.addHandler(self.console)
        logger.setLevel(logging.DEBUG)
        return logger


if __name__ == "__main__":
    logs = TestLogger('./logs').console_log()
    logs.info("111000")
    logs.warning("war_start")
    logs.critical("criminal")
    logs.error("error00001")


