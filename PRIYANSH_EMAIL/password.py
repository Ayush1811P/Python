def PASS(P):
    correct=False
    if len(str(P))>=6:
        if isinstance(P,int):
            correct=True
    return correct

