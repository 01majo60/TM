from turing_machine.xdtm import XDTM 
xdtm = XDTM(
states = {'qacc', 'qrej', 'q0'},
input_symbols = {'b', 'a'},
tape_symbols = {'>', 'b', '.', 'a'},
left_end = '>',
transitions = {'q0': {('>', '>', '>'): ('q0', '>', '>', '>', 'R', 'R', 'R'), ('a', '.', '.'): ('q0', 'a', 'a', '.', 'R', 'R', 'S'), ('b', '.', '.'): ('q0', 'b', '.', 'b', 'R', 'S', 'R'), ('.', '.', '.'): ('q0', '.', '.', '.', 'S', 'L', 'L'), ('.', 'a', 'b'): ('q0', '.', 'a', 'b', 'S', 'L', 'L'), ('.', '>', 'b'): ('qrej', '.', '>', 'b', 'S', 'S', 'S'), ('.', 'a', '>'): ('qrej', '.', 'a', '>', 'S', 'S', 'S'), ('.', '>', '>'): ('qacc', '.', '>', '>', 'S', 'S', 'S')}},
initial_state = 'q0',
blank_symbol = '.',
reject_state = 'qrej', 
final_states = 'qacc' 
)
