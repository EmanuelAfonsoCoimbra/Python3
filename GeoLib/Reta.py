from Ponto import ponto

class reta (object):
    def __init__(self, A=ponto(), B=ponto()):
        self.A=A
        self.B=B
        
    def comprimento(self):
        auxA = self.A.info_ponto() 
        auxB = self.B.info_ponto()
        dist = ((auxA[0]-auxB[0])**2 + (auxA[1]-auxB[1])**2 + (auxA[2]-auxB[2])**2)**(0.5)
        return dist
    
    def info_reta(self):
        return [self.A.info_ponto(), self.B.info_ponto()]
        
