% Special Pythagorean triplet

:- use_module(library(clpfd)).

solve(Answer) :-
    Vars = [A, B, C],
    domain(Vars, 1, 998),

    A * A + B * B #= C * C,
    A + B + C #= 1000,
    Answer #= A * B * C,
    
    labeling([], Vars).