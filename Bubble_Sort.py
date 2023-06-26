class Solution:
     def __init__(self, array):
        self.array = array

     def Bubble_Sort(self,array,n):
         n = len(arr)
    
         for i in range(n - 1):
            swapped = False
            for j in range(n - 1 - i):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    swapped = True
            if not swapped:
                break # If no swaps occurred, the array is already sorted
                
     def display(self):
        print("Sorted array:", self.array)
        


t = int(input("Enter the use case number "))
for _ in range(0 ,t ):
    n = int(input("Enter number of element"))
    arr = list(map(int ,input("enter the numbers to be sorted").split()))
    bs = Solution(arr)
    bs.Bubble_Sort(arr , n)  # Perform Bubble Sort
    bs.display()  # Display the sorted array