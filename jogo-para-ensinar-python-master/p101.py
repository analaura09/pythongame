import run()
            solução:
            def voto(ano):
            from datetime import datetime
            now = datetime.now()
            soma = now.year - ano
            if soma >= 18 and soma <65:
                return f'Você tem {soma} anos de idade, e você deve votar!'
            elif soma < 16:
                return f'Você tem {soma} anos de idade, e você ainda não pode votar'
            elif soma > 65:
                return f'Você tem {soma} anos de idade, e seu voto é opcional'
            elif 16 <= soma < 18:
                return f'Vocẽ tem {soma} anos de idade, e seu voto é opcional'

        ano = int(input('Em que ano você nasceu: '))
        print(voto(ano))

opçao = int(input('deseja repetir esse exercicio?[1] \ndeseja voltar para o mundo3? [2] \ndeseja sair do jogo?[3]'))
if opçao == 101:
    import p101
    p101.run()
if opçao ==2:
    import mundo3
    mundo3.run()
if opçao == 3:
    print('Obrigada por jogar! Volte sempre :)')
