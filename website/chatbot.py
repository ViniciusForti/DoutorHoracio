'''from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot(
    'Doutor Horácio'
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri=None,
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch'
    ]
)

# Get a few responses from the bot

bot.get_response('What time is it?')

bot.get_response('What is 7 plus 7?')
'''