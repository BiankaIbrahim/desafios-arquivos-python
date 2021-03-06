# desafios-arquivos-python

## Desafio 1 - PyFinanceiro
Neste desafio, você tem a tarefa de criar um script Python para analisar os registros financeiros de sua empresa. Você fornecerá um conjunto de dados financeiros chamado dados_financeiros.txt. O conjunto de dados é composto por duas colunas: Data e Lucros/Perdas, separados por virgula. (Felizmente, sua empresa tem padrões bastante flexíveis para a contabilidade, então os registros são simples.)

Sua tarefa é criar um script Python que analise os registros para calcular cada um das seguintes informações:

- O número total de meses incluídos no conjunto de dados

- O valor total líquido de "Lucros / Perdas" durante todo o período

- A média dos "Lucros / Perdas" durante todo o período

- A média das mudanças em "Lucros / Perdas" durante todo o período

- O maior aumento nos lucros (data e valor) durante todo o período

- A maior redução nas perdas (data e valor) ao longo de todo o período

Por exemplo, sua análise deve ser semelhante a esta abaixo:

### >> Analise financeira

<p>-Total de meses: 86 </p>
<p>-Total: $ 38382578 </p>
<p>-Média: $ 446309,04 </p>
<p>-Variação da média: $ -2315,12 </p>
<p>-Maior aumento nos lucros: fevereiro de 2012 ($ 1926159) </p>
<p>-Maior redução nos lucros: setembro de 2013 ($ -2196167)</p>


*obs: Além disso, seu script final deve imprimir a análise no terminal e exportar um arquivo de texto **relatório.txt** com os resultados.*


## Desafio 2 - PyVotação

Neste desafio, você tem a tarefa de ajudar uma pequena cidade rural a modernizar seu processo de contagem de votos. (Até agora, o tio Cleiton vinha contando-os um por um com confiança, mas, infelizmente, sua concentração não é o que costumava ser.)

Você receberá um conjunto de dados de enquete chamado dados_eleção.txt. O conjunto de dados é composto por três colunas: ID do eleitor,Município e Candidato. Sua tarefa é criar um script Python que analise os votos e calcule cada uma das seguintes informações:

- O número total de votos expressos

- Uma lista completa de candidatos que receberam votos

- A porcentagem de votos que cada candidato ganhou

- O número total de votos que cada candidato ganhou

- O vencedor da eleição com base no voto popular.

Por exemplo, sua análise deve ser semelhante a esta abaixo:

### >> Resultados eleitorais

<p>- Total de votos: 3521001</p>

<p>Khan: 63.0% (2218231)</p>
<p>Correy: 20.0% (704200)</p>
<p>Li: 14.0% (492940)</p>
<p>O'Tooley: 3.0% (105630)</p> 

<p><b>Vencedor: Khan</b></p>


*obs: Além disso, seu script final deve imprimir a análise no terminal e exportar um arquivo de texto **resultado.txt** com os resultados.*
