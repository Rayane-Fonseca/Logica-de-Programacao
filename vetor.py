#acessar elementos

vetor = ["a","b","c", 1, 2, 3]
primeiro = vetor[0]

#pega uma faixa de elementos
sub_vetor = vetor[1:4]
print(sub_vetor)

#adiciona elemento ao final do vetor
vetor.append("d") 
print(vetor)

#adicionar varios elementos de uma vez
vetor.extend([4,5])
print(vetor)

#remover elementos
vetor.remove("b")
print(vetor)

#remover elemento por indice (posicao)
del vetor [2]
print(vetor)

#atribui um novo valor para a posicao especifica
vetor[0] = "JLR"
print(vetor)