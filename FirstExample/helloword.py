
# range sgnifica intervalo, cai comecar no 2 e parar no 3
# for i in range (2,4):
#   {
#  print ("Tabuada: " + str(i))
#  for j in range(0, 11):{
#      print(str(j) + "x" + str(i) + "=" + str(j*i))
#  }

# }
#
# r significa somete leitura
arquivo = open('pessoas.txt', 'r')
for linha in arquivo:
lista = linha.split()
print lista()

arquivo.close()
