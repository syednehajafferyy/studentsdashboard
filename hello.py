import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Student Dashboard")
root.geometry("500x700")
root.configure(bg="#FFDDEE")  # Light Pink

subject_entries = []


def create_subjects():
    global subject_entries

    # Clear old subject boxes
    for widget in marks_frame.winfo_children():
        widget.destroy()

    subject_entries = []
    result_label.config(text="")

    try:
        num_subjects = int(subject_number_entry.get())

        if num_subjects <= 0:
            messagebox.showerror(
                "Error",
                "Please enter a valid number of subjects."
            )
            return

        # Create Subject 1, Subject 2, Subject 3...
        for i in range(num_subjects):
            label = tk.Label(
                marks_frame,
                text=f"Subject {i + 1} Marks:",
                font=("Arial", 11),
                bg="#FFDDEE"
            )
            label.pack(pady=3)

            entry = tk.Entry(
                marks_frame,
                width=20
            )
            entry.pack(pady=3)

            subject_entries.append(entry)

    except ValueError:
        messagebox.showerror(
            "Error",
            "Please enter numbers only."
        )


def calculate_result():
    try:
        student_name = name_entry.get().strip()
        roll_number = roll_entry.get().strip()

        if student_name == "" or roll_number == "":
            messagebox.showerror(
                "Error",
                "Please enter student name and roll number."
            )
            return

        if not subject_entries:
            messagebox.showerror(
                "Error",
                "Please create subjects first."
            )
            return

        marks = []

        for entry in subject_entries:
            if entry.get().strip() == "":
                messagebox.showerror(
                    "Error",
                    "Please enter marks for all subjects."
                )
                return

            mark = float(entry.get())

            if mark < 0 or mark > 100:
                messagebox.showerror(
                    "Error",
                    "Marks must be between 0 and 100."
                )
                return

            marks.append(mark)

        total = sum(marks)
        maximum = len(marks) * 100
        percentage = (total / maximum) * 100

        # Grade and Remarks
        if percentage >= 90:
            grade = "A+"
            remarks = "Excellent"
        elif percentage >= 80:
            grade = "A"
            remarks = "Very Good"
        elif percentage >= 70:
            grade = "B"
            remarks = "Good"
        elif percentage >= 60:
            grade = "C"
            remarks = "Average"
        elif percentage >= 50:
            grade = "D"
            remarks = "Pass"
        else:
            grade = "F"
            remarks = "Fail"

        result_label.config(
            text=f"Name: {student_name}\n"
                 f"Roll No: {roll_number}\n"
                 f"Total Marks: {total}/{maximum}\n"
                 f"Percentage: {percentage:.2f}%\n"
                 f"Grade: {grade}\n"
                 f"Remarks: {remarks}"
        )

    except ValueError:
        messagebox.showerror(
            "Error",
            "Please enter valid numeric marks."
        )


# Title
title = tk.Label(
    root,
    text="Student Dashboard",
    font=("Arial", 20, "bold"),
    bg="#FFDDEE"
)
title.pack(pady=20)

# Student Name
name_label = tk.Label(
    root,
    text="Student Name:",
    font=("Arial", 11),
    bg="#FFDDEE"
)
name_label.pack()

name_entry = tk.Entry(
    root,
    width=30
)
name_entry.pack(pady=5)

# Roll Number
roll_label = tk.Label(
    root,
    text="Roll Number:",
    font=("Arial", 11),
    bg="#FFDDEE"
)
roll_label.pack()

roll_entry = tk.Entry(
    root,
    width=30
)
roll_entry.pack(pady=10)

# Number of Subjects
subject_label = tk.Label(
    root,
    text="Enter Total Number of Subjects:",
    font=("Arial", 11),
    bg="#FFDDEE"
)
subject_label.pack()

subject_number_entry = tk.Entry(
    root,
    width=20
)
subject_number_entry.pack(pady=10)

# Create Subject Boxes
create_button = tk.Button(
    root,
    text="Create Subjects",
    command=create_subjects,
    width=20
)
create_button.pack(pady=10)

# Frame for Marks
marks_frame = tk.Frame(
    root,
    bg="#FFDDEE"
)
marks_frame.pack(pady=10)

# Calculate Button
calculate_button = tk.Button(
    root,
    text="Calculate Result",
    command=calculate_result,
    width=20
)
calculate_button.pack(pady=20)

# Result Display
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 12),
    bg="#FFDDEE",
    justify="left"
)
result_label.pack(pady=10)

root.mainloop()