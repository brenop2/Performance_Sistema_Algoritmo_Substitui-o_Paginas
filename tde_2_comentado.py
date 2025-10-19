def fifo(paginas, qtd_quadros):
    quadros = [] # lista que guarda as paginas na memoria
    faltas = 0 # conta as faltas de pagina

    print("Página\t\tQuadros")
    for pagina in paginas:
        if pagina not in quadros: # se a pagina nao estiver na memória
            faltas += 1 # entao conta como falta
            if len(quadros) < qtd_quadros: # se ainda tem espaço
                quadros.append(pagina) # então coloca a pagina
            else: # se esta cheio
                quadros.pop(0) # remove a mais antiga
                quadros.append(pagina) # e adiciona a mais nova
        print(pagina, "\t\t", quadros) # print com tabulação pra mostrar a memória
    return faltas

def lru(paginas, qtd_quadros):
    quadros = []
    faltas = 0

    print("Página\t\tQuadros")
    for pagina in paginas:
        if pagina in quadros: # se ta na memoria
            quadros.remove(pagina) # entao tira pra colocar no final
            quadros.append(pagina)
        else: # se nao ta na memoria
            faltas += 1
            if len(quadros) < qtd_quadros:
                quadros.append(pagina) # ainda tem espaço, entao adiciona
            else:
                quadros.pop(0) # remove a menos usada
                quadros.append(pagina) # faz o append da nova
        print(pagina, "\t\t", quadros)
    return faltas

def mru(paginas, qtd_quadros):
    quadros = []
    faltas = 0

    print("Página\t\tQuadros")
    for pagina in paginas:
        if pagina in quadros:
            quadros.remove(pagina) # tira pra colocar no final
            quadros.append(pagina)
        else:
            faltas += 1
            if len(quadros) < qtd_quadros:
                quadros.append(pagina)
            else:
                quadros.pop(-1) # removendo a ultima usada (no caso a mais recente)
                quadros.append(pagina)
        print(pagina, "\t\t", quadros)
    return faltas

# TESTES

paginas_a = [4, 3, 25, 8, 19, 6, 25, 8, 16, 35, 45, 22, 8, 3, 16, 25, 7]
paginas_b = [4, 5, 7, 9, 46, 45, 14, 4, 64, 7, 65, 2, 1, 6, 8, 45, 14, 11]
paginas_c = [4, 6, 7, 8, 1, 6, 10, 15, 16, 4, 2, 1, 4, 6, 12, 15, 16, 11]
qtd_quadros = 8

print("Ítem 1.")

print("\na)")
fifo(paginas_a, qtd_quadros)
lru(paginas_a, qtd_quadros)
mru(paginas_a, qtd_quadros)

print("\nb)")
fifo(paginas_b, qtd_quadros)
lru(paginas_b, qtd_quadros)
mru(paginas_b, qtd_quadros)

print("\nc)")
fifo(paginas_c, qtd_quadros)
lru(paginas_c, qtd_quadros)
mru(paginas_c, qtd_quadros)