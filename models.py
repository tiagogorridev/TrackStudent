"""
Models - Definição das classes de modelo do sistema TrackStudent.
"""

from datetime import datetime
from typing import Dict


class Student:
    """Classe que representa um estudante no sistema TrackStudent."""
    
    def __init__(self, name: str, email: str, course: str, age: int):
        """Inicializa uma nova instância de Student."""
        self.matricula = self._generate_matricula()
        self.name = name
        self.email = email
        self.course = course
        self.age = age
        self.registration_date = datetime.now().strftime("%Y-%m-%d")
    
    @staticmethod
    def _generate_matricula() -> str:
        """Gera uma matrícula única baseada no timestamp atual."""
        return f"STU{datetime.now().strftime('%Y%m%d%H%M%S')}"
    
    def to_dict(self) -> Dict:
        """Converte a instância do estudante para um dicionário."""
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
        """Cria uma instância de Student a partir de um dicionário."""
        student = cls(data['name'], data['email'], data['course'], data['age'])
        student.matricula = data['matricula']
        student.registration_date = data['registration_date']
        return student
    
    def __str__(self) -> str:
        """Retorna uma representação em string do estudante."""
        return (f"Matrícula: {self.matricula} | Nome: {self.name} | "
                f"Curso: {self.course} | Email: {self.email} | Idade: {self.age}")