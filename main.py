from models import Student
from validators import StudentValidator
from database import DatabaseManager
from reports import ReportManager


class TrackStudent:
    """Sistema principal de gerenciamento de estudantes."""
    
    def __init__(self):
        self.db_manager = DatabaseManager()
        self.report_manager = ReportManager(self.db_manager)
        self.validator = StudentValidator()
    
    def run(self):
        """Executa o sistema principal."""
        print("=== TRACKSTUDENT - Sistema de Gerenciamento de Estudantes ===")
        print("Desenvolvido por: Tiago Kasprzak Gorri, Mateus Zanettin, Matheus Muller, Vitor Vieira")
        
        while True:
            self.show_menu()
            choice = input("\nEscolha uma opção: ").strip()
            
            if choice == '1':
                self.add_student_menu()
            elif choice == '2':
                self.search_student_menu()
            elif choice == '3':
                self.update_student_menu()
            elif choice == '4':
                self.remove_student_menu()
            elif choice == '5':
                self.generate_reports_menu()
            elif choice == '6':
                self.show_statistics()
            elif choice == '0':
                print("Obrigado por usar o TrackStudent!")
                break
            else:
                print("Opção inválida! Tente novamente.")
            
            input("\nPressione Enter para continuar...")
    
    def show_menu(self):
        """Exibe o menu principal."""
        print("\n" + "="*50)
        print("MENU PRINCIPAL")
        print("="*50)
        print("1. Cadastrar Estudante")
        print("2. Buscar Estudante")
        print("3. Atualizar Dados")
        print("4. Remover Estudante")
        print("5. Gerar Relatórios")
        print("6. Estatísticas")
        print("0. Sair")
        print("="*50)
    
    def add_student_menu(self):
        """Menu para adicionar estudante."""
        print("\n=== CADASTRAR ESTUDANTE ===")
        
        try:
            name = input("Nome completo: ").strip()
            if not self.validator.validate_name(name):
                print("Erro: Nome inválido! Digite um nome com pelo menos 2 caracteres.")
                return
            
            email = input("Email: ").strip()
            if not self.validator.validate_email(email):
                print("Erro: Email inválido! Digite um email no formato correto.")
                return
            
            course = input("Curso: ").strip()
            if not self.validator.validate_course(course):
                print("Erro: Curso inválido! Digite um curso com pelo menos 3 caracteres.")
                return
            
            age = int(input("Idade: "))
            if not self.validator.validate_age(age):
                print("Erro: Idade inválida! A idade deve estar entre 16 e 80 anos.")
                return
            
            student = Student(name, email, course, age)
            
            if self.db_manager.add_student(student):
                print(f"\nEstudante cadastrado com sucesso!")
                print(f"Matrícula gerada: {student.matricula}")
            else:
                print("Erro ao cadastrar estudante!")
        
        except ValueError:
            print("Erro: Idade deve ser um número válido!")
        except Exception as e:
            print(f"Erro inesperado: {e}")
    
    def search_student_menu(self):
        """Menu para buscar estudante."""
        print("\n=== BUSCAR ESTUDANTE ===")
        print("1. Buscar por matrícula")
        print("2. Buscar por nome")
        
        choice = input("Escolha o tipo de busca: ").strip()
        
        if choice == '1':
            matricula = input("Digite a matrícula: ").strip()
            student = self.db_manager.find_student_by_matricula(matricula)
            if student:
                print(f"\nEstudante encontrado:")
                print(student)
            else:
                print("Estudante não encontrado!")
        
        elif choice == '2':
            name = input("Digite o nome (ou parte dele): ").strip()
            students = self.db_manager.find_students_by_name(name)
            if students:
                print(f"\n{len(students)} estudante(s) encontrado(s):")
                for i, student in enumerate(students, 1):
                    print(f"{i}. {student}")
            else:
                print("Nenhum estudante encontrado!")
        
        else:
            print("Opção inválida!")
    
    def update_student_menu(self):
        """Menu para atualizar dados do estudante."""
        print("\n=== ATUALIZAR DADOS ===")
        matricula = input("Digite a matrícula do estudante: ").strip()
        
        student = self.db_manager.find_student_by_matricula(matricula)
        if not student:
            print("Estudante não encontrado!")
            return
        
        print(f"\nDados atuais: {student}")
        print("\nDeixe em branco para manter o valor atual:")
        
        try:
            new_name = input(f"Novo nome ({student.name}): ").strip()
            new_email = input(f"Novo email ({student.email}): ").strip()
            new_course = input(f"Novo curso ({student.course}): ").strip()
            new_age = input(f"Nova idade ({student.age}): ").strip()
            
            updated_data = {}
            
            if new_name and self.validator.validate_name(new_name):
                updated_data['name'] = new_name
            elif new_name and not self.validator.validate_name(new_name):
                print("Nome inválido! Mantendo o nome atual.")
            
            if new_email and self.validator.validate_email(new_email):
                updated_data['email'] = new_email
            elif new_email and not self.validator.validate_email(new_email):
                print("Email inválido! Mantendo o email atual.")
            
            if new_course and self.validator.validate_course(new_course):
                updated_data['course'] = new_course
            elif new_course and not self.validator.validate_course(new_course):
                print("Curso inválido! Mantendo o curso atual.")
            
            if new_age:
                age_int = int(new_age)
                if self.validator.validate_age(age_int):
                    updated_data['age'] = age_int
                else:
                    print("Idade inválida! Mantendo a idade atual.")
            
            if updated_data:
                if self.db_manager.update_student(matricula, updated_data):
                    print("Dados atualizados com sucesso!")
                else:
                    print("Erro ao atualizar dados!")
            else:
                print("Nenhum dado foi alterado.")
        
        except ValueError:
            print("Erro: Idade deve ser um número válido!")
    
    def remove_student_menu(self):
        """Menu para remover estudante."""
        print("\n=== REMOVER ESTUDANTE ===")
        matricula = input("Digite a matrícula do estudante: ").strip()
        
        student = self.db_manager.find_student_by_matricula(matricula)
        if not student:
            print("Estudante não encontrado!")
            return
        
        print(f"\nEstudante encontrado: {student}")
        confirm = input("Tem certeza que deseja remover este estudante? (s/n): ").strip().lower()
        
        if confirm == 's':
            if self.db_manager.remove_student(matricula):
                print("Estudante removido com sucesso!")
            else:
                print("Erro ao remover estudante!")
        else:
            print("Operação cancelada.")
    
    def generate_reports_menu(self):
        """Menu para gerar relatórios."""
        print("\n=== GERAR RELATÓRIOS ===")
        print("1. Relatório de todos os estudantes")
        print("2. Relatório por curso")
        
        choice = input("Escolha o tipo de relatório: ").strip()
        
        if choice == '1':
            report = self.report_manager.generate_all_students_report()
            print(report)
        elif choice == '2':
            report = self.report_manager.generate_course_report()
            print(report)
        else:
            print("Opção inválida!")
    
    def show_statistics(self):
        """Exibe estatísticas do sistema."""
        print("\n=== ESTATÍSTICAS ===")
        total_students = self.db_manager.get_students_count()
        print(f"Total de estudantes cadastrados: {total_students}")
        
        if total_students > 0:
            students = self.db_manager.get_all_students()
            
            # Estatísticas por curso
            courses = {}
            ages = []
            
            for student in students:
                if student.course not in courses:
                    courses[student.course] = 0
                courses[student.course] += 1
                ages.append(student.age)
            
            print(f"Número de cursos diferentes: {len(courses)}")
            
            if ages:
                avg_age = sum(ages) / len(ages)
                print(f"Idade média dos estudantes: {avg_age:.1f} anos")
                print(f"Idade mínima: {min(ages)} anos")
                print(f"Idade máxima: {max(ages)} anos")


# Ponto de entrada do programa
if __name__ == "__main__":
    try:
        system = TrackStudent()
        system.run()
    except KeyboardInterrupt:
        print("\n\nPrograma interrompido pelo usuário.")
    except Exception as e:
        print(f"\nErro inesperado: {e}")
        print("Encerrando o programa...")