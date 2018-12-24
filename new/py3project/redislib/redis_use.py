# coding =utf-8
import redis

# cmd=redis-server.exe  redis.conf
# download_url =https://github.com/MicrosoftArchive/redis/releases
redisConnect = redis.Redis(host='localhost', port=6379, decode_responses=True)
redisConnect.set('name', value='chen')
print redisConnect.get('name')  # single get data_value equal:print redisConnect['name']

redisConnect.mset(GitId='GitCommitId', SvnNum='CD_DevOps')  # set many key=value
print redisConnect.mget({'GitId': 'GitCommitId', 'SvnNum': 'CD_DevOps'}) # equal :redisConnect.mget(['GitId', 'SvnNum'])
ss=redisConnect.mget(('GitId', 'SvnNum'))
