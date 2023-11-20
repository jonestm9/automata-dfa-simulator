# general path

# user inputs the information about the DFA


print("Welcome to the DFA Simulator! Input the information about your DFA below.")

alphabet_str = input("\nEnter the alphabet of the DFA, separated by commas: ")
alphabet = alphabet_str.split(",")

states_str = input("\nEnter the states of the DFA, separated by commas: ")
states = set(states_str.split(","))

start_state = input("\nEnter the start state of the DFA: ")
while start_state not in states:
    print("\nError: start state not in state set.")
    start_state = input("\nEnter the start state of the DFA: ")
    
# start state
# set of accepting states
# all states
# transitions - input - validation
# transition is (state, character) -> state
# - checking if state(s) in transition exists in state set (if not, throw error)
# - checking if character exists in alphabet (if not, send to trap state)
# - checking if transition exists in transition set already (just duplicate - do nothing) 
# - checking if transition exists for that state/input pair already (if it does, throw error for nondeterminism)

def recognize_string(input_str):
    print("\nRecognizing string {}...".format(input_str))
    
    
    
    return False

while True:
    user_input = input("\nEnter a string for your specified DFA to recognize: ")
    res = recognize_string(user_input)
    if res:
        print("\nSuccess - string accepted by your DFA!")
    else:
        print("\nFailure - string not in the language recognized by your DFA.")
    
    cont = input("\nWould you like to continue? (y/n): ")
    if cont.lower() != "y":
        break
    