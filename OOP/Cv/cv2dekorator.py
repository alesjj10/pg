from abc import ABC, abstractmethod

class MetodaNeimplementovana(Exception):
    pass

def abstractmethod_decorator(func):
    def wrapper(*args, **kwargs):
        raise MetodaNeimplementovana("Metoda musí být implementována")
    return wrapper


class AbstractClass(ABC):
    @abstractmethod_decorator
    def method(self):
        pass

class MyClass(AbstractClass):
    def method(self):
        print("Implementace metody")

if __name__ == "__main__":
    my_object = MyClass()
    my_object.method()
    
    ab_object = AbstractClass() 
    ab_object.method()