#
# import pika
# cre = pika.PlainCredentials('danei','123456789')
# connection = pika.BlockingConnection(
#     pika.ConnectionParameters(host='localhost', port=5672, virtual_host='dane', credentials=cre))
# channel = connection.channel()
#
# channel.queue_declare(queue='test_queue', durable=True)
# def callback(ch, method, properties, body):
#     print(body)
#     print(" [x] Done")
#     ch.basic_ack(delivery_tag=method.delivery_tag)
#
# channel.basic_qos(prefetch_count=1)
# channel.basic_consume(queue='test_queue', on_message_callback=callback)
# channel.start_consuming()
# import face_recognitiong
# load = face_recognition.load_image_file("ImageTest/Dane.jpg")
# encode = face_recognition.face_encodings(load)
# # print(encode)
import face_recognition
# import numpy as np
load = face_recognition.load_image_file("SectionC/ChenSokheng.jpg")
encode = face_recognition.face_encodings(load)[0]
for x in encode:
    print(type(x))
# x = np.array2string(encode, precision=10)
# print(x)

# print(res)
# print(type(res))

# print(encode)
# print(len(encode))
# convertString = encode.tostring()
# print(type(convertString))
#
# # dataNumpyArray = np.fromstring(convertString, dtype=float)
# # print(dataNumpyArray)
