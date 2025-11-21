import json

def ler_json(caminho="data.json"):
    with open(caminho, encoding="utf-8") as f:
        return json.load(f)


#Função para pegar valores numéricos de uma variável específica e remover valores nulos
def get_valores_numericos(nome_variavel, caminho="data.json"):
    valores = apresenta_dado(nome_variavel, caminho).values()
    valores_numericos = [v for v in valores if (type(v) == int or type(v) == float) and v != 0]
    if not valores_numericos:
        return None
    return valores_numericos

#Função que apresenta o valor de uma variável específica para todos os países
def apresenta_dado(nome_variavel, caminho="data.json"):
    dados = ler_json(caminho)
    resultado = {}
    for pais, info in dados.items():
        valor = info.get(nome_variavel)
        resultado[pais] = valor
    return resultado

#Função que apresenta todos os dados de um país específico
def apresenta_pais(nome_pais, caminho="data.json"):
    dados = ler_json(caminho)
    return dados.get(nome_pais)

#Função que calcula a média de uma variável específica
def calcula_media_dado(nome_variavel, caminho="data.json"):
    valores_numericos = get_valores_numericos(nome_variavel, caminho)
    if not valores_numericos:
        return None
    
    return sum(valores_numericos) / len(valores_numericos)

#Função que calcula a variância de uma variável específica
def calcula_variancia_dado(nome_variavel, caminho="data.json"):
    valores_numericos = get_valores_numericos(nome_variavel, caminho)
    if not valores_numericos:
        return None
    
    media = sum(valores_numericos) / len(valores_numericos)

    variancia = sum([(v - media) ** 2 for v in valores_numericos]) / len(valores_numericos)
    return variancia

#Função que calcula a média ponderada de uma variável específica, usando outra variável como peso
def calcula_media_ponderada_dado(nome_variavel, caminho="data.json", nome_peso="população"):
    dados = ler_json(caminho)
    soma_ponderada = 0
    soma_pesos = 0

    for pais, info in dados.items():
        valor = info.get(nome_variavel)
        peso = info.get(nome_peso)

        if (type(valor) == int or type(valor) == float) and (type(peso) == int or type(peso) == float) and valor != 0 and peso != 0:
            soma_ponderada += valor * peso
            soma_pesos += peso
            
    if soma_pesos == 0:
        return None
    
    return soma_ponderada / soma_pesos

#Função que calcula a média de uma variável apenas para os países onde o valor da variável é maior que a variavel em x país
def calcula_media_variavel_maior_x_pais(nome_variavel, pais_x, caminho="data.json"):
    dados = ler_json(caminho)
    valores_filtrados = []
    valor_pais_x = dados[pais_x].get(nome_variavel)

    for pais, info in dados.items():
        valor = info.get(nome_variavel)
        if (type(valor) == int or type(valor) == float) and valor >= valor_pais_x:
            valores_filtrados.append(valor)

    if not valores_filtrados:
        return None

    return sum(valores_filtrados) / len(valores_filtrados)

def resumo_dados_variavel(nome_variavel):
    print(f"Resumo estatístico para a variável: {nome_variavel}\n")
    print(f"Valores por país:")
    for pais, valor in apresenta_dado(nome_variavel).items():
        print(f"  {pais}: {valor}")
    print()
    valores_numericos = get_valores_numericos(nome_variavel)
    if not valores_numericos:
        print("Não há valores numéricos válidos para esta variável.")
        return
    print(f"Média simples: {calcula_media_dado(nome_variavel):.2f}")
    print(f"Média ponderada (população): {calcula_media_ponderada_dado(nome_variavel):.2f}")
    print(f"Variância: {calcula_variancia_dado(nome_variavel):.2f}")
    print(f"Média dos países com valor maior ou igual ao do país com maior valor (Japão): {calcula_media_variavel_maior_x_pais(nome_variavel, 'Japão'):.2f}")

# Exemplo de uso:
resumo_dados_variavel('pib_per_capita')