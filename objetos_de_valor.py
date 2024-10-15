from enum import Enum

PESO_DAS_CARTAS: tuple[str, ...] = (
    "Zap",
    "7 de Copas",
    "Espadilha",
    "7 de Ouros",
    "3",
    "2",
    "A",
    "K",
    "J",
    "Q",
    "7",
    "6",
    "5",
    "4",
)

VALORES_DAS_CARTAS: tuple[str, ...] = ("A", "K", "J", "Q", "7", "6", "5", "4", "3", "2")

FIGURAS_DOS_NAIPES: list[str] = ["♠", "♣", "♦", "♥"]


class Naipes(Enum):
    OUROS = "Ouros"
    ESPADAS = "Espadas"
    COPAS = "Copas"
    PAUS = "Paus"
