#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Compléter les tuples avec 0 si nécessaire pour avoir 2 éléments
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)
    # Décomposer les tuples en 2 éléments
    a1, a2 = tuple_a[:2]
    b1, b2 = tuple_b[:2]
    # Additionner les éléments correspondants
    return (a1 + b1, a2 + b2)
