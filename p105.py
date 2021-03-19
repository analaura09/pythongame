import run()
def notas(*n,sit=False):
    
    '''> funçaopara analisar notas e situaçoes de varios alunos'''

    r = dict()
    r['total'] = len(n)
    r['maior'] = len(n)
    r['menor'] = len(n)
    r['media'] = len(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situaçao'] = 'boa'
        elif r['media'] >= 5:
            r['situaçao'] = 'razoavel'
        else:
            r['situaçao'] = 'ruim'
    return r
resp= notas(9.0,5.5,8.0, sit=True)
print(resp)
#help(notas)
    
opçao = int(input('deseja repetir esse exercicio?[1] \ndeseja voltar para o mundo3? [2] \ndeseja sair do jogo?[3]'))
if opçao == 1:
    import p105
    p105.run()
if opçao ==2:
    import mundo3
    mundo3.run()
if opçao == 3:
    print('Obrigada por jogar! Volte sempre :)')
