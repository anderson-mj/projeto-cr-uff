class Disciplina:

    def __init__(self, matricula):
        disciplinas = iniciar.arquivo_df[iniciar.arquivo_df['MATRICULA'] == matricula]['COD_DISCIPLINA'].tolist()
        ano_semestre = iniciar.arquivo_df[iniciar.arquivo_df['MATRICULA'] == matricula]['ANO_SEMESTRE'].tolist()
        self.lista_disc_semestre = []
        for i in range(len(disciplinas)):                                                              # loop pra relacionar cada disciplina com o semestre em que foi cursada
            cada_disc_semestre = (disciplinas[i], ano_semestre[i])                                     # criando uma tupla pra cada disciplina e seu respectivo ano em que foi cursada
            self.lista_disc_semestre.append(cada_disc_semestre)