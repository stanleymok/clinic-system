import sqlite3

class DBM:

        def __init__(self):
                self.conn = sqlite3.connect('clinic.db')
                print ("Opened database successfully")

        def create_tables(self):
                self.conn.execute('''CREATE TABLE IF NOT EXISTS PATIENTS
                        (PATIENT_ID    VARCHAR(10) PRIMARY KEY NOT NULL,
                        NAME           VARCHAR(50)    NOT NULL,
                        AGE            INT     NOT NULL,
                        GENDER         CHAR(1)     NOT NULL)
                        ;''')
                print ("PATIENTS Table created successfully")
                self.conn.execute('''CREATE TABLE IF NOT EXISTS DOCTORS
                        (DOC_ID        VARCHAR(10) PRIMARY KEY NOT NULL,
                        NAME           VARCHAR(50)    NOT NULL)
                        ;''')
                print("DOCTORS Table created successfully")
                self.conn.execute('''CREATE TABLE IF NOT EXISTS APPOINTMENTS
                        (APPT_ID       VARCHAR(15) PRIMARY KEY NOT NULL,
                        DATE           CHAR(8) NOT NULL,
                        TIME           CHAR(8) NOT NULL,
                        DOC_ID        VARCHAR(10),
                        PATIENT_ID    VARCHAR(10) NOT NULL,
                        PATIENT_NAME           VARCHAR(50) NOT NULL,
                        PATIENT_AGE            INT     NOT NULL,
                        PATIENT_GENDER         CHAR(1)     NOT NULL)
                        ;''')
                print("APPOINTMENTS Table created successfully")

        def add_patient(self, id, name, age, gender):
                self.conn.execute("INSERT OR IGNORE INTO PATIENTS (PATIENT_ID,NAME,AGE,GENDER) values (?, ?, ?, ?)",
                        (id, name, age, gender))
                self.conn.commit()
        def add_doctor(self, id, name):
                self.conn.execute("INSERT OR IGNORE INTO DOCTORS (DOC_ID,NAME) values (?, ?)",
                        (id, name))
                self.conn.commit()
        def add_appt(self, appt_id, date, time, d_id, p_id, p_name, p_age, p_gender):
                self.conn.execute("INSERT OR IGNORE INTO APPOINTMENTS (APPT_ID,DATE,TIME,DOC_ID,PATIENT_ID,PATIENT_NAME,PATIENT_AGE,PATIENT_GENDER) \
                        values (?, ?, ?, ?, ?, ?, ?, ?)",
                        (appt_id, date, time, d_id, p_id, p_name, p_age, p_gender))
                self.conn.commit()

        def get_appts(self, doc_id, date, time):
                cursor = self.conn.execute(f"SELECT * FROM APPOINTMENTS WHERE DOC_ID = \"{doc_id}\" AND DATE = \"{date}\" AND TIME = \"{time}\";")
                for row in cursor:
                        print(row)

        def close(self):
                self.conn.close()