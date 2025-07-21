# ✅ Excel Task Tracker

A simple command-line based task manager that stores tasks in an Excel workbook using Python's `openpyxl`. Add, view, filter, update, and export your tasks from a clean CLI interface — no complex software needed.

# Tech stack

| Module                 | Purpose                                |
|------------------------|----------------------------------------|
| openpyxl               | Create and manipulate Excel files programmatically|
| Python I/O             | Create files, read/write data, and validate paths |
| CLI Design             | Basic command line interface (menu, input, feedback) |
---

## 📌 Features

- Add new tasks with project name, due date, and notes
- View all tasks in Excel format
- Filter tasks by project name or task status (e.g., Pending, Completed)
- Update task status by Task ID
- Export filtered tasks (by status) to a new `.xlsx` file

---

## 📄 Excel File Format

| Task ID | Task Name | Project | Date Created | Due Date | Status | Notes |
|---------|-----------|---------|---------------|----------|--------|-------|
|         |           |         |               |          |        |       |

---

## 🧰 How It Works

1. First run will create `task_tracker.xlsx` with headers
2. User inputs task details via terminal prompts
3. File is updated and saved automatically
4. You can then view/filter/export the task data anytime

---

## 🚀 Run the App

```bash
python task_tracker.py
