from src.models import Student

def test_student_creation_default():
    student = Student("João Silva", "joao@gmail.com", "ADS", 20)

    assert student.name == "João Silva"
    assert student.email == "joao@gmail.com"
    assert student.course == "ADS"
    assert student.age == 20
    assert "STU" in student.matricula
