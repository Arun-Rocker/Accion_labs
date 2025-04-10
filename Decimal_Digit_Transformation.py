class DigitTransformer:
    def __init__(self, x):
        """
        Initialize with a digit to transform.
        
        Args:
            x (int): A single digit (0-9)
        """
        if not isinstance(x, int):
            raise ValueError("Input must be an integer")
        if x < 0 or x > 9:
            raise ValueError("Input must be a single digit (0-9)")
        self.x = x
    
    def calculate_series(self):
        """
        Calculate X + XX + XXX + XXXX
        
        Returns:
            int: The computed sum
        """
        xx = int(f"{self.x}{self.x}")
        xxx = int(f"{self.x}{self.x}{self.x}")
        xxxx = int(f"{self.x}{self.x}{self.x}{self.x}")
        return self.x + xx + xxx + xxxx
    
    @staticmethod
    def compute(x):
        """
        Static method for one-time computation with validation
        
        Args:
            x (int): A single digit (0-9)
            
        Returns:
            int: The computed sum
        """
        transformer = DigitTransformer(x)
        return transformer.calculate_series()

# Example usage
if __name__ == "__main__":
    test_cases = [
        3,    # Valid case (should return 3702)
        9,    # Edge case with max digit
        0,    # Edge case with min digit
        # "5", # Uncomment to test string input error
        # 12,  # Uncomment to test multi-digit error
        # -1   # Uncomment to test negative input error
    ]
    
    for digit in test_cases:
        try:
            transformer = DigitTransformer(digit)
            result = transformer.calculate_series()
            print(f"X = {digit}: {digit} + {digit}{digit} + {digit}{digit}{digit} + {digit}{digit}{digit}{digit} = {result}")
        except ValueError as e:
            print(f"Error for input {digit}: {str(e)}")