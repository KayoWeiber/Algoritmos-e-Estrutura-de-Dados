def recursividade(n):
    if n==0:
        return 0
    
    return n+recursividade(n-1)
numero=998
resultado=recursividade(numero)
print(f"O fatorial de {numero} é {resultado}")