# Target_Sistemas

## 1
Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
Imprimir(SOMA);
Ao final do processamento, qual será o valor da variável SOMA?

O resultado retornará o valor da variável SOMA, ao mudar o valor de indice, o resultado mudará

## 2
Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

A entrada do código é passada por linha de comando, ao executar o código passar o valor que quer saber se pertence ou não à sequencia de fibonacci, e o código mostrará se pertence ou não

## 3
Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

A saída mostrará os menores valores de faturamento contando com valores nulos e sem valores nulos, se não houverem valores nulos no mês, o resultado será o mesmo, o maior faturamento e o número de dias em que o faturamento mensal foi superior à média mensal

## 4
Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

• SP – R$67.836,43

• RJ – R$36.678,66

• MG – R$29.229,88

• ES – R$27.165,48

• Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.  

A saída mostra os estados e a porcentagem representação que cada estado teve

## 5
Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;

A saída retorna uma string invertida, no exemplo utilizei a maior palavra da lingua portuguesa, e ao pedir para evitar funções pontas, não utilizei string_inversa = string[::-1], pois considerei que também era função pronta, por isso fiz um looping que começa no último índice da string e vai para o inicio

