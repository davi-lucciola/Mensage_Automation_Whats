# Classes
class Aluno:
    def __init__(self, nome:str, numero:str) -> None:
        self.__nome = nome
        self.__numero = numero
    
    @property
    def nome(self):
        return self.__nome

    @property
    def numero(self):
        return self.__numero
    
class Aula:
    def __init__(self, aluno: Aluno, hora: list, data: str, curso: str, monitor: str) -> None:
        self.__aluno = aluno
        self.__hora = hora
        self.__data = data
        self.__curso = curso
        self.__monitor = monitor
    
    def __repr__(self) -> str:
        return f'{self.aluno} - {self.hora} - {self.data}'

    # Getters
    @property
    def aluno(self):
        return self.__aluno

    @property
    def hora(self):
        return self.__hora
    
    @property
    def data(self):
        return self.__data
    
    @property
    def curso(self):
        return self.__curso
    
    @property
    def monitor(self):
        return self.__monitor

    @data.setter
    def data(self, new_data):
        self.__data = new_data
