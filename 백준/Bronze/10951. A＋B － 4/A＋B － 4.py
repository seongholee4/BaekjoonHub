try:
    while True:
        s = input()
        if s == "":
            break
        else:
            A, B = map(int, s.split())
            print(A + B)
except EOFError:
    pass