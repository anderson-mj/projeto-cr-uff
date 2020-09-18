# projeto-cr-uff

Projeto do desafio 3 do Processo de Seleção do STI. O programa recebe um arquivo csv, lê e manipula seus dados usando a biblioteca do Pandas.

## controle.py

Nesse programa acontece o processamento dos dados pro fim desejado, usando as classes importadas, cria uma lista que contém cada aluno do arquivo como um objeto da classe Alunos. Usando suas matrículas, notas e cargas horárias, seleciona cada aluno para calcular seus respectivos CRs.

## Aluno.py

Armazena a classe que recebe os dados de cada aluno e os armazena como atributos.

## Disciplina.py

Esse armazena a classe Disciplina, que recebe a matrícula do aluno e também recebe o arquivo a ser manipulado para relacionar cada disciplina com seu semestre cursado pelo aluno.

## Curso.py

Armazena cada curso e seus atributos são usados no cálculo do CR médio dos cursos.


## /Entrada

Essa pasta contém o arquivo csv usado nesse exemplo como entrada.