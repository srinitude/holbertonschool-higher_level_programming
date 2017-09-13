# Almost a Circle

<img src="https://github.com/srinitude/monty/blob/master/monty.png" style="height:15%;width:15%" />

## Welcome
Thanks for visiting our project, Almost a Circle. It is entirely written in C and any reference to Python is purely accidental. Monty is a simple calculator implementing Addition, Subtraction, Multiplication, Division, and Modulo operations with simple bytecodes in a *.m file. This use of a stack (with limited features of a queue) is a basic Reverse Polish Notation calculator.

The code uses only one global variable (extern) and is highly modular. Expansion of this calculator to include more bytecode instructions or scientific functions would be fairly easy.

## Table of Contents
* [Requirements](#requirements)
* [Installation](#installation)
* [Usage](#usage)
* [Bytecode Instructions](#bytecode-instructions)
* [Credits](#credits)
* [License](#license)

## Requirements
* Ubuntu 14.04 LTS
* gcc 4.8.4 (-Wall, -Werror, -Wextra, and -pedantic flags)

## Installation
In your terminal, git clone the directory with the following command:
```
git clone https://github.com/srinitude/monty.git
```

Compile the files using:

```sh
gcc -Wall -Werror -Wextra -pedantic *.c -o monty
```

If you as a developer would like to fork our current project and create your own domain-specific monty, please give us a shout-out.

## Usage
```sh
./monty [./myFile.m]
```
where `[./myFile.m]` contains the direct path to the file containing the Monty bytecode instructions. Each file lists one instruction per line maximum. Each line is read individually and evaluated. The file can contain blank lines (empty or made of spaces only. Any additional text after the opcode or its required argument is not taken into account. If there are comments, denoted by a "#" is ignored as well.

If the Monty file contains an error, where the program cannot run or process it, the program will print an error message and exit with EXIT_FAILURE.

To start Monty at your shell prompt, type:
```sh
./monty [myFile.m]
```

An example [myFile.m] Monty file:
```push 0
push 1
push 2
  push 3
                   pall
add
pall
push 110
push 111
push 116
push 114
push 101
push 98
push 108
push 111
push 72
pstr

```

## Bytecode Instructions
The commands that you can use with Monty

| Category    | Instruction    | Description                            |
|-------------|----------------|----------------------------------------|
| Enter Data  | push (operand) | Push operand onto stack/queue          |
|             | pop            | Remove top element off stack           |
| Change Data | swap           | Swap the top two elements of the stack |
|             | rotl           | Rotate the top element to the bottom   |
|             | rotr           | Rotate the bottom element to the top   |
|             | stack          | Change to stack mode                   |
|             | queue          | Change to queue mode                   |
| Operations  | add            | Add top two operands                   |
|             | div            | Divide top two operands                |
|             | mod            | Modulo top two operands                |
|             | mul            | Multiply top two operands              |
|             | sub            | Subtract top two operands              |
|             | nop            | No operation (misnomer)                |
|             | #              | Comment (Not an operation)             |
| Output      | pall           | print all elements                     |
|             | pint           | print integer                          |
|             | pchar          | print element as a character           |
|             | pstr           | print elements as a string             |

We do check for division by zero in the div and mod functions

## Credits
Monty is owned and maintained by Kiren Srinivasan ([@srinitude](https://twitter.com/srinitude)) and Felicia Hsieh ([@feliciahsiehsw](https://twitter.com/feliciahsiehsw)). You can reply to us and to [@holbertonschool](https://twitter.com/holbertonschool) on Twitter for more updates on this project and our forked projects.

## License
Monty is released under the MIT license. See [LICENSE](https://github.com/srinitude/monty/blob/master/LICENSE) for details.