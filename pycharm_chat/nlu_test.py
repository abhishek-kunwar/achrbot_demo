import logging, pprint
from rasa_nlu import config
from rasa_nlu.training_data import load_data
from rasa_nlu.model import Interpreter, Trainer
from rasa_nlu.test import run_evaluation

# load the model from the file
interpreter = Interpreter.load("./models/nlu/default/current")

# perform few tests
pprint.pprint(interpreter.parse("hey there"))
pprint.pprint(interpreter.parse("i am Abhishek"))

from rasa_core.agent import Agent
from rasa_nlu.model import Interpreter
policy = Agent.load('models/dialogue', interpreter=interpreter)
print(policy.handle_message('i am Abhishek'))
print(policy.handle_message('hey there"'))