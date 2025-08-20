import math

def prorate_integer(cost: int, weights: list):
    # Case when cost < 0: error
    if cost < 0:
        raise ValueError("cost >= 0")
    # Case when sum of weight = 0 or no weightes : Error
    if not weights or sum(weights) == 0:
        raise ValueError("weights must contain at least one non-zero")

    # Compute sum of all weights (to scale later)
    W = sum(weights)
    list_exact_prorata = []
    for w in weights:
        # if weight = 0, we store 0
        if w == 0:
            list_exact_prorata.append(0.0)
        else:
            # Compute the exact prorated cost
            list_exact_prorata.append(cost * (w / W))

    # Get score by flooring each element of prorated to get integers
    floors = [math.floor(e) for e in list_exact_prorata]
    # Store the difference between sum of floored elements and cost
    R = cost - sum(floors)
    items = []
    # Compute a score for each element to check the difference between expected and real number
    for i, w in enumerate(weights):
        if w == 0:
            score = float('-inf')
        else:
            # score equals the differences betwwen exact and floored prorated cost, regularized by weight (max 1, min - 1)
            frac = list_exact_prorata[i] - floors[i]
            score = (2*frac - 1) / w
        items.append((score, i))

    # Sort by element with highest score (ie scores that are the furthest from prorated cost, regularized)
    items.sort(reverse=True)
    alloc = floors[:]
    # as a reminder, R represents the difference between prorated cost and floored prorated cost
    # So for each difference, we add 1 to the item that has the highest score to make sure the sum of all prorated cost equal original cost
    for k in range(R):
        idx = items[k][1]
        alloc[idx] += 1
    return alloc


normal_case_394 = prorate_integer(394, [0.3, 0.5, 0.2])
weight_case_3485 = prorate_integer(3485, [0.3, 0.6, 0.13])
weight_case_0_897 = prorate_integer(897, [0.3, 0.45, 0, 0.54])
print(f"Normal case for integer 394: {normal_case_394}, sum of list: {sum(normal_case_394)}")
print(f"Case for integer 394 where weights do not sum to 1: {weight_case_3485}, sum of list: {sum(weight_case_3485)}")
print(f"Case for integer 897 where one weight equals 0: {weight_case_0_897}, sum of list: {sum(weight_case_0_897)}")
