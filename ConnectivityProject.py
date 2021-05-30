import mysql.connector
TeacherName = input("Enter teacher name: ")
Subject = input("Enter Subject name: ")
Punctuality = int(input("Punctuality Rating : "))
Knowledge = int(input("Knowledge on Topic Rating: "))
Comm = int(input("Communication Skills Rating: "))
Rating = int(input("Final Rating: "))

# establishing the connection
conn = mysql.connector.connect(
    user='root', password='password', host='localhost', database='Survey')

# Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Preparing SQL query to INSERT a record into the database.
insert_stmt = (
    "INSERT INTO FEEDBACK(TEACHER_NAME, SUBJECT, PUNCTUALITYRATING_OUT_OF_5, KNOWLEDGEOFSUBJECT_OUT_OF_5, COMMUNICATIONSKILLS_OUT_OF_5, FINALRATING_OUT_OF_5)"
    "VALUES (%s, %s, %s, %s, %s)"
)
data = (TeacherName, Subject, Punctuality, Knowledge, Comm, Rating)

try:
    # Executing the SQL command
    cursor.execute(insert_stmt, data)

    # Commit your changes in the database
    conn.commit()

except:
    # Rolling back in case of error
    conn.rollback()

print("Data inserted")

# Closing the connection
conn.close()
