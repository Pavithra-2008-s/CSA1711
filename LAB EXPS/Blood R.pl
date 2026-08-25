% BLOOD RELATIONSHIP DATABASE

% Gender
male(ravi).
male(kumar).
male(arun).
male(suresh).

female(latha).
female(priya).
female(anitha).
female(meena).

% Parent
parent(ravi, kumar).
parent(latha, kumar).

parent(kumar, arun).
parent(priya, arun).

parent(kumar, anitha).
parent(priya, anitha).

parent(arun, meena).

% Father
father(X,Y) :-
    male(X),
    parent(X,Y).

% Mother
mother(X,Y) :-
    female(X),
    parent(X,Y).

% Sibling
sibling(X,Y) :-
    parent(P,X),
    parent(P,Y),
    X \= Y.

% Grandparent
grandparent(X,Y) :-
    parent(X,Z),
    parent(Z,Y).

% Grandfather
grandfather(X,Y) :-
    male(X),
    grandparent(X,Y).

% Grandmother
grandmother(X,Y) :-
    female(X),
    grandparent(X,Y).

% Child
child(X,Y) :-
    parent(Y,X).

% Relationship between two persons
relationship(X,Y) :-
    father(X,Y),
    write(X), write(' is Father of '), write(Y).

relationship(X,Y) :-
    mother(X,Y),
    write(X), write(' is Mother of '), write(Y).

relationship(X,Y) :-
    child(X,Y),
    write(X), write(' is Child of '), write(Y).

relationship(X,Y) :-
    sibling(X,Y),
    write(X), write(' is Sibling of '), write(Y).

relationship(X,Y) :-
    grandfather(X,Y),
    write(X), write(' is Grandfather of '), write(Y).

relationship(X,Y) :-
    grandmother(X,Y),
    write(X), write(' is Grandmother of '), write(Y).

% Family
family(X,Y) :-
    parent(X,Y).

family(X,Y) :-
    parent(Y,X).

family(X,Y) :-
    sibling(X,Y).

family(X,Y) :-
    grandparent(X,Y).

family(X,Y) :-
    grandparent(Y,X).
