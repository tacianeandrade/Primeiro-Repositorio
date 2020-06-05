#dicionario chave - valor (arrey de diferentes tipos de dados)
pessoa = {'nome': 'Lea', 'idade': 21}
#print(pessoa['nome'])
#print(pessoa['idade'])
#add uma nova chave ao meu dicionario 
pessoa['curso'] = 'computação'
#print(pessoa)
 
#for chave, valor in pessoa.items():
   #  print("Chave: " + str(chave))
    # print("Valor: " + str(valor))
   #  print()

#vai imprimir so as chaves
#for chave in pessoa.keys():
    #print (chave.title())

linguagens = {'lea': 'python', 'sara': 'c', 'eddie': 'java', 'phil': 'python', }

#print('A linguagem usada por Lea é: ' + linguagens['lea'].title())
    
linguagens = {'lea': 'python', 'sara': 'c', 'eddie': 'java', 'phil': 'python', }

#nome e linguagem sao variais, items() acessa as chaves e valores do meu dic
#for nome, linguagem in linguagens.items(): 
 #print(nome.title() + " programa em " + linguagem.title())
        

pessoa1 = {'nome': 'Lea', 'idade': 25}
pessoa2 = {'nome': 'Eddie', 'idade': 21}
pessoa3 = {'nome': 'Phil', 'idade': 23}
#pessoa com dicionarios
pessoas = [pessoa1, pessoa2, pessoa3]
#for pessoa in pessoas: print(pessoa)
