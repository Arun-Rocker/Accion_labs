class EvenFibonacciSum:
    def __init__(self, count=100):
        """
        Initialize the calculator with the number of even Fibonacci numbers to sum.
        
        Args:
            count (int): Number of even Fibonacci numbers to sum (default: 100)
        """
        self.count = count
        self.sum = 0
        self.even_fib_numbers = []
        
    def calculate(self):
        """
        Calculate the sum of the first 'count' even Fibonacci numbers.
        
        Returns:
            int: The sum of even Fibonacci numbers
        """
        a, b = 1, 1  # Initialize first two Fibonacci numbers
        found = 0
        
        while found < self.count:
            # Generate next Fibonacci number
            a, b = b, a + b
            
            # Check if even
            if b % 2 == 0:
                self.even_fib_numbers.append(b)
                self.sum += b
                found += 1
                
        return self.sum
    
    def get_sequence(self):
        """
        Get the list of even Fibonacci numbers found.
        
        Returns:
            list: List of even Fibonacci numbers
        """
        return self.even_fib_numbers

# Example usage
if __name__ == "__main__":
    # Create calculator for first 100 even Fibonacci numbers
    calculator = EvenFibonacciSum(100)
    
    # Calculate the sum
    result = calculator.calculate()
    
    # Print results
    print(f"Sum of first 100 even Fibonacci numbers: {result}")
    print(f"First 5 even Fibonacci numbers found: {calculator.get_sequence()[:5]}")
    print(f"Last 5 even Fibonacci numbers found: {calculator.get_sequence()[-5:]}")