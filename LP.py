from pulp import *
from pathlib import Path


def main():
    """
    We assume the vertices number range is from 1 to n. The input is like this for
    every edge: source destination capacity cost
    """
    n, m, S, D = list(map(int, input().split())
                      )  # Vertices, edges, source, and destination
    capacities = dict()
    costs = dict()
    decision_variables = dict()
    vertices = dict()
    for i in range(m):
        source, destination, capacity, cost = list(map(int, input().split()))
        key = f'x{source}_{destination}'
        try:
            decision_variables[key]
        except KeyError:
            decision_variables[key] = LpVariable(key)
            capacities[key] = capacity
            costs[key] = cost

        try:
            vertices[source]['out'].append(key)
        except KeyError:
            vertices[source] = {'out': [], 'in': []}
            vertices[source]['out'].append(key)

        try:
            vertices[destination]['in'].append(key)
        except KeyError:
            vertices[destination] = {'out': [], 'in': []}
            vertices[destination]['in'].append(key)

    # larger than the greatest cost + 10. I want to force the solver to choose the edge with zero cost
    BIG_VALUE = max(costs.values()) + 10

    problem = LpProblem('The_Min_Cost_Max_Flow', LpMaximize)
    # 1 / cost -> This trick will force the solver to choose edges with the lowest costs.
    coeffs = [(1 / costs[key]) * decision_variables[key] if costs[key]
              != 0 else BIG_VALUE * decision_variables[key] for key in decision_variables.keys()]

    problem += lpSum(coeffs)

    for key in decision_variables.keys():  # An arbitary edge's flow must be lower than its total capacity
        problem += decision_variables[key] <= capacities[key]
        problem += decision_variables[key] >= 0  # Bigger than zero

    for vertex in range(2, n):  # Check the flow consistency between the middle nodes
        problem += lpSum([decision_variables[vertices[vertex]['in'][j]]
                          for j in range(len(vertices[vertex]['in']))]) == \
            lpSum([decision_variables[vertices[vertex]['out'][j]]
                  for j in range(len(vertices[vertex]['out']))])

    problem.writeLP(Path(__file__).parent / 'problem.lp')
    status = problem.solve()

    total_cost = 0
    total_flow = 0
    for var in decision_variables.values():
        print(var.name, var.value())
        if var.name in vertices[S]['out']:
            total_flow += var.value()
        total_cost += var.value() * costs[var.name]

    print()
    print('Total flow over the network', total_flow)
    print('Total flow cost', total_cost)


if __name__ == '__main__':
    main()
