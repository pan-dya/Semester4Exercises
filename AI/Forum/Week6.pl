# A *right triangle* is a triangle in which one angle is equal to 90 degrees.
# It is known that the sum of all angles in any triagle is 180 degrees.
# Assume that the sum of two angles in a given triangle is 90 degrees.
# Write a Prolog program that shows that this is the *right triangle*.
% Define a predicate to check if a triangle is a right triangle.

is_right_triangle(A, B, C) :-
    % Check if the sum of two angles is 90 degrees.
    (A + B =:= 90 ; A + C =:= 90 ; B + C =:= 90),
    % Check if the sum of all angles is 180 degrees.
    A + B + C =:= 180,
    
    write('This is a right triangle.').
