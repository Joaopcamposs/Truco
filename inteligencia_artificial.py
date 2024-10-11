import random
import numpy as np
from sklearn.tree import DecisionTreeClassifier

# Simulando dados de treinamento (rodada, carta_jogador, carta_ia, ação da IA)
# Para simplificar, as ações são jogar a carta de índice 0, 1 ou 2
dados_treinamento = []
acoes_treinamento = []


# Função para simular dados de treinamento
def gerar_dados_treinamento():
    for i in range(1000):  # Gerando 1000 rodadas de dados
        rodada = random.randint(1, 3)
        carta_jogador = random.randint(1, 10)  # Valor de 1 a 10
        carta_ia_1 = random.randint(1, 10)
        carta_ia_2 = random.randint(1, 10)
        carta_ia_3 = random.randint(1, 10)

        # IA escolhe a ação baseada na carta mais alta, média ou baixa (simplificação)
        if rodada == 1:
            acao = np.argmax(
                [carta_ia_1, carta_ia_2, carta_ia_3]
            )  # Joga carta mais alta na rodada 1
        else:
            acao = np.argmin(
                [carta_ia_1, carta_ia_2, carta_ia_3]
            )  # Joga a mais baixa nas outras rodadas

        # Adiciona os dados ao treinamento
        dados_treinamento.append(
            [rodada, carta_jogador, carta_ia_1, carta_ia_2, carta_ia_3]
        )
        acoes_treinamento.append(acao)


# Gera os dados de treinamento
gerar_dados_treinamento()

# Treinando a árvore de decisão
modelo = DecisionTreeClassifier()
modelo.fit(dados_treinamento, acoes_treinamento)


# Função que a IA usará para tomar decisões baseadas no modelo
def jogada_ia_inteligente(rodada, carta_jogador, mao_ia):
    carta_ia_1, carta_ia_2, carta_ia_3 = mao_ia
    acao = modelo.predict([[rodada, carta_jogador, carta_ia_1, carta_ia_2, carta_ia_3]])
    return mao_ia[acao[0]]


# Exemplo de uso
rodada = 1
mao_jogador = random.randint(1, 10)
mao_ia = [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]

# IA toma a decisão com base no modelo treinado
carta_escolhida = jogada_ia_inteligente(rodada, mao_jogador, mao_ia)
print(f"IA escolheu a carta: {carta_escolhida}")
