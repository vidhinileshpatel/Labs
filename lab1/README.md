# Lab 1

Lab one will cover basic Python literacy, tools, and algorithms.

# Lab

The objective of this lab is to retrieve data from the internet and run an analysis on it.
Use the following URLs to download a small graduate admission dataset, and build a linear
regression to predict admission probability.

Training data:
https://drive.google.com/uc?export=download&id=1-NRy3Q2AewrnZcenGmf1x48vvj2bxqeb

Application Data:
https://drive.google.com/uc?export=download&id=1OevU8V0tyhF9Sfxs_DzPqz1jBdg4FZBE

Here are roughly the steps you will want to take:

1. Download all of the data.
2. Prepare the data, separate independent and dependent variables and training and test sets.
3. Use the scikit-learn linear regression library found
[here](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)
to fit a line to the given data.
4. Do this for each independent variable and cross validate.
5. Apply the best coefficient to the application data set.
6. Write your results to a JSON file.


# Introduction to Python

Python is a great language for working with data. It's been adopted by
many of the top institutions involved in machine learning and data
science since it was born in the 1980s. That being said, we are going to
focus on three fundamental processes:

1. Getting data into the program
2. Doing useful things with the data
3. Getting data out of the program

All code should be run with Python 3.x


## Basic Python Literacy

Learning a new language can be daunting, especially if you are new to
programming. Just keep in mind that these languages were made by
people to be understood by people. It just takes a little patience
and practice.

### Variables 

If we want to store data somewhere, we have to ask the computer to make
space for it and give it a name so we can use it. In Python, we don't need
to tell the computer what `type` the variable is, and we can change the type
at any time without breaking a sweat.

Here is an example:

```Python
# Here we set the variable named "a" to an integer value 5
a = 5

# Now let's change it to a string
a = "I'm a string now"

# And now a float value
a = 1.234

# And now a boolean value
a = True
```

There are more complex variables, as well. If we would like to express
a `list` or `dict` of items, we can do that, too.

```Python
# Here is a list of values
# They do not need to be the same types
list_of_things = [1, 2, "three", "four", 5.0]

# This will print the third element in the list ("three")
print(list_of_things[2])

# Here is a dict (a.k.a. a map)
dictionary = {
	"key_1" : 1,
	"key_2" : "value"
}

# This will print the value for "key_1" (1)
print(dictionary["key_1"])
```


### Logic

Once we have data stored in the program in variables, we can draw
conclusions from it and manipulate it.

#### Conditional Logic

Conditional logic is used to make decisions within the program. This
largely occurs in the form of `if statements`. 

```Python
first_name = "Bill"
last_name = "Gates"
age = 62

# Here is the EQUALITY oeprator
if first_name == "Bill":
	# This will print
	print("My name is Bill")
else:
	print("My name is not Bill")

# Here is the NOT operator
# Can also be written as `last_name != "Gates"`
if not last_name == "Gates":
	print("My last name is not Gates")
else:
	# This will print
	print("My last name is Gates")

# This is the AND operator
if first_name == "Bill" and last_name == "Gates":
	# This will print
	print("My name is Bill Gates")

# This is the OR operator
if first_name == "Bill" or first_name == "Jill":
	# This will print
	print("My name is either Bill or Jill")

# Here is less than and greater than
if age < 70 and age > 59:
	# This will print
	print("I am in my 60s")

# Here is less or equal to and greater than or equal to
if age <= 69 and age >= 60:
	# This will print
	print("Once again, I am in my 60s")
```

#### Loops

Loops let us iterate over collections of items or perform the same operations
many times in a row.

The `while loop` iterates while a given condition is true.  The following
program prints the digits 0-9

```Python
my_number = 0

while my_number < 10:
	print(my_number)
	my_number += 1
```

The `for loop` iterates over a collection or range. When iterating over a list, the
loop returns the values at each index. When iterating over a dict, the loop returns the
keys at each iteration:

```Python
# Here we print the digits 0-9 using a range
for i in range(0, 10):
	print(my_number)

# Here we iterate over a list and print each value
my_list = [1, 2, 3, 4, 5]
for value in my_list:
	print(value)

# Here we iterate over the keys in a dict and
# print the associated values
my_dict = {
	"key_1": 1,
	"key_2": 2
}
for key in my_dict:
	print(my_dict[key])
```

Keep in mind that Python provides two handy keywords to manage loops:
`break` and `continue`. `break` indicates that the program should cease iterating
and break out of the loop. `continue` indicates that the program should move onto
the next iteration without completing the loop's logic block.

The following program prints all even numbers up to 100:

```Python
my_number = -1

while True:
	my_number += 1

	if my_number % 2 == 0:
		print(my_number)
		continue

	if my_number > 99:
		break
```

### Functions

Functions are a great way of refactoring and reusing code. With functions, you can give
a name to a block of code and invoke that block simply by calling the name. They are like
miniature programs in themselves. They do three simple things:

1. Take data in
2. Do something useful with data
3. Return some data

Sound familiar?

Let's create a function that returns all even numbers in a range.  First we
define the function, and then we call it:

```Python
"""
	"def" indicates that we want to make a function

	"evens" is the name of the function

	Function arguments go between the parentheses next to
	the function name. Here this is "lower_limit" and "upper_limit"
"""
def evens(lower_limit, upper_limit):
	# Create an empty list
	even_numbers = []

	# Iterate over the given range
	for x in range(lower_limit, upper_limit):
		if x % 2 == 0:
			# If the number is even, add it to the list
			even_numbers.append(x)

	# The return keyword indicates what the function should
	# send back to its caller
	return even_numbers


# Call the function
result = evens(0, 10)

# Prints [0, 2, 4, 6, 8]
print(result)

```

### List Comprehension

Python has some useful shorthand notations that can be hugely advantageous. One such
notation is called `list comprehension`. `list comprehension` is just a combination
of list, loop, and conditional notation.

Let's rewrite the "evens" function in one line:

```Python
def evens(lower_limit, upper_limit):
	return [x for x in range(lower_limit, upper_limit) if x % 2 == 0]


result = evens(0, 10)
print(result)
```

This yields the same exact result as the original "evens" function. Let's break it down:

1. First we indicate that we are going to create a list by using brackets 

	[...]

2. Then we start using a for loop, since we want to iterate over a range:

	[ for x in range(lower_limit, upper_limit) ]

3. We also need to indicate that we just want to take `x` from the loop:

	[ x for x in range(lower_limit, upper_limit) ]

	We are essentially saying "Take `x` for each `x` in this range"

4. Now apply the condition because we only want even numbers:

	[ x for x in range(lower_limit, upper_limit) if x % 2 == 0 ]

What if we wanted to format `x` as a string instead of just taking the value?

	[ "Even - " + str(x) for x in range(lower_limit, upper_limit) if x % 2 == 0 ]

We simply applied a transformation to `x` up front. Now this gives:

	['Even - 0', 'Even - 2', 'Even - 4', 'Even - 6', 'Even - 8']



## Data IO

Data can come from anywhere and be used for pretty much anything. If you doubt
this simply Google the infamous Cloudflare Lava Lamps.

Some commons data sources are files, databases, the internet at large, and hardware
(cameras, microphones, keyboards, etc.)  We will go over files and the internet for
the time being.

Generally, data can be found in one of the following three formats: JSON, CSV, and HTML/XML.
JSON is extremely popular on the internet and is widely preferred over XML since
it is more compressed and human readable. CSV is popular for storing any data that is
tabular.  HTML is mostly found when presenting web pages (websites are just data, too.)


### Files

Imagine that we have a text file in the same directory as our program called
"hello.txt".  It simply says "Hello World!"

We can access that file by opening it and reading its contents. Here is how to do
that manually:

```Python
# fin is assigned an open file object
fin = open("./hello.txt")

# Read in the contents
contents = fin.read()
print(contents)

# Close the file
fin.close()
```

The more "pythonic" way of doing it that closes the file automatically goes as follows:

```Python
with open("./hello.txt") as fin:
	contents = fin.read()
	print(contents)
```

Once the program exits the `with` block, the file is closed.

Now let's print it to a new file:

```Python
with open("./hello.txt") as fin:
	contents = fin.read()
	with open("another_file.txt", "w") as fout:
		fout.write(contents)
```

Now the file "another_file.txt" will read "Hello World!". Notice that we needed to
pass the "w" flag to the `open` function to indicate that we are writing to file.


### The Internet

The internet is made up of many computers just like yours and they have their very own
languages for talking to each other, one of which you've probably heard: `HTTP`. So to
let our computer join the conversation, we just need an internet connection and a basic
understanding of `HTTP` requests and responses. For more information on `HTTP`, check
out [this article](http://www.garshol.priv.no/download/text/http-tut.html).

We will use the simple and fun `requests` library to do this. It is not built into vanilla 
Python and needs to be downloaded as a package.

In the following program we will ask Wikipedia for their page on Python:

```Python
import requests

response = requests.get("https://en.wikipedia.org/wiki/Python_(programming_language)")

if response.status_code >= 200 and response.status_code < 300:
	print(response.text)
else:
	print("Oh no! Something went horribly wrong!")
```

Here is the program step by step:

1. We import the `requests` library so that we can use it.
2. We use the `requests` library to make a `GET` request to Wikipedia's Python page.
3. Check to make sure the request was successful by making sure the response's status
code is in the 200 range.
4. Print the returned HTML


### Example Program

Here is a sample program that downloads a csv file, converts it to JSON, and writes it
out to a file. If there is something that is unfamiliar to you, look it up!

```Python
import requests
import csv
import io
import json

# The address of the CSV file
CSV_URL = "https://drive.google.com/uc?export=download&id=1fHySh9SSdM-WQgkqEQpKJWLlRRMeHf-3"

# Function Definitions
def get_csv():
	"""
		get_csv

		Attempt 10 times to fetch the csv file before terminating program.

		Return raw csv data on success
	"""
	attempts = 1
	data = None
	while data is None and attempts <= 10:
		print(">> Fetching CSV file (Attempt #" + str(attempts) + ") ...")
		r = requests.get(CSV_URL)
		status_code = r.status_code

		if status_code >= 200 and status_code < 300:
			data = r.text

		attempts += 1
	
	if data is None:
		print(">> Could not download csv file.")
		exit(1)

	print(">> CSV retreived.")
	return data


def csv_to_json(csv_data):
	"""
		csv_to_json

		Takes in csv_data and converts it to a file object. The file object
		is then converted to a csv reader to iterate elegantly over rows.

		Rows are converted to JSON objects.

		Returns JSON formatted csv data
	"""
	print(">> Converting CSV to JSON ...")
	json_data = []

	fin = io.StringIO(csv_data)
	reader = csv.reader(fin)

	# Extract headers first
	headers = reader.__next__()

	# Convert each row to JSON
	for row in reader:
		row_obj = {}
		for index, value in enumerate(headers):
			row_obj[value] = row[index]

		json_data.append(row_obj)

	# Pretty Print and return the JSON
	return json.dumps(json_data, indent=2)


# Execution starts here
csv_data = get_csv()
json_data = csv_to_json(csv_data)

print(">> Writing data to './output.json' ...")
with open("./output.json", "w") as fout:
	fout.write(json_data)

```

## Common Data Science Tools

There are a ton of common data science tools that you can draw from
when using Python. These are mostly found in the form of libraries, which are
just bundes of code that other people wrote so you don't have to. Reusability
is one of the most powerful features of programming languages, and it's how
we can build things like nueral networks on a whim.

Many languages come equipped with a package manager so that you can easily
acquire these libraries of code: Python's is called `pip`.  If you haven't
already try installing a library with it.  Example: `pip install requests`.


### Anaconda

The Anaconda Python Distribution is an open source Python distribution that
comes equipped with many of the core data science libraries that you will 
end up using.

To find out more, checkout out 
[this post](https://opensource.com/article/18/4/getting-started-anaconda-python).


### Numpy

Numpy boasts that it is "fundamental package for scientific computing with Python"
and they are pretty much right. It is a library that allows the quick and easy 
construction and manipulation of scientific data structures, notably matrices.

Find out more [here](http://www.numpy.org/).


### Pandas

Pandas is in the same ballpark as Numpy, in fact it relies on the Numpy library
for its underlying architecture, but there are differences, and some programmers
prefer one or the other. It is simply a high performance data structure and
analysis library.

Check it out [here](https://pandas.pydata.org/).


### Scikit-Learn

Scikit-Learn is an extremely accessible Python interface for machine learning
algorithms. It makes it terrifyingly easy to whip up non trivial algorithms
like Support Vector Machines and Non-negative Matrix Factorizations.

Check it out [here](http://scikit-learn.org/stable/).