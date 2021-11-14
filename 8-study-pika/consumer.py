# @Time    : 2021/11/14 17:55
# @Author  : Lizo
# @File    : consumer.py


import pika
from pika.adapters.blocking_connection import BlockingChannel

def callback(ch: BlockingChannel, method, properties, body):
    print(body)
    """
    消费者从队列中取出数据后，队列中的该就没了，这里手动确认
    """
    ch.basic_ack(delivery_tag=method.delivery_tag)


def simple():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue="test")

    # 公平分发，
    channel.basic_qos(prefetch_count=1)

    # auto_ack=False手动确认:因为队列中的数据被取出来后就没了，防止在callback函数中出错而导致数据无法恢复
    channel.basic_consume(queue='test', on_message_callback='callback', auto_ack=False)
    channel.start_consuming()


def fanout():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.exchange_declare(exchange="book", exchange_type="fanout")

    channel.queue_declare(queue="fanout_queue_book")
    channel.queue_bind(queue="fanout_queue_book", exchange="book")

    # auto_ack=False手动确认:因为队列中的数据被取出来后就没了，防止在callback函数中出错而导致数据无法恢复
    channel.basic_consume(queue='fanout_queue_info  ', on_message_callback='callback', auto_ack=False)
    channel.start_consuming()


def direct():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.exchange_declare(exchange="log", exchange_type="direct")

    channel.queue_declare(queue="direct_queue_log")
    channel.queue_bind(queue="direct_queue_log", exchange="log", routing_key="debug")
    # channel2.queue_bind(queue="direct_queue_log", exchange="log", routing_key="info")
    # channel3.queue_bind(queue="direct_queue_log", exchange="log", routing_key="error")
    # channel3.queue_bind(queue="direct_queue_log", exchange="log", routing_key="warm")   # 可以同时关联多个，但是要份两行写

    # auto_ack=False手动确认:因为队列中的数据被取出来后就没了，防止在callback函数中出错而导致数据无法恢复
    channel.basic_consume(queue='fanout_queue_info  ', on_message_callback='callback', auto_ack=False)
    channel.start_consuming()


def topic():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.exchange_declare(exchange="school", exchange_type="topic")

    channel.queue_declare(queue="topic_queue_school")
    channel.queue_bind(queue="topic_queue_school", exchange="topic", routing_key="primary.one")
    # channel2.queue_bind(queue="topic_queue_school", exchange="topic", routing_key="primary.#")
    # channel3.queue_bind(queue="topic_queue_school", exchange="topic", routing_key="*.one")

    # auto_ack=False手动确认:因为队列中的数据被取出来后就没了，防止在callback函数中出错而导致数据无法恢复
    channel.basic_consume(queue='topic_queue_school  ', on_message_callback='callback', auto_ack=False)
    channel.start_consuming()
