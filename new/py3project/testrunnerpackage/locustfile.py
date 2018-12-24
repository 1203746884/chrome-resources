# coding =utf-8
from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):

    def on_start(self):
        self.login()

        """ 类似初始化调用locust后任何任务在被执行前的准备工作"""

    def login(self):
        self.client.post("/login", {"username": "ellen_key", "password": "education"})

    @task(2)
    def index(self):
        self.client.get("/")

    @task(1)
    def profile(self):
        self.client.get("/profile")


# 继承Httplocust类
class WebsiteUser(HttpLocust):
    TaskSet = UserBehavior
    min_wait = 1000
    max_wait = 15000
    # https://docs.locust.io/en/latest/quickstart.html
    # https://blog.csdn.net/a464057216/article/details/48448231
    # https://blog.csdn.net/guangyinglanshan/article/details/78910472
# """ 文件执行方式，第一直接进入locust 文件所在目录执行locust ;
#     第二：进入locust.py文件所在目录，执行locust -f  文件名此处为locustfile.py
#     第三：locust -f  指定脚本名此处为locust_test.py  --host=http://example.com #指定服务器
#
#
#     如果我们想在多台机器上运行分布式Locust，我们还必须在启动从机时指定主机
#     （在运行分布在单台机器上的Locust时不需要这样做，因为主机主机默认为127.0.0.1）：
#      locust -f locust_files/my_locust_file.py --slave --master-host=192.168.0.100 --host=http://example.com
#     """

# 要运行分布在多个进程中的Locust，我们将通过指定--master以下内容来启动主进程,
# locust -f locust_files/my_locust_file.py --master --host=http://example.com

# 然后我们将启动任意数量的从属进程：
# locust -f locust_files/my_locust_file.py --slave --host=http://example.com，


