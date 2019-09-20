import os
import face_recognition
import pika
import json
import numpy as np
import psycopg2
import os
import numpy as np
import face_recognition
# create a credentail connect to User of Queue
creddentail = pika.PlainCredentials('danei', '123456789')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, virtual_host='dane', credentials=creddentail))
channel = connection.channel()
#Information about the queue
channel.queue_declare(queue='test_queue3', durable=True)

attendence = []
def compare(data):
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "Daro@070818373",
                                      host = "127.0.0.1",
                                      port = "5432",
                                      database = "encode128")
        cursor = connection.cursor()
        SQLCode= "select * from dataset "
        cursor.execute(SQLCode)
        record = cursor.fetchall()
        for ENCODE in record:
            DATA_ENCODE = ENCODE[2][1:len(ENCODE[2])-1]
            numpy128D = np.asarray(DATA_ENCODE.split(), dtype=np.float64)
            print(type(numpy128D))
            distance = np.linalg.norm(data - numpy128D)
            print("{} {}".format(ENCODE[1], distance))
            if distance.item() <0.48:
                   attendence.append(ENCODE)
            print(attendence
                  )

    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PstgreSQL", error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")


def callback(ch, method, body):
        recieveData = json.loads(body)
        #convert to numpy array
        numpyArray =np.array(recieveData)
        convertString = numpyArray.tostring()
        dataNumpyArray = np.fromstring(convertString, dtype=float)
        print(dataNumpyArray)
        compare(dataNumpyArray)
        # take the dataset know image with Queue image
        # path = "ImageTest"
        # for image in os.listdir(path):
        #     load = face_recognition.load_image_file(path+"/" + image)
        #     encode = face_recognition.face_encodings(load)
        #     distance = np.linalg.norm(dataNumpyArray - encode)
        #     print("{} {}".format(image[:-4], distance))
        #     if distance.item() <0.48:
        #         attendence.append(image[:-4])
        # channel.stop_consuming()
        print("----------------------------------------------------------")
        ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='test_queue3', on_message_callback=callback)
channel.start_consuming()



