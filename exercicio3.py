import json

with open('dados.json','r') as arq:
    dados = json.load(arq)

min_with_zero = 9999999
min_without_zero = 9999999
max = 0
soma_media = 0
n_dias_media = 0
n_dias_maior = 0
for item in dados:
    if item['valor'] > 0:
        soma_media += item['valor']
        n_dias_media +=1
    if item['valor'] < min_with_zero:
        min_with_zero = item['valor']
    if item['valor'] < min_without_zero and item['valor'] > 0:
        min_without_zero = item['valor']
    if item['valor'] > max:
        max = item['valor']

media = soma_media/n_dias_media

for item in dados:
    if item['valor'] > media:
        n_dias_maior += 1


print(f"O menor valor de faturamento ocorrido em um dia do mês foi {min_with_zero} contando os valores zerados")
print(f"O menor valor de faturamento ocorrido em um dia do mês foi {min_without_zero} sem contar os valores zerados")
print(f"O maior valor de faturamento ocorrido em um dia do mês foi {max}")
print(f"O número de dias em que 0 valor de faturamento diário foi superior à média mensal foi de {n_dias_maior} dias")



