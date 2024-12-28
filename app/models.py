from app import mysql

class Student:
    def __init__(self):
        self.cursor = mysql.connection.cursor()
    
    @classmethod
    def get(self, *args, **kwargs):
        pass 

    @classmethod
    def all(self) -> list:
        pass 

    @classmethod
    def count(self):
        pass

    @classmethod 
    def set(self, student_id: str, data: list):
        pass 

    @classmethod 
    def delete(self, *student_id):
        pass

class Program:
    def __init__(self):
        self.cursor = mysql.connection.cursor()
    
    @classmethod
    def get(self, *args, **kwargs):
        pass 

    @classmethod
    def all(self) -> list:
        pass 

    @classmethod
    def count(self):
        pass

    @classmethod 
    def set(self, student_id: str, data: list):
        pass 

    @classmethod 
    def delete(self, *student_id):
        pass

class College:
    def __init__(self):
        self.cursor = mysql.connection.cursor()
    
    @classmethod
    def get(self, *args, **kwargs):
        pass 

    @classmethod
    def all(self) -> list:
        # returns a paged list [2d array]
        pass 

    @classmethod
    def count(self):
        pass

    @classmethod 
    def set(self, student_id: str, data: list):
        pass 

    @classmethod 
    def delete(self, *student_id):
        pass
