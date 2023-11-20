from dfa_sim import recognize_string

def test_recognition():
    test_inputs = [
        ["0", {"0","1"}, 'q0', {'q1'}, {('q0', '1'): 'q1', ('q0', '0'): 'q1'}, True],
        ["1", {"0","1"}, 'q0', {'q1'}, {('q0', '1'): 'q1', ('q0', '0'): 'q1'}, True],
        ["01", {"0","1"}, 'q0', {'q1'}, {('q0', '1'): 'q1', ('q0', '0'): 'q1'}, False],
        #...
        ["010101", {"0", "1"}, 'q0', {'q2'}, {('q0', '1'): 'q1', ('q0', '0'): 'q2', ('q1', '1'): 'q1', ('q1', '0'): 'q2', ('q2', '1'): 'q2', ('q2', '0'): 'q2'}, True],

        # # Test case 5: DFA with a loop and different start and accepting states
        # ["01010", {"0", "1"}, 'q1', {'q1'}, {('q1', '1'): 'q1', ('q1', '0'): 'q2', ('q2', '1'): 'q2', ('q2', '0'): 'q1'}, True],

        # Test case 6: DFA with an invalid character
        ["0231", {"0", "1"}, 'q0', {'q1'}, {('q0', '1'): 'q1', ('q0', '0'): 'q1'}, False],

        
    ]
    pass_all = True
    for test_input in test_inputs:
        res = recognize_string(test_input[0], test_input[1], test_input[2], test_input[3], test_input[4])
        if res != test_input[5]:
            print("Test failed for input: {}".format(test_input))
            pass_all = False
            
    return pass_all

if test_recognition():
    print("All tests passed!")
else:
    print("One or more tests failed.")