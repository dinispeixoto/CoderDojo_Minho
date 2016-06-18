# coding=UTF-8
from datetime import datetime


def hello(nome):

	print "Olá %s, eu sou um BOT! Podes chamar-me Pythoninho!" % nome

	#falta verificar se a string tem numeros ou não!

def pergunta1():	
	resposta1 = raw_input("Sabes o que é um BOT?\n").lower()
	print '\n'

	if resposta1 == "sim" or pergunta1 == "sim ":
		print "Sabes? Boa!! Eu fui criado pelos teus mentores de Python com a finalidade de ter uma conversa contigo."

	elif resposta1 == "nao" or resposta1 == "nao " or resposta1=="não" or resposta1=="não ":
		print "BOT é um diminutivo de 'robot'."
		print "No meu caso sou um simples programa em Python criado pelos teus mentores, eles programaram-me de maneira a poder ter uma pequena conversa contigo."

	else:
		fail()
		pergunta1()


def pergunta2():
	idade = raw_input("Que idade tens?\n").lower()
	print '\n'


	if idade.isdigit():
		idadenum = int(idade)
		if idadenum <= 14 and idadenum > 0:
			print "%s anos?" % idade
			print "Pareces muito novo para aprender Python, mas tenho a certeza que vais conseguir!"

		elif idadenum > 14:
			print "%s anos?" % idade
			print "Estás na idade certa para aprenderes a programar em linguagens mais sérias, como por exemplo Python!"
			
		else:
			fail()
			pergunta2()

	else:
		fail3()
		pergunta2()




def pergunta3():

	print "Agora vou deixar-te fazer-me uma pergunta! Gostavas que fosse sobre o quê?\n"
	print "1. Matemática\n"
	print "2. Palavras\n"
	print "3. Data/Hora\n"

	pergunta3 = raw_input("Escolhe o número do tema que queres: ")
	print '\n'

	if pergunta3 == "1":
		print "Muito bem, escolheste 'Matematica'."
		tema1()

	elif pergunta3 == "2":
		print "Muito bem, escolheste 'Palavras'."
		tema2()

	elif pergunta3 == "3":
		print "Muito bem, escolheste 'Data/Hora'."
		tema3()

	else:
		fail3()
		pergunta3()


def tema1():

	print "Escolhe dois números e eu vou dizer-te qual o resultado da soma deles!"
	numero1 = (raw_input("Introduz o primeiro número: "))
	numero2 = (raw_input("Introduz o segundo número: "))
	print '\n'
	resultado = 0

	if numero1.isdigit() and numero2.isdigit() and int(numero1)>=0 and int(numero2)>=0:
		resultado = int(numero2) + int(numero1)
		print "O resultado da soma de %s e %s é %s!" % (numero1,numero2,resultado)
	elif numero1 < 0 or numero2 <0:
		print "Desculpa mas ainda só sei somar números positivos! Tenta outra vez!"
		tema1()

	elif not numero1.isdigit() or not numero2.isdigit:
		fail3()
		tema1()

def tema2():

	palavra = raw_input("Escreve uma palavra e eu direi quantas letras ela tem:\n")
	print '\n'
		

	if palavra.isalpha() and len(palavra) > 0:
		print "A palavra '%s' tem %d letras!" % (palavra,len(palavra))

	else:
		fail4()
		tema2()

def tema3():
	now = datetime.now()


	print 'Hoje é o dia %s/%s/%s e são %sh e %sm!' % (now.day, now.month, now.year,now.hour, now.minute)



def pergunta4():

	resposta4 = raw_input("Já tiveste alguma experiência com algum tipo de programção?\n").lower()
	print '\n'

	if resposta4 == "sim" or resposta4 == "sim ":
		print "Isso é ótimo, assim aprender Python vai ser muito mais simples para ti!"

	elif resposta4 == "nao" or resposta4 == "nao " or resposta4 == "não" or resposta4 == "não ":
		print "Não há problema, há sempre uma primeira vez para tudo!"

	else:
		fail()
		pergunta4()

def pergunta5():

	resposta5 = raw_input("Gostavas de aprender a fazer um bot como eu?\n").lower()
	print '\n'

	if resposta5 == "sim" or resposta5 == "sim ":
		print "Boa, tenho a certeza que os mentores te podem ajudar nisso!"

	elif resposta5 == "nao" or resposta5 == "nao " or resposta5 == "não" or resposta5 == "não ":
		print "Não??? Os mentores vão ensinar-te na mesma, pode ser que entretanto mudes de ideias!"

	else:
		fail()
		pergunta5()

def nome_do_bot():

	bot_name = raw_input("Que nome darias ao teu bot?\n")
	print '\n'
	bot_name_lower = bot_name.lower()

	if bot_name_lower.isalnum() and len(bot_name_lower)>0:
		print("%s hm... Parece-me um bom nome! Devias começar já a programa-lo!\nEspero que nos voltemos a ver em breve! Adeus %s!" ) % (bot_name,nome)
	else:
		print("%s, não me parece um bom nome para o teu bot. Tenta outro!\nDICA: Para que o nome do teu BOT ser simples não uses números nem caracteres especiais!") % bot_name
		nome_do_bot()



def fail():
	print "Esta resposta não me parece adequada à pergunta. Tenta novamente!"

def fail2():
	print "Estás a usar caracteres desconhecidos por mim! Tenta novamente!"

def fail3():
	print "Usa apenas números para responder a esta questão! Tenta novamente!"

def fail4():
	print "Usa apenas letras para responder a esta questão! Tenta novamente!"




############### PROGRAMA ###################
nome = raw_input("Como te chamas?\n")
print '\n'
hello(nome)
pergunta1()
pergunta2()
pergunta3()
pergunta4()
pergunta5()
nome_do_bot()
################################################