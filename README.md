# Code for Sysadmin Show Podcast

Code for interview 30 April 2020 with Dustin Reybrouck for https://sysadminshow.com/about/.

I will attempt to explain why Python is a better choice than bash for many coding tasks.
As an exercise, I will show a bash implementation of the `head` command and how we might better write it in Python.

In the interview, I mentioned a couple of Python programs that I use to create new programs:

* `new_bash.py`: in the `sh-head` directory is a Python program I used to stub out the `head.sh` program
* `new.py`: in the `py-head` directory is the Python program I used to create the `head.py` program

Much of our discussion centered on how the `new.py` program creates a Python program with functions and uses the `argparse` module to define and document the program's parameters.
We also discussed the `test.py` program which uses the `pytest` module/program to run a test suite on both the `head.sh` and `head.py` programs.

Finally, we discussed the use of `make` and `Makefile` to document and automate the running of tests and shortcuts and commands and such.
I mentioned another tutorial I wrote here:

https://github.com/kyclark/make-tutorial

All of these ideas are discussed in greater detail in _Tiny Python Projects_ available now from Manning.

# Links

* [Tiny Python Projects](https://www.manning.com/books/tiny-python-projects?a_aid=youens&a_bid=b6485d52)
* https://github.com/kyclark/tiny_python_projects
* [YouTube videos](https://www.youtube.com/user/kyclark)

# Author

Ken Youens-Clark <kyclark@gmail.com>

* [@kycl4rk](https://twitter.com/kycl4rk)
* [LinkedIn](https://www.linkedin.com/in/kycl4rk/)
