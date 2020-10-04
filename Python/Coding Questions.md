# Write a function that will give the nth entry in the fibonacci series. (submitted by [abxsantos](https://github.com/abxsantos))

 First you'll need to understand what is the fibonacci sequence. If you already do, that's great! If you don't know, [here's a wikipedia entry explaning what it is.](https://en.wikipedia.org/wiki/Fibonacci_number)


 To answer this question you can either make a iterative solution or a recursive solution.

 All the code listed here can be found in the [suppporting_files](https://github.com/RaviKarrii/Awesome-interview-preparation/tree/main/Python/supporting_files) folder.

 ### Iterative solution
 ```
  def iterative_fibonacci(index):
      """Iterative solution for the fibonacci sequence"""
      fib_array = [0, 1]
      i = 2
      while i <= index:
          last_value = fib_array[-1]
          prev_from_last_value = fib_array[-2]
          fib_array.append(last_value + prev_from_last_value)
          i += 1
      return fib_array[index]
 ```
 The key part is to understand that the first two numbers (0 and 1) must be already set up. From there you just need to implement the algorithm to calculate the next numbers in the sequence.

 The main problem in this solution is due to the Runtime complexity, since we are appending each number to an array. This should be pointed out when you give this answer.

 ### Recursive solution
 ```
  def recursive_fibonacci(index):
      """Recursive solution for the fibonacci sequence"""
      if index < 2:
          return index
      return recursive_fibonacci(index - 1) + recursive_fibonacci(index - 2)
 ```
 The recursive solution will also set the return for the first two numbers of the sequence (0 and 1, as seen in the if statement.)
 From there, the function will keep calling itself until a base case is achieved returning the number at the given argument index.

 In this approach the main problem is the time required to return the value. To solve this, you can wrap the recursive_fibonacci function in a memoization function, improving it's next calls.

