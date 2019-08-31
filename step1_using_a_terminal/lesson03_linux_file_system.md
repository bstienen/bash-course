# Lesson 03: Linux file system
*In this lesson you will learn about the folders in the root directory of the Linux filesystem and about hidden files*

## The folders in the root directory
Let us go to the root directory for a moment. If we list the content of this directory we see a whole list of directories with names you might have never heard of. In normal daily use you will probably never encounter these folders, but for more complicated operations a bit of understanding about these folders might go a long way.

Before we start: you probably don't have the right permissions to write to or alter the folders in the root directory. Don't worry about fudging things up: you are probably not allowed to by the system. Nevertheless: be aware that if you are ever in the situation that you *do* have the proper permissions, that you can wreck your entire system.

**`/bin`**: Basic programs like `ls` are stored here as binary files (hence the name `bin`, a shortened version of *binary*).
**`/boot`**: When you start your computer, it is not the operating system that is started initially, but the motherboard itself. The motherboard then calls the programs on your hard drive that start the right program to start the operating system. This program is called the *boot loader* and is located in this folder.
**`/cdrom`**: If your computer has a CD-rom drive, any CD-rom you put in your machine can be accessed in this folder.
**`/dev`**: A bit of a weird story, but *everything* in Linux is technically a file. Not only files and folders, but also all devices you link to your computer: webcams, keyboards and mice included. As a normal user you can immediately forget this information again, but if you want to have a look: every file in this folder is one of the linked devices.
**`/etc`**: This folder contains all configurations that have to be applied system wide, regardless of the user.
**`/home`**: As seen in the previous lesson, this folder contains the home directory of all the users.
**`/lib`**, **`/lib64`**, **`/lib32`**: When you write a computer program, you very seldomly write all your code on your own. More often then not you use functions written by other people. These functions are stored in library files. To use them, you just have to write code like "hey computer, i want to use that library *over there*". The `/lib*` folders collect all libraries that programs could need.
**`/mnt`**, **`/media`**: If you link an external storage to your machine (including mobile phones) and want to access it, you need to *mount* it. This is just slang for "making is accessible". In Ubuntu this is nowadays automatically done to the `/media` folder. If you ever mount a drive by yourself, you are expected to do this to the `/mnt` folder.
**`/opt`**: Folder to store manually installed software.
**`/proc`**: Running programs are called *processes*. Processes can need storage. Files associated with processes are stored here by process ID.
**`/root`**: The home directory of the *root user*: the user with no restrictions in the system.
**`/run`**: Stores information about the current session of the system. Any information here will be removed at reboot.
**`/sbin`**: Basically the same as `/bin`, but these programs can only be used by users with super user rights (like the root user).
**`/scratch`**: Location to store files. These files will not be subjected to backups and are bound to the machine.
**`/snap`**: Location where so called *snap packages* are installed. 
**`/srv`**: If you set up your system with a server functionality, the `/srv` folder will in general be used as the entry point for external users.
**`/sys`**: Stores files to interface to the kernel. In laymen terms: software needs information to work with the hardware of your computer. This information is stored here.
**`/tmp`**: Files and folders stored in this folder are removed when the system is rebooted. If you need to store a file but want to have it removed after you used it, this is a nice location to put it. Be however aware that every user can access this folder and its contents.
**`/usr`**: Like `/etc`, but the information here is only applied on specific users.
**`/var`**: Variable directory. Basically this is a location location for files that are expected to grow over time, like logs and crash reports.

## Hidden files
A last point that I want to make about the Linux file system before we continue to learn more terminal commands is that not all files are visible by default. Files and folders with a name starting with a dot (e.g. `.hiddenfile`) are so-called *hidden files*. These are mostly used to store configurations or to store files needed for bookkeeping.

## Exercises
1. In a couple of lessons we will see how we can make hidden files visible in the terminal. For now you can just start a file explorer window. Navigate to your home directory. If you press `CTRL+H` the hidden files are shown alongside the not-hidden files (you can press this key combination again to hide them again). Can you identify the source of some of the hidden files?
