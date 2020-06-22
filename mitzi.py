#!/usr/bin/env python3.8
# Versão: 0.3

# Variáveis:
info = "uashdua"

# Script

print ("--------------------------------------------------------------")
print ("|                                                            |")
print ("|                Bem vindo ao chatbot Mitzi                  |")
print ("|                                                            |")
print ("--------------------------------------------------------------")
#Indentifica-se-há-um-nome------------------------------------------------------------------------------
try: 
    nome_existente = open(".nome", "r")

except IOError:
    print ("Mitzi" ": Olá! Qual é seu nome?")
    nome = input("Você: ")
    print ("Mitzi: Olá", nome+", como vai você?")
    novo_nome = open(".nome", "a")
    novo_nome.write(nome)
    novo_nome.close()

else:
    nome_existente = open(".nome", "r")
    nome = nome_existente.read()
    print ("Mitzi: Olá", nome+", como vai você?")
    nome_existente.close()

#Loop-de-conversa---------------------------------------------------------------------------------------
while(info != "tchau"):
	info = input("Você: ")
	info = info.lower()

	if info == ("tchau"):
		
		print ("Mitzi: Ok, até a próxima!")
		exit()
		
	else:

		try:
			responder = open("cérebro/" + info, "r")
	
		except IOError:
			print ("Mitzi: Ainda não sei o que você quis dizer, o que eu deveria responder?")
			resposta = input("Você: [Resposta literal]: ")
			novo_arquivo = open("cérebro/" + info, "w") 
			novo_arquivo.write(resposta)
			print ("Mitzi: Certo, devo falar [", resposta, "]")
			novo_arquivo.close()
			
		else:
			responder = open("cérebro/" + info, "r")
			falar = responder.read()
			print ("Mitzi: " + falar)
#------------------------------------------------------------------------------------------------------
