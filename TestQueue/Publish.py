
#!/usr/bin/env python
import pika
import os
import json
import face_recognition


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='Face', durable=True)

for img in  os.listdir("face_128D"):
    read_image = face_recognition.load_image_file("face_128D/"+img)
    encode = face_recognition.face_encodings(read_image)[0]
        #res = encode.tolist()
    res =encode.tolist()
    channel.basic_publish(
                        exchange='',
                        routing_key='Face',
                        body= json.dumps(res),
                        properties=pika.BasicProperties(
                            delivery_mode=2,  # make message persistent
                        ))
    print(img[:-4])

print("All Message are finished")
connection.close()



# credentials = pika.PlainCredentials('labdaro18@kit.edu.k', 'Darolab@123')
# parameters = pika.ConnectionParameters('testhost',
#                                        5672,
#                                        '/',
#                                        credentials)
