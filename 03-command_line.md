# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > date - Displays current date and time  
ls - lists all files in directory  
pwd - show current directory  
cd - change directory  
mv - move  
rm - delete  
cp - copy  
touch - create file  
head - shows first 10 lines of file  
file - describes the type of text in the file  
grep - Global regular expression print, searches for text patterns in the file  
find - file name search

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > `ls`: lists all non-hidden files in directory, doesn't display any details  
`ls -a`: includes hidden files  
`ls -l`: inludes details about the files, including date, size, permissions  
`ls -lh`: changes the file sizes to more human-readable format (i.e. K, M, G for kilo, mega, giga)  
`ls -lah`: same as above except also includes hidden files  
`ls -t`: sorts by date and time modified (newest first)  
`ls -Glp`: -G removes the group ID from the list details. -p appends a / to the end of shortcut paths

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

>>  `ls -R`: Recursively lists all files  
`ls -r`: Reverses the list order  
`ls -m`: Lists files using comma separator   
`ls -S`: Sorts by file size  
`ls -g`: removes the file owner's name from the list details

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > `xargs` builds and executes command lines from the standard input. The most common example is to use it in conjunction with the `find` command. For example: `$ find . -name "*.py" | xargs rm` will find and delete all files with a .py extension.  

 

