class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(alist,n):
            combinations=[]
            if not n:
                number1=alist.count("(")
                number2=alist.count(")")
                return [alist+")"*(number1-number2)]
            

            if not alist:
                combinations.extend(generate("(",n-1))
            else:
                print(alist,n)
                combinations.extend(generate(alist+"(",n-1))
                if alist.count("(")>alist.count(")"):
                    combinations.extend(generate(alist+")",n))
            return combinations
        
        
        return generate("",n)