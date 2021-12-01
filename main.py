
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from rediscluster import RedisCluster

def hello_world():

    redisCluster = RedisCluster(
        host="127.0.0.1",
        port=6379,
        decode_responses=True,
        skip_full_coverage_check=True,
    )
    redisCluster.set("MyFirstValue", "Hello World")
    print(redisCluster.get("MyFirstValue"))


if __name__ == '__main__':
    hello_world()


