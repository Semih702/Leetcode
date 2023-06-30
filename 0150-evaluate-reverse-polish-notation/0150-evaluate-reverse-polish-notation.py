class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        hashset=set(("*","/","+","-"))
        
        stack=[]
        
        for i in range(-1,-len(tokens)-1,-1):
            stack.append(int(tokens[i]) if tokens[i] not in hashset else tokens[i])  
            while len(stack)>2 and stack[-3] in hashset and isinstance(stack[-1],int) and isinstance(stack[-2],int):
                num1=stack.pop()
                num2=stack.pop()
                ope=stack.pop()

                if ope=="*":
                    stack.append(num1 * num2)
                elif ope=="/":
                    stack.append(int(num1 / num2))
                elif ope=="-":
                    stack.append(num1 - num2)
                else:
                    stack.append(num1 + num2)
        return stack[0]
                    
        
                    
            