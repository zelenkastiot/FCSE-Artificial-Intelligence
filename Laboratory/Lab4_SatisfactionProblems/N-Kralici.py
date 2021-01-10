from constraint import *


def queens_attacking_constraint(q1, q2):
    if q1[0] == q2[0] or q1[1] == q2[1] or (abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])):
        return False
    return True


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    n = int(input())
    domain = [(i, j) for i in range(0, n) for j in range(0, n)]

    queens = range(1, n+1)

    problem.addVariables(queens, domain)

    for queens1 in queens:
        for queens2 in queens:
            if queens1 < queens2:
                problem.addConstraint(queens_attacking_constraint, (queens1, queens2))
    if n > 6:
        solution = problem.getSolution()
        print(solution)
    else:
        solution = problem.getSolutions()
        print(len(solution))

