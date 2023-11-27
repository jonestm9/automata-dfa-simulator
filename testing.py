from dfa_sim import recognize_string

def test_recognition():
    test_inputs = [
        # Each test array includes the following fields:
        # 1. The string to test in the DFA (aka the user's inputted string)
        # 2. The alphabet of the DFA, in set format
        # 3. The start state of the DFA, in string format
        # 4. The accepting states of the DFA, in set format
        # 5. The transitions of the DFA, in dictionary format (key: tuple, value: string)
        # 6. The expected result of the input string in our recognizer function based on the provided DFA specifications
        
        
        # Test cases 1-3: Testing different strings on a simple DFA that only accepts strings with 0 or 1 of length 1
        ["0", {"0","1"}, 'q0', {'q1'}, {('q0', '1'): 'q1', ('q0', '0'): 'q1'}, True],
        ["1", {"0","1"}, 'q0', {'q1'}, {('q0', '1'): 'q1', ('q0', '0'): 'q1'}, True],
        ["01", {"0","1"}, 'q0', {'q1'}, {('q0', '1'): 'q1', ('q0', '0'): 'q1'}, False],
        
        # Test case 4: Testing different DFA 
        ["010101", {"0", "1"}, 'q0', {'q2'}, {('q0', '1'): 'q1', ('q0', '0'): 'q2', ('q1', '1'): 'q1', ('q1', '0'): 'q2', ('q2', '1'): 'q2', ('q2', '0'): 'q2'}, True],

        # Test case 5: DFA with a loop and different start and accepting states
        ["010100", {"0", "1"}, 'q1', {'q1'}, {('q1', '1'): 'q1', ('q1', '0'): 'q2', ('q2', '1'): 'q2', ('q2', '0'): 'q1'}, True],

        # Test case 6: DFA with an invalid character
        ["0231", {"0", "1"}, 'q0', {'q1'}, {('q0', '1'): 'q1', ('q0', '0'): 'q1'}, False],

    ]
    pass_all = True
    ctr = 0
    for test_input in test_inputs:
        ctr += 1
        res = recognize_string(test_input[0], test_input[1], test_input[2], test_input[3], test_input[4])
        if res != test_input[5]:
            print("Test failed for test number {}.".format(ctr))
            pass_all = False
            
    return pass_all

if test_recognition():
    print("All tests passed!")
else:
    print("One or more tests failed.")