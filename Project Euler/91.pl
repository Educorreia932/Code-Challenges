% Right triangles with integer coordinates

:- use_module(library(clpfd)).
:- use_module(library(lists)).

pivoting(_, [], [], []).

pivoting([A, B], [[C, D]|T], [[C, D]|L], G):-
    D > B,
    pivoting([A, B],T,L,G).

pivoting([A, B], [[C, D]|T], [[C, D]|L], G):-
    D = B,
    C > A,
    pivoting([A, B], T, L, G).

pivoting([A,B], [[C,D]|T], L, [[C, D]|G]):-
    D < B,
    pivoting([A, B], T, L, G).

pivoting([A, B], [[C, D]|T], L, [[C, D]|G]):-
    D = B,
    C < A,
    pivoting([A, B], T, L, G).

pivoting([A, B], [[C, D]|T], L, G):-
    A = C,
    D = B,
    pivoting([A,B], T, L, G).

q_sort([], Acc, Acc).

q_sort([H|T], Acc, Sorted):-
    pivoting(H, T, L1, L2),
    q_sort(L1, Acc, Sorted1),
    q_sort(L2, [H|Sorted1], Sorted).

quick_sort(List, Sorted) :-
    q_sort(List, [], Sorted).

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

solve(Answer) :-
    Coords = [X0, Y0, X1, Y1, X2, Y2],
    Coords ins 0..50,

    X0 #= 0,
    Y0 #= 0,

    P0 = [X0, Y0],
    P1 = [X1, Y1],
    P2 = [X2, Y2],
    
    Points = [P0, P1, P2],

    % Points must have distinct pairs of coordinates
    dif_all(Points),

    % Vectors that represent the triangle's sides
    vector(P0, P1, V0),
    vector(P1, P2, V1),
    vector(P0, P2, V2),

    dot_product(V0, V1, D0),
    dot_product(V0, V2, D1),
    dot_product(V0, V1, D2),

    % The dot product of two sides must be zero (90 degree angle)
    D0 #= 0 #\/ D1 #= 0 #\/ D2 #= 0,

    findall(Points, label(Coords), Triangles),
    maplist(quick_sort, Triangles, OrderedTriangles),
    sort(OrderedTriangles, UniqueTriangles), % Remove duplicates
    length(UniqueTriangles, Answer). 
