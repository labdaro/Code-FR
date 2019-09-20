import face_recognition
import os
import psycopg2
import numpy as np
try:
    connection = psycopg2.connect(user = "postgres",
                                  password = "Daro@070818373",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "encode128")

    cursor = connection.cursor()
    path = "SectionC"
    attendence = []
    for know in os.listdir(path):
        load = face_recognition.load_image_file(path + "/" + know)
        encode = face_recognition.face_encodings(load)[0]
        SQLCode = "select * from dataset "
        cursor.execute(SQLCode)
        record = cursor.fetchall()
        for ENCODE in record:
            DATA_ENCODE = ENCODE[2][1:len(ENCODE[2])-1]
            numpy128D = np.asarray(DATA_ENCODE.split(), dtype=np.float64)
            distance = np.linalg.norm(encode - numpy128D)
            print("{} {}".format(ENCODE[1], distance))
            if distance.item() < 0.40:
                attendence.append(ENCODE[1])
        print(attendence)


except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PstgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


