
import pandas as pd
import numpy as np

# markov property -> the probability of moving from the current state
# to the other depends solely on the present state.
# 

class MarkovChain(object):
    
    def __init__(self, transition_prob):
        self.transition_prob = transition_prob
        self.states = list(transition_prob.keys())

    
    def next_state(self, current_state):

        probs = [self.transition_prob[current_state][next_state] for next_state in self.states]
        return np.random.choice(self.states, p=probs)

    def generate_states(self, current_state, no=10):
        future_states = []
        for _ in range(no):
            next_state = self.next_state(current_state)
            future_states.append(next_state)
            current_state = next_state
        return future_states


def main_program():

    transition_prob = {'Sunny': {'Sunny': 0.8, 'Rainy': 0.19, 
                        'Snowy': 0.01},
                        'Rainy': {'Sunny': 0.2, 'Rainy': 0.7,
                        'Snowy': 0.1},
                        'Snowy': {'Sunny': 0.1, 'Rainy': 0.2,
                        'Snowy': 0.7}}

    weather_chain = MarkovChain(transition_prob)
    next_s = weather_chain.next_state('Rainy')
    print(next_s)
    next_prob_states = weather_chain.generate_states(current_state='Sunny', no=20) 
    print(next_prob_states)

if __name__ == '__main__':
    main_program()