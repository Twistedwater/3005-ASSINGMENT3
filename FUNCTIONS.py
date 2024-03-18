import psycopg2
conn = psycopg2.connect(host = "localhost", dbname="students", user="postgres", password ="postgres", port = 5432 )

cur =conn.cursor()

# function to return all students
def getAllStudents(conn):
    cur.execute("SELECT * FROM students;")
    for record in cur.fetchall():
        print(record)

# funcion to add students to table
def addStudent(conn, first_name, last_name, email, enrollment_date):
    cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);",
                    (first_name, last_name, email, enrollment_date))
    conn.commit()

#function to update students
def updateStudentEmail(conn, student_id, new_email):
    cur.execute("UPDATE students SET email = %s WHERE student_id = %s;",
                    (new_email, student_id))
    conn.commit()

def deleteStudent(conn,student_id):
    cur.execute("DELETE FROM students WHERE student_id = %s;",
            (student_id,))
    conn.commit()

# test for functions
print("Initial list of students:")
getAllStudents(conn)

print("\nAdding a new students:")
addStudent(conn, 'Joseph', 'jupiter', 'joseph@example.com', '2023-09-03')
getAllStudents(conn)

print("\nUpdating a student's email:")
updateStudentEmail(conn, 1, 'john.new@example.com')
getAllStudents(conn)

print("\nDeleting a student's email:")
deleteStudent(conn,7)
getAllStudents(conn)
