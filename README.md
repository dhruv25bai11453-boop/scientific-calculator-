# 📘 Calculator with Complex Numbers & Matrix Operations

This project is an interactive Python-based calculator that supports:

-   ✔️ Real numbers\
-   ✔️ Complex numbers\
-   ✔️ Matrix operations\
-   ✔️ Trigonometric functions\
-   ✔️ Standard arithmetic

It allows users to seamlessly switch between numeric mode and matrix
mode, providing a flexible and user-friendly command-line experience.

## 🚀 Features

### 🔢 Numeric Mode

Supports operations on real and complex numbers:

-   Addition (`+`)
-   Subtraction (`-`)
-   Multiplication (`*`)
-   Division (`/`)
-   Modulus (`%`)
-   `sin`, `cos`, `tan` (using `cmath` for complex values)

Example inputs:

    4
    2.5
    3+4j

### 🧮 Matrix Mode

Type `m` when prompted to switch to matrix input mode.

Supported matrix operations:

-   `MAT_ADD` --- Matrix Addition\
-   `MAT_MUL` --- Matrix Multiplication

Matrix input format example:

    Row 1: 1 2 3
    Row 2: 4 5 6

Matrices support complex numbers as well.

## 📂 How It Works

1.  The calculator first prompts for two inputs:
    -   A number (real/complex) **or**
    -   `m` to enter matrix mode
2.  Based on the inputs:
    -   If both are numbers → numeric operations
    -   If both are matrices → matrix operations
    -   Mixed inputs are not allowed
3.  Results are printed to the console.

## ▶️ Running the Program

Make sure you have Python 3 installed.

Run the script:

``` bash
python calculator.py
```

## 📌 Code Structure Summary

-   `get_number()` → Reads numeric or matrix mode selection\
-   `get_matrix()` → Reads matrices row by row\
-   `matrix_shape()` → Returns matrix dimensions\
-   `add_matrices()` → Matrix addition\
-   `multiply_matrices()` → Matrix multiplication\
-   Main interactive CLI loop

## ⚠️ Notes

-   Mixed operations (number + matrix) are not supported.
-   There is an extra line `b_is_matrix = False` in the provided code
    that overwrites matrix selection for B. Remove it.

## 💡 Future Improvements

-   Add advanced numeric functions\
-   Add determinant, transpose, inverse for matrices\
-   Add GUI or web interface\
-   Add expression parsing
