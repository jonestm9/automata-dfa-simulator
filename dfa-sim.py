from collections import defaultdict


print("Welcome to the DFA Simulator! Input the information about your DFA below.")

alphabet_str = input("\nEnter the alphabet of the DFA, separated by commas: ").replace(" ", "")
alphabet = set(alphabet_str.split(","))

print(alphabet)

states_str = input("\nEnter the states of the DFA, separated by commas: ").replace(" ", "")
states = set(states_str.split(","))

start_state = input("\nEnter the start state of the DFA: ").replace(" ", "")
while start_state not in states:
    print("\nError: start state not in state set.")
    start_state = input("\nEnter the start state of the DFA: ").replace(" ", "")

accepting_states_str = input("\nEnter the accepting states of the DFA, separated by commas: ").replace(" ", "")
accepting_states = set(accepting_states_str.split(","))

transitions = {}
while True:
    transition = input("\nEnter a transition of the DFA in the form (state, input) -> state, or type 'done' to finish: ")
    if transition == "done":
        break
    transition = transition.replace(" ", "")
    transition = transition.replace("(", "")
    transition = transition.replace(")", "")
    transition = transition.split("->")
    transition[0] = tuple(transition[0].split(','))
    if len(transition) != 2:
        raise Exception("\nError: invalid transition format.")
    # if specified state doesn't exist or specified char not in alphabet, fails
    if transition[0][0] not in states or transition[0][1] not in alphabet or transition[1] not in states:
        raise Exception("\nError: invalid transition.")
    if transition[0] in transitions:
        raise Exception("\nError: nondeterminism. This input/state pair already has a transition.")
    
    transitions[transition[0]] = transition[1]
        
    
    
    
    
    
# transition is (state, character) -> state
# - checking if transition exists in transition set already (just duplicate - do nothing) 
# - checking if transition exists for that state/input pair already (if it does, throw error for nondeterminism)

# user inputs a string to be recognized by the DFA
def recognize_string(input_str):
    print("\nRecognizing string {}...".format(input_str))
    curr_state = start_state
    for char in input_str:
        if char not in alphabet:
            print("\nError: invalid character in string.")
            return False
        if tuple([curr_state,char]) not in transitions:
            print("\nError: no transition for state {} and input {}.".format(curr_state, char))
            return False
        curr_state = transitions[tuple([curr_state,char])]
    if curr_state and curr_state in accepting_states:
        return True
    else:
        return False


while True:
    user_input = input("\nEnter a string for your specified DFA to recognize: ").replace(" ", "")
    res = recognize_string(user_input)
    if res:
        print("\nSuccess - string accepted by your DFA!")
    else:
        print("\nFailure - string not in the language recognized by your DFA.")
    
    cont = input("\nWould you like to recognize another string? (y/n): ")
    if cont.lower() != "y":
        break
    
    
# testing??