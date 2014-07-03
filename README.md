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

Git branches:

1. endpoints-getting-started: complete code from the Google Developers endpoints tutorial
2. lesson2a: the "Hello Endpoints" app developed in the first half of UD859 lesson 2
3. lesson2b: the start of the "Conference Central" app in the second half of UD859 lesson 2
