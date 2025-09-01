from datetime import datetime
from typing import Dict


class Student:
    """Classe que representa um estudante no sistema."""
    
    def __init__(self, name: str, email: str, course: str, age: int):
        self.matricula = self._generate_matricula()
        self.name = name
        self.email = email
        self.course = course
        self.age = age
        self.registration_date = datetime.now().strftime("%Y-%m-%d")
    
    @staticmethod
    def _generate_matricula() -> str:
        """Gera uma matrícula única baseada no timestamp."""
        return f"STU{datetime.now().strftime('%Y%m%d%H%M%S')}"
    
    def to_dict(self) -> Dict:
        """Converte o estudante para dicionário."""
        return {
            'matricula': self.matricula,
            'name': self.name,
            'email': self.email,
            'course': self.course,
            'age': self.age,
            'registration_date': self.registration_date
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Student':
        """Cria um estudante a partir de um dicionário."""
        student = cls(data['name'], data['email'], data['course'], data['age'])
        student.matricula = data['matricula']
        student.registration_date = data['registration_date']
        return student
    
    def __str__(self) -> str:
        return f"Matrícula: {self.matricula} | Nome: {self.name} | Curso: {self.course} | Email: {self.email} | Idade: {self.age}"