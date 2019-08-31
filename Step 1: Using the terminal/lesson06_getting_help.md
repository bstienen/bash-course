# Lesson 06: Getting help
*In this lesson you will learn where to find information about commands and their arguments*

## Command types
Commands come in different shapes and sizes, but also in different types. Which type of command is in general not incredibly important: the only thing that matters is that is does what it is supposed to do. When you want to know more about the command, the type of the command suddenly becomes important however.

To find the type of the command, you can use the `type` command, followed by the command you want to know the type of. The following type command for example

```
type cd
```

shows that `cd` is a `shell builtin` command. On the other hand, if we check the type of `ls`, we get back that it is an executable program located in `/bin`. There are four types that commands can be:

- An executable program (like `ls`)
- A command that is builtin into the shell (like `cd`)
- A shell function (you will probably not encounter these)
- An alias (we will get back to these in the last lesson of this course)

## Getting help on shell builtin commands
If you encounter a shell builtin that you want to know more about, you need to use the `help` command, followed by that command. For example:

```
help cd
```

The text that is shown outlines what the command does, how to use it and which options (or arguments as we called them earlier).

## Getting help on executable programs
For executable programs such help pages do not exist, but most of these programs *do* have manual pages. You can open these with the `man` command, followed by the command you want the manual of.

```
man ls
```

Many programs also implement access to their manual through the `-h` and/or `--help` arguments. How to access the manual for a specific command is however command specific, so it might take some trial and error.

### Searching for executable programs
Imagine the following situation: you know you want to see a list of all processes on your computer (similar to the task manager on Windows), but are so charmed by idea of a terminal that you want to know if such a functionality is available in the terminal. To perform a search for commands, the `apropos` command can be used, followed by a keyword on which you want to base your search. The following search

```
apropos processes
```

results on my computer for example in a list that ends with

```
...
renice (1)              - alter priority of running processes
snmpa_supervisor (3erl) - A supervisor for the SNMP agent Processes
top (1)                 - display Linux processes
XmUpdateDisplay (3)     - A function that processes all pending exposure events immediately "XmUpdateDisplay"
```

The `top` command seems to be exactly what we were looking for! The text behind the command is a short, one line description of the command. It is taken from the manual. If you are only interested in this specific message (for example if you want to check if you indeed have the command you think you have), the `whatis` command can be used.

```
whatis pwd
```

will for example result in

```
pwd (1)              - print name of current/working directory
```

## Exercises
1. List all files in your home directory, *including* the hidden files
2. List all files in your home directory in a listing format
3. Combine the previous exercises in a single command
4. The `python` command is the program that runs your python code. Print the version of your python program.
5. `htop` is an improved version of `top`. It however did not turn up when running the `apropos processes` command. Why not?
6. Find or create a file with 20 lines of text (note that there should therefore be at least 19 enters in your file). The `head` command outputs the top of the file to the terminal. Output the first 4 lines.
7. Use the `whatis` and `apropos` commands to find a command that prints the bottom of the file. Use it to output the last 7 lines.
