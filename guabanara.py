sala = []
aluno = {}

for i in range (1, 4):
    aluno['name'] = str(input('Nome: '))
    aluno['nota'] = int(input('Nota: '))

    if aluno['nota'] > 7:
        aluno['situacao']='aprovado'
    else:
        aluno['situacao']='reprovado'
    sala.append(aluno.copy())

print(sala)