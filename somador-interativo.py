import os
def somar(*args):
    total = 0
    for i in args:
        total += i
    
    return f'Resultado: {total}'
def coletar_numeros_iniciais():
    numeros = []
    for texto in ["Digite um numero: ", "Digite outro numero: "]:
        while True:
            try:
                numeros.append(int(input(texto)))
                break
            except ValueError:
                print("Digite apenas números!")
    return numeros
numeros = coletar_numeros_iniciais()
while True:
    os.system("clear")
    print("Oque deseja?")
    resp = input("[1] Mostrar Soma\n[2] Adicionar outro número\n[3] Mostrar soma e sair\nEscolha uma das opções acima: ")
    if resp == '1':
        print(somar(*numeros))
        pgt = input("Deseja continuar? [Sim/Não]\n").lower().startswith("s")
        if pgt:
            numeros = coletar_numeros_iniciais()
            continue
        else:
            break
    elif resp == '2':
        numeros.append(int(input("Digite outro numero: ")))
    elif resp == '3':
        print(somar(*numeros))
        break
    
    
