# import numpy as np
# numList = ['1', '2', '3', '4','1', '2', '3', '4']
# seperator = ' '
# res =seperator.join(numList)
# dataNumpyArray = np.fromstring(res, dtype=float)

import numpy as np
import face_recognition
load = face_recognition.load_image_file("SectionC/LabDaro.jpg")
encode = face_recognition.face_encodings(load)[0]
x = np.array2string(encode,precision=9)
print(x)