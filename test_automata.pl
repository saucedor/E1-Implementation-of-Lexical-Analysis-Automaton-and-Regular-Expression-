% Author: César Ignacio Saucedo Rodríguez 
% Date: March 22, 2025

% Load your main file with the automaton.
:- ['main'].

% Valid cases
test_0  :- parse_list([0]).
test_1  :- parse_list([1]).
test_2  :- parse_list([2]).
test_3  :- parse_list([0,1]).
test_4  :- parse_list([1,2]).
test_5  :- parse_list([2,0]).
test_6  :- parse_list([0,1,2]).
test_7  :- parse_list([2,1,2]).
test_8  :- parse_list([1,0,2]).
test_9  :- parse_list([0,1,2,0,1,2]).
test_10 :- parse_list([2,0,1,2,0,1]).
test_11 :- parse_list([2,0,2,1,2,0]).
test_12 :- parse_list([0,1,2,0,1,2,0,1,2]).
test_13 :- parse_list([2,0,1,2,0,1,2,0,1]).
test_14 :- parse_list([1,2,0,1,2,0,1,2,0]).
test_15 :- parse_list([0,2,1,0,2,1,0,2,1]).

% Invalid cases (contain prohibited patterns)
test_16 :- \+ parse_list([1,1,0,1]).       
test_17 :- \+ parse_list([1,1,2,2]).       
test_18 :- \+ parse_list([1,0,1,1]).       
test_19 :- \+ parse_list([1,0,1,2]).
test_20 :- \+ parse_list([2,2,2,1,0,1,2,0,0,0]).      
test_21 :- \+ parse_list([0,0,0,1,1,2,2,1,1,1]).      
test_22 :- \+ parse_list([2,0,1,1,0,1,0,0,0]).
test_23 :- \+ parse_list([0,1,2,2,2,0,1,1,2,2]).
test_24 :- \+ parse_list([0,1,1,0,1,0,1,1]).
test_25 :- \+ parse_list([0,2,2,1,1,0,1,1,0]).

% Run all tests
run_tests :-
    test_0,  test_1,  test_2,  test_3,  test_4,
    test_5,  test_6,  test_7,  test_8,  test_9,
    test_10, test_11, test_12, test_13, test_14,
    test_15, test_16, test_17, test_18, test_19,
    test_20, test_21, test_22, test_23, test_24,
    test_25.
