from fastapi import FastAPI
import mysql.connector
from pydantic import BaseModel
from typing import List

app = FastAPI()

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="course_recommendation"
)

cursor = db.cursor()

class Student(BaseModel):
    name: str
    course: str
    class_level: str
    field: str
    gpa: float
    cgpa: float
    
@app.post("/add_students/")
def add_students(student: Student):
    sql = "INSERT INTO students (name, course, class_level, field, gpa, cgpa) VALUES (%s, %s, %s, %s, %s,%s )"
    cursor.execute(sql, (student.name, student.course, student.class_level, student.field, student.gpa, student.cgpa))
    db.commit()


@app.get("/recommend/{student_id}")
def recommend_courses(student_id: int):
    cursor.execute("SELECT course, class_level, field, gpa, cgpa FROM students WHERE id = %s", (student_id,))
    student = cursor.fetchone()

    if not student:
        return {"error": "Student not found"}
    
    course, class_level, field, gpa, cgpa = student

    if gpa > 3.5:
        level = "Advanced"

    elif gpa > 2.5:
        level = "Intermediate"

    else:
        level = "Beginner"

    cursor.execute(
        "SELECT course_name, FROM courses WHERE field = %s AND difficulty_level = %s", 
        (field, level)
        )
    courses = [row[0] for row in cursor.fetchall()]

    cursor.execute(
      "SELECT title, material_type FROM materials WHERE difficulty_level = %s",  
     (level,)
    )
    materials =[{"title": row[0], "type": row[1]} for row in cursor.fetchall()]
    
    return {"recommended_courses": courses, "recommended_materials": materials}
