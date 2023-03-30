class Factorial:
    
    def factorial(self,a):
        ans = 1 
        for i in range(1,a+1):
            ans*=i

        return ans 
