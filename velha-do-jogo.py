#tabuleiro
tabuleiro = ['-','-','-',
             '-','-','-',
             '-','-','-']
# exibir tabuleiro
def exiba_tabuleiro():
    t = tabuleiro
    print(t[0], '|' ,t[1], '|' ,t[2])
    print(t[3], '|' ,t[4], '|' ,t[5])
    print(t[6], '|' ,t[7], '|' ,t[8])

proximo = 'O'
def troca_jogador():
    global proximo
    if  proximo == 'X':
        proximo = 'O'
    else:
        proximo = 'X'

#jogadas

def pega_jogada():
    while True:
        posicao = input('Digite uma posição de (1 a 9):')
        posicao = int(posicao)-1
        if  tabuleiro[posicao] == '-':
            tabuleiro[posicao] = proximo
            break

def analisar_linhas():
linha1 = tabuleiro[0] == tabuleiro[1] == tabuleiro[2]
if linha1:
    if tabuleiro == [0] == 'X':
        return 'X'
    if tabuleiro == [0] == 'O':
        return 'O'
if linha2 = tabuleiro[3] == tabuleiro[4] ==
def analisar_colunas():
coluna1 =
coluna2 =
coluna3 =
def analisar_diagonais():
diagonal1 =
diagonal2 =

#trocar de jogador

jogo_nao_acabe = True

def checa_se_acabou():
        global jogo_nao_acabe
        t = tabuleiro
        jogo_nao_acaba = '-' in t

#Analisando resultado

def jogar():
    while jogo_nao_acabe:
        exiba_tabuleiro()
        pega_jogada()
        troca_jogador()
        checa_vencedor()
        checa_se_acabou()
    exiba_tabuleiro()
jogar()
