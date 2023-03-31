# ia_roobot_vacuum
Algoritmo desenvolvido como atividade durante o curso de Inteligência Artificial. 

Para implementação do *model-based-reflex agent*, eu utilizei da ideia de independente da posição inicial do agente, o primeiro passo é move-lo para o canto superior esquerdo `(0,0)`. A partir da posição inicial da matriz eu utilizo um método que percorre toda a matriz, esse método funciona a partir de camadas, a `camada` começa em `0` representando a primeira linha da matriz. Então é criado um `while` que executa enquanto a variável `camada` for menor ou igual a altura da matriz. Dentro do `while`, existe 4 laços de repetição `for`.

- o **primeiro** serve para percorrer a primeira linha até a última coluna;
- o **segundo**, percorre da última coluna até a última linha;
- o **terceiro**, percorre da última linha até a primeira coluna;
- o **quarto**, percorre da primeira coluna atá a primeira linha;

Cada vez que é percorrido os laços `for` é incrementado a variável `camada`, sendo assim, na primeira execução a primeira linha seria a linha `0`, já na segunda execução a primeira linha seria a linha `1`. Sendo assim, o agente realiza um movimento em caracol até chegar a última posição não percorrida.

Minha ideia de melhoria do código é a utilização do método de busca em profundidade. Ademáis de um algoritmo que gera aleatóriamente obstáculos em ambientes aleatórios, seria possível a verificação, se essa posição vizinha da posição atual do agente for um obstáculo, então retira ela da lista de 'à visitar'. Entretanto, fiquei com dificuldade de salvar o caminho real exercido pelo agente.

Imaginando uma matriz 3x3 `[[1,2,3],[4,5,6],[7,8,9]]` partindo da posição `(1,1)`,teriamos de vizinho do número 5 o `2,4,6,8`. Na hora de visitar esses visinhos, iriamos para o dois que é vizinho do 1 e do 3, gerando a seguinte lista: `(2,4,6,8,1,3)` Ao sair do dois o algoritmo volta para o 5 e em seguida vai para o 4 que é vizinho do 1 e do 7 `(4,6,8,1,3,7)`. Volta para o 5 e em seguida visita o 6 que é vizinho do 7 e do 9 `(6,8,1,3,7,9)`. Volta para o 5 e sem seguida visita o 8. Sobrando `(1,3,7,9)`. Minha dificuldade atual é traçar o caminho seguindo a regra de poder andar somente para cima, baixo, esquerda e direita. Então no algoritmo que eu implementei ele parte do 8 vai pro 5 e vai para 1. O ideal era antes de visitar o 1 ele passar pelo dois antes. `8 -> 5 -> 2 -> 1`.
