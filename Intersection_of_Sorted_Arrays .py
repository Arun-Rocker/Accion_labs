class SortedArrayIntersection:
    def __init__(self, arr1, arr2):
        """
        Initialize with two sorted arrays of integers.
        
        Args:
            arr1 (list[int]): First sorted array
            arr2 (list[int]): Second sorted array
        """
        self.arr1 = arr1
        self.arr2 = arr2
        self.intersection = []
        
    def find_intersection(self):
        """
        Find the intersection of two sorted arrays without duplicates.
        
        Returns:
            list[int]: Array containing common elements
        """
        i = j = 0
        len1, len2 = len(self.arr1), len(self.arr2)
        
        while i < len1 and j < len2:
            if self.arr1[i] < self.arr2[j]:
                i += 1
            elif self.arr1[i] > self.arr2[j]:
                j += 1
            else:
                # Found common element
                if not self.intersection or self.arr1[i] != self.intersection[-1]:
                    self.intersection.append(self.arr1[i])
                i += 1
                j += 1
                
        return self.intersection
    
    def get_intersection(self):
        """
        Get the intersection result.
        
        Returns:
            list[int]: The intersection array
        """
        return self.intersection

# Example usage
if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([1, 2, 3, 4, 5], [2, 4, 6, 8]),        # Normal case
        ([1, 2, 2, 3], [2, 2, 3, 4]),            # Duplicates in input
        ([1, 3, 5], [2, 4, 6]),                  # No intersection
        ([], [1, 2, 3]),                         # Empty array
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),      # Identical arrays
        ([1, 5, 10, 20], [5, 10, 15, 20])        # Larger numbers
    ]
    
    for arr1, arr2 in test_cases:
        finder = SortedArrayIntersection(arr1, arr2)
        intersection = finder.find_intersection()
        print(f"Array1: {arr1}\nArray2: {arr2}")
        print(f"Intersection: {intersection}\n")