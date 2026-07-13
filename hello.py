import tkinter as tk
from tkinter import messagebox

# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("Student Dashboard")
root.geometry("550x700")
root.configure(bg="#FFDDEE")

subject_entries = []

# ---------------- SCROLLABLE AREA ----------------
canvas = tk.Canvas(root, bg="#FFDDEE", highlightthickness=0)
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)

main_frame = tk.Frame(canvas, bg="#FFDDEE")

main_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=main_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")


# ---------------- FUNCTIONS ----------------
def create_subjects():
    global subject_entries

    # Remove old subject boxes
    for widget in marks_frame.winfo_children():
        widget.destroy()

    subject_entries = []
    result_label.config(text="")

    try:
        num_subjects = int(subject_number_entry.get())

        if num_subjects <= 0:
            messagebox.showerror(
                "Error",
                "Enter a valid number of subjects."
            )
            return

        # Create Subject 1, Subject 2, ... Subject n
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
                width=25
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
        name = name_entry.get().strip()
        roll_no = roll_entry.get().strip()
        section = section_entry.get().strip()

        if name == "" or roll_no == "":
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
            text=(
                f"Name: {name}\n"
                f"Roll No: {roll_no}\n"
                f"Class/Section: {section}\n"
                f"Subjects: {len(marks)}\n"
                f"Total Marks: {total}/{maximum}\n"
                f"Percentage: {percentage:.2f}%\n"
                f"Grade: {grade}\n"
                f"Remarks: {remarks}"
            )
        )

    except ValueError:
        messagebox.showerror(
            "Error",
            "Please enter valid numeric marks."
        )


# ---------------- GUI ----------------
title = tk.Label(
    main_frame,
    text="Student Dashboard",
    font=("Arial", 20, "bold"),
    bg="#FFDDEE"
)
title.pack(pady=20)

tk.Label(
    main_frame,
    text="Student Name:",
    font=("Arial", 11),
    bg="#FFDDEE"
).pack()

name_entry = tk.Entry(main_frame, width=30)
name_entry.pack(pady=5)

tk.Label(
    main_frame,
    text="Roll Number:",
    font=("Arial", 11),
    bg="#FFDDEE"
).pack()

roll_entry = tk.Entry(main_frame, width=30)
roll_entry.pack(pady=5)

tk.Label(
    main_frame,
    text="Class / Section:",
    font=("Arial", 11),
    bg="#FFDDEE"
).pack()

section_entry = tk.Entry(main_frame, width=30)
section_entry.pack(pady=10)

tk.Label(
    main_frame,
    text="Enter Total Number of Subjects:",
    font=("Arial", 11),
    bg="#FFDDEE"
).pack()

subject_number_entry = tk.Entry(main_frame, width=20)
subject_number_entry.pack(pady=10)

tk.Button(
    main_frame,
    text="Create Subjects",
    command=create_subjects,
    width=20
).pack(pady=10)

marks_frame = tk.Frame(main_frame, bg="#FFDDEE")
marks_frame.pack(pady=10)

tk.Button(
    main_frame,
    text="Calculate Result",
    command=calculate_result,
    width=20
).pack(pady=20)

result_label = tk.Label(
    main_frame,
    text="",
    font=("Arial", 12),
    bg="#FFDDEE",
    justify="left"
)
result_label.pack(pady=10)

root.mainloop()
