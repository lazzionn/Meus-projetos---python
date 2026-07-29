# jogo da forca feito por lazzionn
import random
import os
import time

inicio = time.perf_counter()
erros = 0
acertos = 0
jogadas = 0
resposta_final = ''
chute_certo = 0
chute_errado = 0
r2 = ''
limite_erros = 8
chute_certo = 0
chute_errado = 0
acertos_totais = 0
erros_totais = 0
jogadas_totais = 0
base_palavras = [
    # animais
    'cachorro', 'borboleta', 'elefante', 'jacare', 'papagaio',
    'tartaruga', 'hamster', 'camaleao', 'tubarao', 'pinguim',
    
    # tecnologia
    'computador', 'teclado', 'monitor', 'impressora', 'notebook',
    'algoritmo', 'programa', 'internet', 'servidor', 'software',
    
    # objetos
    'bicicleta', 'cadeira', 'geladeira', 'televisao', 'microfone',
    'mochila', 'guarda-chuva', 'calendario', 'calculadora', 'lanterna',
    'caneta', 'lapis', 'violao', 'caderno',
    
    # natureza
    'fazenda', 'cachoeira', 'montanha', 'floresta', 'vulcao',
    'tempestade', 'arco-iris', 'deserto', 'oceano', 'peninsula',
    
    # cotidiano
    'trabalho', 'escola', 'mercado', 'restaurante', 'hospital',
    'biblioteca', 'academia', 'farmacia', 'padaria', 'aeroporto'
]

def placar(a, e, j, cc, ce, tj): # a = acertos, e = erros, j = jogadas
    os.system("clear")
    a = (   print('--------------------------------------------------'),
            print(f'|{21*' '}Placar{21*' '}|'),
            print('--------------------------------------------------'),
            print(f'|{3*' '}Acertos: {a}{5*' '}Erros: {e}{5*' '}Jogadas: {j}{7*' '}'),
            print(f'|{3*' '}Chutes Certos: {cc}{5*' '}Chutes Errados: {ce}{7*' '}'),
            print(f'|{3*' '}Tempo Jogado: {tj:.2f} minutos{19*' '}'),
            print('--------------------------------------------------'),
            print("Até mais! \nmade by: lazion") )
    return a


palavra_secreta = random.choice(base_palavras)
print('-------------------------')
print("Palavra secreta definida!")
print('-------------------------')

while resposta_final != palavra_secreta:
    
   
    r1 = input("Digite uma letra ou a palavra secreta: ")
    
    # PRA VERIFICAR ERROS DE ENTRADA:
    
    if len(r1) <= 0:
        print("Digite no minimo uma letra!")
        continue
    
    if len(r1) > 1 and r1 != palavra_secreta:
        os.system('clear')
        chute_errado += 1
        print("Você errou a palavra secreta")
        sair = input("Deseja recomeçar o jogo? [sim]/[nao] ").lower().startswith("s")
        if sair is True:
            print('-------------------------')
            print("Palavra secreta definida!")
            print('-------------------------')
            
            resposta_final = ''
            r2 = ''
            erros = 0
            acertos = 0
            jogadas = 0
            palavra_secreta = random.choice(base_palavras)
            continue
        else:
            fim = time.perf_counter()
            tempo_segundos = fim - inicio
            tempo_minutos = tempo_segundos / 60
            placar(acertos_totais, erros_totais, jogadas_totais, chute_certo, chute_errado, tempo_minutos)
            break
        
    if r1.isdigit():
        os.system('clear')
        print("Por favor, digite apenas letras!")
        continue
        

    ################################
    # Sistema de verificação das letras 
    
    if len(r1) > 1 and r1 == palavra_secreta:
        os.system('clear')
        chute_certo += 1
        print(f"Caramba! Você acertou a palavra secreta completa com \n{jogadas} jogadas e {erros} erro(s)!\nA palavra era {palavra_secreta.upper()}")
        sair = input("Deseja continuar jogando? [sim]/[nao] ").lower().startswith("s")
        if sair is True:
            print('-------------------------')
            print("Palavra secreta definida!")
            print('-------------------------')
            resposta_final = ''
            r2 = ''
            erros = 0
            acertos = 0
            jogadas = 0
            palavra_secreta = random.choice(base_palavras)
            continue
        else:
            fim = time.perf_counter()
            tempo_segundos = fim - inicio
            tempo_minutos = tempo_segundos / 60
            placar(acertos, erros, jogadas, chute_certo, chute_errado, tempo_minutos)
            break
    else:
        if r1 in palavra_secreta: 
            os.system('clear')
            print(f"'{r1}' está na palavra secreta!") 
            jogadas += 1
            acertos += 1
            jogadas_totais += 1
            acertos_totais += 1
            print(f"Tentativas: {jogadas}")
            print(f"Erros: [{erros}/{limite_erros}]")
            
            r2 += r1 
            resposta_final = '' 
            for letra in palavra_secreta: 
                if letra in r2: 
                    resposta_final += letra 
                else:
                    resposta_final += '_ ' 
            print(f'Palavra formada: {resposta_final}')
            if resposta_final == palavra_secreta:
                os.system('clear')
                print(f"Parabens!  Você acertou a palavra secreta, com o total de {jogadas} jogadas, {erros} erros e {acertos} acertos!\n A palavra era {palavra_secreta.upper()}")
                sair = input("Deseja continuar jogando? [sim]/[nao] ").lower().startswith("s")
                if sair is True:
                    print('-------------------------')
                    print("Palavra secreta definida!")
                    print('-------------------------')
                    resposta_final = ''
                    r2 = ''
                    erros = 0
                    acertos = 0
                    jogadas = 0
                    palavra_secreta = random.choice(base_palavras)
                    continue
                else:
                    fim = time.perf_counter()
                    tempo_segundos = fim - inicio
                    tempo_minutos = tempo_segundos / 60
                    placar(acertos, erros, jogadas, chute_certo, chute_errado, tempo_minutos)
                    break
        else: 
            os.system('clear')
            print(f"'{r1}' não está na palavra secreta!")
            print(f'Palavra formada: {resposta_final}')
            jogadas += 1
            erros += 1
            jogadas_totais += 1
            erros_totais += 1
            print(f"Tentativas: {jogadas}")
            print(f"Erros: [{erros}/{limite_erros}]")
            if erros > (limite_erros - 1):
                os.system('clear')
                print(f"Acabou suas tentativas! \nA palavra era {palavra_secreta.upper()}")
                sair = input("Deseja continuar jogando? [sim]/[nao] ").lower().startswith("s")
                if sair is True:
                    print('-------------------------')
                    print("Palavra secreta definida!")
                    print('-------------------------')
                    resposta_final = ''
                    r2 = ''
                    erros = 0
                    acertos = 0
                    jogadas = 0
                    palavra_secreta = random.choice(base_palavras)
                    continue
                else:
                    fim = time.perf_counter()
                    tempo_segundos = fim - inicio
                    tempo_minutos = tempo_segundos / 60
                    placar(acertos, erros, jogadas, chute_certo, chute_errado, tempo_minutos)
                    break


