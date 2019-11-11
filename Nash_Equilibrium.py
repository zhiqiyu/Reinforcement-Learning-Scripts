import cvxopt
from cvxopt.modeling import variable, op, matrix, dot
import numpy as np
import pandas as pd

if __name__ == "__main__":
    
    V = variable(1, "V")

    pi = variable(3, "pi")

    c1 = (0 * pi[0] + 1.0 * pi[1] -0.39 * pi[2] >= V)
    c2 = (-1.0 * pi[0] + 0 * pi[1] + 1.0 * pi[2] >= V)
    c3 = (0.39 * pi[0] -1.0 * pi[1] + 0 * pi[2] >= V)
    c4 = (pi[0] + pi[1] + pi[2] == 1)

    lp = op(V, [c1, c2, c3, c4])
    lp.solve()
    print(lp.status)
    print(pi.value)


