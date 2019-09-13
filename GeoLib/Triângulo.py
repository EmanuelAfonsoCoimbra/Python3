from Ponto import ponto
from Reta import reta

class triangulo(object):
    def __init__(self,A=ponto(),B=ponto(),C=ponto()):
        self.A=A
        self.B=B
        self.C=C
    def info_triangulo(self):
        AB = reta(self.A,self.B)
        BC = reta(self.B,self.C)
        CA = reta(self.C,self.A)
        return [AB.info_reta(), BC.info_reta(), CA.info_reta()]
    def info_perimetro(self):
        AB = reta(self.A,self.B)
        BC = reta(self.A,self.C)
        CA = reta(self.A,self.C)
        return (AB.comprimento() + BC.comprimento() + CA.comprimento())
    def info_cos(self):
        AB = reta(self.A,self.B)
        BC = reta(self.A,self.C)
        CA = reta(self.A,self.C)
        aux1 = (((CA.comprimento()**2) - (BC.comprimento()**2) - (AB.comprimento()**2))/((-2)*BC.comprimento()*AB.comprimento()))
        aux2 = (((BC.comprimento()**2) - (AB.comprimento()**2) - (CA.comprimento()**2))/((-2)*AB.comprimento()*CA.comprimento()))
        aux3 = (((AB.comprimento()**2) - (BC.comprimento()**2) - (CA.comprimento()**2))/((-2)*BC.comprimento()*CA.comprimento()))
        if((aux1**2) or (aux2**2) or (aux3**2) >= 1.0):
            erro='Triangulo Impóssivel'
        else:
            erro=''
        return [aux1,aux2,aux3,erro]
    def info_sen(self):
        AB = reta(self.A,self.B)
        BC = reta(self.A,self.C)
        CA = reta(self.A,self.C)
        aux1 = (((CA.comprimento()**2) - (BC.comprimento()**2) - (AB.comprimento()**2))/((-2)*BC.comprimento()*AB.comprimento()))
        aux2 = (((BC.comprimento()**2) - (AB.comprimento()**2) - (CA.comprimento()**2))/((-2)*AB.comprimento()*CA.comprimento()))
        aux3 = (((AB.comprimento()**2) - (BC.comprimento()**2) - (CA.comprimento()**2))/((-2)*BC.comprimento()*CA.comprimento()))
        if(aux1**2 or aux2**2 or aux3**2 >= 1.0):
            erro='Triangulo Impóssivel'
        else:
            erro=''
        return [(1-(aux1**2))**0.5 , (1-(aux2**2))**0.5 , (1-(aux3**2))**0.5, erro]
    def info_area(self):
        AB = reta(self.A,self.B)
        BC = reta(self.A,self.C)
        CA = reta(self.A,self.C)
        aux1 = (((CA.comprimento()**2) - (BC.comprimento()**2) - (AB.comprimento()**2))/((-2)*BC.comprimento()*AB.comprimento()))
        aux2 = (((BC.comprimento()**2) - (AB.comprimento()**2) - (CA.comprimento()**2))/((-2)*AB.comprimento()*CA.comprimento()))
        aux3 = (((AB.comprimento()**2) - (BC.comprimento()**2) - (CA.comprimento()**2))/((-2)*BC.comprimento()*CA.comprimento()))
        aux4 = [(1-(aux1**2))**0.5 , (1-(aux2**2))**0.5 , (1-(aux3**2))**0.5]
        return ((AB.comprimento()*CA.comprimento()*aux4[0])/2)
        
        
