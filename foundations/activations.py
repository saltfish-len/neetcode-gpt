class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        def obj(x):
            return x**2
        
        def deri(x):
            return 2*x
        x = init
        for i in range(iterations):
            x -= learning_rate*deri(x)
        return round(x, 5)