

class Papu:
    __trolo__ = 0
    def __init__(self):
        Papu.__trolo__ += 1
        self.id = Papu.__trolo__

# papito = Papu()
# print(papito.id) 
# Yo digo que queda en 1 porque se esta creando una instancia. Al atributo
# de clase se le esta incrementando en uno porque es una instancia de papu y todos los objetos de papu
# comparten ese atributo.

for i in range(4):
    b = Papu()

print(b.id)
# aca yo digo que b.id es 3 porque cada instancia incrementa id.

class Mamacita(Papu):
    pass

uy = Mamacita()
print(uy.id)
# aca yo digo que id se incrementa igual porque no se definio una nueva
# variable de clase.

que = Mamacita()
hola = Papu()
hola2 = Papu()

# aca yo digo que Mamacita recibe una copia de id desde Papu, pero si mamacita incrementa
# papu no, es como una shallow copy(?)

class Perrito(Papu):
    def __init__(self):
        self.id = 102

cat = Perrito()
print(cat.id)
# digo que Perrito sobreescribe el atributo para perritos.

class Gatito(Papu):
    def __init__(self):
        super().__init__()
# Aca es lo mismo que la nada, Gatito se inicializa con el constructor de Papu, lo cual ya hacia.abs
perrito = Gatito()
print(perrito.id)

class Delfin(Papu):
    def __init__(self):
        self.id = 103
        super().__init__()
# Aca sobreescribimos el id para el objecto pero despues llamamos al init de Papu
tiburon = Delfin()
print(tiburon.id)

class Base():
    """ My base class """

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

class User(Base):
    """ My User class """
    pass

b = Base()
u = User()
print(u.id)