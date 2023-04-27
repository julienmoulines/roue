import random

ACTIONS = [
    {'name': 'action 1', 'probability': 0.1},
    {'name': 'action 2', 'probability': 0.2},
    {'name': 'action 3', 'probability': 0.15},
    {'name': 'action 4', 'probability': 0.25},
    {'name': 'action 5', 'probability': 0.2},
    {'name': 'action 6', 'probability': 0.1}
]

def spin_wheel():
    probabilities = [action['probability'] for action in ACTIONS]
    action_index = random.choices(range(len(ACTIONS)), probabilities)[0]
    return ACTIONS[action_index]

