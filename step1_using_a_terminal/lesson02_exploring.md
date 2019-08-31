# Lesson 02: Exploring
*In this lesson you will learn how to navigate through folders and what the difference is between absolute and relative paths*

## So.. where are you?
When you open a file explorer window, you will immediately see the contents of the folder you have opened. Anything you do in that window you do to that folder and its contents. The terminal works similarly: when you open a terminal, it by default opens your `home` directory. In contrast however to the file explorer window you don't see the contents of the folder immediately.

And with that observation we will now learn one of the most used commands in whole of bash: the command to `list` the current folder's contents. The command is:

```
ls
```

Enter the command in your terminal and see that indeed the content of your home directory is printed to the terminal. The files and folders you see here are the ones you have immediately access to: you don't need to move directory to open or delete them, just as in a file explorer window. Again, in contrast to a file explorer window you can not just double click a folder to move there.

## Moving and relative paths
To change directories in a terminal you need the `change directory` (`cd`) command. If you want to move to the Downloads folder for example, you can type

```
cd Downloads
```

Do this and verify (with the `ls` command) that you are indeed now in the Downloads folder. The path we gave the `cd` command is called a *relative path*: a path that is defined relative to the directory in which we already were. We were in the home directory; Home contains Downloads; so if we say "Go to Downloads" the system knows which folder to move to. Home also contains a folder called Documents. We currently are however not in Home, but in Downloads. We can therefore not simply say:

```
cd Documents
```

We first have to move back to the home directory. To go back to the parent folder (i.e. the folder that contains the folder you are currently in), you can use the `parent directory` indicator: `..`.

```
cd ..
```

Using this command moves you back to your home directory, and from there you can go to Documents with the `cd Documents` command. Alternatively we could have also combined these two commands in a single one:

```
cd ../Documents
```

Using relative paths you want move from anywhere in the system to any other location in the system, as long as you know which folders you pass on your way.

## Auto complete and <TAB>
Using a terminal requires quite some typing, as you might have already noticed if you were typing along. This typing can however be alleviated by the auto complete function of the terminal. By pressing the `<TAB>` button the terminal tries to automatically complete the command or location you were typing. If you have typed `cd Docume` and then press `<TAB>`, the command will (most likely) be completed to `cd Documents`. If however you typed `cd D` the terminal will not be able to complete your command: it does not know if you meant `Documents` or `Downloads` (or alternatively any other file or folder starting with a 'D'). Double pressing `<TAB>` shows you all options to complete the command.

## Absolute paths
Using only relative paths can become confusion rather fast. In order to use them correctly you need to know at every moment *where* you are in the system. It would be nice if we were able to have an absolute reference, a foundation from where we can reference to any file or location in the system.

There are two such absolute locations in the system. The first one is your home directory. If you just type `cd` without any location, the command will actually send you directly to your home directory. Alternatively you can use the special symbol `~`: `cd ~` will send you to your home directory as well. The use of the tilde has as advantage that you can chain it directly with folders in your home directory. To move to the Downloads folder, regardless of where you are in your folder structure, you can use

```
cd ~/Downloads
```

For daily use the absolute reference to your home folder is a perfectly fine as a way of defining absolute paths. For more complicated operations however (like operations that span different user accounts or operations that make use of folders outside of your home folder) a more *absolute* absolute path definition would be useful: one that is not dependent on your home directory.

The absolute path definition we are looking for is the definition with respect to the *root directory*. This is the directory that contains *everything* in the system and can be compared to `C:\` in Windows. The location of this directory is just `/`. Let us move there.

```
cd /
```

From the root directory we can access *any* file in the system. To go to your home directory for example, using the absolute path definition, we can use

```
cd /home/username
```

where you replace `username` with your own username of course.

Let us go back to the root directory for a moment. If we list the content of this directory we see a whole list of directories with names you might have never heard of. In normal daily use you will probably never encounter these folders, but for completeness we will have a look at them in the next lesson.

---
## Exercises
1. Try to use **relative** paths to go to the following paths:
  - `/home/username/Pictures`
  - `/tmp`
  - `/home/username/Desktop`
  - `/var`
