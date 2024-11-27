---
layout: page
title: Front-End Compiler
description: Built a front-end compiler for an imperative programming language using ANTLR.
importance: 1
category: fun
img: assets/img/project_preview/compiler.png
---

Implemented a **front-end compiler** for an imperative programming language inspired by the structure of C, utilizing **ANTLR** for grammar definition and **C** for code generation. The compiler covered essential phases such as **lexical analysis**, **syntax analysis**, and **semantic checking**, offering a foundational understanding of compiler design and language processing.

### Key Contributions

The grammar for the front-end programming language was implemented in ANTLR, defining structures like functions, parameters, loops, conditions, and variable declarations. The compiler adhered to a clean and modular structure to process the input source code. After designing the grammar, a **listener** was implemented to traverse the parse tree and extract semantic information. The code generation phase translated high-level constructs into low-level operations, mimicking the behavior of assembly-like instructions.

The generated code executed operations such as arithmetic calculations, control flow, and input/output. For example, it handled tasks like managing activation records, updating stack pointers, performing arithmetic operations, and handling jumps or conditional statements. The integration of these features made the compiler capable of generating accurate and efficient intermediate representations.

### Grammar and Code Generation

The grammar, designed to parse imperative programs, included constructs for variable declarations, expressions, control flow, and function definitions. Here is a snapshot of some generated instructions:

1. `m[top + j].{i, d} = m[top + k].{i, d} op m[top + r].{i, d};`  
   Performs arithmetic operations (e.g., `+`, `-`, `*`, `/`, `%`) between stack variables.

2. `m[top + j].{i, d} = op m[top + k].{i, d};`  
   Handles unary operations like negation (`-`) or logical NOT (`!`).

3. `printInt(m[top + j].i);` and `printDouble(m[top + j].d);`  
   Outputs integer and double values stored at specific memory locations.

4. `goto label;` and `if (m[top + j].{i, d} relop m[top + k].{i, d}) goto label;`  
   Implements unconditional and conditional jumps for control flow, where `relop` is a relational operator such as `<`, `<=`, `==`, etc.

5. `m[top + j].i = readInt();`  
   Reads an integer input and stores it in the stack.

6. `bottom += 4;`  
   Adjusts the activation record to handle function calls and returns.

The generated code reflects a stack-based approach, with explicit management of pointers (`top` and `bottom`) and memory locations for executing high-level constructs.

This project was part of a **Compiler Design** course, providing hands-on experience in building a front-end compiler and understanding the intricacies of language processing.