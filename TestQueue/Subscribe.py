import os
import face_recognition
import pika
import json
import numpy as np
# create a credentail connect to User of Queue
creddentail = pika.PlainCredentials('danei', '123456789')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, virtual_host='dane', credentials=creddentail))
channel = connection.channel()
#Information about the queue
channel.queue_declare(queue='test_queue3', durable=True)

attendence = []
def callback(ch, method, body):
        recieveData = json.loads(body)
        #convert to numpy array
        numpyArray =np.array(recieveData)
        convertString = numpyArray.tostring()
        dataNumpyArray = np.fromstring(convertString, dtype=float)
        print(dataNumpyArray)

        # take the dataset know image with Queue image
        path = "ImageTest"
        for image in os.listdir(path):
            load = face_recognition.load_image_file(path+"/" + image)
            encode = face_recognition.face_encodings(load)
            distance = np.linalg.norm(dataNumpyArray - encode)
            print("{} {}".format(image[:-4], distance))
            if distance.item() <0.48:
                attendence.append(image[:-4])
        # channel.stop_consuming()
        print("----------------------------------------------------------")
        print(attendence)
        ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='test_queue3', on_message_callback=callback)
channel.start_consuming()



