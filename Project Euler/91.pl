% Right triangles with integer coordinates

:- use_module(library(clpfd)).

dot_product([], [], 0).

dot_product([H1|T1], [H2|T2], Result) :-
    Product #= H1 * H2,
    dot_product(T1, T2, Remaining),
    Result #= Product + Remaining.

dif_all([]).

dif_all([H|T]) :-
    maplist(dif(H), T),
    dif_all(T).

vector([], [], []).

vector([X0, Y0], [X1, Y1], [Vx, Vy]) :-
    Vx #= X1 - X0,
    Vy #= Y1 - Y0.

solve(Coords) :-
    Coords = [X0, Y0, X1, Y1, X2, Y2],
    Coords ins 0..2,

    X0 #= 0,
    Y0 #= 0,

    P0 = [X0, Y0],
    P1 = [X1, Y1],
    P2 = [X2, Y2],
    
    Points = [P0, P1, P2],

    % Points must have distinct pairs of coordinates
    dif_all(Points),

    vector(P0, P1, V0),
    vector(P0, P2, V1),

    dot_product(V0, V1, 0),

    label(Coords),
    aggregate_all(count, label(Coords), Answer).
