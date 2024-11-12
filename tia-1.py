class MathOperations:


    def main_operation(self, num1: int, num2: int) -> dict:
        """Performs multiple operations on two numbers and returns the results in a dictionary."""

        def subtract(a, b):
            """Returns the difference between two numbers."""
            return a - b

        def add(a, b):
            """Returns the sum of two numbers. """
            def inner(c,d):
                print(inner of  add)
            return a + b

        def multiply(a, b):
            """Returns the product of two numbers. """
            return a * b


        # Call nested functions and store results  
        results = {
            'product': multiply(num1, num2),
            'sum': add(num1, num2),
            'difference': subtract(num1, num2)
        }

        # Example of calling A nested function recursively (e.g., adding numbers up to a target)
    results['recursive_sum'] = recursive_sum(min(num1, num2))
    
    def recursive_sum(n):
        """Calculates the sum of all numbers from 1 to n."""
        if n <= 1:
            return n
        return n + recursive_sum(n - 1)


        return results

# Example usage:
math_ops = MathOperations()
print(math_ops.main_operation(5, 3))
