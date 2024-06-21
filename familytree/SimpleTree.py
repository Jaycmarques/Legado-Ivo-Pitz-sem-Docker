class Pessoa:
  def __init__(self,nome):
    self.nome = nome
    self.filhos = []
    self.conjuge = ""
  def addConjuge(self,conjuge):
    self.conjuge = conjuge
  def addFilho(self,filho):
    self.filhos.append(filho)
  def getNome(self):
    return self.nome
  def situation(self):
    if self.conjuge != "" and len(self.filhos) > 0:
      return "MarriedWithChildren"
    elif self.conjuge != "" and len(self.filhos) == 0:
      return "Married"
    else:
      return "Single"
  def printBranch(self,level=0):
    tab = "\t"*level
    print (f'{tab}{self.nome:s}: casou-se com {self.conjuge.getNome():s} e teve os seguintes filhos: ')
    for f in self.filhos:
      if f.situation() == "MarriedWithChildren":
        f.printBranch(level+1)
      elif f.situation() == "Married":
        print (f'{tab}\t{f.getNome():s}: casou-se com {f.conjuge.getNome():s}. ')
      else:
        print (f'{tab}\t{f.getNome():s}')

ivo = Pessoa("Ivo Pitz")
igor = Pessoa("Ígor Berta Pitz")
michelle = Pessoa("Michelle")
igor.addConjuge(michelle)
luisa = Pessoa("Luísa")
rommel = Pessoa("Rommel")
davi = Pessoa("Davi")
igor.addFilho(luisa)
igor.addFilho(rommel)
igor.addFilho(davi)
dani = Pessoa("Daniele Aparecida Pitz")
william = Pessoa("William")
lucas = Pessoa("Lucas Pitz")
tiago = Pessoa("Tiago Pitz")
dani.addConjuge(william)
dani.addFilho(lucas)
dani.addFilho(tiago)
diogo = Pessoa("Diogo Berta Pitz")
ana = Pessoa("Ana Flávia")
diogo.addConjuge(ana)
delvir = Pessoa("Delvir Berta Pitz")
ivo.addConjuge(delvir)
ivo.addFilho(igor)
ivo.addFilho(dani)
ivo.addFilho(diogo)

ivo.printBranch()