alpha = ['A', 'E', 'I', 'O', 'U']
result = []

def dfs(word):
    result.append(word) 
    
    if len(word) == 5:
        return
    
    for ch in alpha:
        dfs(word + ch)

def solution(word):
    for ch in alpha:
        dfs(ch)
    
    return result.index(word) + 1 