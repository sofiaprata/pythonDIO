class Bicicleta:
    def __init__(self,cor,modelo,ano,valor):
    #atributos da classe
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
       # self.marcha = 1
    
    def buzinar(self):
        print("Plim plim...")
        
    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")
    
    def correr(self):
        print("Vruummmmm....")
        
    def __str__(self):
        return f"Bicicleta: {self.cor}, {self.modelo}, {self.ano}, {self.valor}"

    #def trocar_marcha(self,nro_marcha):
        #print("Trocando mrcha...") 
        #_self = self      
        
        #def _trocar_marcha(nro_marcha):
            #if nro_marcha > _self.marcha:
                #print("Marcha trocada.")
           # else:
              #  print("Não foi possivel trocar a marcha.")


b1 = Bicicleta("vermelha", "caloi", 2022, 600)
#b1.buzinar()
#b1.correr()
#b1.parar()
#print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("verde", "monark", 2000, 189)
#Bicicleta.buzinar(b2)
#Bicicleta.buzinar(b2) = b2.buzinar()
print(b2)