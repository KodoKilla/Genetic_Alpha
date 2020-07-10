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

# [COL, VALOR, RESULTADO]*N, [FIT]

####################################################################
import pandas as pd
import numpy as np
import random
import copy

def print_pop(populacao):
    #Exibicao de cada individuo#
    for i in populacao:
        print(i)
        print()

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
        individuo_valores = []
        individuo = []
        get_coluna(dataframe, col, individuo_valores)
        previsao = get_preview(ultima_coluna, individuo_valores)
        traduz_individuo(dataframe, individuo_valores, previsao)
        individuo.append(individuo_valores)
        individuos.append(individuo)
    #del melhor[len(melhor)-1] #-> Remover Fitness
    return individuos

def traduz_individuo(df, individuo, previsao):
    for i in range(0, 6):
        dataframe = df[[str(i)]]
        valores = pd.unique(dataframe.to_numpy().reshape(-1))
        individuo[i+(i+1)] = valores[individuo[i+(i+1)]]
    individuo[12] = previsao[individuo[12]]

def fitness(df_teste, individuo):
    ## Alterar fitness para ser uma estrutura
    acertos = 0
    fitness = [1]
    for teste in range(len(df_teste)):
        classificacao = 1
        melhor_coluna = 0
        melhor_valor = 0
        for solucao in range(len(individuo)):
            total_carac = 0
            for coluna in range(0, 6):
                col_teste = individuo[solucao][coluna*2]
                valor_teste = individuo[solucao][coluna+(coluna+1)]
                if(df_teste.iloc[teste, int(col_teste)] == valor_teste):
                    total_carac += 1

            if(total_carac > melhor_valor):
                melhor_valor = total_carac
                melhor_coluna = solucao
        classificacao = individuo[melhor_coluna][12]
        # Classifica baseado no que teve maior numero de acertos
        if(classificacao == 1):
            classificacao = '1'
        if(classificacao == df_teste.iloc[teste, df_teste.shape[1] - 1]):
            acertos += 1

    fitness[0] = (acertos / len(df_teste)) * 100

    return fitness

def avalia_pop(individuos, df_teste):
    individuos_aux = []
    fit = []
    individuos_aux = copy.deepcopy(individuos)
    # Utilizado Copy.DeepCopy para realmente copiar a lista e não fazer uma referência
    for x in range(len(individuos_aux)):
        fit = fitness(df_teste, individuos_aux[x])
        individuos_aux[x].append(fit)
        if (x == 0):
           melhor = individuos_aux[x][len(individuos_aux[x])-1]
        if (individuos_aux[x][len(individuos_aux[x])-1] > melhor):
            melhor = individuos_aux[x][len(individuos_aux[x])-1]
    print('Melhor: ', melhor)
    return 0

def get_par(individuos):
    total = len(individuos)

    posicao = np.random.randint(0, total)
    return posicao

def crossover(pai, mae):
    tamanho_pai = len(pai)-1
    tamanho_mae = len(mae)-1
    filho = []

    pai_aux = copy.deepcopy(pai[random.randint(0, tamanho_pai)])
    mae_aux = copy.deepcopy(mae[random.randint(0, tamanho_mae)])

    corte_pai = int((len(pai_aux)-1)/2)
    corte_mae = int((len(mae_aux)-1)/2)

    filho1_1 = copy.deepcopy(pai_aux[0:corte_pai])
    filho1_2 = copy.deepcopy(mae_aux[corte_mae:])

    filho2_1 = copy.deepcopy(mae_aux[0:corte_mae])
    filho2_2 = copy.deepcopy(pai_aux[corte_pai:])

    filho1 = np.append(filho1_1, filho1_2).tolist()
    filho2 = np.append(filho2_1, filho2_2).tolist()

    filho.append(filho1)
    filho.append(filho2)

    return filho

def mutacao():
    return True

def main():
    # Parametros
    tamanhopop = 10 # Tamanho da populacao Inicial
    dados = 'car.csv' # DataSet
    qtdgeracoes = 100

    # Inicializacao
    df = pd.DataFrame(pd.read_csv(dados))
    ultima_coluna = df.iloc[:, -1]
    df_teste = df[round((len(df) - (len(df)/3))):len(df)]
    qtd_Colunas = df.shape[1] - 1 #Removendo a coluna a ser prevista

    pop = inicializa_pop(df, df_teste, qtd_Colunas, tamanhopop, ultima_coluna)

    for geracao in range(0,qtdgeracoes):
        filho = crossover(pop[get_par(pop)], pop[get_par(pop)])
        pop.append(filho)

        print("Geracao: ", geracao)
        avalia_pop(pop, df_teste)
        print()


main()
