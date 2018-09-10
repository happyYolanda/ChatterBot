from chatterbot import ChatBot

chatbot = ChatBot(
	'Ron Obvious',
	trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

def main():
	prompt = "Please enter the question:\n"
	while True:
		sentence = raw_input(prompt)
		if sentence == 'quit':
			break
		else:
			response = chatbot.get_response(sentence)
			print (str(response) + '\n')

if __name__ == "__main__":
	main()