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
                print ("PATIENTS Table opened/created successfully")
                self.conn.execute('''CREATE TABLE IF NOT EXISTS DOCTORS
                        (DOC_ID        VARCHAR(10) PRIMARY KEY NOT NULL,
                        NAME           VARCHAR(50)    NOT NULL)
                        ;''')
                print("DOCTORS Table opened/created successfully")
                self.conn.execute('''CREATE TABLE IF NOT EXISTS APPOINTMENTS
                        (APPT_ID        VARCHAR(15) PRIMARY KEY NOT NULL,
                        DATE            CHAR(8) NOT NULL,
                        TIME            CHAR(8) NOT NULL,
                        DOC_ID          VARCHAR(10) NOT NULL,
                        PATIENT_ID      VARCHAR(10),
                        PATIENT_NAME    VARCHAR(50) NOT NULL,
                        PATIENT_AGE     INT,
                        PATIENT_GENDER  CHAR(1))
                        ;''')
                print("APPOINTMENTS Table opened/created successfully")

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
                                        values (?, ?, ?, ?, ?, ?, ?, ?)", (appt_id, date, time, d_id, p_id, p_name, p_age, p_gender))
                self.conn.commit()

        def get_appts(self, doc_id, date, time):
                print("\n===================== RUNNING =======================")
                cursor = self.conn.execute(f"SELECT * FROM APPOINTMENTS WHERE DOC_ID = \"{doc_id}\" AND DATE = \"{date}\" AND TIME = \"{time}\";")
                for row in cursor:
                        print(row)
                print("Select statement executed successfully.")
                                
        def fix_appt(self, patient_name, doc_id, date, time):
                print("\n===================== RUNNING =======================")
                time_wo_colon = time[0:2] + time[3:5] + time[6:8]
                if time_wo_colon >= "080000" and time_wo_colon <= "160000":
                        # get biggest appt_id primary key from table and increment
                        cursor = self.conn.execute(f"SELECT MAX(APPT_ID) FROM APPOINTMENTS")                           
                        appt_id = cursor.fetchone()[0]
                        # inc id by one
                        appt_id = appt_id[0] + str(int(appt_id[1:]) + 1)
                        self.conn.execute("INSERT INTO APPOINTMENTS (APPT_ID, PATIENT_NAME, DOC_ID, DATE, TIME) \
                                                values (?, ?, ?, ?, ?)", (appt_id, patient_name, doc_id, date, time))
                        self.conn.commit()
                        print("Insert statement executed successfully.")
                else:
                        print("Doctor's consultation time between 080000 to 160000")

        def del_appt(self, patient_name, doc_id, date, time):
                print("\n===================== RUNNING =======================")
                self.conn.execute(f"DELETE FROM APPOINTMENTS WHERE PATIENT_NAME = \"{patient_name}\" AND DOC_ID = \
                                        \"{doc_id}\" AND  DATE = \"{date}\" AND TIME = \"{time}\";")
                self.conn.commit()
                print("Delete statement executed successfully.")


        def close(self):
                self.conn.close()