def latest(scores):
    return scores.pop()


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    scores.sort(reverse=True)
    print(scores)
    if len(scores) < 3:
        return scores

    return scores[:3]
