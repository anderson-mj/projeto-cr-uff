import pandas as pd
from Curso import Curso
from Disciplina import Disciplina
from Aluno import Aluno


class Controle:

    def __init__(self, arquivo):

        self.arquivo_df = pd.read_csv(arquivo)
        self.cada_matricula = self.arquivo_df['MATRICULA'].drop_duplicates().sort_values().tolist()    # armazenando a matricula de cada aluno
        self.todos_alunos = []                                                                         # lista para armazenar cada aluno como um objeto da classe Aluno
        self.alunos_cr = []                                                                            # lista para armazenar matricula e CR de cada aluno
        self.cada_curso = self.arquivo_df['COD_CURSO'].drop_duplicates().sort_values().tolist()        # armazenando o codigo de cada curso
        self.todos_cursos = []                                                                         # armazenando cada curso como um objeto da classe Curso
        self.cursos_cr = []                                                                            # lista pra armazenar codigo e CR médio de cada curso

    def lista_alunos(self):

        for i in self.cada_matricula:                                                                  # criando cada aluno como um objeto da classe Aluno
            aluno_novo = Aluno(i, Disciplina(i, self.arquivo_df).lista_disc_semestre, self.arquivo_df[self.arquivo_df['MATRICULA'] == i]['COD_CURSO'], self.arquivo_df[self.arquivo_df['MATRICULA'] == i]['NOTA'], self.arquivo_df[self.arquivo_df['MATRICULA'] == i]['CARGA_HORARIA'])
            self.todos_alunos.append(aluno_novo)

    def calcular_cr(self):

        for i in range(len(self.cada_matricula)):                                                      # loop pra calcular cada CR
            nota_carga_a = (self.todos_alunos[i].nota * self.todos_alunos[i].carga).tolist()
            numerador_a = sum(nota_carga_a)
            carga_total_a = self.todos_alunos[i].carga.sum()
            coeficiente_a = round(numerador_a / carga_total_a, 2)
            self.alunos_cr.append([self.todos_alunos[i].matricula, coeficiente_a])

    def media_cursos(self):

        for i in self.cada_curso:                                                                      # criando cada curso como objeto da classe Curso
            curso_novo = Curso(i, self.arquivo_df[self.arquivo_df['COD_CURSO'] == i]['NOTA'], self.arquivo_df[self.arquivo_df['COD_CURSO'] == i]['CARGA_HORARIA'])
            self.todos_cursos.append(curso_novo)

        for j in range(len(self.cada_curso)):                                                          # loop pra calcular cada CR envolvendo o curso
            nota_carga_c = (self.todos_cursos[j].notas * self.todos_cursos[j].carga).tolist()
            numerador_c = sum(nota_carga_c)
            carga_total_c = self.todos_cursos[j].carga.sum()
            coeficiente_c = round(numerador_c / carga_total_c, 2)
            self.cursos_cr.append([self.todos_cursos[j].codigo, coeficiente_c])


if __name__ == '__main__':

    iniciar = Controle('./Entrada/notas.csv')
    iniciar.lista_alunos()
    iniciar.calcular_cr()
    iniciar.media_cursos()

    print('------ O CR dos alunos é: ------')
    for aluno in iniciar.alunos_cr:
        print('{}  -  {}'.format(aluno[0], aluno[1]))
    print('--------------------------------')

    print('---- Média de CR dos cursos ----')
    for curso in iniciar.cursos_cr:
        print('{}   -   {}'.format(curso[0], curso[1]))
    print('--------------------------------')