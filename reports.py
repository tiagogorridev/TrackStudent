"""
Reports - Módulo de geração de relatórios do sistema TrackStudent.
"""

from datetime import datetime
from database import DatabaseManager


class ReportManager:
    """Gerenciador de relatórios do sistema."""
    
    def __init__(self, db_manager: DatabaseManager):
        self.db_manager = db_manager
    
    def generate_all_students_report(self) -> str:
        """Gera relatório de todos os estudantes."""
        students = self.db_manager.get_all_students()
        if not students:
            return "Nenhum estudante cadastrado."
        
        report = [
            "\n=== RELATÓRIO DE ESTUDANTES ===",
            f"Total de estudantes: {len(students)}",
            f"Data do relatório: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n"
        ]
        
        report.extend(f"{i}. {student}" for i, student in enumerate(students, 1))
        
        return "\n".join(report)
    
    def generate_course_report(self) -> str:
        """Gera relatório por curso."""
        students = self.db_manager.get_all_students()
        if not students:
            return "Nenhum estudante cadastrado."
        
        courses = {}
        for student in students:
            courses[student.course] = courses.get(student.course, 0) + 1
        
        report = [
            "\n=== RELATÓRIO POR CURSO ===",
            f"Data do relatório: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n"
        ]
        
        report.extend(
            f"Curso: {course} - {count} estudante(s)"
            for course, count in sorted(courses.items())
        )
        
        return "\n".join(report)