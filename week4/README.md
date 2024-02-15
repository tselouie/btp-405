[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-7f7980b617ed060a017424585567c406b6ee15c891e84e1186181d67ecf80aa0.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=13547093)
# Activity 2 (Due Feb 4 - 7%)

Provide solutions to following problems in the empty files given in this repository. There are numerous "Introduction to Python" tutorials and textbooks available online and via [Seneca's digital library](https://library.senecacollege.ca) which you can reference.

Good coding practices from your previous courses should be used.  The submitted functions should also be annotated with *docstrings* as described [here](https://peps.python.org/pep-0257/).

1. (10 points) Write a Python function `getPrimeNumbers(n)` which returns a list containing all prime numbers between 2 and _n_.  Create a helper function to determine if a particular number is prime and then use a comprehension to generate your list.

2. (20 points) Write a Python function `graphSnowfall(t)` which retrives data in a text file _t_ and displays that information in a bar chart.

The file will have a single number on each line representing the amount of snowfall accumulation for a given day. Aggregate these values so that each one contributes to a particular 10 cm range.  For example, a file containing

10

15

45

5

20

25

would have

* 2 between 0-10cms
* 2 between 11-20cms
* 1 between 21-30cms
* 0 between 31-40cms
* 1 between 41-50cms

Use module [matplotlib](https://matplotlib.org/) to plot a bar graph showing your results. The x-axis should show the ranges and the y-axis should show the number of occurances in that range.

3. (15 points) Write a Python function `wordCount(t)` which retrives data in a text file _t_ and returns a dictionary where the _keys_ are unique words in the files and the corresponding _values_ are lists of line numbers where the words are found in the text.
4. (25 points) Write a Python function `printStats(t)` which retrives data in a text file _t_ which reads in lines of numbers.  For each line read in, the function must call a _decorator_ function which prints 
* the numbers read
* the count of the numbers read
* the average of the numbers
* the maximum of the numbers

5. (10 points) Consider the following code blocks which generate the same output.
    1. (7 points) Describe what each program snippet does to compute its results.
    Approach one is a function that takes a number parameter that denotes
    what the for loop will iterate to. And for each number it iterates, it will be multiplied by 2 and appended to a list which is then returned by the function. Then the function is called in the for loop to print the values.

    Approach 2 directly creates the list in the for loop iterator given the number 5
    and prints out the numbers.

    Approach 3 also takes a parameter much like approach 1 but instead of appending the calculated value into a list it returns/yields a sequence of numbers after multiplying it so it could be used as 'i' in the print iterator.

    2. (3 points) What type of function is `doubleG(n)`? What is the advantage of using such a function?
    doubleG(n) is a generator function, the advantage of using such a function is that it is more memory efficient as it does not need to allocate as much space to calculate the values as opposed to using a list which you need to use more memory right off the bat to assign it to values.


```
#Approach 1
// receives a number 'n' and creates a list of numbers up to n in multiples of 2 and returns the list
//initializes the list
//iterates through range and appends to res
def doubleL(n):
    res = []
    for i in range(n): res.append(i * 2)
    return res

//prints the index of the number in the format "i:n*2"
for i in doubleL(5): 
    print(i, end=' : ')
```

```
#Approach 2
// provided the number 5 in range it iterates and creates the list
for x in [n * 2 for n in range(5)]:
    print(x, end=' : ')
```

```
#Approach 3
//
def doubleG(n):
        for i in range(n):
            yield i * 2

for i in doubleG(5):
        print(i, end=' : ')
```


6. (20 points) Be prepared to present and explain your work in the lab session immediately after the due date. 


