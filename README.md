# Performance_Sistema_Algoritmo_Substitui-o_Paginas
Apresentação do codigo para professor Andrey

## Integrantes e link do vídeo no YouTube

- Abílio Pedro Alcântara Mota Batista
- Breno Augusto Rocha

Link do vídeo YOUTUBE: https://youtu.be/5W4Mov4pVcI

## Explicando o codigo:

# Algoritmos de Substituição de Páginas – FIFO, LRU e MRU

## 1. Introdução

Nos sistemas operacionais, quando um processo precisa acessar uma página que não está na memória, ocorre uma falta de página (page fault).
O sistema então precisa decidir qual página na memória será removida para
dar espaço à nova. Os algoritmos de substituição são estratégias pra decidir isso.

Este projeto tem três deles:

- **FIFO (First In, First Out)**  
- **LRU (Least Recently Used)**  
- **MRU (Most Recently Used)**  

Cada função desenvolvida em Python simula o funcionamento desses algorítmos.

## 2. Explicação da função ```fifo```

O FIFO é o algoritmo mais simples entre os três. Basicamente, a ideia é que a primeira página que entrou na memória também seja a primeira a sair.

**No código, temos que:**

```
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
```

- Mantém uma lista que funciona como uma fila.
- A cada falta, insere a nova página no fim.
- Quando a memória está cheia, remove a que entrou primeiro com o pop(0).

## 3. Explicação da função ```lru```

No LRU, quando é preciso remover alguma página, ele escolhe a menos recentemente usada.

**No código, temos que:**

```
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
```

- Quando uma página é usada, ela vai pro final da lista.
- Aí o início da lista representa a página menos usada.
- Quando precisa remover, ele tira a do início com o pop(0).

## 4. Explicação da função ```mru```

É o oposto do LRU. Quando precisa remover uma página, escolhe a página usada mais recente.

```
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
```

- Move as páginas acessadas pro fim da lista.
- Quando precisa remover uma página, remove a última pop(-1), que é a mais recente.


Projeto do TDE 2 apresentado à disciplina Performance em Sistemas Ciberfísicos, ministrada pelo Professor Andrey Cabral Meira do curso de Ciência da Computação da Pontificia Universidade Católica do Paraná.
