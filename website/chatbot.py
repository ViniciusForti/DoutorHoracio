from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# Creating ChatBot Instance
chatbot = ChatBot(
    'Dr. Horácio'
    )

 # Training with Personal Ques & Ans 
conversation = [
    #Apresentação
    "Olá"
    "Olá, eu sou o Dr. Horácio, como você está?\nO que você está sentindo hoje?"
    "Oi"
    "Oi, eu sou o Dr. Horácio, tudo bem?\nO que você está sentindo hoje?"

    #Dor de cabeça
    "Estou com dor de cabeça"
    "Que pena! Uma dor de cabeça pode ter várias possíveis causas, como:\n- Estresse;\n- Desidratação;\n- Anemia;\n- Doença Crônica;\n- Problemas hormonais;\n- Mudanças de Rotina\nou até mesmo um Tumor Cerebral, mas esses casos extremamente raros.\n\nA dor de cabeça pode ser causada por fontes simples que podemos resolver facilmente, porém podem ser causadas por fatores graves. Se você está sentindo dores de cabeça frequentemente procure um NEUROLOGISTA de sua confiança para investigar o caso!"

    #Dor nas costas
    
]

response = chatbot.get_response("Olá! Eu queria uma ajuda com meu(s) sintoma(s)!")
print(response)

trainer = ListTrainer(chatbot)
trainer.train(conversation)