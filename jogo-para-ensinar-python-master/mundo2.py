def run():
    print('==================================')
    print('=== BEM VINDO AO MUNDO 2- GELO ===')
    print('=== AS FASES DESSE MUNDO SAO ===')
    print('12. condiçoes aninhadas')
    print('13. estrutura de repetiçao for')
    print('14. estrutura de repetiçao while')
    print("15. interrompendo repetiçoes while")
    print('16. <voltar para o menu dos mundos>')
    opçao = int(input('qual fase voce escolhe(digite um numero do 12 ao 16)?'))
    if opçao == 12:
        import fase12
        fase12.run()
    if opçao == 13:
        import fase13
        fase13.run()
    if opçao == 15:
        import fase15
        fase15.run()
    if opçao == 14:
        import fase14
        fase14.run()
    if opçao == 16:
        import menu
        menu.run()
run()