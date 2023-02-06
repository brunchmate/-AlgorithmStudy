def solution(board, moves):
    answer = 0
    basket = []
    for m in moves:
        for b in board:
            if b[m-1] == 0:
                continue
            basket.append(b[m-1])
            b[m-1] = 0
            
            if len(basket) < 2:
                break
            if basket[-1] == basket[-2]:
                basket.pop()
                basket.pop()
                answer += 2
            break
    return answer
#처음에 문제의 배열이 의미하는것을 제대로 이해하지 못 해 시간이 오래걸렸다.
