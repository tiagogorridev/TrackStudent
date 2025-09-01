import json
from typing import List, Dict, Optional
from models import Student


class DatabaseManager:
    """Gerenciador de dados dos estudantes."""
    
    def __init__(self, filename: str = "students_data.json"):
        self.filename = filename
        self.students: List[Student] = []
        self.load_data()
    
    def load_data(self):
        """Carrega dados dos estudantes do arquivo."""
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.students = [Student.from_dict(student_data) for student_data in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.students = []
    
    def save_data(self):
        """Salva dados dos estudantes no arquivo."""
        try:
            with open(self.filename, 'w', encoding='utf-8') as file:
                data = [student.to_dict() for student in self.students]
                json.dump(data, file, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"Erro ao salvar dados: {e}")
            return False
    
    def add_student(self, student: Student) -> bool:
        """Adiciona um estudante ao banco de dados."""
        self.students.append(student)
        return self.save_data()
    
    def find_student_by_matricula(self, matricula: str) -> Optional[Student]:
        """Busca um estudante pela matrícula."""
        for student in self.students:
            if student.matricula == matricula:
                return student
        return None
    
    def find_students_by_name(self, name: str) -> List[Student]:
        """Busca estudantes pelo nome (busca parcial)."""
        name_lower = name.lower()
        return [student for student in self.students if name_lower in student.name.lower()]
    
    def update_student(self, matricula: str, updated_data: Dict) -> bool:
        """Atualiza dados de um estudante."""
        student = self.find_student_by_matricula(matricula)
        if student:
            if 'name' in updated_data:
                student.name = updated_data['name']
            if 'email' in updated_data:
                student.email = updated_data['email']
            if 'course' in updated_data:
                student.course = updated_data['course']
            if 'age' in updated_data:
                student.age = updated_data['age']
            return self.save_data()
        return False
    
    def remove_student(self, matricula: str) -> bool:
        """Remove um estudante do banco de dados."""
        student = self.find_student_by_matricula(matricula)
        if student:
            self.students.remove(student)
            return self.save_data()
        return False
    
    def get_all_students(self) -> List[Student]:
        """Retorna todos os estudantes cadastrados."""
        return self.students.copy()
    
    def get_students_count(self) -> int:
        """Retorna o número total de estudantes."""
        return len(self.students)