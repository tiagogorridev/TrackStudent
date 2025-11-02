from database import DatabaseManager
from models import Student

def test_add_and_find_student():
    db = DatabaseManager("test_db.json")
    student = Student("Ana", "ana@gmail.com", "ADS", 20)

    result = db.add_student(student)
    assert result == True

    found = db.find_student_by_matricula(student.matricula)
    assert found is not None
