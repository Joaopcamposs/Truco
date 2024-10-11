import random

# Definindo as cartas do Truco
cartas = [
    ("4", 1),
    ("5", 2),
    ("6", 3),
    ("7", 4),
    ("Q", 5),
    ("J", 6),
    ("K", 7),
    ("A", 8),
    ("2", 9),
    ("3", 10),
]

# Definindo as manilhas (cartas mais fortes)
manilhas = {"4": 11, "5": 12, "6": 13, "7": 14}


# Função para embaralhar e distribuir as cartas
def distribuir_cartas():
    baralho = cartas * 4
    random.shuffle(baralho)
    mao_jogador = baralho[:3]
    mao_ia = baralho[3:6]
    return mao_jogador, mao_ia


# Função para exibir cartas do jogador
def mostrar_mao(mao):
    print("Suas cartas são:")
    for i, carta in enumerate(mao):
        print(f"{i + 1}: {carta[0]}")


# Função para avaliar o valor das cartas, incluindo manilhas
def valor_carta(carta):
    valor = carta[1]
    if carta[0] in manilhas:
        valor = manilhas[carta[0]]
    return valor


# Função de jogada da IA
def jogada_ia(mao_ia, rodada_atual):
    if rodada_atual == 0:
        # Joga a carta mais fraca na primeira rodada
        return min(mao_ia, key=lambda c: valor_carta(c))
    else:
        # Joga a carta mais forte nas rodadas seguintes
        return max(mao_ia, key=lambda c: valor_carta(c))


# Função que controla as rodadas
def jogar_rodada(mao_jogador, mao_ia):
    rodada = 0
    pontos_jogador = 0
    pontos_ia = 0

    while rodada < 3:
        print(f"\n--- Rodada {rodada + 1} ---")
        mostrar_mao(mao_jogador)

        # Jogador escolhe sua carta
        escolha = int(input("Escolha uma carta para jogar (1, 2, 3): ")) - 1
        carta_jogador = mao_jogador.pop(escolha)

        # IA escolhe sua carta
        carta_ia = jogada_ia(mao_ia, rodada)
        mao_ia.remove(carta_ia)

        print(f"Você jogou {carta_jogador[0]}, IA jogou {carta_ia[0]}")

        # Avalia quem venceu a rodada
        if valor_carta(carta_jogador) > valor_carta(carta_ia):
            print("Você venceu a rodada!")
            pontos_jogador += 1
        else:
            print("IA venceu a rodada!")
            pontos_ia += 1

        rodada += 1

        if pontos_jogador == 2:
            print("\nVocê ganhou a partida!")
            return
        elif pontos_ia == 2:
            print("\nIA ganhou a partida!")
            return


# Função principal do jogo
def jogar_truco():
    mao_jogador, mao_ia = distribuir_cartas()
    jogar_rodada(mao_jogador, mao_ia)


# Inicia o jogo
if __name__ == "__main__":
    jogar_truco()
