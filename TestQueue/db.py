import psycopg2
import os
import numpy as np
import face_recognition


try:
    connection = psycopg2.connect(user = "postgres",
                                  password = "Daro@070818373",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "encode128")

    cursor = connection.cursor()
    # path = "SectionC"
    # STUDENT_ID = 1101801079
    # for student in os.listdir(path):
    #     load = face_recognition.load_image_file(path +"/" + student)
    #     encode = face_recognition.face_encodings(load)[0]
    #     data128D = np.array2string(encode, precision=10)
    #     insert = f"insert into dataset(id,name,encode) values('{STUDENT_ID}','{student[:-4]}','{data128D}')"
    #     print(student[:-4]+" is successfully")
    #     cursor.execute(insert)
    #     connection.commit()
    #     STUDENT_ID += 1
    res = "select encode from dataset "
    cursor.execute(res)
    record = cursor.fetchall()
    print(record)




    # res = "select encode_data from sectionC"
    # cursor.execute(res)
    # record = cursor.fetchone()
    # print(record)

    # path = "SectionC"
    # ID = 1101801079
    # for STUDEN_NAME in os.listdir(path):
    #     insert = f"insert into sectionC(id,name) values('{ID}','{STUDEN_NAME[:-4]}')"
    #     cursor.execute(insert)
    #     connection.commit()
    #     ID += 1
    # print("All sucessfully")

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PstgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")