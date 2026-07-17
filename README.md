# Calculadora de IMC

Calculadora de Índice de Massa Corporal (IMC) desenvolvida como prática de lógica de programação. O projeto tem duas versões: um script em Python que roda no terminal e uma versão web em HTML/JavaScript.

## Sobre o projeto

O IMC é calculado a partir do peso e da altura da pessoa, e classificado em faixas (abaixo do peso, peso normal, sobrepeso, obesidade grau I, II ou III). A altura pode ser digitada em metros (ex: `1.75`) ou em centímetros (ex: `175`) — o programa identifica automaticamente o formato.

## Estrutura do repositório

```
calculadora-imc/
├── README.md
├── calculadora.py           # versão em Python (terminal)
└── calculadora_imc.html     # versão web (HTML/JS)
```

## Versão Python (terminal)

### Como rodar

```bash
python calculadora.py
```

O programa vai pedir peso e altura pelo terminal e mostrar o resultado com a classificação.

### Funções principais

- `calculadora(peso, altura)`: calcula o IMC a partir da fórmula `peso / altura²`
- `verificacao_altura(altura)`: converte a altura para metros, caso tenha sido digitada em centímetros
- `main()`: controla a entrada do usuário, trata erros de digitação e imprime o resultado

## Versão Web (HTML/JS)

### Como rodar

Basta abrir o arquivo `calculadora_imc.html` em qualquer navegador — não precisa de servidor ou instalação.

### O que essa versão traz

- Campos de entrada para peso e altura
- Mensagem de erro caso o valor digitado não seja um número válido
- Resultado do IMC exibido na tela, com a classificação correspondente
- Tabela de classificação com destaque automático na faixa em que o resultado se encaixa

> Essa versão reimplementa a mesma lógica do script Python, adaptada para JavaScript e para rodar no navegador.

## Tabela de classificação (adultos)

| IMC | Classificação |
|---|---|
| Menos de 18,5 | Abaixo do peso |
| 18,5 a 24,9 | Peso normal |
| 25,0 a 29,9 | Sobrepeso |
| 30,0 a 34,9 | Obesidade grau I |
| 35,0 a 39,9 | Obesidade grau II |
| 40 ou mais | Obesidade grau III (grave) |

## O que pratiquei com esse projeto

- Lógica condicional (`if`/`elif`) para classificar faixas de valores
- Tratamento de erros de entrada (`try`/`except`)
- Tradução de uma mesma lógica entre linguagens diferentes (Python → JavaScript)
- Organização de um repositório com múltiplas versões de um mesmo projeto

## Aviso

Este projeto tem fins educacionais e de prática de programação. O resultado não substitui uma avaliação médica.
