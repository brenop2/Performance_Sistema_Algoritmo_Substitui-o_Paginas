# Performance_Sistema_Algoritmo_Substitui-o_Paginas
Apresentação do codigo para professor Andrey

## Explicando o codigo:

🧩 TDE 2 – Algoritmos de Substituição de Páginas

Este projeto tem como objetivo simular e comparar o funcionamento dos algoritmos de substituição de páginas utilizados no gerenciamento de memória de sistemas operacionais: FIFO, LRU e MRU.

🧠 Conceito Geral

Quando a memória física (RAM) está cheia e o sistema precisa carregar uma nova página, é necessário decidir qual página existente será removida.
Essa decisão é feita por meio de uma política de substituição de páginas, cujo objetivo é minimizar o número de faltas de página (page faults).

⚙️ Estrutura do Código

O código é dividido em três funções principais — uma para cada algoritmo — e uma parte final de testes com diferentes sequências de páginas.

🔹 1. Função fifo(paginas, qtd_quadros)

Implementa o algoritmo First-In, First-Out (FIFO).

Mantém uma lista (quadros) que representa a memória.

Quando ocorre uma falta de página:

Se houver espaço livre, a nova página é adicionada;

Caso contrário, a página mais antiga (a primeira que entrou) é removida (pop(0)) e substituída pela nova.

Segue o princípio: “a primeira que entra é a primeira que sai”.

Esse método é simples, mas pode ser ineficiente em alguns casos, apresentando o Paradoxo de Belady (quando mais memória gera mais faltas).

🔹 2. Função lru(paginas, qtd_quadros)

Implementa o algoritmo Least Recently Used (LRU).

Também usa uma lista (quadros) para representar a memória.

Quando uma página é usada, ela é movida para o final da lista, indicando que foi a mais recentemente utilizada.

Quando ocorre uma falta e a memória está cheia, a primeira página da lista (a menos usada recentemente) é removida.

Esse algoritmo se baseia no Princípio da Localidade Temporal, que diz que páginas usadas recentemente têm alta probabilidade de serem usadas novamente.
Na prática, o LRU é considerado o algoritmo mais eficiente e realista para substituição de páginas.

🔹 3. Função mru(paginas, qtd_quadros)

Implementa o algoritmo Most Recently Used (MRU).

Similar ao LRU, mas faz o oposto:

Quando há falta e a memória está cheia, ele remove a página mais recentemente usada (pop(-1)).

Essa estratégia é útil em situações específicas, como em bancos de dados com varreduras sequenciais, onde uma página recém-usada dificilmente será reutilizada logo depois.

🧪 Testes e Simulações

O código contém três listas de teste, cada uma com uma sequência de referências de páginas:

paginas_a = [4, 3, 25, 8, 19, 6, 25, 8, 16, 35, 45, 22, 8, 3, 16, 25, 7]
paginas_b = [4, 5, 7, 9, 46, 45, 14, 4, 64, 7, 65, 2, 1, 6, 8, 45, 14, 11]
paginas_c = [4, 6, 7, 8, 1, 6, 10, 15, 16, 4, 2, 1, 4, 6, 12, 15, 16, 11]
qtd_quadros = 8


Cada sequência é testada com os três algoritmos (FIFO, LRU e MRU).
Durante a execução, o programa exibe na tela o estado dos quadros da memória após cada acesso, mostrando quais páginas estão carregadas e quantas faltas ocorrem.

📊 Resultados Esperados

FIFO: fácil de implementar, mas pode gerar resultados inconsistentes.

LRU: apresenta o melhor desempenho geral, com o menor número de faltas de página.

MRU: funciona bem apenas em situações específicas, mas geralmente tem desempenho inferior ao LRU.

🏁 Conclusão

Com base nas simulações realizadas:

O FIFO é o mais simples, porém menos eficiente.

O MRU é útil apenas em casos específicos.

O LRU é a melhor política de substituição na prática, por equilibrar desempenho e realismo, reduzindo significativamente as faltas de página.
