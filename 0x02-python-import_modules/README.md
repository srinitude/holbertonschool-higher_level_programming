<h1 class="gap">0x02. Python - import &amp; modules</h1>


<h4 class="task">
    0. Import a simple function from a simple file
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a program that imports the function <code>def add(a, b):</code> from the file <code>add_0.py</code> and prints the result of the addition <code>1 + 2 = 3</code></p><ul>
<li>You have to use <code>print</code> function with string format to display integers</li>
<li>You have to assign:

<ul>
<li>the value <code>1</code> to a variable called <code>a</code> </li>
<li>the value <code>2</code> to a variable called <code>b</code></li>
<li>and use those two variables as arguments when calling the functions <code>add</code> and <code>print</code></li>
</ul></li>
<li><code>a</code> and <code>b</code> must be define in 2 different lines: <code>a = 1</code> and another <code>b = 2</code></li>
<li>Your program should print: <code>&lt;a value&gt; + &lt;b value&gt; = &lt;add(a, b) value&gt;</code> followed with a new line</li>
<li>You can only use the word <code>add_0</code> once in your code</li>
<li>You are not allowed to use <code>*</code> for importing or <code>__import__</code></li>
<li>Your code should not be executed when imported</li>
</ul>


<h4 class="task">
    1. My first toolbox!
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a program that imports functions from the file <code>calculator_1.py</code>, does some Maths, and prints the result.</p><ul>
<li>Do not use the function <code>print</code> (with string format to display integers) more than 4 times </li>
<li>You have to define:

<ul>
<li>the value <code>10</code> to a variable <code>a</code></li>
<li>the value <code>5</code> to a variable <code>b</code></li>
<li>and use those two variables only, as arguments when calling functions (included <code>print</code>)</li>
</ul></li>
<li><code>a</code> and <code>b</code> must be define in 2 different lines: <code>a = 10</code> and another <code>b = 5</code></li>
<li>Your program should call each of the imported functions. See example bellow for format</li>
<li>the word <code>calculator_1</code> should be used only once in your file</li>
<li>You are not allowed to use <code>*</code> for importing or <code>__import__</code></li>
<li>Your code should not be executed when imported</li>
</ul>


<h4 class="task">
    2. How to make a script dynamic!
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a program that prints the number of and the list of its arguments.</p><ul>
<li>The output should be:

<ul>
<li>Number of argument(s) followed by <code>argument</code> (if number is one) or <code>arguments</code> (otherwise), followed by</li>
<li><code>:</code> (or <code>.</code> if no argument where passed) followed by</li>
<li>a new line, followed by (if at least one argument),</li>
<li>one line per argument:

<ul>
<li>the position of the argument (starting at <code>1</code>) followed by <code>:</code>, followed by the argument value and a new line</li>
</ul></li>
</ul></li>
<li>Your code should not be executed when imported</li>
<li>The number of elements of <code>argv</code> can be retrieved by using: <code>len(argv)</code></li>
<li>You do not have to fully understand lists yet, but imagine that <code>argv</code> can be used just like a C array: you can use an index to walk through it. There are other ways (preferred in a near Future), if you know them you can use them.</li>
</ul>


<h4 class="task">
    3. Infinite addition
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a program that prints the result of the addition of all arguments</p><ul>
<li>The output should be the result of the addition of all arguments, followed by a new line</li>
<li>You can cast arguments into integers by using <code>int()</code> (you can assume that all arguments can be casted into integers)</li>
<li>Your code should not be executed when imported</li>
</ul>


<h4 class="task">
    4. Who are you?
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a program that prints all the names defined by the compiled module <a href="/rltoken/ruwpgYfycPUr5OV3b3Dh5Q" target="_blank" title="hidden_4.pyc">hidden_4.pyc</a> (please download it locally).</p><ul>
<li>You should print one name per line, in alpha order</li>
<li>You should print only names that do <strong>not</strong> start with <code>__</code></li>
<li>Your code should not be executed when imported</li>
</ul>


<h4 class="task">
    5. Everything can be imported
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a program that imports the variable <code>a</code> from the file <code>variable_load_5.py</code> and prints its value.</p><ul>
<li>You are not allowed to use <code>*</code> for importing or <code>__import__</code></li>
<li>Your code should not be executed when imported</li>
</ul>


<h4 class="task">
    6. Build my own calculator!
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
</h4><p>Write a program that imports all functions from the file <code>calculator_1.py</code> and handles basics operations.</p><ul>
<li>Usage: <code>./100-my_calculator.py a operator b</code>
<ul>
<li>If the number of arguments is not 3, your program has to:

<ul>
<li>print <code>Usage: ./100-my_calculator.py &lt;a&gt; &lt;operator&gt; &lt;b&gt;</code> followed with a new line</li>
<li>exit with the value <code>1</code></li>
</ul></li>
<li><code>operator</code> can be: 

<ul>
<li><code>+</code> for addition</li>
<li><code>-</code> for subtraction</li>
<li><code>*</code> for multiplication</li>
<li><code>/</code> for division</li>
</ul></li>
<li>If the operator is not one of the above:

<ul>
<li>print <code>Unknown operator. Available operators: +, -, * and /</code> followed with a new line</li>
<li>exit with the value <code>1</code></li>
</ul></li>
<li>You can cast <code>a</code> and <code>b</code> into integers by using <code>int()</code> (you can assume that all arguments will be castable into integers)</li>
<li>The result should be printed like this: <code>&lt;a&gt; &lt;operator&gt; &lt;b&gt; = &lt;result&gt;</code>, followed by a new line</li>
</ul></li>
<li>You are not allowed to use <code>*</code> for importing or <code>__import__</code></li>
<li>Your code should not be executed when imported</li>
</ul>


<h4 class="task">
    7. Easy print
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
</h4><p>Write a program that prints <code>#pythoniscool</code>, followed by a new line, in the standard output.</p><ul>
<li>Your program should be maximum 2 lines long</li>
<li>You are not allowed to use <code>print</code> or <code>import sys</code> in your file <code>101-easy_print.py</code></li>
</ul>


<h4 class="task">
    8. ByteCode -&gt; Python #3
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
</h4><p>Write the Python function <code>def magic_calculation(a, b):</code> that does exactly the same as the following Python bytecode:</p>


<h4 class="task">
    9. Fast alphabet
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
</h4><p>Write a program that prints the alphabet in uppercase, followed by a new line.</p><ul>
<li>Your program should be maximum 3 lines long</li>
<li>You are not allowed to use:

<ul>
<li>any loops</li>
<li>any conditional statements</li>
<li><code>str.join()</code></li>
<li>any string literal</li>
<li>any system calls</li>
</ul></li>
</ul>

