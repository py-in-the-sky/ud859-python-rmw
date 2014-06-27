Python version of the Java project in Udacity's UD859 course.

To "rehydrate" this project on OSX after cloning, do the following in the command line:

1. navigate to the project directory
2. create a virtual environment named "venv":   $ virtualenv venv
3. activate the virtual environment:            $ source venv/bin/activate
4. pip install the dependencies:                $ pip install -r requirements.txt

The original project used folders (e.g., "Lesson_2", "Lesson_3") to separate the stages
in the development of the full application.  This project uses branches instead.  In
order to get lesson 2's version, for example, type "git checkout lesson-2" at the
command line; to get the final version, type "git checkout conference-central-complete"
at the command line.
