# TrackStudent

Sistema de gerenciamento de estudantes desenvolvido em Python.

## Sobre

O TrackStudent permite cadastrar, consultar, atualizar e remover estudantes de forma simples. Todos os dados são salvos em arquivo JSON.

## Funcionalidades

- Cadastro de estudantes
- Consulta por matrícula ou nome
- Atualização de dados
- Remoção de estudantes
- Relatórios (geral e por curso)
- Validação automática de dados

## Estrutura

```
TrackStudent/
├── models.py           # Modelo de estudante
├── validators.py       # Validações
├── database.py         # Persistência JSON
├── handlers.py         # Interface do usuário
├── reports.py          # Geração de relatórios
├── main.py             # Arquivo principal
└── students_data.json  # Base de dados
```

## Como usar

1. Clone o repositório:

```bash
git clone https://github.com/tiagogorridev/TrackStudent.git
cd TrackStudent
```

2. Execute o sistema:

```bash
python main.py
```

## Requisitos

- Python 3.7+

## Qualidade do Código

Análise com Radon:

- Complexidade média: 2.41
- 100% dos blocos com classificação A
- Alta manutenibilidade
