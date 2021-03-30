from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
bot= ChatBot(
'kid', 
storage_adapter='chatterbot.storage.SQLStorageAdapter',
input_adapter ='chatterbot.input.TerminalAdapter',
output_adapter='chatterbot.output.TerminalAdapter',
logic_adapter=["chatterbot.logic.BestMatch"],
database='./database.sqlite3')
bot.set_trainer(ListTrainer)
data = open('Chat_bot.txt').read()
talk=data.strip().split('\n')
bot.train(talk)
while True:
    try:
        bot_input=bot.get_response(None)
        
    except(KeyboardInterrupt,EOFError,SystemExit):
        break
