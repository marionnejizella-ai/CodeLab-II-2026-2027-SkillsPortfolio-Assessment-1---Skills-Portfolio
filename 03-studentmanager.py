import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

FILE_NAME = "students.json"


# Load student records
def load_students():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            return []
    return []


students = load_students()


# Save student records
def save_students():
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


# Clear input fields
def clear_fields():
    id_entry.config(state="normal")
    id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)


# Add student
def add_student():
    student_id = id_entry.get().strip()
    name = name_entry.get().strip()
    age = age_entry.get().strip()
    course = course_entry.get().strip()

    if not all([student_id, name, age, course]):
        messagebox.showwarning("Warning", "Please fill in all fields!")
        return

    if any(s["id"] == student_id for s in students):
        messagebox.showerror("Error", "Student ID already exists!")
        return

    if not age.isdigit() or int(age) <= 0:
        messagebox.showerror("Error", "Please enter a valid age!")
        return

    students.append({
        "id": student_id,
        "name": name,
        "age": int(age),
        "course": course
    })

    save_students()
    refresh_table()
    clear_fields()

    messagebox.showinfo("Success", "Student added successfully!")


# Display students
def refresh_table(records=None):
    for item in student_table.get_children():
        student_table.delete(item)

    if records is None:
        records = students

    for student in records:
        student_table.insert("", tk.END, values=(
            student["id"],
            student["name"],
            student["age"],
            student["course"]
        ))


# Search student
def search_student():
    keyword = search_entry.get().strip().lower()

    results = [
        s for s in students
        if keyword in s["id"].lower()
        or keyword in s["name"].lower()
    ]

    refresh_table(results)


# Select student
def select_student(event):
    selected = student_table.focus()

    if selected:
        values = student_table.item(selected, "values")

        clear_fields()

        id_entry.insert(0, values[0])
        name_entry.insert(0, values[1])
        age_entry.insert(0, values[2])
        course_entry.insert(0, values[3])

        id_entry.config(state="disabled")


# Update student
def update_student():
    student_id = id_entry.get().strip()

    for student in students:
        if student["id"] == student_id:
            name = name_entry.get().strip()
            age = age_entry.get().strip()
            course = course_entry.get().strip()

            if not all([name, age, course]):
                messagebox.showwarning(
                    "Warning", "Please fill in all fields!"
                )
                return

            if not age.isdigit() or int(age) <= 0:
                messagebox.showerror("Error", "Invalid age!")
                return

            student["name"] = name
            student["age"] = int(age)
            student["course"] = course

            save_students()
            refresh_table()
            clear_fields()

            messagebox.showinfo("Success", "Student updated!")
            return

    messagebox.showerror("Error", "Student not found!")


# Delete student
def delete_student():
    student_id = id_entry.get().strip()

    if not student_id:
        messagebox.showwarning("Warning", "Select a student first!")
        return

    for student in students:
        if student["id"] == student_id:
            confirm = messagebox.askyesno(
                "Confirm", "Delete this student?"
            )

            if confirm:
                students.remove(student)
                save_students()
                refresh_table()
                clear_fields()

                messagebox.showinfo("Success", "Student deleted!")
            return

    messagebox.showerror("Error", "Student not found!")


# Main window
root = tk.Tk()
root.title("Students Manager System")
root.geometry("900x650")
root.configure(bg="#F2F5FA")


# Header
header = tk.Label(
    root,
    text="STUDENTS MANAGER SYSTEM",
    font=("Arial", 22, "bold"),
    bg="#23395D",
    fg="white",
    pady=20
)
header.pack(fill="x")


# Student form
form = tk.Frame(root, bg="white", padx=20, pady=20)
form.pack(fill="x", padx=25, pady=20)


# Student ID
tk.Label(form, text="Student ID", bg="white").grid(
    row=0, column=0, sticky="w"
)
id_entry = tk.Entry(form, width=25)
id_entry.grid(row=1, column=0, padx=10, pady=8)


# Student Name
tk.Label(form, text="Student Name", bg="white").grid(
    row=0, column=1, sticky="w"
)
name_entry = tk.Entry(form, width=25)
name_entry.grid(row=1, column=1, padx=10, pady=8)


# Age
tk.Label(form, text="Age", bg="white").grid(
    row=2, column=0, sticky="w"
)
age_entry = tk.Entry(form, width=25)
age_entry.grid(row=3, column=0, padx=10, pady=8)


# Course
tk.Label(form, text="Course", bg="white").grid(
    row=2, column=1, sticky="w"
)
course_entry = tk.Entry(form, width=25)
course_entry.grid(row=3, column=1, padx=10, pady=8)


# Buttons
button_frame = tk.Frame(form, bg="white")
button_frame.grid(
    row=4, column=0, columnspan=2, pady=15
)

tk.Button(
    button_frame,
    text="Add Student",
    command=add_student,
    bg="#2878D0",
    fg="white",
    width=15
).pack(side="left", padx=5)

tk.Button(
    button_frame,
    text="Update",
    command=update_student,
    bg="#E6A23C",
    fg="white",
    width=12
).pack(side="left", padx=5)

tk.Button(
    button_frame,
    text="Delete",
    command=delete_student,
    bg="#D9534F",
    fg="white",
    width=12
).pack(side="left", padx=5)

tk.Button(
    button_frame,
    text="Clear",
    command=clear_fields,
    width=12
).pack(side="left", padx=5)


# Search section
search_frame = tk.Frame(root, bg="#F2F5FA")
search_frame.pack(fill="x", padx=25)

tk.Label(
    search_frame,
    text="Search Student:",
    font=("Arial", 11, "bold"),
    bg="#F2F5FA"
).pack(side="left", padx=5)

search_entry = tk.Entry(search_frame, width=35)
search_entry.pack(side="left", padx=5)

tk.Button(
    search_frame,
    text="Search",
    command=search_student,
    bg="#2878D0",
    fg="white"
).pack(side="left", padx=5)

tk.Button(
    search_frame,
    text="Show All",
    command=lambda: refresh_table()
).pack(side="left", padx=5)


# Student table
table_frame = tk.Frame(root)
table_frame.pack(
    fill="both", expand=True, padx=25, pady=20
)

columns = ("ID", "Name", "Age", "Course")

student_table = ttk.Treeview(
    table_frame,
    columns=columns,
    show="headings"
)

for column in columns:
    student_table.heading(column, text=column)
    student_table.column(
        column, width=180, anchor="center"
    )

student_table.pack(fill="both", expand=True)
student_table.bind(
    "<<TreeviewSelect>>", select_student
)


# Start application
refresh_table()
root.mainloop()
