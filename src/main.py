import sys
import os
from db_manager import DBM

HELP_TEXTS = ["", "==================== HELP ========================", 
                "Read csv: type <read_csv>",
                "Get appts: type <get_appt>",
                "Fix appt: type <fix_appt>",
                "Del appt: type <del_appt>",
                "Exit: type <exit>",
                "Help: type <help> or any string unspecified above"] 
CWD = os.getcwd()
PATH_TO_INPUTS = "/../inputs/"


class Server:
    def __init__(self):
        self.dbm = DBM()
        self.dbm.create_tables()

    def print_help(self):
        for help_text in HELP_TEXTS:
            print(help_text) 

    def read_file(self):
        print("Input file name: ")
        file_name = input()
        f = open(CWD + PATH_TO_INPUTS + file_name,"r")
        lines = f.readlines()[1:]
        # data processing
        for line in lines:
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
            self.dbm.add_patient(patient_id, patient_name, patient_age, patient_gender)
            self.dbm.add_doctor(doc_id, doc_name)
            self.dbm.add_appt(appt_id, date, time, doc_id, patient_id, patient_name, patient_age, patient_gender)
        print("Read CSV successfully.")
        self.print_help()

    def get_doc_appts(self):
        print("Input doc_id:")
        doc_id = input()
        print("Input date: format <dd><mm><yyyy>")
        date = input()
        print("Input time: format <hh>:<mm>:<ss>")
        time = input()
        self.dbm.get_appts(doc_id, date, time)
        print("Select statement executed successfully.")
        self.print_help()

    def fix_appt(self):
        print("Input patient_name:")
        patient_name = input()
        print("Doctor's id:")
        doc_id = input()
        print("Input date: format <dd><mm><yyyy>")
        date = input()
        print("Input time: format <hh>:<mm>:<ss>")
        time = input()
        self.dbm.fix_appt(patient_name, doc_id, date, time)
        print("Insert statement executed successfully.")
        self.print_help()

    def del_appt(self):
        print("Input patient_name:")
        patient_name = input()
        print("Doctor's id:")
        doc_id = input()
        print("Input date: format <dd><mm><yyyy>")
        date = input()
        print("Input time: format <hh>:<mm>:<ss>")
        time = input()
        self.dbm.del_appt(patient_name, doc_id, date, time)
        print("============================================")
        print("Delete statement executed successfully.")
        self.print_help()

    def run(self):
        print("Type <help> for help")
        for line in sys.stdin:
            line = line.rstrip()
            if line == "read_csv":
                self.read_file()
            elif line == "get_appt":
                self.get_doc_appts()
            elif line == "fix_appt": # patient wont know his ID, and doc's ID, hence never include
                self.fix_appt()
            elif line =="del_appt":
                self.del_appt()
            elif line == "exit":
                break
            elif line == "help":
                self.print_help()
            else:
                self.print_help()
        self.dbm.close()

if __name__ == "__main__":
    server = Server()
    server.run()