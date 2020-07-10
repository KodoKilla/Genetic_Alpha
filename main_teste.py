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

def get_coluna(dataframe ,col, individuo):
    for coluna in range(0, col):
        individuo.append(coluna)
        get_valor(dataframe, coluna, individuo)

    return True

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
    individuos = []
    for i in range(0, pessoas):
        individuo = []
        get_coluna(dataframe, col, individuo)
        previsao = get_preview(ultima_coluna, individuo)
        traduz_individuo(dataframe, individuo, previsao)

        fit = fitness(dataframe, individuo)
        individuo.append(fit)
        if(i == 0):
            melhor = individuo
        if(individuo[len(individuo)-1] > melhor[len(individuo)-1]):
            melhor = individuo
        individuos.append(individuo)
    print('Melhor: ',melhor)

    # print(individuos[1][1]) --> 1 Individuo - Coluna 2
    for i in range(0, len(individuos)):
        print(get_par(individuos))
    return 1

def traduz_individuo(df, individuo, previsao):
    for i in range(0, 6):
        dataframe = df[[str(i)]]
        valores = pd.unique(dataframe.to_numpy().reshape(-1))
        individuo[i+(i+1)] = valores[individuo[i+(i+1)]]
    individuo[12] = previsao[individuo[12]]

def fitness(df_teste, individuo):
    acertos = 0
    total_carac = 0
    for x in range(len(df_teste)):
        classificacao = 1
        total_carac = 0
        for i in range(0, 6):
            if(df_teste.iloc[x, individuo[i*2]] == individuo[i+(i+1)]):
                classificacao = individuo[12]
                total_carac += 1
        if(classificacao == 1):
            classificacao = '1'
        if(classificacao == df_teste.iloc[x, df_teste.shape[1] - 1] and total_carac == 6):
            acertos += 1

    fitness = (acertos / len(df_teste)) * 100

    return fitness

def get_par(individuos):
    total = len(individuos)

    posicao = np.random.randint(0, total)
    return posicao

def crossover(individuos, taxa_co):
    return True

def main():
    # Parametros
    tamanhopop = 4
    dados = 'car.csv'


    # Inicializacao
    df = pd.DataFrame(pd.read_csv(dados))
    ultima_coluna = df.iloc[:, -1]
    df_teste = df[round((len(df) - (len(df)/3))):len(df)]
    qtd_Colunas = df.shape[1] - 1 #Removendo a coluna a ser prevista

    inicializa_pop(df, df_teste, qtd_Colunas, tamanhopop, ultima_coluna)

main()
