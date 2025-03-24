% Author: César Ignacio Saucedo Rodríguez 
% Date: March 22, 2025

%initial state
start_state(q0).

% Transitions

% q0 transitions
transition(q0, 0, q0).
transition(q0, 1, q1).
transition(q0, 2, q0).

% q1 transitions
transition(q1, 0, q2).
transition(q1, 1, q4).
transition(q1, 2, q0).

% q2 transitions
transition(q2, 1, q3).
transition(q2, 2, q0).
transition(q2, 0, q0).

%q3 transitions
transition(q3, 0, q0).
transition(q3, 1, state_1011).
transition(q3, 2, state_1012).

%q4 transitions
transition(q4, 0, q5).
transition(q4, 2, q6).
transition(q4, 1, q0).

%q5 transitions
transition(q5, 1, state_1101).
transition(q5, 0, q0).
transition(q5, 2, q0).

%q6 transitions
transition(q6, 2, state_1122).
transition(q6, 1, q0).
transition(q6, 0, q0).


%forbiden combinations
forbiden(state_1011).
forbiden(state_1012).
forbiden(state_1101).
forbiden(state_1122).
