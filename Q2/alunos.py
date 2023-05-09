def alunos_acima_media(situacao):
    alunos_acima_media = [(aluno, nota) for aluno, nota in situacao if nota > 7]
    return alunos_acima_media
