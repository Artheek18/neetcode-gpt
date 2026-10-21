class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places

        get_to_minimun = init

        if iterations == 0:
            return init

        for i in range(iterations):
            get_to_minimun = get_to_minimun - (learning_rate * 2*get_to_minimun)

        return round(get_to_minimun, 5)
