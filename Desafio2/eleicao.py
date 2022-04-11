
lista = []
candidatos = []
ids = []

with open('Desafio2/dados_elecao.txt') as dados:
  lista = dados.readlines()
  for l in lista[1:]:
    id = l.replace('\n', '')
    id = id.split(',')
    ids.append(id[0])
    candidatos.append(id[2])
  
  k = candidatos.count('Khan')
  c = candidatos.count('Correy')
  li = candidatos.count('Li')
  o = candidatos.count("O'Tooley")

  if k > c and k > li and k > o:
    vencedor = 'Khan'
  elif c > k and c > li and c > o:
    vencedor = 'Correy'
  elif li > k and li > c and li > o:
    vencedor = 'Li'
  elif o > k and o > c and o > li:
    vencedor = "O'Tooley"

with open('Desafio2/resultado-elecao.txt', 'w') as result:
  result.write(f"\n{f'Resultados Eleitorais':^35}\n"
              f"\n{'-'*40}\n")
  result.write(f'\nTotal de votos: {len(ids)}\n'
                f"\n{'-'*40}\n")
  result.write(f'\nKhan: {round(k/len(ids)*100,2)}% ({k})\n')
  result.write(f'\nCorrey: {round(c/len(ids)*100,2)}% ({c})\n')
  result.write(f'\nLi: {round(li/len(ids)*100,2)}% ({li})\n')
  result.write(f"\nO'Tooley: {round(o/len(ids)*100,2)}% ({o})\n"
               f"\n{'-'*40}\n")
  result.write(f'\nVencedor: {vencedor}'
               f"\n{'-'*40}\n")