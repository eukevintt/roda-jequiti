import pygame
import random
import sys
import time
import unicodedata
import basededados

pygame.mixer.init()


def roletaRodando():
    # Função que quando chamada, a roleta é girada.
    print('Girando a roleta...')
    pygame.mixer.music.load('musics/roleta.mp3')
    pygame.mixer.music.play()
    time.sleep(13.5)
    roleta = ['Passa a Vez', 'Perdeu Tudo'] + list(range(100, 1000))[::50] + [1000, 1000, 'Passa a Vez', 'Perdeu Tudo']
    return random.choice(roleta)


def listaPalavrasAnom(listaPalavras):
    # Pega a lista de palavras e transforma as palavras em anônimo.
    # list -> list
    i = 0
    novaLista = []
    palavrasAnom = []
    while i < len(listaPalavras):
        a = 0
        palavrasAnom.clear()
        while a < len(listaPalavras[i]):
            palavrasAnom.append('_')
            a = a + 1
        palavrasAnoma = palavrasAnom[:]
        novaLista.append(palavrasAnoma)
        i = i + 1
    return novaLista


def placar(rodada, turno, listaPontos, palavrasMostrar, palavraLista, letrasErradas, participantes, escolhaRoleta):
    # Uma função que retorna o placar, toda vez que o código reinicia
    # int, int, int, list, list, list, list, tuple
    print('+===============================================')
    print('| RODADA {} - TURNO {}'.format(rodada, turno))
    print('+===============================================')
    print('| ANA - {} | BARBARA - {} | CARLOS - {}'.format(listaPontos[0], listaPontos[1], listaPontos[2]))
    print('+===============================================')
    print('Jogador ativo: {}'.format(participantes[i]))
    print('Pontuação atual: {}'.format(listaPontos[i]))
    print('Roleta: {}'.format(escolhaRoleta))
    print('Nova pontuacao: {}'.format(
        escolhaRoleta + listaPontos[i] if isinstance(escolhaRoleta, int) else escolhaRoleta))
    print('+===============================================')
    print('Tema: {}'.format(tema))
    print('P1) {} (contendo {} letras a palavra é {})'.format(''.join(palavrasMostrar[0]), len(palavrasMostrar[0]),
                                                              palavraLista[0]))
    print('P2) {} (contendo {} letras a palavra é {})'.format(''.join(palavrasMostrar[1]), len(palavrasMostrar[1]),
                                                              palavraLista[1]))
    print('P3) {} (contendo {} letras a palavra é {})'.format(''.join(palavrasMostrar[2]), len(palavrasMostrar[2]),
                                                              palavraLista[2]))
    print('Letras Erradas: {}'.format('-'.join(letrasErradas)))


def fimDoPrograma(participante):
    # Assim que o número total de letras forem concluidas, essa função mostra o ganhador.
    # str -> str
    print('E o ganhador dessa edição é...')
    time.sleep(1)
    print('Parabéns {}, você é o ganhador de hoje!'.format(participante))
    pygame.mixer.music.load('musics/ganhou.mp3')
    pygame.mixer.music.play()
    time.sleep(8)
    sys.exit()


def tiraAcentos(palavra):
    # Função que retira os acentos de uma string utilizando o modulo unicodedata
    # str -> str
    return unicodedata.normalize('NFD', palavra).encode('ASCII', 'ignore').decode('utf-8')


# Pega um tema aleatório da lista e de dentro desse tema, pega 3 assuntos.
tema = random.choice(list(basededados.base_de_dados))
random.shuffle(basededados.base_de_dados[tema])


i = 0
palavraListaAcento = []
palavraLista = []
while i < 3:
    palavraListaAcento.append(basededados.base_de_dados[tema][i])
    i = i + 1

for palavra in palavraListaAcento:
    palavraSemAcento = tiraAcentos(palavra)
    palavraLista.append(palavraSemAcento)
# --------------------------------------------------------------------


pontos = [0, 0, 0]  # Pontos iniciais
participantes = ['Ana', 'Bárbara', 'Carlos']  # Participantes que irão participar
rodada = 0 # Rodada Inicial
turno = 0 # Turno Inicial

palavrasMostrar = listaPalavrasAnom(palavraLista)  # Palavras com anonimato
letrasErradas = [] # Lista com todas as letras erradas, que o usuário digitar
i = 0
fimDoPrograma = 0
tamanhoDasPalavras = len(palavraLista[0]) + len(palavraLista[1]) + len(palavraLista[2])
while fimDoPrograma < tamanhoDasPalavras:
    i = 0
    turno = 1
    rodada = rodada + 1

    while i < len(participantes):
        escolhaRoleta = roletaRodando()

        placar(rodada, turno, pontos, palavrasMostrar, palavraLista, letrasErradas, participantes, escolhaRoleta)

        if escolhaRoleta == 'Passa a Vez':
            input('Passou a vez, aperte enter para continuar')
            i = i + 1
            turno = turno + 1

        elif escolhaRoleta == 'Perdeu Tudo':
            pygame.mixer.music.load('musics/perdeutudo.mp3')
            pygame.mixer.music.play()
            pontos[i] = 0
            time.sleep(5)
            i = i + 1
            turno = turno + 1

        a = 0
        if escolhaRoleta != 'Passa a Vez' and escolhaRoleta != 'Perdeu Tudo':
            letraEscolhida = input('{}, Escolha uma letra: '.format(participantes[i]))
            while a < len(palavraLista[0]):
                if letraEscolhida.upper() == palavraLista[0][a].upper():
                    palavrasMostrar[0][a] = palavraLista[0][a].upper()
                    pygame.mixer.music.load('musics/acerto.wav')
                    pygame.mixer.music.play()
                    fimDoPrograma = fimDoPrograma + 1
                    time.sleep(0.5)
                a = a + 1
            b = 0
            while b < len(palavraLista[1]):
                if letraEscolhida.upper() == palavraLista[1][b].upper():
                    palavrasMostrar[1][b] = palavraLista[1][b].upper()
                    pygame.mixer.music.load('musics/acerto.wav')
                    pygame.mixer.music.play()
                    fimDoPrograma = fimDoPrograma + 1
                    time.sleep(0.5)
                b = b + 1
            c = 0
            while c < len(palavraLista[2]):
                if letraEscolhida.upper() == palavraLista[2][c].upper():
                    palavrasMostrar[2][c] = palavraListaAcento[2][c].upper()
                    pygame.mixer.music.load('musics/acerto.wav')
                    pygame.mixer.music.play()
                    fimDoPrograma = fimDoPrograma + 1
                    time.sleep(0.5)
                c = c + 1
            if letraEscolhida.upper() not in palavraLista[0].upper() and letraEscolhida.upper() not in palavraLista[
                1].upper() and letraEscolhida.upper() not in \
                    palavraLista[2].upper():
                turno = turno + 1
                if letraEscolhida.upper() in letrasErradas:
                    pygame.mixer.music.load('musics/erro.mp3')
                    pygame.mixer.music.play()
                    print('\033[1;41mA letra que você digitou já foi digitada antes, digite outra!\033[m')
                    time.sleep(3)
                else:
                    pygame.mixer.music.load('musics/erro.mp3')
                    pygame.mixer.music.play()
                    time.sleep(1)
                    letrasErradas.append(letraEscolhida.upper())
                    i = i + 1

            if fimDoPrograma == tamanhoDasPalavras:
                fimDoPrograma(participantes)

            if fimDoPrograma >= (tamanhoDasPalavras - 3):
                placar(rodada, turno, pontos, palavrasMostrar, palavraLista, letrasErradas, participantes,
                       escolhaRoleta)
                poderEscolher = input('Você quer dizer a palavra inteira? (s/n)').upper()
                if poderEscolher == 'S':
                    pygame.mixer.music.load('musics/segundos.mp3')
                    pygame.mixer.music.play()
                    print('5 Segundos para pensar...')
                    time.sleep(5)
                    vitoria = 0
                    for palavra in palavraLista:
                        respostasFinais = input('Qual a palavra?').upper()
                        if respostasFinais.upper() == palavra.upper():
                            vitoria = vitoria + 1
                        if vitoria == 3:
                            fimDoPrograma(participantes[i - 2])
                        else:
                            i = i + 1

            if letraEscolhida.upper() in palavraLista[0].upper() or letraEscolhida.upper() in palavraLista[
                1].upper() or letraEscolhida.upper() in palavraLista[2].upper():
                pontos[i] = pontos[i] + escolhaRoleta
                turno = turno + 1
