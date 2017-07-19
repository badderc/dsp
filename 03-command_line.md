# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> > 
1. pwd - print working directory
2. mkdir - create a directory
3. rm -r - removes/deletes an entire directory and all sub-directories
4. touch - creates a file in current directory
5. rm - deletes a file
6. mv filename1 filename2 - changes file name from 1 to 2 
6.5. mv filename directoryname - moves file into directoryname
7. ls -a - will list all files, including hidden ones, in current directory
8. cp filename newdirectoryname - copies a file into desired directory
9. echo stdin > desiredfile - redirects the standard output to a new file
10. cat file - outputs contents of a file to the terminal
10.1. cat file1 > file2 - places contents of file1 into file2
10.2. cat file1 >> file2 - appends file1 to file2
10.3. cat < file1 - redirects standard input to a command
11. '|' - the pipe redirects standard output of the command on the left to another command on the right
12. sort - sorts lines of file alphabetically
13. uniq - filters out duplicate, adjacent lines of text
14. grep - "global regular expression print" - search for a text pattern/output it
15. sed - searches for a text pattern, modifies it, and outputs it

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > 
1. 'ls' = list all files in the current directory
2. 'ls -a' = lists all files includig hidden files (beginning with .)
3. 'ls -l' = lists files in long form (permissions, links, owner, group, size, time, name)
4. 'ls -lh' = lists files in long form with size in easy to understand units
5. 'ls -lah' = lists all files including hidden files in long form with size units
6. 'ls -t' = sorts files by last time modified 
7. 'ls -Glp' = lists files color-coded by type and with a '/' after the name if the file is a directory

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > 
1. 'ls -m' = lists files in a comma-separated list
2. 'ls -R' = prints all sub-directories with directories
3. 'ls -1' = displays list with one file per line
4. 'ls -d' = displays only directories
5. 'ls -F' = flags file names

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > REPLACE THIS TEXT WITH YOUR RESPONSE

 

