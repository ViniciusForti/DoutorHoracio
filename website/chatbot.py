from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# Creating ChatBot Instance
chatbot = ChatBot('Dr. Horácio')

 # Training with Personal Ques & Ans 
conversation = [
    #Apresentação
    "Olá"
    "Olá, eu sou o Dr. Horácio, como você está?\nO que você está sentindo hoje?"
    "Oi"
    "Oi, eu sou o Dr. Horácio, tudo bem?\nO que você está sentindo hoje?"
    "Obrigado!"
    "Disponha! Posso te auxiliar em algo mais hoje?"

    #Dor de cabeça
    "Estou com dor de cabeça"
    "Que pena! Uma dor de cabeça pode ter várias possíveis causas, como:\n- Estresse;\n- Desidratação;\n- Anemia;\n- Doença Crônica;\n- Problemas hormonais;\n- Mudanças de Rotina\nou até mesmo um Tumor Cerebral, mas esses casos extremamente raros.\n\nA dor de cabeça pode ser causada por fontes simples que podemos resolver facilmente, porém podem ser causadas por fatores graves. Se você está sentindo dores de cabeça frequentemente procure um NEUROLOGISTA de sua confiança para investigar o caso!"

    #Dor nas costas
    "Estou com dor nas costas"
    "Que pena! Uma dor nas costas pode ter várias possíveis causas, como:\n- Lesão Muscular\n- Doenças Respiratórias\n- Pedra nos Rins\n- Dor Ciática\n- Infarto\n- Hérnia de Disco \n- Contratura Muscular\nem mulheres pode ser até mesmo Gravidez.\n\nA dor nas costas pode ser causada por fontes simples que podemos resolver facilmente, porém pode ser causada por fatores graves. Se você está sentindo dores nas costas frequentemente procure um CLÍNICO GERAL de sua confiança para investigar o caso!"

    #Dor nas pernas
    "Estou com dor nas pernas"
    "Que pena! Uma dor nas pernas pode ter várias possíveis causas, como:"

    #Dor nos braços
    "Estou com dor nos braços"
    "Que pena! Uma dor nos braços pode ter várias possíveis causas, como:"

    #Febre
    "Estou com dor nos braços"
    "Que pena! Uma dor nos braços pode ter várias possíveis causas, como:"

    #Tosse
    "Estou com dor nos braços"
    "Que pena! Uma dor nos braços pode ter várias possíveis causas, como:"

    #Dor de Gargante
    "Estou com dor nos braços"
    "Que pena! Uma dor nos braços pode ter várias possíveis causas, como:"

    #Dor de Ouvido
    "Estou com dor nos braços"
    "Que pena! Uma dor nos braços pode ter várias possíveis causas, como:"

    #Dor no Corpo
    "Estou com dor nos braços"
    "Que pena! Uma dor nos braços pode ter várias possíveis causas, como:"
    
]

response = chatbot.get_response("Olá! Eu queria uma ajuda com meu(s) sintoma(s)!")
print(response)

trainer = ListTrainer(chatbot)
trainer.train(conversation)