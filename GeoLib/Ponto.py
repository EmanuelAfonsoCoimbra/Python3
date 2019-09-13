class ponto(object):
    def __init__(self, X=0, Y=0, Z=0,):
        self.X=X
        self.Y=Y
        self.Z=Z
    def info_ponto(self):
        return [self.X,self.Y,self.Z]
