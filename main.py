"""
TrackStudent - Sistema de Gerenciamento de Estudantes
Versão otimizada sem funcionalidades de estatísticas.

Autores: Tiago Kasprzak Gorri, Mateus Zanettin, Matheus Muller, Vitor Vieira
"""

from validators import StudentValidator
from database import DatabaseManager
from reports import ReportManager
from handlers import MenuHandler, StudentInputHandler, StudentUpdateHandler, SearchHandler


class TrackStudent:
    """Sistema principal de gerenciamento de estudantes."""
    
    def __init__(self):
        """Inicializa o sistema com todos os componentes necessários."""
        self.db_manager = DatabaseManager()
        self.report_manager = ReportManager(self.db_manager)
        self.validator = StudentValidator()
        self.menu_handler = MenuHandler()
        self.input_handler = StudentInputHandler(self.validator)
        self.update_handler = StudentUpdateHandler(self.validator)
        self.search_handler = SearchHandler(self.db_manager)
    
    def run(self):
        """Executa o loop principal do sistema."""
        self._show_welcome_message()
        
        while True:
            self.menu_handler.show_main_menu()
            choice = self.menu_handler.get_menu_choice()
            
            if choice == '0':
                print("Obrigado por usar o TrackStudent!")
                break
            
            self._handle_menu_choice(choice)
            self.menu_handler.wait_for_continue()
    
    def _show_welcome_message(self):
        """Exibe mensagem de boas-vindas do sistema."""
        welcome = [
            "=== TRACKSTUDENT - Sistema de Gerenciamento de Estudantes ===",
            "Desenvolvido por: Tiago Kasprzak Gorri, Mateus Zanettin, Matheus Muller, Vitor Vieira"
        ]
        print("\n".join(welcome))
    
    def _handle_menu_choice(self, choice):
        """Direciona a escolha do menu para o método apropriado."""
        menu_actions = {
            '1': self._add_student,
            '2': self._search_student,
            '3': self._update_student,
            '4': self._remove_student,
            '5': self._generate_reports
        }
        
        action = menu_actions.get(choice)
        if action:
            action()
        else:
            print("Opção inválida! Tente novamente.")
    
    def _add_student(self):
        """Gerencia o processo de cadastro de novo estudante."""
        print("\n=== CADASTRAR ESTUDANTE ===")
        
        student = self.input_handler.collect_student_data()
        if not student:
            return
        
        if self.db_manager.add_student(student):
            print(f"\nEstudante cadastrado com sucesso!")
            print(f"Matrícula gerada: {student.matricula}")
        else:
            print("Erro ao cadastrar estudante!")
    
    def _search_student(self):
        """Delega a busca para o handler específico."""
        self.search_handler.handle_search_menu()
    
    def _update_student(self):
        """Gerencia o processo de atualização de dados do estudante."""
        print("\n=== ATUALIZAR DADOS ===")
        matricula = input("Digite a matrícula do estudante: ").strip()
        
        student = self.db_manager.find_student_by_matricula(matricula)
        if not student:
            print("Estudante não encontrado!")
            return
        
        updated_data = self.update_handler.collect_updated_data(student)
        
        if updated_data:
            if self.db_manager.update_student(matricula, updated_data):
                print("Dados atualizados com sucesso!")
            else:
                print("Erro ao atualizar dados!")
        else:
            print("Nenhum dado foi alterado.")
    
    def _remove_student(self):
        """Gerencia o processo de remoção de estudante."""
        print("\n=== REMOVER ESTUDANTE ===")
        matricula = input("Digite a matrícula do estudante: ").strip()
        
        student = self.db_manager.find_student_by_matricula(matricula)
        if not student:
            print("Estudante não encontrado!")
            return
        
        print(f"\nEstudante encontrado: {student}")
        if self._confirm_removal():
            if self.db_manager.remove_student(matricula):
                print("Estudante removido com sucesso!")
            else:
                print("Erro ao remover estudante!")
        else:
            print("Operação cancelada.")
    
    def _confirm_removal(self):
        """Confirma se o usuário quer remover o estudante."""
        confirm = input("Tem certeza que deseja remover este estudante? (s/n): ").strip().lower()
        return confirm == 's'
    
    def _generate_reports(self):
        """Gerencia a geração de relatórios do sistema."""
        print("\n=== GERAR RELATÓRIOS ===")
        print("1. Relatório de todos os estudantes")
        print("2. Relatório por curso")
        
        choice = input("Escolha o tipo de relatório: ").strip()
        
        if choice == '1':
            print(self.report_manager.generate_all_students_report())
        elif choice == '2':
            print(self.report_manager.generate_course_report())
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    try:
        system = TrackStudent()
        system.run()
    except KeyboardInterrupt:
        print("\n\nPrograma interrompido pelo usuário.")
    except Exception as e:
        print(f"\nErro inesperado: {e}")
        print("Encerrando o programa...")