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
        
        report = "\n=== RELATÓRIO DE ESTUDANTES ===\n"
        report += f"Total de estudantes: {len(students)}\n"
        report += f"Data do relatório: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n\n"
        
        for i, student in enumerate(students, 1):
            report += f"{i}. {student}\n"
        
        return report
    
    def generate_course_report(self) -> str:
        """Gera relatório por curso."""
        students = self.db_manager.get_all_students()
        if not students:
            return "Nenhum estudante cadastrado."
        
        courses = {}
        for student in students:
            if student.course not in courses:
                courses[student.course] = 0
            courses[student.course] += 1
        
        report = "\n=== RELATÓRIO POR CURSO ===\n"
        report += f"Data do relatório: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n\n"
        
        for course, count in sorted(courses.items()):
            report += f"Curso: {course} - {count} estudante(s)\n"
        
        return report