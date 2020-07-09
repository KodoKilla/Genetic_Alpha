## ORGANIZAR EM FUNCOES POSTERIORMENTE ##
# FEITO POR: ENZO TRAMONTIN
# OBJETIVO: MONTAR UMA ESTRUTURA(INDUCAO DE ARVORES DE DECISAO) PARA UTILIZACAO FUTURA EM ARVORES DE DECISAO PARA PREVISAO DE RESULTADOS

####################################################################
# CRIAR UM SISTEMA GENETICO CAPAZ DE ESCOLHER UMA COLUNA E MONTAR UM PADRAO
# TESTAR ESSE PADRAO NA BASE DE TESTE PARA FITNESS (ARVORE DE DECISAO)
# BASEADO NO FITNESS, REPRODUZIR
# REPRODUCAO DEVE GERAR UMA COMPARACAO MAIS COMPLEXA COM AND E OR

# CAMPOS - VERSAO BASICA - PARA ESTRUTURAS MAIS COMPLEXAS TEREI QUE REVER
# COLUNA DO TESTE
# OPERACAO DO TESTE
# VALOR DO TESTE
# RESULTADO
# FITNESS
####################################################################
# ESTRUTURA DE TESTE

# COLUNAS - PRECO, MANUTENCAO, PORTAS, CAPACIDADE, PORTA-MALAS, SEGURANCA

# OPERACOES - =, !

# VALOR - VALOR ATUAL DO CAMPO A SER COMPARADO

# RESULTADO - INACEITO, ACEITO, BOM, MUITO BOM

# FITNESS - VALOR DE FITNESS

####################################################################

# [COL, VALOR, RESULTADO, FIT]

####################################################################
import pandas as pd
import numpy as np
import random


def print_pop(populacao):
    #Exibicao de cada individuo#
    for i in populacao:
        print(i)

def divide_dataset(col, dataset):
    for i in range(0, col-1):
        x = 1

    return 1

def get_coluna(col, individuo):
    coluna = random.randint(0, col)
    individuo.append(coluna)

    return coluna

def get_valor(dataframe, coluna, individuo):
    dataframe = dataframe[[str(coluna)]]
    valores = pd.unique(dataframe.to_numpy().reshape(-1))
    rangevalores = valores.shape[0]
    valor = random.randint(0, rangevalores - 1)
    individuo.append(valor)

    return valores

def get_preview(ultima_coluna, individuo):
    valores = pd.unique(ultima_coluna.to_numpy().reshape(-1))
    rangevalores = valores.shape[0]
    valor = random.randint(0, rangevalores - 1)
    individuo.append(valor)

    return valores

def inicializa_pop(dataframe, df_teste, col, pessoas, ultima_coluna):

    for i in range(0, pessoas):
        individuo = []
        coluna = get_coluna(col, individuo)
        valores = get_valor(dataframe, coluna, individuo)
        previsao = get_preview(ultima_coluna, individuo)
        traduz_individuo(individuo, valores, previsao)

        fit = fitness(df_teste, individuo)
        individuo.append(fit)
        if(i == 0):
            melhor = individuo
        if(individuo[3] > melhor[3]):
            melhor = individuo
    print(melhor)
    return 1

def traduz_individuo(individuo, valores, previsao):

    individuo[1] = valores[individuo[1]]
    individuo[2] = previsao[individuo[2]]

def fitness(dataframe, individuo):
    acertos = 0
    for i in range(len(dataframe)):
        if(dataframe.iloc[i, individuo[0]] == individuo[1]):
            classificacao = individuo[2]
        else:
            classificacao = 'v-good'
        if(classificacao == dataframe.iloc[i, dataframe.shape[1] - 1]):
            acertos += 1

    fitness = (acertos / len(dataframe)) * 100

    return fitness

def main():

    df = pd.DataFrame(pd.read_csv('car.csv'))
    ultima_coluna = df.iloc[:, -1]

    df_teste = df[round((len(df) - (len(df)/3))):len(df)]

    qtd_Colunas = df.shape[1] - 2 #Removendo a coluna a ser prevista

    inicializa_pop(df, df_teste, qtd_Colunas, 3, ultima_coluna)

main()
