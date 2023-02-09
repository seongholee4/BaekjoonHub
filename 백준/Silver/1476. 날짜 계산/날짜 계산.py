E, S, M = map(int, input().split())
e_, s_, m_ = 1, 1, 1
i = 1
while(True):
    if e_ == E and s_ == S and m_ == M:
        print(i)
        break
    e_+=1
    s_+=1
    m_+=1
    if e_ == 16:
        e_ = 1
    if s_ == 29:
        s_ = 1
    if m_ == 20:
        m_ = 1
    i+=1