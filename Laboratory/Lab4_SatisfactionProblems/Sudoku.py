from constraint import *

if __name__ == '__main__':
    solver = input()
    if solver == "BacktrackingSolver":
        problem = Problem()
    elif solver == "RecursiveBacktrackingSolver":
        problem = Problem(RecursiveBacktrackingSolver())
    else:
        problem = Problem(MinConflictsSolver())
    variables = range(0, 81)
    domain = range(1, 10)
    problem.addVariables(variables, domain)
    lista = [[k for j in range(3) for k in range(z + i+9*j, z+i+9*j+3)] for z in range(0, 81, 27) for i in range(0,9,3)]
    for element in lista:
        problem.addConstraint(AllDifferentConstraint(), element)

    for row in range(9):
        problem.addConstraint(AllDifferentConstraint(), [r for r in range(9*row, 9*row+9)])

    for col in range(9):
        problem.addConstraint(AllDifferentConstraint(), [9*l+col for l in range(9)])

    solution = problem.getSolution()

    print(solution)