"""
Handlers - Classes especializadas para diferentes operações do sistema.
"""

from models import Student
from validators import StudentValidator


class MenuHandler:
    """Classe para gerenciar operações de menu e entrada do usuário."""
    
    @staticmethod
    def show_main_menu():
        """Exibe o menu principal do sistema."""
        menu = [
            "\n" + "="*50,
            "MENU PRINCIPAL",
            "="*50,
            "1. Cadastrar Estudante",
            "2. Buscar Estudante",
            "3. Atualizar Dados",
            "4. Remover Estudante",
            "5. Gerar Relatórios",
            "0. Sair",
            "="*50
        ]
        print("\n".join(menu))
    
    @staticmethod
    def get_menu_choice():
        """Obtém e valida a escolha do menu principal."""
        return input("\nEscolha uma opção: ").strip()
    
    @staticmethod
    def wait_for_continue():
        """Pausa a execução até o usuário pressionar Enter."""
        input("\nPressione Enter para continuar...")


class StudentInputHandler:
    """Classe responsável por coletar e validar dados de entrada dos estudantes."""
    
    def __init__(self, validator: StudentValidator):
        self.validator = validator
    
    def collect_student_data(self):
        """Coleta todos os dados necessários para criar um novo estudante."""
        data_collectors = {
            "name": (self._get_valid_name, "Nome inválido! Digite um nome com pelo menos 2 caracteres."),
            "email": (self._get_valid_email, "Email inválido! Digite um email no formato correto."),
            "course": (self._get_valid_course, "Curso inválido! Digite um curso com pelo menos 3 caracteres."),
            "age": (self._get_valid_age, "Idade inválida! A idade deve estar entre 16 e 80 anos.")
        }
        
        collected_data = {}
        
        for field_name, (collector_func, error_msg) in data_collectors.items():
            value = collector_func()
            if value is None:
                print(f"Erro: {error_msg}")
                return None
            collected_data[field_name] = value
        
        try:
            return Student(**collected_data)
        except Exception as e:
            print(f"Erro ao criar estudante: {e}")
            return None
    
    def _get_valid_name(self):
        """Obtém e valida o nome do estudante."""
        name = input("Nome completo: ").strip()
        return name if self.validator.validate_name(name) else None
    
    def _get_valid_email(self):
        """Obtém e valida o email do estudante."""
        email = input("Email: ").strip()
        return email if self.validator.validate_email(email) else None
    
    def _get_valid_course(self):
        """Obtém e valida o curso do estudante."""
        course = input("Curso: ").strip()
        return course if self.validator.validate_course(course) else None
    
    def _get_valid_age(self):
        """Obtém e valida a idade do estudante."""
        try:
            age = int(input("Idade: "))
            return age if self.validator.validate_age(age) else None
        except ValueError:
            return None


class StudentUpdateHandler:
    """Classe responsável por atualizar dados dos estudantes."""
    
    def __init__(self, validator: StudentValidator):
        self.validator = validator
    
    def collect_updated_data(self, student):
        """Coleta novos dados para atualização de um estudante existente."""
        print(f"\nDados atuais: {student}")
        print("\nDeixe em branco para manter o valor atual:")
        
        updated_data = {}
        
        # Campos de texto
        text_fields = [
            ("name", f"Novo nome ({student.name}): ", self.validator.validate_name),
            ("email", f"Novo email ({student.email}): ", self.validator.validate_email),
            ("course", f"Novo curso ({student.course}): ", self.validator.validate_course)
        ]
        
        for field, prompt, validator in text_fields:
            self._update_text_field(field, prompt, validator, updated_data)
        
        # Campo idade
        self._update_age_field(student.age, updated_data)
        
        return updated_data
    
    def _update_text_field(self, field, prompt, validator, updated_data):
        """Atualiza um campo de texto com validação."""
        new_value = input(prompt).strip()
        if new_value:
            if validator(new_value):
                updated_data[field] = new_value
            else:
                print(f"{field.capitalize()} inválido! Mantendo o valor atual.")
    
    def _update_age_field(self, current_age, updated_data):
        """Atualiza o campo idade com validação específica."""
        new_age = input(f"Nova idade ({current_age}): ").strip()
        if new_age:
            try:
                age_int = int(new_age)
                if self.validator.validate_age(age_int):
                    updated_data["age"] = age_int
                else:
                    print("Idade inválida! Mantendo a idade atual.")
            except ValueError:
                print("Idade deve ser um número! Mantendo a idade atual.")


class SearchHandler:
    """Classe responsável por operações de busca de estudantes."""
    
    def __init__(self, db_manager):
        self.db_manager = db_manager
    
    def handle_search_menu(self):
        """Gerencia o menu de busca de estudantes."""
        print("\n=== BUSCAR ESTUDANTE ===")
        print("1. Buscar por matrícula")
        print("2. Buscar por nome")
        
        choice = input("Escolha o tipo de busca: ").strip()
        
        if choice == '1':
            self._search_by_matricula()
        elif choice == '2':
            self._search_by_name()
        else:
            print("Opção inválida!")
    
    def _search_by_matricula(self):
        """Realiza busca por matrícula."""
        matricula = input("Digite a matrícula: ").strip()
        student = self.db_manager.find_student_by_matricula(matricula)
        
        if student:
            print(f"\nEstudante encontrado:\n{student}")
        else:
            print("Estudante não encontrado!")
    
    def _search_by_name(self):
        """Realiza busca por nome."""
        name = input("Digite o nome (ou parte dele): ").strip()
        students = self.db_manager.find_students_by_name(name)
        
        if students:
            print(f"\n{len(students)} estudante(s) encontrado(s):")
            for i, student in enumerate(students, 1):
                print(f"{i}. {student}")
        else:
            print("Nenhum estudante encontrado!")