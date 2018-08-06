from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/winereviewnlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-338852207585-338852207697-338875482081-70cfc46b579800dbd944d5ffcb4fc5ab', #app verification token
							'xoxb-338875483985-93uFF04D7Ab9kh94iPBSUxE9', # bot verification token
							'bFmYfLiCbvRdfK0ERie2HrVu', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))
