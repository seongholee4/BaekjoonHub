class P1546_평균():
    def 평균(self, n: int, score: list) -> float:
        max_score = max(score)
        for i in range(len(score)):
            score[i] = score[i]/max_score*100
        
        # average
        sum = 0
        for i in range(len(score)):
            sum += score[i]
        avg = sum/len(score)
        return avg

if __name__ == '__main__':
    n = int(input())
    score = list(map(int, input().split()))
    s = P1546_평균()
    print(s.평균(n, score))