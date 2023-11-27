# Deterministic Finite Automata (DFA) Simulator 

To run, make sure you have Python installed.

Then, run

```
python3 dfa_sim.py
```

in your terminal when in the repo's directory.

Once running, you'll be prompted to input your DFA's alphabet, states, start state, accepting states, and transitions.
The program will prompt you with the format of the inputs, but they are listed below for clarity.

- Enter the alphabet as a string of characters seperated by commas. Ex: 0,1,2 or A,B,C
- Enter the states of the DFA as a string of characters seperated by commas. Ex: q0,q1,q2 or state0, state1, state2
- Enter the start state of the DFA (it must be a state previously entered in the last step). Ex: q0
- Enter the accepting states of the DFA (must be previously entered into states). Ex: q1,q2
- Enter the transitions of the DFA in the format (state, input) -> state. Ex:
```
(q0, 0) -> q1
```

Then, you'll be prompted to enter strings that your DFA will either accept or reject as being recognized in the language.

To run the testing suite, run 
```
python3 testing.py
```

This was written for CS3252 - Theory of Automata, Formal Languages, and Computation.
