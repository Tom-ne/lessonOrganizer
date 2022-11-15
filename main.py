import os
import tkinter as tk

# Creating the window
root = tk.Tk()
root.geometry("500x300")
root.title("Directory Orgenizer")

# Making input fields
year = tk.StringVar()
cemester = tk.StringVar() 
course = tk.StringVar()
lesson = tk.StringVar()

def create():
    # Making a function to create directories
    def createDirectory(path):
        # Trying to make the directory, if it alread exits, ignore error and continue
        try:
            os.mkdir(path)
        except OSError:
            pass

    # Getting entries from the inputs
    yearField = year.get()
    cemesterField = cemester.get()
    courseField = course.get()
    lessonField = lesson.get()

    # Getting the current directory
    createFrom = os.getcwd()

    # Getting paths for the lesson, course and lesson
    yearPath = os.path.join(createFrom, "year" + yearField)
    cemesterPath = os.path.join(yearPath, "C" + cemesterField)
    coursePath = os.path.join(cemesterPath, courseField)
    lessonPath = os.path.join(coursePath, "lesson" + lessonField)

    # Getting paths for homework and classwork
    homeworkPath = os.path.join(lessonPath, "homework")
    classworkPath = os.path.join(lessonPath, "classwork")

    # Adding all paths to a list
    paths = [ yearPath, cemesterPath, coursePath, lessonPath, homeworkPath, classworkPath ]

    # Creating all directories
    for path in paths:
        createDirectory(path)
    
# Adding a label and entry for year, cemester, course and lesson and adding them to the screen
yearText = tk.Label(root, text="Enter the current learning year" ,width=150).pack()
yearEntry = tk.Entry(root, width=50, textvariable=year).pack()

cemesterText = tk.Label(root, text="Enter the current cemester", width=150).pack()
cemesterEntry = tk.Entry(root, width=30, textvariable=cemester).pack()

courseText = tk.Label(root, text="Enter the course", width=150).pack()
courseEntry = tk.Entry(root, width=50, textvariable=course).pack()

lessonText = tk.Label(root, text="Enter the current lesson", width=150).pack()
lessonEntry = tk.Entry(root, width=50, textvariable=lesson).pack()

# Adding a create button to create directories
createButton = tk.Button(root, text="Create Directory", command=create).pack()


root.mainloop()
