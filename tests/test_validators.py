import pytest
from validators import StudentValidator

# NOME
@pytest.mark.parametrize("nome, esperado", [
    ("", False),      # vazio (CI-N2)
    ("A", False),     # 1 char (CI-N1)
    ("Li", True),     # 2 chars limite (CE-N1)
    ("Ana", True),    # 3 chars acima (CE-N1)
    ("Ana123", False),# numeros (CI-N3)
    ("Ana@", False),  # simbolos (CI-N4)
])
def test_nome(nome, esperado):
    assert StudentValidator.validate_name(nome) == esperado


# EMAIL
@pytest.mark.parametrize("email, esperado", [
    # Casos Inválidos (CI)
    ("", False),           # CI-E1: Vazio 
    ("a@b.", False),       # CI-E1: < 5 chars (AVL Mínimo - 1) 
    ("email.com", False), # CI-E2: Sem "@" 
    ("ana@", False),       # CI-E3: Sem domínio 
    ("ana@gmail", False), # CI-E4: Sem extensão 

    # Casos Válidos (CE)
    ("a@b.c", True),       # CE-E1/E2: No limite (AVL Mínimo) 
    ("a@b.cd", True),      # CE-E1/E2: Acima (AVL Mínimo + 1) 
    ("joao@gmail.com", True) # CE-E1/E2: Caso padrão
])
def test_email(email, esperado):
    assert StudentValidator.validate_email(email) == esperado


# CURSO
@pytest.mark.parametrize("curso, esperado", [
    ("", False),      # vazio
    ("TI", False),    # 2 chars
    ("ADS", True),    # limite
    ("Medicina", True),
])
def test_curso(curso, esperado):
    assert StudentValidator.validate_course(curso) == esperado


# IDADE
@pytest.mark.parametrize("idade, esperado", [
    (15, False),     # abaixo limite (CI-I1)
    (16, True),      # limite inferior (CE-I1)
    (17, True),      # acima
    (80, True),      # limite superior (CE-I1)
    (81, False),     # acima (CI-I2)
    ("vinte", False) # inválida (CI-I3)
])
def test_idade(idade, esperado):
    assert StudentValidator.validate_age(idade) == esperado
