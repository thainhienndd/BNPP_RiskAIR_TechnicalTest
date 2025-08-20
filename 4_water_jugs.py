from collections import deque
from math import gcd

def water_jugs_min_seq(target, capacities):
    """
        The idea of this algorithm is to test all the possible state from a starting point until we reach the desired amount.
        To optimize it, we ignore the state that were already seen.
        We end the algorithm when we reach the target.
        Then, we get all the states / actions that enabled to reach the target.
    """
    if target <= 0:
        raise ValueError("target must be > 0")
    if not capacities or any(c <= 0 for c in capacities):
        raise ValueError("capacities must be non-empty and > 0")

    # Solve mathematical case if there is no solutions at the problem
    g = 0
    for c in capacities:
        g = gcd(g, c)
    if target % g != 0 or target > max(capacities):
        return None


    n = len(capacities)
    start = tuple(0 for _ in capacities)
    q = deque([start])
    visited = {start}
    parent = {start: (None, None)}

    # Function that enables to reconstruct the actions and state from the target
    def reconstruct(state):
        seq = []
        cur = state
        while parent[cur][0] is not None:
            prev, op = parent[cur]
            seq.append((op, cur))
            cur = prev
        seq.reverse()
        return seq

    while q:
        state = q.popleft()
        if any(x == target for x in state):
            return reconstruct(state)

        # 1) Fill in a jug
        for i in range(n):
            if state[i] < capacities[i]:
                new = list(state); new[i] = capacities[i]; newt = tuple(new)
                if newt not in visited:
                    visited.add(newt); parent[newt] = (state, (-1, i))
                    if any(x == target for x in newt):
                        return reconstruct(newt)
                    q.append(newt)

        # 2) Vider (i -> -1)
        for i in range(n):
            if state[i] > 0:
                new = list(state); new[i] = 0; newt = tuple(new)
                if newt not in visited:
                    visited.add(newt); parent[newt] = (state, (i, -1))
                    if any(x == target for x in newt):
                        return reconstruct(newt)
                    q.append(newt)

        # 3) Verser (i -> j) jusqu’à ce que i soit vide ou j plein
        for i in range(n):
            if state[i] == 0:
                continue
            for j in range(n):
                if i == j or state[j] == capacities[j]:
                    continue
                amount = min(state[i], capacities[j] - state[j])
                if amount == 0:
                    continue
                new = list(state)
                new[i] -= amount
                new[j] += amount
                newt = tuple(new)
                if newt not in visited:
                    visited.add(newt); parent[newt] = (state, (i, j))
                    if any(x == target for x in newt):
                        return reconstruct(newt)
                    q.append(newt)
    return None

def print_steps(seq):
    for (src, dst), state in seq:
        state_fmt = "(" + ",".join(str(x) for x in state) + ")"
        print(f"{src:2d} -> {dst:2d} : {state_fmt}")

seq = water_jugs_min_seq(23, [8,145, 5])
print_steps(seq)
