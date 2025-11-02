"""
Validators - Módulo de validação de dados para o sistema TrackStudent.
"""

import re
from typing import Union


class StudentValidator:
    """Classe responsável pela validação de dados dos estudantes."""
    
    MIN_AGE, MAX_AGE = 16, 80
    MIN_NAME_LENGTH, MIN_COURSE_LENGTH = 2, 3
    
    @staticmethod
    def validate_email(email: str) -> bool:
        """Valida o formato do endereço de email."""
        if not email or not isinstance(email, str):
            return False
        
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{1,}$'
        return re.match(pattern, email.strip()) is not None
    
    @classmethod
    def validate_age(cls, age: Union[int, str]) -> bool:
        """Valida se a idade está dentro dos limites permitidos."""
        try:
            age_int = int(age)
            return cls.MIN_AGE <= age_int <= cls.MAX_AGE
        except (ValueError, TypeError):
            return False
    
    @classmethod
    def validate_name(cls, name: str) -> bool:
        """Valida o nome do estudante."""
        if not name or not isinstance(name, str):
            return False
        
        name_clean = name.strip()
        if len(name_clean) < cls.MIN_NAME_LENGTH:
            return False
        
        name_no_spaces = name_clean.replace(' ', '')
        return name_no_spaces.isalpha() and len(name_no_spaces) > 0
    
    @classmethod
    def validate_course(cls, course: str) -> bool:
        """Valida o nome do curso."""
        if not course or not isinstance(course, str):
            return False
        
        return len(course.strip()) >= cls.MIN_COURSE_LENGTH