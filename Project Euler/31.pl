% Coin sums

:- use_module(library(clpfd)).

solve(Answer) :-
    Vars = [
        A, % 1p
        B, % 2p
        C, % 5p
        D, % 10p
        E, % 20p
        F, % 50p
        G, % £1
        H  % £2
    ],

    domain(Vars, 0, 200),

    A + B * 2 + C * 5 + D * 10 + E * 20 + F * 50 + G * 100 + H * 200 #= 200,

    findall(Vars, labeling([], Vars), Solutions),
    length(Solutions, Answer).
