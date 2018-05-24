from turing_machine.ntm import NTM 
ntm = NTM(
states = {'q3', 'q1', 'q0', 'q4', 'q5', 'rj', 'q2', 'qi'},
input_symbols = {'1', '0'},
tape_symbols = {'.', '0', 'y', 'x', '1', '>'},
left_end = '>',
transitions = {'qi': {'>': {('q0', '>', 'R')}}, 'q0': {'0': {('q5', '0', 'R'), ('rj', '0', 'R'), ('q1', 'x', 'R')}, 'y': {('q3', 'y', 'R')}}, 'q1': {'0': {('q1', '0', 'R')}, '1': {('q2', 'y', 'L'), ('rj', '1', 'R')}, 'y': {('q1', 'y', 'R')}}, 'q2': {'0': {('q2', '0', 'L')}, 'x': {('q0', 'x', 'R')}, 'y': {('q2', 'y', 'L')}}, 'q3': {'y': {('q3', 'y', 'R')}, '.': {('q4', '.', 'R')}}, 'q5': {'0': {('q5', '0', 'R')}, '.': {('rj', '0', 'R')}}},
initial_state = 'qi',
blank_symbol = '.',
reject_state = 'rj', 
final_states = 'q4' 
)