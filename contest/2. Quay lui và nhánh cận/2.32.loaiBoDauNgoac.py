from collections import deque

def is_valid(expression):
    balance = 0
    for char in expression:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
        if balance < 0:  
            return False
    return balance == 0

def remove_invalid_parentheses(expression):
    queue = deque([expression])
    visited = set([expression])
    valid_expressions = set()
    found = False
    max_len = 0
    
    while queue:
        current = queue.popleft()
        
        if max_len and len(current) < max_len:
            continue
        
        if is_valid(current):
            valid_expressions.add(current)
            if not max_len:
                max_len = len(current)
            found = True
        
        if found:
            continue
        
        for i in range(len(current)):
            if current[i] not in "()":
                continue
            next_expr = current[:i] + current[i+1:]
            if next_expr not in visited:
                visited.add(next_expr)
                queue.append(next_expr)
    
    return sorted(valid_expressions) if valid_expressions else ["-1"]

def main():
    # print(" ".join(remove_invalid_parentheses('()())()')))
    print(" ".join(remove_invalid_parentheses('(u)())()')))

main()