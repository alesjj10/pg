import sys
import json

class InvalidData(Exception):
    pass

class Car:
    def __init__(self, znacka, model, barva):
        self.znacka = znacka
        self.model = model
        self.barva = barva

    def __str__(self):
        return f'Auto: {self.znacka} / {self.model} / {self.barva}'
    
    @classmethod
    def parse(cls, jdata):
        data = json.loads(jdata)
        for value in ('znacka', 'model', 'barva'):
               if value not in data:
                   raise InvalidData(f'Missing {value} in data')
        return cls(data['znacka'], data['model'], data['barva'])
        


if __name__ == "__main__":

    data = [
        '{"znacka": "Skoda", "model": "Octavia", "barva": "modra"}',
        '{"znacka": "Ford", "model": "Focus", "barva": "cervena"}',
        '{"znacka": "Toyota", "model": "Corolla", "barva": "bila"}'
    ]


    for item in data:
        try:
            auto = Car.parse(item)
            print(auto)
        except InvalidData as e:
            print(e)


"""
    data = json.loads(jdata1)
    
    if 'znacka' not in data:
        raise InvalidData('missing "znacka"')
    if 'model' not in data:
        raise InvalidData('missing "model"')
    if 'barva' not in data:
        raise InvalidData('missing "barva"')

    znacka = data['znacka']
    model = data['model']
    barva = data['barva']

    auto = Car(znacka, model, barva)
    print(auto)

"""