# EXAM: Python Basics

### Getting Started
 - Fork this repository under your own account
 - Clone the forked repository to your computer
 - Commit your progress frequently and with descriptive commit messages
 - All your answers and solutions should go in this repository

### What can I use?
- You can use any resource online, but **please work individually**
- **Don't just copy-paste** your answers and solutions, use your own words instead.


# Tasks
## 1-5. Complete the tasks seen in the first-fifth.py files! (~120 mins)
### Acceptance criteria
The application is accepted if:
- The solution works according to specification [1p each]
- Has proper error handling where the specification says it [1p each]
- Has the correct loops, methods, filters [1p each]
- The code is clean, without unnecessary repetition, and with descriptive names [1p each]
- You commit frequently, after each task, with descriptive commit messages [1p]
- The solution follows [styleguide](https://github.com/greenfox-academy/teaching-materials/blob/master/styleguide/python.md) [1p]

## 6. Question time! (~30 mins) [6p]

### Explain the algorithm seen in `third.py`. Use a flowchart, structogram or pseudo code. [2p]
#### Your answer:
    *pseudo code*

    function takes 2 parameters(first par.: where second par parameter is being searched,
                                second par.: a character, what is searched in the first parameter)

    checking the first parameter if it's a string:
      - if not: return 0

    initializing the count variable to zero (it represents the number matches of second parameter in first parameter)

    starting a loop which goes trough all off the characters in given string (first parameter):
       - if the actual character is equal to the given character (second parameter):
            - increment the count variable
       - if there is no more characters in the string:
            - end of the loop
       - otherwise continue the loop

    at the end return the count variable

### How can you create a graphical user interface and draw a rectangle on it in python? What are the tools needed for it? [2p]
#### Your answer:

    First, the tkinter gui package must be imported.
    Then a Tk() object and a Canvas() object must be created (its main arguments are the width and height). The canvas object must be packed into its parent object, which is the Tk() object.
    To draw rectangle a method must be called on the canvas named create_rectangle().
    The main argument of this methods are 4 parameters, representing the two coordinates of the upper left and the lower right corner of the rectangle). With the fill option we can color the rectangle.

### What does V stand for in MVC? [2p]
#### Your answer:

    V stands for the View component in the MVC design pattern. It's used for displaying the data and the information received from the controller (which received it from the model). It displays the data in a suitable way for interaction, but the interaction is controlled by the controller.
