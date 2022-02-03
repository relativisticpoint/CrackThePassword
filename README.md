# CrackThePassword
This is a fun python/golang multi-threaded program to simulate a password cracking by bruteforce
# The Python code :
to run the python code open a terminal on the folder and execute the folloxing command :
```
python2 bruteforce.py <the_password_you_want_to_crack>
```
We use a python2 interpreter because it runs exception-free, the script works with python3 as well but calls some annoyhing exceptions from the multithreading module (this is probably due to a change of support from python2 to python3 that hasn't been updated on the multithreading library..).

The program will first look into a list of common passwords and a list of common names to try and find your password, and at the same time, it bruteforces it by testing different combinations of letters and checking wether they match with your password, whichever method finds your password first will return it.

Note That: in this first version of the program, the password you pass as an argument must be lowercase and must not contain numbers nor special caracters, this will come with the following versions.

The main aim of this mini-project is to get an understanding of how complex bruteforce may get when you start dealing with longer passwords, you can try out several combinations, and you'll remark upon the fact that the longer your password gets the more time it takes for the program to crack, untill you reach a certain lenght that would make it basically impossible to bruteforce (technically it's still possible but you would have to let the program run for days/weeks/years ).

Have Fun !

