class Solution:
    def scoreOfStudents(self, s: str, answers):
        
    
        def correct_eval(expr):
            stack = []
            num = 0
            op = '+'
            
            for i, ch in enumerate(expr):
                if ch.isdigit():
                    num = int(ch)
                
                if not ch.isdigit() or i == len(expr) - 1:
                    if op == '+':
                        stack.append(num)
                    elif op == '*':
                        stack[-1] *= num
                    op = ch
            return sum(stack)
        
        correct_answer = correct_eval(s)
        
        
        from functools import lru_cache
        
        @lru_cache(None)
        def compute(expr):
            results = set()
            
            if expr.isdigit():
                return {int(expr)}
            
            for i in range(len(expr)):
                if expr[i] in "+*":
                    left_results = compute(expr[:i])
                    right_results = compute(expr[i+1:])
                    
                    for l in left_results:
                        for r in right_results:
                            if expr[i] == '+':
                                val = l + r
                            else:
                                val = l * r
                            
                            if val <= 1000:
                                results.add(val)
            
            return results
        
        possible_answers = compute(s)
        
        
        score = 0
        
        for ans in answers:
            if ans == correct_answer:
                score += 5
            elif ans in possible_answers:
                score += 2
        
        return score