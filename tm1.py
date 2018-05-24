from turing_machine.dtm import DTM 
dtm = DTM(
states = {'q1', 'q0', 'q4', 'q2', 'qi', 'rj', 'q3'},
input_symbols = {'1', '0'},
tape_symbols = {'1', '.', 'x', 'y', '0', '>'},
left_end = '>',
transitions = {'qi': {'>': ('q0', '>', 'R')}, 'q0': {'0': ('q1', 'x', 'R'), '1': ('rj', '1', 'R'), 'y': ('q3', 'y', 'R')}, 'q1': {'0': ('q1', '0', 'R'), '1': ('q2', 'y', 'L'), 'y': ('q1', 'y', 'R')}, 'q2': {'0': ('q2', '0', 'L'), 'x': ('q0', 'x', 'R'), 'y': ('q2', 'y', 'L')}, 'q3': {'y': ('q3', 'y', 'R'), '1': ('rj', '1', 'R'), '.': ('q4', '.', 'R')}},
initial_state = 'qi',
blank_symbol = '.',
reject_state = 'rj', 
final_states = 'q4' 
)
