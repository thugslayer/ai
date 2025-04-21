import math

def minimax(depth, node_index, is_max, values, alpha, beta, max_depth):
    if depth == max_depth:
        return values[node_index]

    if is_max:
        best = -math.inf
        for i in range(2):
            val = minimax(depth + 1, node_index * 2 + i, False, values, alpha, beta, max_depth)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break  # Beta cut-off
        return best
    else:
        best = math.inf
        for i in range(2):
            val = minimax(depth + 1, node_index * 2 + i, True, values, alpha, beta, max_depth)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break  # Alpha cut-off
        return best

if __name__ == "__main__":
    values = [2, 3, 5, 9, 0, 1, 7, 5]  
    max_depth = 3 
    best_score = minimax(0, 0, True, values, -math.inf, math.inf, max_depth)
    print("The optimal value is:", best_score)
