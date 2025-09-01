import re


class StudentValidator:
    """Classe para validação de dados dos estudantes."""
    
    @staticmethod
    def validate_email(email: str) -> bool:
        """Valida o formato do email."""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    @staticmethod
    def validate_age(age: int) -> bool:
        """Valida a idade do estudante."""
        return 16 <= age <= 80
    
    @staticmethod
    def validate_name(name: str) -> bool:
        """Valida o nome do estudante."""
        return len(name.strip()) >= 2 and name.strip().replace(' ', '').isalpha()
    
    @staticmethod
    def validate_course(course: str) -> bool:
        """Valida o curso do estudante."""
        return len(course.strip()) >= 3