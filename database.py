"""
Database - Módulo de gerenciamento de persistência de dados.
"""

import json
import os
from typing import List, Dict, Optional
from models import Student


class DatabaseManager:
    """Gerenciador de persistência de dados dos estudantes."""
    
    def __init__(self, filename: str = "students_data.json"):
        """Inicializa o gerenciador de banco de dados."""
        self.filename = filename
        self.students: List[Student] = []
        self._load_data()
    
    def _load_data(self) -> bool:
        """Carrega dados dos estudantes do arquivo JSON."""
        try:
            if not os.path.exists(self.filename):
                return True
            
            with open(self.filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.students = [Student.from_dict(student_data) for student_data in data]
            
            return True
        except (json.JSONDecodeError, Exception) as e:
            print(f"Erro ao carregar dados: {e}")
            self.students = []
            return False
    
    def _save_data(self) -> bool:
        """Salva dados dos estudantes no arquivo JSON."""
        try:
            data = [student.to_dict() for student in self.students]
            
            with open(self.filename, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=2)
            
            return True
        except Exception as e:
            print(f"Erro ao salvar dados: {e}")
            return False
    
    def add_student(self, student: Student) -> bool:
        """Adiciona um novo estudante ao banco de dados."""
        if not isinstance(student, Student):
            return False
        
        if any(s.matricula == student.matricula for s in self.students):
            return False
        
        self.students.append(student)
        return self._save_data()
    
    def find_student_by_matricula(self, matricula: str) -> Optional[Student]:
        """Busca um estudante pela matrícula."""
        if not matricula:
            return None
        
        matricula_clean = matricula.strip()
        return next((s for s in self.students if s.matricula == matricula_clean), None)
    
    def find_students_by_name(self, name: str) -> List[Student]:
        """Busca estudantes pelo nome (busca parcial, case-insensitive)."""
        if not name:
            return []
        
        name_lower = name.strip().lower()
        return [s for s in self.students if name_lower in s.name.lower()]
    
    def update_student(self, matricula: str, updated_data: Dict) -> bool:
        """Atualiza dados de um estudante existente."""
        student = self.find_student_by_matricula(matricula)
        if not student:
            return False
        
        valid_fields = ['name', 'email', 'course', 'age']
        
        for field, value in updated_data.items():
            if field in valid_fields:
                setattr(student, field, value)
        
        return self._save_data()
    
    def remove_student(self, matricula: str) -> bool:
        """Remove um estudante do banco de dados."""
        student = self.find_student_by_matricula(matricula)
        if not student:
            return False
        
        self.students.remove(student)
        return self._save_data()
    
    def get_all_students(self) -> List[Student]:
        """Retorna uma cópia da lista de todos os estudantes."""
        return self.students.copy()
    
    def get_students_count(self) -> int:
        """Retorna o número total de estudantes cadastrados."""
        return len(self.students)