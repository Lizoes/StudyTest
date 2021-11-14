# @Time    : 2021/11/14 17:50
# @Author  : Lizo
# @File    : producer.py


import pika


def simple():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    # queue="test"，声明一个名字为test的队列
    # durable=True声明可持久化的队列，防止rabbitmq服务挂了导致数据丢失。队列只能声明一次是否为可持久化的
    channel.queue_declare(queue="test", durable=True)

    # 向队列丢入数据,并且在每次丢入数据时可以选择数据是否持久化
    channel.basic_publish(exchange='',
                          routing_key='test',
                          body=b'1',
                          properties=pika.BasicProperties(delivery_mode=2)
                          )
    channel.close()


def fanout():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    # 此时没有涉及队列，但是需要声明一个交换机，类型为fanout
    channel.exchange_declare(exchange="book", exchange_type="fanout")

    # 向队列丢入数据,并且在每次丢入数据时可以选择数据是否持久化
    channel.basic_publish(exchange='book',
                          routing_key='',
                          body=b'1',
                          properties=pika.BasicProperties(delivery_mode=2)
                          )
    channel.close()


def direct():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    # 此时没有涉及队列，但是需要声明一个交换机，direct
    channel.exchange_declare(exchange="log", exchange_type="direct")

    # 向队列丢入数据,并且在每次丢入数据时可以选择数据是否持久化
    channel.basic_publish(exchange='log',
                          routing_key='',
                          body=b'1',
                          properties=pika.BasicProperties(delivery_mode=2)
                          )
    channel.close()


def topic():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    # 此时没有涉及队列，但是需要声明一个交换机，topic
    channel.exchange_declare(exchange="school", exchange_type="topic")

    # *代表一个，#代表一个或多个
    channel.basic_publish(exchange='school',
                          routing_key='primary.one',
                          body=b'1',
                          properties=pika.BasicProperties(delivery_mode=2)
                          )
    channel.basic_publish(exchange='school',
                          routing_key='primary.two',
                          body=b'1',
                          properties=pika.BasicProperties(delivery_mode=2)
                          )
    channel.close()