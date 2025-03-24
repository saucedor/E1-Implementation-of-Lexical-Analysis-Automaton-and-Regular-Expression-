% Author: César Ignacio Saucedo Rodríguez 
% Date: March 22, 2025

% load the other prolog file
:- consult('automata').

% base case: the string of numbers is end and are not in a forbiden state.
accept(State, []) :-
    \+ forbiden(State).

% Recursive function
accept(Current, [Symbol | Rest]) :-
    transition(Current, Symbol, Next),
    accept(Next, Rest).

% validate
parse_list(InputList) :-
    start_state(Start),
    accept(Start, InputList).