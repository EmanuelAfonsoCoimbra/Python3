from Ponto import ponto

class vetor (object):
    def __init__(self, A=ponto(), B=ponto()):
        self.A=A
        self.B=B
        
    def comprimento(self):
        auxA = self.A.info_ponto() 
        auxB = self.B.info_ponto()
        dist = ((auxA[0]-auxB[0]), (auxA[1]-auxB[1]), (auxA[2]-auxB[2]))
        return dist
    
    def info_vetor(self):
        return [self.A.info_ponto(), self.B.info_ponto()]
