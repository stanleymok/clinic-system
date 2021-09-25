# Entities
## Patient
- String ID (Constrained to start with P)
- String Name
- Int Age
- Char Gender (Constrained to 'M' or 'F')
- List of Doctors
- List of Appointments
  
## Doctor
- String ID (Constrained to start with D)
- String Name
- List of Patients
- List of Appointments

## Appointments
- String ID (Constrained to start with A)
- String Date & Time (Constrained to 08:00:00 to 16:00:00)
- Doctor ID
- Patient ID


#### Q2 (H) Get all appointments for the given doctor & date 
- store in hashtable of key: doc_id + date_time -> value: Appointments
- clinic system server will provide appointments upon valid query (type gda -> doct id, date_time)

#### Q3 (H) Fix appointment by patient, doctor and date & time
- add to doct -> appt hashtable
- clinic system server will allow fixing appointments upon valid query (type aa -> patient id, doct id, date & time)

#### Q4 (H) Cancel appointment by patient, doctor and date & time
- del fr doct -> appt hashtable
- clinic system server will allow deleting appointments upon valid query (type da -> patient id, doct id, date & time)
