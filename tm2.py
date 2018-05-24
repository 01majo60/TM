from turing_machine.ntm import NTM 
ntm = NTM(
states = {'rj', 'q1', 'qi', 'q3', 'q0', 'q2', 'q4', 'q5'},
input_symbols = {'0', '1'},
tape_symbols = {'.', '0', 'y', '>', 'x', '1'},
left_end = '>',
transitions = {'qi': {'>': {('q0', '>', 'R')}}, 'q0': {'0': {('q1', 'x', 'R'), ('q5', '0', 'R'), ('rj', '0', 'R')}, 'y': {('q3', 'y', 'R')}}, 'q1': {'0': {('q1', '0', 'R')}, '1': {('rj', '1', 'R'), ('q2', 'y', 'L')}, 'y': {('q1', 'y', 'R')}}, 'q2': {'0': {('q2', '0', 'L')}, 'x': {('q0', 'x', 'R')}, 'y': {('q2', 'y', 'L')}}, 'q3': {'y': {('q3', 'y', 'R')}, '.': {('q4', '.', 'R')}}, 'q5': {'0': {('q5', '0', 'R')}, '.': {('rj', '0', 'R')}}},
initial_state = 'qi',
blank_symbol = '.',
reject_state = 'rj', 
final_states = 'q4' 
)
