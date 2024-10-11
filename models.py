from dataclasses import dataclass


@dataclass
class Carta:
    valor: str
    naipe: str
    nome: str
    peso: int
