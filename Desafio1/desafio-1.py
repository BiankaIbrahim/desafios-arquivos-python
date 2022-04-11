
lista = []
meses = []
valores = []
with open('Desafio1/dados_financeiro.txt') as dados:
  lista = dados.readlines()
  for i in lista[1:]:
    mes = i.replace('\n', '')
    mes = mes.split(',')
    meses.append(mes[0])
    valores.append(int(mes[1]))
    
  variacao = []
  for n in range(1, len(valores)):
      varia = valores[n] - valores[n-1]
      variacao.append(varia)
  
with open('Desafio1/relatório.txt', 'w') as relat:
  relat.write(f"\n{f'Análise Financeira':^28}"
              f"\n{'-'*32}")
  relat.write(f'\nTotal de meses: {len(valores)}')
  relat.write(f'\nTotal: $ {round(sum(valores),2)}')
  relat.write(f'\nMédia: $ {round(sum(valores)/len(valores),2)}')
  relat.write(f'\nVariação da média: $ {round(sum(variacao)/len(variacao),2)}')
  relat.write(f'\nMaior aumento nos lucros:  {meses[variacao.index(max(variacao))+1]} ($ {max(variacao)})')
  relat.write(f'\nMaior redução nos lucros:  {meses[variacao.index(min(variacao))+1]} ($ {min(variacao)})')