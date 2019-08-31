# Lesson 05: Command arguments
*In this lesson you will learn how commands can be configured to make them more versatile*

## Changing the behaviour of commands
In the previous lessons you might have noticed a couple of situations in which the commands you learned were a bit restricted in their use. The `ls` command for example just prints the complete content in a list, but does not say anything about *what* each of these elements is. Another example you encountered in the exercises of the last lesson: the `cp` command can not copy folders.

If you were a Linux developer, you could of course say "well, let's make another command then. Let us call it `cpdir` and everyone will be happy". They could have absolutely done that; it would have been a completely valid solution to the problem. However: it would mean that every time you want specific behaviour of a command, you would need *another* command. This would rapidly expand the thesaurus of Linux commands, making the already inaccessible terminal even more inaccessible.

The solution that was chosen was therefore different. Instead of making new commands, the developers chose to allow the user to specify the behaviour of existing commands. This *extends* commands, instead of *creating* new ones. The down side is that every command now has to come with a manual on how to configure them, but given given that the list of available commands is now relatively shorter, this seems like the more sensible solution.

## Single dashed arguments
Although each command is free to specify how to configure it, the formatting that is chosen by most of the commands is generally the same. A command can be configured using arguments. Arguments either start with a single dash (`-`) or with double dashes (`--`). To solve for sample the problem with the copying of folders in the exercises of the previous lesson, we can add the `-r` argument, indicating that the copying has to be done *recursively*: not only the folder itself should be copied, also its contents should be.

```
cp -r folder folder_copy
```

You can input multiple arguments at the same time. The `-u` argument of `cp` copies the file only if it is newer than the file at the destination location. If we want to use both `-u` and `-r`, we could use `cp -r -u folder folder_copy`. For single dashed arguments however we can just merge the argument letters into a single argument:

```
cp -ru folder folder_copy
```

## Double dashed arguments
The downside of these single dashed arguments is that they are hard to read. What did `u` mean again? To solve this most commands also implement double dashed arguments for their single dashed arguments. These arguments are interpreted not character by character, but as a whole. The double dashed variant of `-r` is for example `--recursive`, and `-u` can also be invoked through `--update`. The previous command could just as well have been written as

```
cp --recursive --update folder folder_copy
```

Note that now that we use double dashed arguments, we can not merge them anymore. The command is however not way easier to read. You win some, you lose some.

In the next lesson we will have a look at where to find the manuals I talked about earlier, the ones that contain which arguments you can use for which commands.
