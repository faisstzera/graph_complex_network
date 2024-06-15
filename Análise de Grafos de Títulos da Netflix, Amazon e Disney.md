
## Introdução

Este relatório apresenta uma análise de grafos construída a partir de dados de títulos de filmes e séries disponíveis nas plataformas de streaming Netflix, Amazon e Disney. O foco da análise é entender as conexões entre atores e diretores, bem como entre os próprios atores, para identificar padrões que possam indicar comportamentos típicos de redes complexas.

## Resultados

### Distribuição de Graus

#### Grafo de Atores para Diretores

![Pasted image 20240614215039.png]

#### Grafo de Atores para Atores

![WhatsApp Image 2024-06-14 at 20.55.41_5d900180.jpg]

**Análise:**
- Assim como foi estudado na matéria, ambos os gráficos seguem uma distribuição de potência, e não um potência Gaussiana, corroborando com a ideia de que grafos que representam problemas reais tendem a ter uma distribuição de potência

### Componentes Conectados

#### Grafo de Atores para Diretores (Direcionado)

**Dados:**

- **Número de Componentes Fortemente Conectados:** 57.563

**Análise:**

- Com um número muito próximo ao total de vértices, podemos inferir que a maioria dos componentes fortemente conectados são pequenos, frequentemente consistindo de pares ou pequenos grupos de atores e diretores, mostrando que a indústria do cinema é altamente fragmentada, com poucos grupos grandes de colaboração contínua. Entretanto, conforme podemos ver abaixo, o grupo de atores tender a ser mais concentrado quando retiramos os diretores da análise.
#### Grafo de Atores para Atores (Não Direcionado)

**Dados:**

- **Número de Componentes Conectados:** 2.263

**Distribuição de Ordem dos Componentes:**

- Os componentes conectados variam em tamanho, desde componentes muito pequenos até alguns potencialmente grandes.

**Análise:**
- Comparado ao número total de vértices, o número de componentes conectados é significativo, indicando que há uma divisão considerável na rede de atores.
- Componentes menores podem representar atores com colaborações isoladas ou nichos específicos na indústria.
- Componentes maiores representam redes mais densas de colaboração, possivelmente refletindo grupos de atores que frequentemente trabalham juntos em múltiplos projetos. 
- Atores como Tom Hanks e Leonardo DiCaprio fazem parte de redes densas de colaboração, o que pode indicar que os atores famosos, que frequentemente estão nas bilheterias de Hollywood, tendem a trabalhar juntos, com um espaço relativamente pequeno para outliers (visto a competitividade para entrar nesse espaço).


### Centralidade por proximidade

#### Grafo de Atores para Diretores (Direcionado)

**Gráfico dos top 10 atores**

**Dados:**
1. Jorge Michel Grau, 0
2. Gilbert Chan, 0
3. Shane Acker, 0
4. Robert Luketic, 0
5. Glenn Triggs, 0
6. Serdar Akar, 0
7. Yasir Al Yasiri, 0
8. Kevin Reynolds, 0
9. Mohamed Diab, 0
10. Shravan Kumar, 0

**Análise:**
- A centralidade zero dos diretores listados indica que, no conjunto de dados ou na estrutura do grafo dirigido analisado, esses diretores não possuem conexões de saída para atores. Isso pode ser devido a várias razões, incluindo dados incompletos ou erros no modelo.
- A centralidade dos vértices foi calculada levando em consideração todo o grafo.

#### Grafo de Atores para Atores (Não Direcionado)

**Gráfico dos top 10 Atores**

**Dados:**
1. Lohana Marinho, 0.9830508474576272 
2. David Adams, 0.9803921568627451
3. Ryan Heumier, 0.9787234042553191
4. Hanleigh Baker, 0.9787234042553191
5. Cj Bernard, 0.9787234042553191
6. Amielynn Woodall, 0.9787234042553191
7. Ashley Brewer, 0.9787234042553191
8. Holly Petty, 0.9787234042553191
9. Jade Michael Lafont, 0.9787234042553191
10. Bailey Freeman, 0.9787234042553191

**Análise:**
- Observa-se que os valores de centralidade dos 10 principais atores estão muito próximos, variando entre 0.9787 e 0.9831.
- Lohana Marinho é a atriz com a maior centralidade, com um valor de 0.9831, indicando que ela ocupa uma posição muito central no grafo.
- David Adams vem logo em seguida, com uma centralidade de 0.9804.
- Os outros oito atores têm exatamente o mesmo valor de centralidade (0.9787), o que sugere que eles estão em posições muito semelhantes dentro do grafo.
- A centralidade dos vértices foi calculada levando em consideração o componente em que cada vértice se encontrava. Isso significa que atores no mesmo componente terão centralidades comparáveis. Esses valores de centralidade indicam a importância de cada ator dentro da rede. Um valor mais alto sugere que o ator é mais central e, provavelmente, mais influente.
- O fato de que a maioria dos atores tem valores de centralidade idênticos (0.9787) pode indicar uma rede altamente conectada onde vários vértices têm papéis semelhantes.
