[//]: # (DataTypes.md)

<h1>DataTypes</h1>

<h2>Numericals</h2>
<p>Numericals are a data type that represents numerical values, such as integers and floating-point numbers. In Python, numerical values are commonly used for mathematical calculations.</p>

<h3>Definition</h3>
<p>Numericals are data types in Python that store numerical values, including integers and floating-point numbers.</p>

<h3>Examples in Python</h3>

<pre><code># Integer
x = 10

# Floating-point number
y = 3.14
</code></pre>

<h2>Decimals</h2>
<p>Decimals are a data type that represent decimal numbers with a fixed number of digits after the decimal point. They provide precise decimal arithmetic in Python.</p>

<h3>Definition</h3>
<p>Decimals are a data type in Python that represents decimal numbers with a fixed number of digits after the decimal point.</p>

<h3>Examples in Python</h3>

<pre><code>from decimal import Decimal

# Decimal number
x = Decimal('3.14159')

# Perform calculations with decimals
result = x + Decimal('2.5')
</code></pre>

<h2>Complex</h2>
<p>Complex numbers are a data type that represent numbers with both real and imaginary parts. They are commonly used in mathematical and scientific calculations.</p>

<h3>Definition</h3>
<p>Complex numbers are a data type in Python that represent numbers with both real and imaginary parts.</p>

<h3>Examples in Python</h3>

<pre><code># Complex number
x = 2 + 3j

# Perform calculations with complex numbers
result = x * (1 + 2j)
</code></pre>

<h2>Sequences</h2>
<p>Sequences are data types in Python that represent ordered collections of elements. Common sequence types include lists, tuples, and strings.</p>

<h3>Definition</h3>
<p>Sequences are data types in Python that represent ordered collections of elements.</p>

<h3>Examples in Python</h3>

<pre><code># List
my_list = [1, 2, 3, 4, 5]

# Tuple
my_tuple = (1, 'a', True)

# String
my_string = "Hello, World!"
</code></pre>

<h2>Mapping Dictionary</h2>
<p>Mapping dictionaries are a data type in Python that represent a collection of key-value pairs. They allow fast lookup and retrieval of values based on their associated keys.</p>

<h3>Definition</h3>
<p>Mapping dictionaries are a data type in Python that represent a collection of key-value pairs.</p>

<h3>Examples in Python</h3>

<pre><code># Dictionary
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Accessing values by key
name = my_dict['name']

# Adding a new key-value pair
my_dict['occupation'] = 'Engineer'
</code></pre>

<h2>Set</h2>
<p>Sets are a data type in Python that represent an unordered collection of unique elements. They are useful for operations such as membership testing and removing duplicates.</p>

<h3>Definition</h3>
<p>Sets are a data type in Python that represent an unordered collection of unique elements.</p>

<h3>Examples in Python</h3>

<pre><code># Set
my_set = {1, 2, 3, 4, 5}

# Adding elements to a set
my_set.add(6)

# Removing elements from a set
my_set.remove(3)
</code></pre>

<h2>Operators</h2>
<p>Operators are symbols or keywords in Python that perform operations on one or more operands. They allow you to perform various calculations and manipulations on data.</p>

<h3>Definition</h3>
<p>Operators are symbols or keywords in Python that perform operations on one or more operands.</p>

<h3>Examples in Python</h3>

<pre><code># Addition operator
result = 2 + 3

# Subtraction operator
result = 5 - 2

# Division operator
result = 10 / 2

# Multiplication operator
result = 4 * 5

# Modulo operator
result = 10 % 3

# Exponentiation operator
result = 2 ** 3
</code></pre>

<h2>Arithmetic</h2>
<p>Arithmetic operators are a subset of operators that perform basic mathematical calculations on numerical values.</p>

<h3>Definition</h3>
<p>ArTo create separate files for each section, we can split the content into different markdown files. Here are the individual files:

**Numericals.md:**

```markdown
[//]: # (Numericals.md)

<h2>Numericals</h2>
<p>Numericals are a data type that represents numerical values, such as integers and floating-point numbers. In Python, numerical values are commonly used for mathematical calculations.</p>

<h3>Definition</h3>
<p>Numericals are data types in Python that store numerical values, including integers and floating-point numbers.</p>

<h3>Examples in Python</h3>

<pre><code># Integer
x = 10

# Floating-point number
y = 3.14



[//]: # (Decimals.md)

<h2>Decimals</h2>
<p>Decimals are a data type that represent decimal numbers with a fixed number of digits after the decimal point. They provide precise decimal arithmetic in Python.</p>

<h3>Definition</h3>
<p>Decimals are a data type in Python that represents decimal numbers with a fixed number of digits after the decimal point.</p>

<h3>Examples in Python</h3>

<pre><code>from decimal import Decimal

# Decimal number
x = Decimal('3.14159')

# Perform calculations with decimals
result = x + Decimal('2.5')
</code></pre>

[//]: # (Complex.md)

<h2>Complex</h2>
<p>Complex numbers are a data type that represent numbers with both real and imaginary parts. They are commonly used in mathematical and scientific calculations.</p>

<h3>Definition</h3>
<p>Complex numbers are a data type in Python that represent numbers with both real and imaginary parts.</p>

<h3>Examples in Python</h3>

<pre><code># Complex number
x = 2 + 3j

# Perform calculations with complex numbers
result = x * (1 + 2j)
</code></pre>

[//]: # (Sequences.md)

<h2>Sequences</h2>
<p>Sequences are data types in Python that represent ordered collections of elements. Common sequence types include lists, tuples, and strings.</p>

<h3>Definition</h3>
<p>Sequences are data types in Python that represent ordered collections of elements.</p>

<h3>Examples in Python</h3>

<pre><code># List
my_list = [1, 2, 3, 4, 5]

# Tuple
my_tuple = (1, 'a', True)

# String
my_string = "Hello, World!"
</code></pre>