% Parker Square

:- use_module(library(clpfd)).

solve(Numbers, Sum) :-
    Numbers = [N1, N2, N3, N4, N5, N6, N7, N8, N9],
    Numbers ins 0..100000000,
    all_distinct(Numbers),

    maplist(
        #=(Sum),
        [
            N1 * N1 + N2 * N2 + N3 * N3,
            N4 * N4 + N5 * N5 + N6 * N6,
            N7 * N7 + N8 * N8 + N9 * N9,
            N1 * N1 + N4 * N4 + N7 * N7,
            N2 * N2 + N5 * N5 + N8 * N8,
            N3 * N3 + N6 * N6 + N9 * N9,
            N1 * N1 + N5 * N5 + N9 * N9,
            N7 * N7 + N5 * N5 + N3 * N3
        ]
    ),
    
    label(Numbers).
    