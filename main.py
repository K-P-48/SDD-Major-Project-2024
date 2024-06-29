import tkinter as tk
import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
from PIL import Image
import random
import os, sys

LARGEFONT = ("Inter", 80, 'bold')

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

## Exercise List & Categories ##

# All exercises
exc = [
    "Bench Press", "Squat", "Deadlift", "BB Row", "Leg Press", "Leg Curl", "Romanian Deadlift", "BB Overhead Press", "Incline DB Press", "Machine Chest Press", "Chest Fly", "Chest Dips", "Lat Pulldown", "DB Row", "Pull Up", "Rack Pull", "Cable Row", 
    "JM Press", "Tricep Extension", "Tricep Dips", "Skull Crusher", "DB Curl", "BB Curl", "Preacher Curl", "Hammer Curl", "Shoulder Press Machine", "DB Overhead Press", "Leg Extension", "Lunge", "DB Split Squat", "DB Romanian Deadlift", "Seated Calf Raises", "Standing calf Raises"
    ]

# Strength
s = ["Bench Press", "Squat", "Deadlift"]

# Strength - Back
sb = ["BB Row"]

# Strength - Legs
sl = ["Leg Press", "Leg Curl", "Romanian Deadlift"]

# Strength - Shoulders
ss = ["BB Overhead Press"]

# Chest
c = ["Incline DB Press", "Machine Chest Press", "Chest Fly", "Chest Dips"]

# Back
bk = ["Lat Pulldown", "DB Row", "Pull Up", "Rack Pull", "Cable Row"]

# Triceps
t = ["JM Press", "Tricep Extension", "Tricep Dips", "Skull Crusher"]

# Biceps
bp = ["DB Curl", "BB Curl", "Preacher Curl", "Hammer Curl"]

# Shoulders
s = ["Shoulder Press Machine", "DB Overhead Press"]

# Quads
q = ["Leg Extension", "Lunge", "DB Split Squat"]

# Hamstring
h = ["DB Romanian Deadlift"]

# Calf
cf = ["Seated Calf Raises", "Standing calf Raises"]

# Muscles to exercise (Reference)
muscle_to_exercise = {
    "Chest": ["Chest Fly"],
    "Back": ["BB Row", "Lat Pulldown", "DB Row", "Pull Up", "Rack Pull", "Cable Row"],
    "Biceps": ["DB Curl", "BB Curl", "Preacher Curl", "Hammer Curl"],
    "Triceps": ["JM Press", "Tricep Extension", "Tricep Dips", "Skull Crusher"],
    "Shoulders": ["BB Overhead Press", "Shoulder Press Machine", "DB Overhead Press"],
    "Quads": ["Leg Press", "Leg Extension", "Lunge", "DB Split Squat"],
    "Hamstrings": ["leg Curl", "DB Romanian Deadlift", "Romanian Deadlift"],
    "Calfs": ["Seated Calf Raises", "Standing calf Raises"],
    "Deadlift": ["Deadlift"],
    "Squat": ["Squat"],
    "Bench": ["Bench Press", "Incline DB Press", "Machine Chest Press", "Chest Dips"]
}

# ROUTINES #
strength_routines = {
    2: {
        '1': ['Deadlift', 'Overhead Press', random.choice(q), random.choice(c), random.choice(bk), random.choice(t)],
        '2': ['Squat', 'Bench Press', random.choice(h), random.choice(s), random.choice(bk), random.choice(bp)]
        },
    3: {
        '1': ['Squat', 'Bench Press', random.choice(q), random.choice(c)],
        '2': ['Deadlift', random.choice(h), 'Overhead Press', random.choice(bk)],
        '3': ['Squat', random.choice(h), random.choice(bk), random.choice(bk), random.choice(bp), random.choice(t)]
        },
    4: {
        '1': ['Bench Press', random.choice(c), random.choice(bk), 'Overhead Press', random.choice(bp)],
        '2': ['Squat', 'Deadlift', 'Leg Press', random.choice(h), random.choice(cf), random.choice(t)],
        '3': [random.choice(c), random.choice(bk), random.choice(bk), 'Lateral Raise', random.choice(t)],
        '4': ['Squat', random.choice(q), 'Leg Curl', random.choice(cf), random.choice(t)]
    }
}

muscle_routines = {
    2: {
        '1': [random.choice(c), random.choice(c), random.choice(s), random.choice(bk), 'Lateral Raise'],
        '2': ['Squat', 'Leg Press', random.choice(h), random.choice(q), random.choice(q), random.choice(cf)]
    },
    3: {
        '1': ['Bench Press', random.choice(s), random.choice(c), random.choice(bk), random.choice(t)],
        '2': [random.choice(bk), random.choice(bk), random.choice(bp), random.choice(bp), random.choice(t)],
        '3': ['Squat', 'Leg Press', random.choice(q), random.choice(h), random.choice(cf)]
    },
    4:{
        '1': ['Bench Press', 'Barbell row', 'Overhead press', random.choice(bp), 'Lateral Raise'],
        '2': ['Squat', 'Deadlift', random.choice(cf)],
        '3': [random.choice(bk), random.choice(c), random.choice(c), 'Overhead Press', random.choice(t), random.choice(bp)],
        '4': [random.choice(bk), random.choice(q), random.choice(q), random.choice(q)]
    }
}

both_routines = {
    2: {
        '1': ['Bench Press', random.choice(bk), 'Overhead Press', 'Barbell Row', random.choice(bp)],
        '2': ['Squat', random.choice(h), 'Leg Press', random.choice(cf)]
    },
    3: {
        '1': ['Squat', 'Overhead Press', random.choice(h), random.choice(bk)],
        '2': ['Bench Press', random.choice(c), 'Barbell Row', random.choice(t), random.choice(bp)],
        '3': ['Deadlifts', 'Barbell Rows', 'DB Shrugs', random.choice(bk), random.choice(cf)]
    },
    4: {
        '1': ['Bench Press', random.choice(c), random.choice(c), random.choice(t)],
        '2': ['Deadlift', 'Barbell Row', random.choice(bk), random.choice(bk)],
        '3': ['Overhead Press', random.choice(bp), random.choice(bp), 'Lateral Raise'],
        '4': ['Squat', random.choice(q), random.choice(q), random.choice(h), random.choice(cf)]
    }
}

user_name = ""
goal = ""
days = ""
user_pref = ""
pic = None

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Initialize screen width and height
        self.s_width = self.winfo_screenwidth()
        self.s_height = self.winfo_screenheight()

        # Create a container
        container = ctk.CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class StartPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.configure(fg_color="#4E4E4E")

        # Load and create the arm image
        arm_img = ctk.CTkImage(Image.open(resource_path("images/flex.png")), size=(250, 150))

        # Create a container frame for the top labels
        top_container = ctk.CTkFrame(self)
        top_container.grid(row=0, column=0, pady=(100, 0), padx=(0, 100))
        
        text_size = int(self.controller.s_height / 8)
        
        # Create the labels inside the top container frame
        arm_label = ctk.CTkLabel(top_container, text="", image=arm_img)
        arm_label.grid(row=0, column=0, padx=(0, 0))
        label = ctk.CTkLabel(top_container, text="FitForge", font=("Inter", text_size, 'bold'))
        label.grid(row=0, column=1, padx=(5, 0))

        # Create a separate label for the middle of the screen
        label_2 = ctk.CTkLabel(self, text="Begin your journey today!", font=("Inter", 35))
        label_2.grid(row=1, column=0, pady=(150, 0))

        # Configure the grid layout to center and position the elements 
        self.grid_rowconfigure(0, weight=0)  # Top row for top_container 
        self.grid_rowconfigure(1, weight=0)  # Middle row for label_2 
        self.grid_columnconfigure(0, weight=1)

        top_container.grid_rowconfigure(0, weight=1)
        top_container.grid_columnconfigure(0, weight=0)
        top_container.configure(fg_color="#4E4E4E")

        start_button = ctk.CTkButton(self, text="Start", font=("Inter", 45, 'bold'), text_color="black", command=lambda: controller.show_frame("PageOne"))
        start_button.grid(row=2, column=0, pady=(50, 0))
        start_button.configure(corner_radius=10, height=int(self.controller.s_height/13), width=int(self.controller.s_width/3), fg_color="#b5b5b5", hover_color="gray")

class PageOne(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        self.configure(fg_color="#4E4E4E")

        # Load and create the arm image
        arm_img = ctk.CTkImage(Image.open(resource_path("images/flex.png")), size=(250, 150))
        
        # Create a container frame for the top labels
        top_container = ctk.CTkFrame(self)
        top_container.grid(row=0, column=0, pady=(100, 0), padx=(0, 100))
        
        text_size = int(self.controller.s_height / 8)
        
        # Create the labels inside the top container frame
        arm_label = ctk.CTkLabel(top_container, text="", image=arm_img)
        arm_label.grid(row=0, column=0, padx=(0, 0))
        label = ctk.CTkLabel(top_container, text="FitForge", font=("Inter", text_size, 'bold'))
        label.grid(row=0, column=1, padx=(5, 0))

        # Create a separate label for the middle of the screen
        label_2 = ctk.CTkLabel(self, text="Your Name:", font=("Inter", 35), text_color="white")
        label_2.grid(row=1, column=0, pady=(150, 10), padx=(0, 300))

        self.name_entry = ctk.CTkEntry(self, placeholder_text="", font=("Inter", 25))
        self.name_entry.configure(width=self.controller.s_width / 3, height=self.controller.s_height / 13, corner_radius=15)
        self.name_entry.grid(row=2, column=0)

        # Configure the grid layout to center and position the elements
        self.grid_rowconfigure(0, weight=0)  # Top row for top_container
        self.grid_rowconfigure(1, weight=0)  # Middle row for label_2
        self.grid_columnconfigure(0, weight=1)

        # Optional: Center the contents within the top container frame if needed
        top_container.grid_rowconfigure(0, weight=1)
        top_container.grid_columnconfigure(0, weight=0)
        top_container.configure(fg_color="#4E4E4E")

        next_button = ctk.CTkButton(self, text="Next", font=("Inter", 45, 'bold'), text_color="black", command=self.save_name_and_next)
        next_button.grid(row=3, column=0, pady=(50, 0))
        next_button.configure(corner_radius=10, height=int(self.controller.s_height / 20), width=int(self.controller.s_width / 4), fg_color="#b5b5b5", hover_color="gray")

    def save_name_and_next(self):
        global user_name
        user_name = self.name_entry.get()
        self.controller.show_frame("PageTwo")


class PageTwo(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.configure(fg_color="#4E4E4E")

        # Load and create the arm image
        arm_img = ctk.CTkImage(Image.open(resource_path("images/flex.png")), size=(250, 150))

        # Create a container frame for the top labels
        top_container = ctk.CTkFrame(self)
        top_container.grid(row=0, column=0, pady=(100, 0), padx=(0, 100))

        button_container = ctk.CTkFrame(self)
        button_container.grid(row=2, column=0, pady=(100, 0), padx=100)
        button_container.configure(fg_color="#4E4E4E")

        button_container.grid_columnconfigure(0, weight=1)
        button_container.grid_columnconfigure(1, weight=1)
        button_container.grid_columnconfigure(2, weight=1)

        text_size = int(self.controller.s_height / 8)

        # Create the labels inside the top container frame
        arm_label = ctk.CTkLabel(top_container, text="", image=arm_img)
        arm_label.grid(row=0, column=0, padx=(0, 0))
        label = ctk.CTkLabel(top_container, text="FitForge", font=("Inter", text_size, 'bold'))
        label.grid(row=0, column=1, padx=(5, 0))

        # Create a separate label for the middle of the screen
        label_2 = ctk.CTkLabel(self, text="My primary goal is developing:", font=("Inter", 35), text_color="white")
        label_2.grid(row=1, column=0, pady=(100, 0))

        # Add button click handlers
        self.s_button = ctk.CTkButton(button_container, text="Strength", font=("Inter", 30, 'bold'), text_color="black", command=lambda: self.set_goal_and_next("s"))
        self.s_button.grid(row=0, column=0, padx=10, pady=5)
        self.s_button.configure(corner_radius=10, height=int(self.controller.s_height / 15), width=int(self.controller.s_height / 4), fg_color="#b5b5b5", hover_color="gray")

        self.m_button = ctk.CTkButton(button_container, text="Muscle", font=("Inter", 30, 'bold'), text_color="black", command=lambda: self.set_goal_and_next("m"))
        self.m_button.grid(row=0, column=1, padx=10, pady=5)
        self.m_button.configure(corner_radius=10, height=int(self.controller.s_height / 15), width=int(self.controller.s_height / 4), fg_color="#b5b5b5", hover_color="gray")

        self.b_button = ctk.CTkButton(button_container, text="Both", font=("Inter", 30, 'bold'), text_color="black", command=lambda: self.set_goal_and_next("b"))
        self.b_button.grid(row=0, column=2, padx=10, pady=5)
        self.b_button.configure(corner_radius=10, height=int(self.controller.s_height / 15), width=int(self.controller.s_height / 4), fg_color="#b5b5b5", hover_color="gray")

        # Configure the grid layout to center and position the elements
        self.grid_rowconfigure(0, weight=0)  # Top row for top_container
        self.grid_rowconfigure(1, weight=0)  # Middle row for label_2
        self.grid_columnconfigure(0, weight=1)

        # Optional: Center the contents within the top container frame if needed
        top_container.grid_rowconfigure(0, weight=1)
        top_container.grid_columnconfigure(0, weight=0)
        top_container.configure(fg_color="#4E4E4E")

    def set_goal_and_next(self, goal_value):
        global goal
        question = messagebox.askyesno("Confirmation", "Are you sure?")
        if question == True:
            goal = goal_value
            self.controller.show_frame("PageThree")

class PageThree(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.configure(fg_color="#4E4E4E")

        # Load and create the arm image
        arm_img = ctk.CTkImage(Image.open(resource_path("images/flex.png")), size=(250, 150))

        # Create a container frame for the top labels 
        top_container = ctk.CTkFrame(self)
        top_container.grid(row=0, column=0, pady=(100, 0), padx=(0, 100))

        item_container = ctk.CTkFrame(self)
        item_container.grid(row=1, column=0, pady=(100, 0), padx=100)
        item_container.configure(fg_color="#4E4E4E")

        item_container.grid_columnconfigure(0, weight=1)
        item_container.grid_columnconfigure(1, weight=1)
        item_container.grid_columnconfigure(2, weight=1)

        text_size = int(self.controller.s_height / 8)

        # Create the labels inside the top container frame
        arm_label = ctk.CTkLabel(top_container, text="", image=arm_img)
        arm_label.grid(row=0, column=0, padx=(0, 0))
        label = ctk.CTkLabel(top_container, text="FitForge", font=("Inter", text_size, 'bold'))
        label.grid(row=0, column=1, padx=(5, 0))

        # Create a separate label for the middle of the screen
        label_2 = ctk.CTkLabel(item_container, text="I can workout", font=("Inter", 35), text_color="white")
        label_2.grid(row=0, column=0)

        label_3 = ctk.CTkLabel(item_container, text="days a week", font=("Inter", 35), text_color="white")
        label_3.grid(row=0, column=2)

        # Configure the grid layout to center and position the elements
        self.grid_rowconfigure(0, weight=0)  # Top row for top_container
        self.grid_rowconfigure(1, weight=0)  # Middle row for label_2
        self.grid_columnconfigure(0, weight=1)

        # Optional: Center the contents within the top container frame if needed
        top_container.grid_rowconfigure(0, weight=1)
        top_container.grid_columnconfigure(0, weight=0)
        top_container.configure(fg_color="#4E4E4E")

        # Create ComboBox for selecting days
        self.day_dropbox = ctk.CTkComboBox(item_container, values=['2','3','4'], font=("Inter", 30), state="normal")
        self.day_dropbox.grid(row=0, column=1, padx=10, pady=5)

        # Create button to trigger get_dropboxval function
        confirm_button = ctk.CTkButton(self, text="Generate my routine!", font=("Inter", 35, 'bold'), text_color="white", command=lambda: self.get_dropboxval())
        confirm_button.grid(row=2, column=0, pady=(100, 0))
        confirm_button.configure(corner_radius=10, fg_color="#b5b5b5", hover_color="gray", text_color="black", height=80, width=250)

    def get_dropboxval(self):
        global days, goal  # Ensure goal is global if needed
        q = messagebox.askyesno("Confirmation", "Are you sure? \n This cannot be changed")
        if q:
            try:
                days = int(self.day_dropbox.get())  # Convert input to integer
            except ValueError:
                messagebox.showerror("Invalid input", "Please select a valid number of days.")
                return

            # Assuming goal is a global variable or accessible here
            self.controller.frames["PageFour"].set_username(user_name)
            self.controller.frames["PageFour"].update_tabs(goal, days)  # Pass both goal and days
            self.controller.show_frame("PageFour")
            identify_preference()

def identify_preference():
    global user_pref
    user_pref = [days, goal]
    print(user_pref)

class PageFour(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.user_name = ""  # Initialize with an empty username

        self.configure(fg_color="#4E4E4E")

        # Load and create the arm image
        arm_img = ctk.CTkImage(Image.open(resource_path("images/flex.png")), size=(130, 75))

        # Create a container frame for the top labels
        top_container = ctk.CTkFrame(self)
        top_container.grid(row=0, column=0, pady=(20, 0), padx=(0, 0), columnspan=2, sticky="nsew")

        text_size = int(self.controller.s_height / 15)

        # Create the labels inside the top container frame
        arm_label = ctk.CTkLabel(top_container, text="", image=arm_img)
        arm_label.grid(row=0, column=0, padx=(0, 0))
        label = ctk.CTkLabel(top_container, text="FitForge", font=("Inter", text_size, 'bold'))
        label.grid(row=0, column=1, padx=(5, 0))

        # Main container for the two frames
        main_container = ctk.CTkFrame(self)
        main_container.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
        main_container.grid_columnconfigure(0, weight=1)  # Left frame
        main_container.grid_columnconfigure(1, weight=2)  # Right frame
        main_container.grid_rowconfigure(0, weight=1)

        pic_frame = ctk.CTkFrame(main_container)
        pic_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        pic_frame.configure(fg_color='#D9D9D9')

        routine_frame = ctk.CTkFrame(main_container)
        routine_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        routine_frame.configure(fg_color='#D9D9D9')

        # Create a label above the exercises
        self.name_label = ctk.CTkLabel(routine_frame, text=f"{self.user_name}'s Weekly Routine", font=("Inter", 20, 'bold'), text_color="black")
        self.name_label.pack(side="top", padx=10, pady=10)

        # Create a scrollbar for the routine_frame
        scrollbar = ctk.CTkScrollbar(routine_frame, orientation="vertical")
        scrollbar.pack(side="right", fill="y")

        # Create a canvas to contain the exercises
        self.canvas = ctk.CTkCanvas(routine_frame, yscrollcommand=scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)

        scrollbar.configure(command=self.canvas.yview, fg_color="#2B2B2B")

        # Create a frame inside the canvas to hold the exercises
        self.exercise_frame = ctk.CTkFrame(self.canvas)
        self.exercise_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window((0, 0), window=self.exercise_frame, anchor="nw")

        # Configure the grid layout to center and position the elements
        self.grid_rowconfigure(0, weight=0)  # Top row for top_container
        self.grid_rowconfigure(1, weight=1)  # Main row for main_container
        self.grid_columnconfigure(0, weight=1)

        top_container.grid_rowconfigure(0, weight=1)
        top_container.grid_columnconfigure(0, weight=0)

        pic_frame.grid_rowconfigure(0, weight=1)
        pic_frame.grid_columnconfigure(0, weight=1)

        top_container.configure(fg_color="#4E4E4E")
        main_container.configure(fg_color='#4E4E4E')

        info_container = ctk.CTkFrame(pic_frame)
        info_container.grid(row=0, column=0, pady=10, padx=10, sticky='n')
        info_container.configure(fg_color="#d9d9d9")

        self.exc_info = ctk.CTkComboBox(info_container, values=exc, font=("Inter", 15), state="normal")
        self.exc_info.grid(row=0, column=0, padx=5)

        self.exc_info_get = ctk.CTkButton(info_container, text="Find muscle target of exercise", font=("Inter", 15), text_color="black", command=lambda: self.get_exer_info())
        self.exc_info_get.grid(row=0, column=1, padx=10)
        self.exc_info_get.configure(fg_color="#b5b5b5", hover_color="gray")

        # Calculate the optimal size for idle_img based on pic_frame size
        pic_frame.update_idletasks()
        width = pic_frame.winfo_width()
        height = pic_frame.winfo_height()

        self.image = resource_path("images/full.png")

        # Adjust the image size proportionally
        img_width = width * 1.8  # Use 90% of the width
        img_height = height * 2.4  # Use 90% of the height
        muscle_img = ctk.CTkImage(Image.open(self.image), size=(int(img_width), int(img_height)))
        muscle_img_label = ctk.CTkLabel(pic_frame, text="", image=muscle_img)
        muscle_img_label.grid(row=1, column=0, pady=5, padx=(0,10), sticky='nsew')
        
    def update_img(self, muscle_group):
        # Logic to update image based on muscle_group
        self.image = resource_path(f"images/{muscle_group}.png")
        print("new image is", self.image)


    def get_exer_info(self):
        selected_exercise = self.exc_info.get()
        for muscle_group, exercises in muscle_to_exercise.items():
            if selected_exercise in exercises:
                # Found the muscle group
                self.update_img(muscle_group)  # Update the image with the muscle group name
                print("muscle group is", muscle_group)
                break  # No need to continue once the muscle group is found

    def set_username(self, username):
        self.user_name = username
        self.name_label.configure(text=f"{self.user_name}'s Weekly Routine", text_color="black")

    def update_tabs(self, goal, days):
        print("update_tabs called with goal:", goal, "and days:", days)  # Debugging output

        # Clear any existing exercises
        for widget in self.exercise_frame.winfo_children():
            widget.destroy()

        # Determine which routines to use based on user's goal
        if goal == "s":
            routines = strength_routines.get(days, {})
        elif goal == "m":
            routines = muscle_routines.get(days, {})
        elif goal == "b":
            routines = both_routines.get(days, {})
        else:
            print("Invalid goal provided")  # Debugging output
            return  # Handle invalid goal

        row_counter = 0
        # Populate the exercise_frame with exercises
        for i in range(days):
            day_label = ctk.CTkLabel(self.exercise_frame, text=f"Day {i + 1}", font=("Inter", 20, 'bold'))
            day_label.grid(row=row_counter, column=0, columnspan=3, sticky="w", padx=10, pady=(10, 5))
            row_counter += 1

            exercises = routines.get(str(i + 1), [])  # Get exercises for current day
            for index, exercise in enumerate(exercises, start=1):
                exercise_frame = ctk.CTkFrame(self.exercise_frame)
                exercise_frame.grid(row=row_counter, column=0, columnspan=1, padx=20, pady=2, sticky="w")
                exercise_frame.configure(fg_color='#2B2B2B')

                exercise_frame.day = i + 1
                exercise_frame.exercise_index = index

                remove_frame = ctk.CTkFrame(self.exercise_frame)
                remove_frame.grid(row=row_counter, column=1, padx=(100, 2), pady=10, sticky="e")
                remove_frame.configure(fg_color='#2B2B2B')

                exercise_label = ctk.CTkLabel(exercise_frame, text=f"Exercise {index}: {exercise}", font=("Inter", 15))
                exercise_label.grid(row=0, column=0, sticky="w")
                
                remove_button = ctk.CTkButton(remove_frame, text="Remove", command=lambda ex_frame=exercise_frame, rm_frame=remove_frame: self.remove_exercise(ex_frame, rm_frame, day=i + 1, exercise_index=index), font=("Inter", 15), text_color="black")
                remove_button.grid(row=0, column=0, sticky="e")
                remove_button.configure(fg_color="#b5b5b5", hover_color="gray")

                # Check if exercise is not empty to show "Add Exercise" button
                if not exercise:  
                    add_button = ctk.CTkButton(exercise_frame, text="Add Exercise", command=lambda ex_frame=exercise_frame: self.add_exercise(ex_frame), font=("Inter", 15), text_color = "black")
                    add_button.grid(row=0, column=2, padx=(10, 0))
                    add_button.configure(fg_color="#b5b5b5", hover_color="gray")

                row_counter += 1

        # Update the canvas scroll region
        self.canvas.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def remove_exercise(self, exercise_frame, remove_frame, day, exercise_index):
        print(f"Removing exercise on Day {exercise_frame.day}, Exercise {exercise_frame.exercise_index}")  # Debugging output
        for widget in exercise_frame.winfo_children():
            widget.destroy()
        for widget in remove_frame.winfo_children():
            widget.destroy()

        # Show the "Add Exercise" button
        add_button = ctk.CTkButton(exercise_frame, text="Add Exercise", command=lambda ex=exercise_frame: self.add_exercise(exercise_frame, remove_frame), font=("Inter", 15), text_color="black")
        add_button.grid(row=0, column=2, padx=(10, 0), sticky="e")
        add_button.configure(fg_color="#b5b5b5", hover_color="gray")

        new_exc_selec = ctk.CTkComboBox(exercise_frame, values=exc, font=("Inter", 15), state="normal") 
        new_exc_selec.grid(row=0, column=1, sticky="w")
        exercise_frame.new_exc_selec = new_exc_selec  # Store the combobox as an attribute of exercise_frame

    def add_exercise(self, exercise_frame, remove_frame):
        new_exercise = exercise_frame.new_exc_selec.get()

        # Clear the content of the exercise frame
        for widget in exercise_frame.winfo_children():
            widget.destroy()

        # Add the new exercise label
        exercise_label = ctk.CTkLabel(exercise_frame, text=f"Exercise {exercise_frame.exercise_index}: {new_exercise}", font=("Inter", 15))
        exercise_label.grid(row=0, column=0, sticky="w")

        # Add the "Remove" button
        remove_button = ctk.CTkButton(remove_frame, text="Remove", command=lambda ex_frame=exercise_frame, rm_frame=remove_frame: self.remove_exercise(ex_frame, rm_frame, day=exercise_frame.day, exercise_index=exercise_frame.exercise_index), font=("Inter", 15))
        remove_button.grid(row=0, column=0, sticky="e")
        remove_button.configure(fg_color="#b5b5b5", hover_color="gray", text_color="black")

app = App()

app.title("FitForge")

app.state('zoomed')
app.resizable(width=False, height=False)
app.configure(bg="#32a852")

app.mainloop()
