import face_recognition
import os

path = "sectionC"
for image in os.listdir(path):
    load = face_recognition.load_image_file(path +"/"+image)
    encode = face_recognition.face_encodings(load)
    print(image)
    print(encode)