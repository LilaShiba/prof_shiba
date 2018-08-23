# Hello and welcome to year one IBCS!

Here is your user documentation for the first lesson. This guide will take you through the steps of setting up a developers environment. Make sure your are familiar with the following terms:

- [what is user documentation](http://www.teach-ict.com/as_a2_ict_new/ocr/A2_G063/331_systems_cycle/slc_stages/miniweb/pg20.htm)
- [what is a developers environment](https://en.wikipedia.org/wiki/Deployment_environment)
- [IDE](https://computersciencewiki.org/index.php/IDE)
- [package manager](https://en.wikipedia.org/wiki/Package_manager)
- [version control](https://whatis.techtarget.com/definition/version-control)
- [object-oriented programming](https://computersciencewiki.org/index.php/Object-Oriented_Programming)
- [terminal](https://www.quora.com/In-coding-terms-what-is-a-terminal-and-what-is-it-used-for)
- slack
- gitlab


## Slack: Sign up for and download slack.

This is how you will get class notes and todos. Slack is basically taking all the good parts of email and leaving the bad parts behind

- [slack](https://slack.com/signin)

our team name is xxxxxxx

### If you have questions:

In slack, there is a channel called q&a. You can post and answer questions here. I will also check this channel everyday, giving help as needed.

## Download Atom:

This will be your IDE for the course. The terminal is where you will run your code.

- [atom](https://atom.io/)
- enable teletype
- file-icons
- and your own theme


## Download homebrew:
This is your package manager. Basically, it is an easy way to download software, stay updated, and manage dependencies.
- [brew](https://brew.sh/)

## Install Oh-my-zsh:
- [oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh)
- check out a few plugins you want to use

## Install python3 with brew
``` bash
brew install python
```

## Make sure ruby is up to date
```bash
brew install ruby
```

## Create a GitHub account
Make sure you keep it professional. This is how the whole programming world will know you
- [github](https://github.com/)


# Project Initium
What is IBCS? Well, it is meant to teach you about hardware, software, networks, programming, the design cycle, version control, etc. There is a ton of material. So, being organized is key.


The first goal of this lesson is to ensure organization. The second goal is to acquaint you with a project-based class. The final goal is to introduce you to managing ambiguity, meaning often times, you will feel lost, confused, and overwhelmed. This is completely normal. All you need to do is accept that this is normal and try your best!

Please email me with any questions or if you get stuck! I will be around campus until August.

## Course Norms:
Every time you write a program, the following will be expected:

- All programs must have comments explaining what your code is doing
- After each program, I will ask you to explain your work in a short paragraph (3-5 sentences)

## Exams
You will only have two tests this year. A midterm and a final. The exams carry a large weight of your grade and will be built up to in the course.


## Part One: Terminal Commands
Create the following file structure in a dir on your desktop called year_one_ibcs. Complete this task using the terminal. If you don't know what a terminal is our any terminal commands, no worries. That is the goal of this project! The first link goes deep into what/how. The second link will get you to where you need to be. It's the tl;dr version.

[learn terminal 1](https://www.learnenough.com/command-line-tutorial)
[learn terminal 2](http://www.cs.virginia.edu/diochnos/tips/terminal/basics.html)

In order to create part one, you'll need to know how to:

- navigate in the terminal  		(cd)
- create folders					(mkdir)
- create files 						(touch)
- remove folders/files      		(rm)
- run a ruby and python program
- what a file path is

These are the basic building blocks of the course.

## Warning: With great power comes great responsibility
- Deleting files/folders in the terminal is a bad idea.
- Dont do anything in the terminal you are unsure about!!!
- Never copy and paste in the terminal!

### Directories at the root level:
Once you have learned enough terminal to be dangerous, make the following file structure:
- unit_0
- unit_1
- unit_2
- unit_3
- unit_4
- oop
- adt
- api
- networks
- control
- extras

These are all the topics covered in year one

### Directories within each unit
All directories need the following two folders and one file inside of them
- programming
- projects
- readme.md


## Part Two: User Documentation

Learn to use [markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) and create a bio in unit_0/readme.md. You can fill with any information you like. Just make sure to include:

- what you want out of the class
- experience level
- some sort of picture
- a snippet of code that stands out to you (not too long!)

## Part Three: Hello World
On the first day of class, you will be asked to run your hello_world program as your introduction to the class. Hello world is a programming tradition when learning a new language. For your hello world, you will print out a few strings from your bio.

A string is a form of datatype in programming, which is composed of a sequence of characters. Think ""

#### How-to
In unit_0/programming create a file called hello_world. If you want to use ruby add .rb to the end of the file, and if you want to use python use .py at the end of the file. The extension lets the computer know what language to expect.

Example:

ruby: file path => unit_0/programming/hello_world.rb
```ruby
puts "Hello, I'm Mr. James and I'm from Chicago and loves dogs"
puts "Machine learning is my hobby, and I one day want to live on Mars"
```

python: file path => unit_0/programming/hello_world.py
```python3
print("Hello, I'm Mr. James and I'm from Chicago and loves dogs")
print("Machine learning is my hobby, and I one day want to live on Mars")
```

To run the program, navigate your terminal to the same dir level. Type ls in the terminal. You should see your program.

```bash
ls
hello_world.py hello_world.rb
```

If using ruby

```ruby
ruby hello_world.rb
```

If using python

```python3
python3 hello_world.py
```

Your terminal should now show the strings you have programmed. Congrats!!!

#### Debug
The terminal will give you clues as to why your program isn't working. For this program, if you are having trouble, check to make sure

- you saved the program
- you have the right file path when running the program

## Policies

- Life happens, if you are going to turn work in late I need an email 48 hours before the work is due asking for an extension.

- Office hours are a real thing! Many students will need to take advantage of this during the year

- If you need a letter of reference, allow at least seven days for completion


# Programming Boot Camp

**Goal**: By the end of this boot camp you will know the basics of programming, the current debates in comp sci, your role in your company, and have three ideas for what your startup will do or create.

**Method** Your group will hone in on one type of technology: hands on building with hardware, backend programming, or visual programming. You will then create a startup that has a product or service that changes the way we view and interact with the world

**What is Programming?**

"Television shows and films often show programmers furiously typing cryptic streams of 1s and 0s on glowing screens, but modern programming isn’t that mysterious. Programming is simply the act of entering instructions for the computer to perform. These instructions might crunch some numbers, modify text, look up information in files, or communicate with other computers over the Internet."

- This [source](https://automatetheboringstuff.com/chapter0/) will be the greatest help for this unit

**Language**:
Python is the recommended language for the following reasons: 
- [reason one](https://stackoverflow.blog/2017/09/14/python-growing-quickly/) 
- [reason two](https://stackoverflow.blog/2017/09/06/incredible-growth-python/). 

You may, however, use [p5js](https://p5js.org/). P5js is best suited for those who wish to visualize (art people looking at you). Please see the teacher if you wish to use p5js.

If you wish to create [tech-fashion](https://learn.adafruit.com/sparkle-skirt/overview) you will have to follow the circuit playground guides. The syntax is much harder, but a great choice if you want to build with your hands.

Take time now to pick a language to use. Read through the sources given and give credence for your choice.


# Playlist Overview for Startup Boot Camp

| Goal                                        | Method         
| --------------------------------------------|------------------------------------------------------------------------------
| Make how-to guides for programs 0 and 1     | [check list](https://github.com/kyle1james/9th_grade_boot_camp/blob/master/how_to_things.md)
| Complete lab 0                              | [Lab 0](https://github.com/kyle1james/9th_grade_boot_camp/tree/master/0#programming-101) Design, program, and comment your own unique programs
| Complete lab 1                              | [Lab 1](https://github.com/kyle1james/9th_grade_boot_camp/tree/master/1#data-structures-and-methods) Design, program, and comment your own unique programs
| Daily Ideas and Tasks                       | [Who did what](https://github.com/kyle1james/9th_grade_boot_camp/blob/master/how_to_things.md#daily-ideas-and-tasks) and any ideas you have for your startup

# Links:

| What                                        | Link         
| --------------------------------------------|------------------------------------------------------------------------------
| Mr. James meeting sign up                   | [link]("#")
| Python FAQ                                  | [link]("#")
| P5JS FAQ                                    | [link]("#")
| Circuit Playground FAQ                      | [link]("#")



### How to Run a Program
[more on how to run a program](http://bfy.tw/JUTI). This is a key skill for programmers.

![file path pic](https://github.com/kyle1james/9th_grade_boot_camp/blob/master/0/filepath.png)

[p5js run a program](https://p5js.org/get-started/)


**File Path**
A path, the general form of the name of a file or directory, specifies a unique location in a file system. A path points to a file system location by following the directory tree hierarchy expressed in a string of characters in which path components, separated by a delimiting character, represent each directory. The delimiting character is most commonly the slash ("/"), the backslash character ("\"), or colon (":")

- [learn more about file paths](https://automatetheboringstuff.com/chapter8/)


### Variables
Variables are used to store information to be referenced and manipulated in a computer program. They also provide a way of labeling data with a descriptive name, so our programs can be understood more clearly by the reader and ourselves. It is helpful to think of variables as containers that hold information. Their sole purpose is to label and store data in memory. This data can then be used throughout your program. [source](https://launchschool.com/books/ruby/read/variables)

Typically, a program consists of instruction s that tell the computer what to do and data that the program uses when it is running

### Assigning Value to Variables
There are four primary data types in programming:

| Data type     | Example       | Assigning    |
| ------------- |:-------------:| ------------:|
| int           | 110           | a = 30       |
| float         | 110.010101    | a = 1.0101   |
| boolean       | True or False | tacos = true |
| string        | "words"       | hi = 'hello' |

In computer science and computer programming, a data type or simply type is a classification of data which tells the compiler or interpreter how the programmer intends to use the data. [source](https://en.wikipedia.org/wiki/Data_type)

### Control Flow

In computer science, control flow (or flow of control) is the order in which individual statements, instructions or function calls of an imperative program are executed or evaluated. 

- [source](https://en.wikipedia.org/wiki/Control_flow)

#### Diagram of Control Flow
A flowchart is a type of diagram that represents an algorithm, workflow or process, showing the steps as boxes of various kinds, and their order by connecting them with arrows. This diagrammatic representation illustrates a solution model to a given problem.

- [learn more about flow charts](https://www.lucidchart.com/pages/what-is-a-flowchart-tutorial)

![pic](https://pics.astrologymemes.com/dmk-fire-safety-flowchart-stop-thats-how-ruff-ryders-roll-26553683.png)

### Types of Control Flow
There are many ways to control your program. Here, we will go over the most commonly used. It is important to remember that there are many ways to write a program, however, we will seek for the best.

### Choice: If/Else statements
![pic1](https://i.imgur.com/xNWld3g.jpg)

The if statement checks for a condition and executes the proceeding statement or set of statements if the condition is 'true'.

```python
# assign an int to a variable called a
a = 5

# begin choice control flow
if a > 10:
  print("I'm greater than 10")
elif a < 0:
  print("I am in the red")
# you can have endless elif statements
else:
  print("I am smaller than 10")
  
```
### Circuit Playground Setup 
If you are working with the Circuit Playground, detour to the link below from here.
- [set up circuit playground](https://github.com/kyle1james/led_art_example/tree/master/circuit_playground)

### Operators
When controlling how a program runs, operators help define conditionals. If x > 10, if y == x, etc.

#### Relational Operator
Operator     | Meaning 
------------ | ------------
x == y | (x is equal to y)
x != y | (x is not equal to y)
x <  y | (x is less than y)
x >  y | (x is greater than y)
x <= y | (x is less than or equal to y)
x >= y | (x is greater than or equal to y)


#### Arithmetic Operator

Operator     | Meaning 
------------ | ------------
x + y  | Adds values on either side of the operator
x - y  | Subtracts right hand operand from left hand operand
x * y  | Multiplies values on either side of the operator
x / y  | Divides left hand operand by right hand operand
x % y  | Modulus Divides left hand operand by right hand operand and returns remainder
x ** y | Performs exponential (power) calculation on operators


### Loops
A loop is a way to repeat a portion of code until a condition is met. For example, imagine having to read through a 1000 page expense report to find all costs above $10,000. A loop could do that for you. Or what if you had to make 1000 tacos? A loop could do that too.

![pic2](https://res.cloudinary.com/teepublic/image/private/s--MmSBmzkg--/t_Preview/b_rgb:262c3a,c_lpad,f_jpg,h_630,q_90,w_1200/v1496757724/production/designs/1649527_1.jpg)


```python
# go through every element in num, which will be called x, and print if it is even

for x in num:
  if x % 2 == 0:
    print(x, " is even")
  else:
    print(x, " is odd")
    
```
in this example x is the iterator. That is the variable which changes value. Meaning, if I have a list = [1,2,3,4] x will first equal 1, then the program will check if 1 is even or odd, and print the result. Then x will equal 2, etc...


```python

n = 0
count = 99

while count < n:
 print(count, "bottles of coke on the wall")
  count = count - 1

```
# What is an Algorithm?
[source](http://www.bbc.co.uk/guides/z3whpv4)

An algorithm is a list of rules to follow in order to solve a problem.

Algorithms need to have their steps in the right order. Think about an algorithm for getting dressed in the morning. What if you put on your coat before your jumper? Your jumper would be on top of your coat and that would be silly! When you write an algorithm the order of the instructions is very important.
