def calculadora(peso: float, altura: float) -> float:
    IMC = peso / (altura ** 2)
    return IMC

def verificacao_altura(altura: float) -> float:
    if altura >= 100:
        altura_verificada = altura / 100
    else:
        altura_verificada = altura
        
    return altura_verificada
        

def main():
    continuar = True
    while continuar:
        try:
            peso = float(input('qual seu peso? ')) 
            altura = float(input('qual sua altura? '))
            continuar = False
        except ValueError:
            print('Isso não é um numero - Digite novamente')
        
    altura_verificada = verificacao_altura(altura)
    IMC = calculadora(peso, altura_verificada )
    
    if IMC < 18.5:
        print(f'Abaixo do peso: {IMC}')
        
    elif 18.5 <= IMC <= 24.9:
        print(f'Peso normal: {IMC}')
        
    elif 25.0 <= IMC <= 29.9:
        print(f'Sobrepeso: {IMC}')
        
    elif 30.0 <= IMC <= 34.9:
        print(f'Obesidade grau 1: {IMC}')
        
    elif 35.0 <= IMC <= 39.9:
        print(f'Obsesidade grau 2: {IMC}')
        
    else:
        print(f'Obesidade grau 3: {IMC}')
        
        
    
print(main())