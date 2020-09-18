class Disciplina:

    def __init__(self, matricula, arquivo):
        self.matricula = matricula
        self.arquivo = arquivo
        disciplinas = self.arquivo[self.arquivo['MATRICULA'] == self.matricula]['COD_DISCIPLINA'].tolist()
        ano_semestre = self.arquivo[self.arquivo['MATRICULA'] == self.matricula]['ANO_SEMESTRE'].tolist()
        self.lista_disc_semestre = []
        for i in range(len(disciplinas)):                                   # loop pra relacionar cada disciplina com o semestre em que foi cursada
            cada_disc_semestre = (disciplinas[i], ano_semestre[i])          # criando uma tupla pra cada disciplina e seu respectivo ano em que foi cursada
            self.lista_disc_semestre.append(cada_disc_semestre)

