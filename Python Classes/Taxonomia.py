class SerVivo(object):
    def __init__(self, Dominio = '', Reino = '', Filo = '', Classe = '', Ordem = '', Familia = '', Genero = '', Especie = ''):
        self.Dominio = Dominio
        self.Reino = Reino
        self.Classe = Classe
        self.Ordem = Ordem
        self.Familia = Familia
        self.Genero = Genero
        self.Especie = Especie

    def info_SerVivo (self):
        return [self.Dominio, self.Reino, self.Classe, self.Ordem, self.Familia, self.Genero, self.Especie]

class Habilidades(SerVivo):
    def __init__(self, Dominio = '', Reino = '', Filo = '', Classe = '', Ordem = '', Familia = '', Genero = '', Especie = '', Locomoçao = '', Visao = '', Respiraçao = '', Pele = ''):
        super(Habilidades, self).__init__(Dominio, Reino, Filo, Classe, Ordem, Familia, Genero, Especie)
        self.Locomoçao = Locomoçao
        self.Visao = Visao
        self.Respiraçao = Respiraçao
        self.Pele = Pele
        
    def info_Habilidades (self):
        super(Habilidades, self).info_SerVivo()
        return [self.Locomoçao, self.Visao, self.Respiraçao, self.Pele]
    
class Fisico(Habilidades):
    def __init__(self, Dominio = '', Reino = '', Filo = '', Classe = '', Ordem = '', Familia = '', Genero = '', Especie = '', Locomoçao = '', Visao = '', Respiraçao = '', Pele = '', Altura = '', Peso = '', Comprimento = '', Idade = ''):
        super(Fisico, self).__init__(Dominio, Reino, Filo, Classe, Ordem, Familia, Genero, Especie, Locomoçao, Visao, Respiraçao, Pele)
        self.Altura = Altura
        self.Peso = Peso
        self.Comprimento = Comprimento
        self.Idade = Idade
        
    def info_Fisico (self):
        super(Fisico, self).info_SerVivo()
        super(Fisico, self).info_Habilidades()
        return [self.Altura, self.Peso, self.Comprimento, self.Idade]
    
class Habitos(Fisico):
    def __init__(self, Dominio = '', Reino = '', Filo = '', Classe = '', Ordem = '', Familia = '', Genero = '', Especie = '', Locomoçao = '', Visao = '', Respiraçao = '', Pele = '', Altura = '', Peso = '', Comprimento = '', Idade = '', Habitat = ''):
        super(Habitos, self).__init__(Dominio, Reino, Filo, Classe, Ordem, Familia, Genero, Especie, Locomoçao, Visao, Respiraçao, Pele, Altura, Peso, Comprimento, Idade)
        self.Habitat = Habitat
    
    def info_Habitos (self):
        super(Habitos, self).info_SerVivo()
        super(Habitos, self).info_Habilidades()        
        super(Habitos, self).info_Fisico()
        return [self.Habitat]

'''==========================Individuos================='''
class Humano(Habitos):
    def __init__(self, Dominio = '', Reino = '', Filo = '', Classe = '', Ordem = '', Familia = '', Genero = '', Especie = '', Locomoçao = '', Visao = '', Respiraçao = '', Pele = '', Altura = '', Peso = '', Comprimento = '', Idade = '', Habitat = ''):
        super(Humano, self).__init__(Dominio, Reino, Filo, Classe, Ordem, Familia, Genero, Especie, Locomoçao, Visao, Respiraçao, Pele, Altura, Peso, Comprimento, Idade, Habitat)
        self.Dominio='Eukaryota'
        self.Reino='Animalia'
        self.Filo='Chordata'
        self.Classe='Mammalia'
        self.Ordem='Primates'
        self.Familia='Hominidae'
        self.Genero='Homo'
        self.Especie='H. Sapiens'
        self.Locomoçao='Bipede'
        self.Respiraçao='Pulmonar'
        self.Habitat = 'Urbano'

    def info_Humano (self):
        return [super(Humano, self).info_SerVivo(), super(Humano, self).info_Habilidades(), super(Humano, self).info_Fisico()]


class Cachorro(Habitos):
    def __init__(self, Dominio = '', Reino = '', Filo = '', Classe = '', Ordem = '', Familia = '', Genero = '', Especie = '', Locomoçao = '', Visao = '', Respiraçao = '', Pele = '', Altura = '', Peso = '', Comprimento = '', Idade = '', Habitat = ''):
        super(Cachorro, self).__init__(Dominio, Reino, Filo, Classe, Ordem, Familia, Genero, Especie, Locomoçao, Visao, Respiraçao, Pele, Altura, Peso, Comprimento, Idade, Habitat)
        self.Dominio='Eukaryota'
        self.Reino='Animalia'
        self.Filo='Chordata'
        self.Classe='Mammalia'
        self.Ordem='Carnivora'
        self.Familia='Canidae'
        self.Genero='Canis'
        self.Especie='Canis lupus'
        self.Locomoçao='Quadrupede'
        self.Respiraçao='Pulmonar'
        self.Habitat = 'Urbano'

    def info_Cachorro (self):
        return [super(Cachorro, self).info_SerVivo(), super(Cachorro, self).info_Habilidades(), super(Cachorro, self).info_Fisico()]

