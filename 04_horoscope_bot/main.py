from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from rasa.core.agent import Agent
from rasa.core.channels.console import CmdlineInput as ConsoleInputChannel
from rasa.core.policies.keras_policy import KerasPolicy
from rasa.core.policies.memoization import MemoizationPolicy
from rasa.core.interpreter import RasaNLUInterpreter

logger = logging.getLogger(__name__)


def train_dialogue(domain_file='domain.yml',
        model_path='./models/dialogue',
        training_data_file='./data/stories.md'):
    agent = Agent(domain_file, policies=[MemoizationPolicy(), KerasPolicy()])

    agent.train(
        training_data_file,
        max_history=3,
        epochs=300,
        batch_size=50,
        validation_split=0.2,
        augmentation_factor=50)

    agent.persist(model_path)
    return agent


def run_weather_bot(serve_forever=True):
    interpreter = RasaNLUInterpreter('./models/nlu/default/weathernlu')
    agent = Agent.load('./models/dialogue', interpreter=interpreter)

    if serve_forever:
        agent.handle_channel(ConsoleInputChannel())

    return agent


if __name__ == '__main__':
    train_dialogue()
    run_weather_bot()


