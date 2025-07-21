# Basic Calculator
A beginner-friendly python claculator that perforrms basic arithemetic operations. The logic is modular, making it easy to extend this into a GUI app using frameworks like Tkinter or PyQt in the future. 

---

## Features
- Handles:
    - Addition (+)
    - Subtraction (-)
    - Multiplication (*)
    - Division (/)
    - Modulo (%)
    - Exponentiation (**)
- Validates user inputs
- Graceful handling of errors like divide by zero
- CLI-ready, GUI-Friendly structure

## Skills used
---
| Module/Concept        | Usage             |
|-----------------------|-------------------|
|'operator' module      | Clean mapping of operators to functions   |
| Python functions      | Core arithemetic and dispatcher functions |
| CLI design            | input handling and feedback loop          |
| Error Handling        | 'try/Except' for input validation and edge cases |
| Modular Code          | Logic seperated from interface (GUI - Ready)     |

## Ready for GUI integration
This project is designed to plug directly into a frontend:
- Tkinter or PyQt buttons can call the same core functions
- All outputs are returned (not printed), allowing widget display
- Clean exception messages for popup alerts or labels

## Future Plans
- GUI version using Tkinter (buttons, input fields, themes)
- Add memory function (m+, m-, mr)
- History/log of previous operations
- Scientific mode (sin, cos, log, etc.)


## How to use (CLI)
'''bash
python basic_calculator.py


