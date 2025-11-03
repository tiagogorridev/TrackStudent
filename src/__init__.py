"""
TrackStudent Package - Sistema de Gerenciamento de Estudantes

Sistema completo para gerenciamento de estudantes,
incluindo cadastro, busca, atualização, remoção e geração de relatórios.
"""

from .models import Student
from .validators import StudentValidator
from .database import DatabaseManager
from .reports import ReportManager
from .handlers import (
    MenuHandler,
    StudentInputHandler, 
    StudentUpdateHandler,
    SearchHandler,
)

__all__ = [
    'Student',
    'StudentValidator', 
    'DatabaseManager',
    'ReportManager',
    'MenuHandler',
    'StudentInputHandler',
    'StudentUpdateHandler', 
    'SearchHandler',
]