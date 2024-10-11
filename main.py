from models import Carta
from regras_de_negocios import distribuir_cartas, gerar_cartas_e_naipes


def main():
    entrada = menu()
    if entrada == 1:
        iniciar_novo_jogo()
    elif entrada == 0:
        exit()


def menu() -> int:
    print("Bem-vindo ao jogo de truco!")
    print("Escolha uma opção:")
    print("1 - Iniciar novo jogo")
    print("0 - Sair")
    entrada = input("Opção: ")
    return int(entrada)


def iniciar_novo_jogo():
    pontos_equipe_1: int = 0
    pontos_equipe_2: int = 0
    while pontos_equipe_1 < 11 or pontos_equipe_2 < 11:
        pontos_equipe_1, pontos_equipe_2 = iniciar_rodada(
            pontos_equipe_1, pontos_equipe_2
        )
    if pontos_equipe_1 == 11 or pontos_equipe_2 == 11:
        pontos_equipe_1, pontos_equipe_2 = iniciar_rodada_final(
            pontos_equipe_1, pontos_equipe_2
        )

    if pontos_equipe_1 == 12:
        print("Equipe 1 venceu!")
    elif pontos_equipe_2 == 12:
        print("Equipe 2 venceu!")


def iniciar_mao(
    pontos_equipe_1_rodada: int, pontos_equipe_2_rodada: int
) -> tuple[int, int]:
    carta_da_rodada: list[Carta] = []
    cartas_jogador_1, cartas_jogador_2, cartas_jogador_3, cartas_jogador_4 = (
        distribuir_cartas(gerar_cartas_e_naipes())
    )

    # todo alterar para print posicao
    print(f"Suas cartas: {[carta.nome for carta in cartas_jogador_1]}")
    print(f"Escolha uma carta: {[i for i in range(len(cartas_jogador_1))]}")
    posicao_da_carta_escolhida = input("Escolha uma carta: ")
    carta_escolhida = cartas_jogador_1.pop(int(posicao_da_carta_escolhida))
    print(f"Você escolheu a carta {carta_escolhida.nome}")

    carta_da_rodada.append(carta_escolhida)

    return pontos_equipe_1_rodada, pontos_equipe_2_rodada


def iniciar_rodada(pontos_equipe_1: int, pontos_equipe_2: int) -> tuple[int, int]:
    pontos_equipe_1_rodada: int = 0
    pontos_equipe_2_rodada: int = 0

    while pontos_equipe_1_rodada < 3 or pontos_equipe_2_rodada < 3:
        pontos_equipe_1_rodada, pontos_equipe_2_rodada = iniciar_mao(
            pontos_equipe_1_rodada, pontos_equipe_2_rodada
        )

    if pontos_equipe_1_rodada > pontos_equipe_2_rodada:
        pontos_equipe_1 += 1
    elif pontos_equipe_2_rodada > pontos_equipe_1_rodada:
        pontos_equipe_2 += 1

    return pontos_equipe_1, pontos_equipe_2


def iniciar_rodada_final(pontos_equipe_1: int, pontos_equipe_2: int) -> tuple[int, int]:
    # criar uma nova rodada
    return pontos_equipe_1, pontos_equipe_2


if __name__ == "__main__":
    main()
