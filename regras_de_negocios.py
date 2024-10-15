import random

from models import Carta
from objetos_de_valor import Naipes, VALORES_DAS_CARTAS, PESO_DAS_CARTAS


def extrair_peso_pelo_nome_da_carta(nome_carta: str) -> str:
    nome_carta = verificar_manilha(nome_carta)
    if nome_carta not in ["Espadilha", "Zap", "7 de Copas", "7 de Ouros"]:
        return nome_carta.split(" de ")[0]
    return nome_carta


def verificar_manilha(nome_carta: str) -> str:
    if nome_carta == "A de Espadas":
        return "Espadilha"
    elif nome_carta == "4 de Paus":
        return "Zap"
    else:
        return nome_carta


def gerar_cartas_e_naipes():
    cartas: list[Carta] = []

    naipes = [naipe.value for naipe in Naipes]
    for naipe in naipes:
        for valor_carta in VALORES_DAS_CARTAS:
            nome_carta = f"{valor_carta} de {naipe}"
            peso_carta = extrair_peso_pelo_nome_da_carta(nome_carta)
            nome_carta = verificar_manilha(nome_carta)

            carta = Carta(
                nome=nome_carta,
                valor=valor_carta,
                naipe=naipe,
                peso=PESO_DAS_CARTAS.index(peso_carta),
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
    indice_da_mao: int,
    cartas_na_rodada: list[Carta | None],
    carta_parceiro: Carta | None,
    cartas_disponiveis: list[Carta],
) -> Carta | int:
    """
    Logicas para escolher a carta da IA. Iremos evoluindo ela, iniciaremos com escolhas simples, randomicas
    """
    ...
    # todo decidir a carta a ser jogada de acordo com rodada, cartas na mesa, carta do parceiro e cartas disponiveis
    # return random.choice(cartas_disponiveis)
    return random.randint(0, len(cartas_disponiveis) - 1)


def verificar_carta_vencedora_da_rodada(lista_de_cartas: dict[str, Carta]) -> str:
    menor_indice = float(
        "inf"
    )  # Começa com um valor infinito para facilitar a comparação
    jogador_com_maior_carta: str = ""

    for jogador, carta in lista_de_cartas.items():
        if carta.peso < menor_indice:
            menor_indice = carta.peso
            jogador_com_maior_carta = jogador

    # todo adicionar empate

    return jogador_com_maior_carta
