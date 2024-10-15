from models import Carta
from regras_de_negocios import (
    distribuir_cartas,
    gerar_cartas_e_naipes,
    escolher_carta_ia,
    verificar_carta_vencedora_da_rodada,
)


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
    indice_da_rodada: int = 1

    pontos_equipe_1: int = 0
    pontos_equipe_2: int = 0
    while pontos_equipe_1 < 11 and pontos_equipe_2 < 11:
        pontos_equipe_1, pontos_equipe_2 = iniciar_rodada(
            indice_da_rodada, pontos_equipe_1, pontos_equipe_2
        )
        indice_da_rodada += 1
    if pontos_equipe_1 == 11 or pontos_equipe_2 == 11:
        pontos_equipe_1, pontos_equipe_2 = iniciar_rodada_final(
            indice_da_rodada, pontos_equipe_1, pontos_equipe_2
        )
        indice_da_rodada += 1

    if pontos_equipe_1 == 12:
        print("Equipe 1 venceu!")
    elif pontos_equipe_2 == 12:
        print("Equipe 2 venceu!")


def iniciar_mao(
    indice_da_rodada: int,
    indice_da_mao: int,
    pontos_equipe_1: int,
    pontos_equipe_2: int,
    pontos_equipe_1_rodada: int,
    pontos_equipe_2_rodada: int,
    cartas_jogador_1: list[Carta],
    cartas_jogador_2: list[Carta],
    cartas_jogador_3: list[Carta],
    cartas_jogador_4: list[Carta],
) -> tuple[int, int]:
    print(f"\n--- Rodada Geral: {indice_da_rodada}  | Mão: {indice_da_mao} ---")
    print(f"Equipe 1: {pontos_equipe_1} | Equipe 2: {pontos_equipe_2}")
    print(
        f"Rodada -> Equipe 1: {pontos_equipe_1_rodada} | Equipe 2: {pontos_equipe_2_rodada}"
    )

    cartas_da_rodada: dict[str, Carta | None] = {
        "jogador_1": None,
        "jogador_2": None,
        "jogador_3": None,
        "jogador_4": None,
    }

    print(f"Suas cartas: {[carta.nome for carta in cartas_jogador_1]}")
    print(f"Escolha uma carta: {[i for i in range(len(cartas_jogador_1))]}")
    posicao_da_carta_escolhida = input("Escolha uma carta: ")
    carta_escolhida = cartas_jogador_1.pop(int(posicao_da_carta_escolhida))
    print(f"Você escolheu a carta {carta_escolhida.nome}")

    cartas_da_rodada["jogador_1"] = carta_escolhida

    indice_carta_escolhida_jogador_2 = escolher_carta_ia(
        indice_da_mao=indice_da_mao,
        cartas_na_rodada=list(cartas_da_rodada.values()),
        carta_parceiro=None,
        cartas_disponiveis=cartas_jogador_2,
    )
    carta_escolhida_jogador_2 = cartas_jogador_2.pop(
        int(indice_carta_escolhida_jogador_2)
    )
    cartas_da_rodada["jogador_2"] = carta_escolhida_jogador_2
    print(f"IA 2 escolheu a carta {carta_escolhida_jogador_2.nome}")

    indice_carta_escolhida_jogador_3 = escolher_carta_ia(
        indice_da_mao=indice_da_mao,
        cartas_na_rodada=list(cartas_da_rodada.values()),
        carta_parceiro=None,
        cartas_disponiveis=cartas_jogador_3,
    )
    carta_escolhida_jogador_3 = cartas_jogador_3.pop(
        int(indice_carta_escolhida_jogador_3)
    )
    cartas_da_rodada["jogador_3"] = carta_escolhida_jogador_3
    print(f"IA 3 escolheu a carta {carta_escolhida_jogador_3.nome}")

    indice_carta_escolhida_jogador_4 = escolher_carta_ia(
        indice_da_mao=indice_da_mao,
        cartas_na_rodada=list(cartas_da_rodada.values()),
        carta_parceiro=None,
        cartas_disponiveis=cartas_jogador_4,
    )
    carta_escolhida_jogador_4 = cartas_jogador_4.pop(
        int(indice_carta_escolhida_jogador_4)
    )
    cartas_da_rodada["jogador_4"] = carta_escolhida_jogador_4
    print(f"IA 4 escolheu a carta {carta_escolhida_jogador_4.nome}")

    jogador_vencedor = verificar_carta_vencedora_da_rodada(cartas_da_rodada)
    if jogador_vencedor == "jogador_1" or jogador_vencedor == "jogador_3":
        pontos_equipe_1_rodada += 1
        equipe_vencedora = "Equipe 1"
    else:
        pontos_equipe_2_rodada += 1
        equipe_vencedora = "Equipe 2"

    print(f"Vencedor da mão: {jogador_vencedor} | {equipe_vencedora}")

    return pontos_equipe_1_rodada, pontos_equipe_2_rodada


def iniciar_rodada(
    indice_da_rodada: int, pontos_equipe_1: int, pontos_equipe_2: int
) -> tuple[int, int]:
    """
    Cada rodada tem 2 ou três mãos, dependendo do resultado
    """

    pontos_equipe_1_rodada: int = 0
    pontos_equipe_2_rodada: int = 0

    cartas_jogador_1, cartas_jogador_2, cartas_jogador_3, cartas_jogador_4 = (
        distribuir_cartas(gerar_cartas_e_naipes())
    )

    for indice_da_mao in range(1, 4):
        if pontos_equipe_1_rodada < 2 and pontos_equipe_2_rodada < 2:
            pontos_equipe_1_rodada, pontos_equipe_2_rodada = iniciar_mao(
                indice_da_rodada,
                indice_da_mao,
                pontos_equipe_1,
                pontos_equipe_2,
                pontos_equipe_1_rodada,
                pontos_equipe_2_rodada,
                cartas_jogador_1,
                cartas_jogador_2,
                cartas_jogador_3,
                cartas_jogador_4,
            )

    pontos_da_rodada = max(pontos_equipe_1_rodada, pontos_equipe_2_rodada)

    if pontos_da_rodada == 2:
        pontos_da_rodada = 1

    if pontos_equipe_1_rodada > pontos_equipe_2_rodada:
        pontos_equipe_1 += pontos_da_rodada
        print(f"Equipe 1 venceu a rodada {indice_da_rodada}")
    else:
        pontos_equipe_2 += pontos_da_rodada
        print(f"Equipe 2 venceu a rodada {indice_da_rodada}")

    return pontos_equipe_1, pontos_equipe_2


def iniciar_rodada_final(
    indice_da_rodada: int, pontos_equipe_1: int, pontos_equipe_2: int
) -> tuple[int, int]:
    # todo implementar rodada diferenciada
    return iniciar_rodada(
        indice_da_rodada=indice_da_rodada,
        pontos_equipe_1=pontos_equipe_1,
        pontos_equipe_2=pontos_equipe_2,
    )


if __name__ == "__main__":
    main()
