Created Date: 21 March 2019

# Rasa-Chatbot-for-various-Domain
Rasa Chatbot for various Domain


To Chat:
run main.py 


MAIN REQUIREMENTS:
1. config_spacy.yml
```
{
  "pipeline":"spacy_sklearn",
  "path":"./models/nlu",
  "data":"./data/data.json"
}
```
2. mkdir model
3. data.json
```
{
 "rasa_nlu_data": {
 "common_examples": [
 {
 "text": "hey",
 "intent": "greet",
 "entities": []
 },
 {
 "text": "howdy",
 "intent": "greet",
 "entities": []
 },
]
 }
}
```

### TO TRAIN:
```
from rasa_nlu.converters import load_data
from rasa_nlu.model import Trainer
from rasa_nlu import config
from rasa_nlu.config import RasaNLUConfig

training_data = load_data('/home/ekbana/workspace/randomfiles/Weatherbot_Tutorial/Full Code/data/data.json')
trainer = Trainer(RasaNLUConfig("config_spacy.yml"))
trainer.train(training_data)
model_directory = trainer.persist('./model/')
```

### TO PREDICT
```
from rasa_nlu.model import Interpreter

# where model_directory points to the model folder
interpreter = Interpreter.load('./model/default/model_20190319-141120')

while True:
    input_text = input("human: ")
    print(interpreter.parse(input_text))
```

### COMPLETE CODE:
```
from rasa_nlu.converters import load_data
from rasa_nlu.model import Trainer
from rasa_nlu import config
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Interpreter

def train(path):
    training_data = load_data(path)
    trainer = Trainer(RasaNLUConfig("config_spacy.yml"))
    trainer.train(training_data)
    model_directory = trainer.persist('./model/')

def predict(model_path):
    # where model_directory points to the model folder
    interpreter = Interpreter.load(model_path)

    while True:
        input_text = input("human: ")
        print(interpreter.parse(input_text))

path = '/home/ekbana/workspace/randomfiles/Weatherbot_Tutorial/Full Code/data/data.json'
customer_bot_path = "/home/ekbana/workspace/randomfiles/rasanlu/customer_bot/data/data.json"
model_path ='./model/default/model_20190319-145038'

# train(customer_bot_path)

predict(model_path)
```
