<h1 class="gap">0x05. Python - Exceptions</h1>


<h4 class="task">
    0. Safe list printing
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a function that prints <code>x</code> elements of a list.</p><ul>
<li>Prototype: <code>def safe_print_list(my_list=[], x=0):</code></li>
<li><code>my_list</code> can contain any type (integer, string, etc.)</li>
<li>All elements must be printed on the same line followed by a new line.</li>
<li><code>x</code> represents the number of elements to print</li>
<li><code>x</code> can be bigger than the length of <code>my_list</code></li>
<li>Returns the real number of elements printed</li>
<li>You have to use <code>try: / except:</code> </li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to use <code>len()</code></li>
</ul>


<h4 class="task">
    1. Safe printing of an integers list
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a function that prints an integer with <code>"{:d}".format()</code>.</p><ul>
<li>Prototype: <code>def safe_print_integer(value):</code></li>
<li><code>value</code> can be any type (integer, string, etc.)</li>
<li>The integer should be printed followed by a new line</li>
<li>Returns <code>True</code> if <code>value</code> has been correctly printed (it means the <code>value</code> is an integer)</li>
<li>Otherwise, returns <code>False</code></li>
<li>You have to use <code>try: / except:</code> </li>
<li>You have to use <code>"{:d}".format()</code> to print as integer</li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to use <code>type()</code></li>
</ul>


<h4 class="task">
    2. Print and count integers
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a function that prints the first <code>x</code> elements of a list and only integers.</p><ul>
<li>Prototype: <code>def safe_print_list_integers(my_list=[], x=0):</code></li>
<li><code>my_list</code> can contain any type (integer, string, etc.)</li>
<li>All integers have to be print in the same line followed by a new line.</li>
<li><code>x</code> represents the number of elements to access in <code>my_list</code></li>
<li><code>x</code> can be bigger than the length of <code>my_list</code></li>
<li>Returns the real number of integers printed</li>
<li>You have to use <code>try: / except:</code> </li>
<li>You have to use <code>"{:d}".format()</code> to print an integer</li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to use <code>len()</code></li>
</ul>


<h4 class="task">
    3. Integers division with debug
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a function that divides 2 integers and prints the result.</p><ul>
<li>Prototype: <code>def safe_print_division(a, b):</code></li>
<li>You can assume that <code>a</code> and <code>b</code> are integers</li>
<li>The result of the division should print in the <code>finally:</code> section preceded by <code>Inside result:</code></li>
<li>Returns the value of the division, otherwise: <code>None</code></li>
<li>You have to use <code>try: / except: / finally:</code> </li>
<li>You have to use <code>"{}".format()</code> to print the result</li>
<li>You are not allowed to import any module</li>
</ul>


<h4 class="task">
    4. Divide a list
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a function that divides element by element 2 lists.</p><ul>
<li>Prototype: <code>def list_division(my_list_1, my_list_2, list_length):</code></li>
<li><code>my_list_1</code> and <code>my_list_2</code> can contain any type (integer, string, etc.)</li>
<li><code>list_length</code> can be bigger than the length of both lists</li>
<li>Returns a new list (length = <code>list_length</code>) with all divisions</li>
<li>If 2 elements can’t be divided, the division result should be equal to <code>0</code></li>
<li>If an element is not an integer or float:

<ul>
<li>print: <code>wrong type</code></li>
</ul></li>
<li>If the division can’t be done (<code>/0</code>):

<ul>
<li>print: <code>division by 0</code></li>
</ul></li>
<li>If <code>my_list_1</code> or <code>my_list_2</code> is too short

<ul>
<li>print: <code>out of range</code></li>
</ul></li>
<li>You have to use <code>try: / except: / finally:</code> </li>
<li>You are not allowed to import any module</li>
</ul>


<h4 class="task">
    5. Raise exception
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a function that raises a type exception.</p><ul>
<li>Prototype: <code>def raise_exception():</code></li>
<li>You are not allowed to import any module</li>
</ul>


<h4 class="task">
    6. Raise a message
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a function that raises a name exception with a message.</p><ul>
<li>Prototype: <code>def raise_exception_msg(message=""):</code></li>
<li>You are not allowed to import any module</li>
</ul>


<h4 class="task">
    7. Safe integer print with error message
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
</h4><p>Write a function that prints an integer.</p><ul>
<li>Prototype: <code>def safe_print_integer_err(value):</code></li>
<li><code>value</code> can be any type (integer, string, etc.)</li>
<li>The integer should be printed followed by a new line</li>
<li>Returns <code>True</code> if <code>value</code> has been correctly printed (it means the <code>value</code> is an integer)</li>
<li>Otherwise, returns <code>False</code> and prints in <code>stderr</code> the error precede by <code>Exception:</code></li>
<li>You have to use <code>try: / except:</code> </li>
<li>You have to use <code>"{:d}".format()</code> to print as integer</li>
<li>You are not allowed to use <code>type()</code></li>
</ul>


<h4 class="task">
    8. Safe function
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
</h4><p>Write a function that executes a function safely.  </p><ul>
<li>Prototype: <code>def safe_function(fct, *args):</code></li>
<li>You can assume <code>fct</code> will be always a pointer to a function</li>
<li>Returns the result of the function,</li>
<li>Otherwise, returns <code>None</code> if something happens during the function and prints in <code>stderr</code> the error precede by <code>Exception:</code></li>
<li>You have to use <code>try: / except:</code> </li>
</ul>


<h4 class="task">
    9. ByteCode -&gt; Python #4
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
</h4><p>Write the Python function <code>def magic_calculation(a, b):</code> that does exactly the same as the following Python bytecode:</p>


<h4 class="task">
    10. CPython #2: PyFloatObject
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
</h4><p>Create three C functions that print some basic info about Python lists, Python bytes an Python float objects.<br/>
<br/>
<img alt="Gif" src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/245/giphy-2.gif">
<br/>
Python lists:</img></p><ul>
<li>Prototype: <code>void print_python_list(PyObject *p);</code></li>
<li>Format: see example</li>
<li>If <code>p</code> is not a valid <code>PyListObject</code>, print an error message (see example)</li>
</ul><p>Python bytes:</p><ul>
<li>Prototype: <code>void print_python_bytes(PyObject *p);</code></li>
<li>Format: see example</li>
<li>Line “first X bytes”: print a maximum of 10 bytes</li>
<li>If <code>p</code> is not a valid <code>PyBytesObject</code>, print an error message (see example)</li>
</ul><p>Python float:</p><ul>
<li>Prototype: <code>void print_python_float(PyObject *p);</code></li>
<li>Format: see example</li>
<li>If <code>p</code> is not a valid <code>PyFloatObject</code>, print an error message (see example)</li>
<li>Read <code>/usr/include/python3.4/floatobject.h</code></li>
</ul><p>About:</p><ul>
<li>Python version: 3.4</li>
<li>You are allowed to use the C standard library</li>
<li>Your shared library will be compiled with this command line: <code>gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 103-python.c</code></li>
<li>You are not allowed to use the following macros/functions:

<ul>
<li><code>Py_SIZE</code></li>
<li><code>Py_TYPE</code></li>
<li><code>PyList_Size</code></li>
<li><code>PyList_GetItem</code></li>
<li><code>PyBytes_AS_STRING</code></li>
<li><code>PyBytes_GET_SIZE</code></li>
<li><code>PyBytes_AsString</code></li>
<li><code>PyFloat_AS_DOUBLE</code></li>
<li><code>PySequence_GetItem</code></li>
<li><code>PySequence_Fast_GET_SIZE</code></li>
<li><code>PySequence_Fast_GET_ITEM</code></li>
<li><code>PySequence_ITEM</code></li>
<li><code>PySequence_Fast_ITEMS</code></li>
</ul></li>
</ul><p><strong>NOTE</strong>:</p><ul>
<li>The python script will be launched using the <code>-u</code> option (Force <code>stdout</code> to be unbuffered).</li>
<li>It is <strong>strongly</strong> advised to either use <code>setbuf(stdout, NULL);</code> or <code>fflush(stdout)</code> in your C functions IF you choose to use <code>printf</code>. The reason to that is that Python<code>s</code>print<code>and libC</code>s <code>printf</code> don’t share the same buffer, and the output can appear disordered.</li>
</ul>

