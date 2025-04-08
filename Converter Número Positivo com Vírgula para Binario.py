def numero_para_binario(numero):
    parte_inteira = int(numero)
    parte_fracionaria = numero - parte_inteira

    print(f"Parte inteira em binário: {bin(parte_inteira)[2:]}", end='.')

    for _ in range(10):  
        parte_fracionaria *= 2
        bit = int(parte_fracionaria)
        print(bit, end='')
        parte_fracionaria -= bit

numero = float(input("Digite um número real: "))
numero_para_binario(numero)
