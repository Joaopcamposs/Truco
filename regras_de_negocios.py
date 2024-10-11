import random

from models import Carta
from objetos_de_valor import Naipes, VALORES_DAS_CARTAS


def verificar_manilha(nome_carta: str) -> str:
    if nome_carta == "A de Espadas":
        return "Espadilha"
    elif nome_carta == "4 de Paus":
        return "Zap"
    return nome_carta


def gerar_cartas_e_naipes():
    cartas: list[Carta] = []

    naipes = [naipe.value for naipe in Naipes]
    for naipe in naipes:
        for valor_carta in VALORES_DAS_CARTAS:
            nome_carta = f"{valor_carta} de {naipe}"
            nome_carta = verificar_manilha(nome_carta)

            carta = Carta(
                nome=nome_carta,
                valor=valor_carta,
                naipe=naipe,
                peso=VALORES_DAS_CARTAS.index(valor_carta),
            )
            cartas.append(carta)

    return cartas


def distribuir_cartas(
    cartas: list[Carta],
) -> tuple[list[Carta], list[Carta], list[Carta], list[Carta]]:
    random.shuffle(cartas)

    mao_jogador_1: list[Carta] = cartas[:3]
    mao_jogador_2: list[Carta] = cartas[3:6]
    mao_jogador_3: list[Carta] = cartas[6:9]
    mao_jogador_4: list[Carta] = cartas[9:12]

    return mao_jogador_1, mao_jogador_2, mao_jogador_3, mao_jogador_4


def escolher_carta_ia(
    rodada_atual: int,
    cartas_mesa: list[Carta],
    carta_parceiro: Carta,
) -> Carta: ...
