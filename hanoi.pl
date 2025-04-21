hanoi(N) :-
    move(N, left, center, right).

move(0, _, _, _) :- !.

move(N, A, B, C) :-
    M is N - 1,
    move(M, A, C, B), 
    format('Move disk ~w from ~w to ~w~n', [N, A, C]),
    move(M, B, A, C).

% input: hanoi(3).
