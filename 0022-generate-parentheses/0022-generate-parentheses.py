class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(alist,n,op=0,cl=0):
            if not n:
                return [alist+")"*(op-cl)]
            combinations=[]
            
            if not alist:
                combinations.extend(generate("(",n-1,op+1,cl))
            else:
                combinations.extend(generate(alist+"(",n-1,op+1,cl))
                if op>cl:
                    combinations.extend(generate(alist+")",n,op,cl+1))
            return combinations
        
        
        return generate("",n)