# FizzBuzz (submitted by [zachary-walters](https://github.com/zachary-walters))

 FizzBuzz is a common interview question used to screen programmer candidates. The program outputs numbers from 1 to n. The program outputs the string "Fizz" when n is a multiple of 3, "Buzz" when n is a multiple of 5, and "FizzBuzz" when n is a multiple of 3 and 5. 

 All the code listed here can be found in the [supporting_files](https://github.com/RaviKarrii/Awesome-interview-preparation/blob/main/Java/supporting_files/FizzBuzz/) folder.


 ### Pre-Java8 Solution
  ```
for (int i = 1; i <= num; i++) {
    if (i % 3 == 0 && i % 5 == 0) {
        System.out.println("fizzbuzz");
    } else if (i % 3 == 0) {
        System.out.println("fizz");
    } else if (i % 5 == 0) {
        System.out.println("buzz");
    } else {
        System.out.println(i);
    }
}
 ```

 The simplicity of the FizzBuzz problem is often what makes it difficult for programmers to overcome. While there are multiple implementations of the problem, this is one of the simplest solutions. This logic can be implemented accross almost all languages, since modulo arithmetic is built into almost every programming language's core. 

  ### Java8+ Solution
 ```
IntStream.rangeClosed(1, 100)
    .mapToObj(i -> i % 3 == 0 ? (i % 5 == 0 ? "FizzBuzz" : "Fizz") : (i % 5 == 0 ? "Buzz" : i))
    .forEach(System.out::println);
 ```
 
 Java version 8 introduced Streams, which are sequences of elements. In the FizzBuzz example, we use a stream of primitive int-valued elements, which is done with IntStream. We are also using a Lambda function, which is new in Java 8, in conjunction with our ternary operator. 