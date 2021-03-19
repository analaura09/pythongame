def run():
    print('======================================')
    print('=== BEM VINDO AO MUNDO 1- FLORESTA ===')
    print('=== AS FASES DESSES MUNDO SAO ===')
    print('1. o que faz um programador \n2. para que serve o python? \n3. instalando o python 3 e o IDLE \n4. primeiros comandos em python \n5. instalando o IDE no PC e no celular')
    print('6. tipos primitivos e saidas de dados \n7. operadores aritimeticos \n8. ultilizando modulos \n9. manipulando strings \n10. estrutura condicional(parte 1) \n11. cores no terminal')
    print('12. <voltar para o menu do mundo>')
    opçao = int(input(' qual fase voce escolhe (digite um numero de 1 ao 12)?'))
    if opçao == 1:
        import fase1
    if opçao == 2:
        import fase2
    if opçao == 3:
        import fase3
    if opçao == 4:
        import fase4
    if opçao == 5:
        import fase5
    if opçao == 6:
        import fase6
    if opçao == 7:
        import fase7
    if opçao == 8:
        import fase8
    if opçao == 9:
        import fase9
    if opçao == 10:
        import fase10
    if opçao == 11:
        import fase11
    if opçao == 12:
        import menu
run()