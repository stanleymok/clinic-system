import sys
import os
from db_manager import DBM

HELP_TEXTS = ["", "==================== HELP ========================", 
                "Read csv: type <read_csv> then type <file_name> in inputs folder"
                "Get appts: type <get_appt> then type <doc_id><space><date_time>",
                "Add appt: type <add_appt> then type <patient_id><space><doct_id><space><date_time>",
                "Del appt: type <del_appt> then type <patient_id><space><doct_id><space><date_time>",
                "Exit: type <exit>",
                "Help: type <help> or any string unspecified above"] 
CWD = os.getcwd()
PATH_TO_INPUTS = "/../inputs/"


def read_file(file_name, dbm):
    f = open(CWD + PATH_TO_INPUTS + file_name,"r")
    lines = f.readlines()[1:]
    # data processing
    for line in lines:
        print(line)
        data = line.split(", ")
        if len(data) < 8: 
            continue
        doc_id = data[0]
        doc_name = data[1]
        patient_id = data[2]
        patient_name = data[3]
        patient_age = data[4]
        patient_gender = data[5]
        appt_id = data[6]
        date_time = data[7]
        date_time = date_time.split()
        date = date_time[0]
        time = date_time[1]
        # add to db
        dbm.add_patient(patient_id, patient_name, patient_age, patient_gender)
        dbm.add_doctor(doc_id, doc_name)
        dbm.add_appt(appt_id, date, time, doc_id, patient_id, patient_name, patient_age, patient_gender)


def get_doc_appts(doc_id, date, time):
    dbm.get_appts(doc_id, date, time)


if __name__ == "__main__":
    dbm = DBM()
    dbm.create_tables()

    print("Type <help> for help")
    for line in sys.stdin:
        line = line.rstrip()
        if line == "read_csv":
            print("Input file name: ")
            read_file(input(), dbm)
        elif line == "get_appt":
            print("Input doc_id:")
            doc_id = input()
            print("Input date: format <dd><mm><yyyy>")
            date = input()
            print("Input time: format <hh>:<mm>:<ss>")
            time = input()
            get_doc_appts(doc_id, date, time)
        elif line == "add_appt":
            pass
        elif line =="del_appt":
            pass
        elif line == "exit":
            break
        elif line == "help":
            for help_text in HELP_TEXTS:
                print(help_text) 
        else:
            for help_text in HELP_TEXTS:
                print(help_text) 

    dbm.close()