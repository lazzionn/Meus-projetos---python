import random
import re

print("Escolha uma opção abaixo: ")
print("[1] Gerar CPF")
print("[2] Validador de CPF")
resp = input()
if resp == '1':
    cpf = ''
    for i in range(9):
        cpf += str(random.randint(0, 9))
    a = 10
    valor = ''
    total = 0
    for i in str(cpf):
        valor = int(i) * a
        a -= 1
        total += valor
    primeiro_digito = total % 11
    if primeiro_digito < 2:
        primeiro_digito = 0
    else:
        primeiro_digito = 11 - primeiro_digito
   
    cpf_pdgt = str(cpf) + str(primeiro_digito)
    b = 11
    total1 = 0
    for i in cpf_pdgt:
        valor = int(i) * b
        b -= 1
        total1 += valor
    segundo_digito = total1 % 11
    if segundo_digito < 2:
        segundo_digito = 0
    else:
        segundo_digito = 11 - segundo_digito
   
    novo_cpf = cpf_pdgt + str(segundo_digito)
    print(f"CPF: {novo_cpf[:3]}.{novo_cpf[3:6]}.{novo_cpf[6:9]}-{novo_cpf[9:]}")
    
    
elif resp == '2':
    cpf = input("Digite um cpf: ")
    
    
    #  Primeiro Digito
    
    
    cpf = re.sub(r'[^0-9]', "", cpf)

    a = 10
    valor = ''
    total = 0
    for i in cpf[0:9]:
        valor = int(i) * a
        a -= 1
        total += valor
    primeiro_digito1 = total % 11
    if primeiro_digito1 < 2:
        primeiro_digito1 = 0
    else:
        primeiro_digito1 = 11 - primeiro_digito1
   
   
   
    #  Segundo Digito
    
    
    cpf_pdgt = str(cpf[0:9]) + str(primeiro_digito1)
    b = 11
    total1 = 0
    valor1 = 0
    for i in cpf_pdgt:
        valor1 = int(i) * b
        b -= 1
        total1 += valor1
    segundo_digito = total1 % 11
    if segundo_digito < 2:
        segundo_digito = 0
    else:
        segundo_digito = 11 - segundo_digito
    cpf_final = str(cpf[0:9]) + str(primeiro_digito1) + str(segundo_digito)
    if cpf_final == cpf:
        print("CPF Válido! ✅")
    else:
        print("CPF Inválido! ❌")
