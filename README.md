# Python Programming Concepts

A comprehensive collection of small Python programs demonstrating various core concepts of the Python programming language.

## Project Structure

```
python-concepts/
├── src/                          # Core concept demonstrations
│   ├── 01_data_types.py         # Data types and variables
│   ├── 02_operators.py          # Operators and expressions
│   ├── 03_control_flow.py       # If/else, loops
│   ├── 04_functions.py          # Function definitions and calls
│   ├── 05_list_comprehension.py # List and dict comprehensions
│   ├── 06_string_operations.py  # String manipulation
│   ├── 07_file_handling.py      # File I/O operations
│   ├── 08_oop_basics.py         # Object-oriented programming
│   ├── 09_decorators.py         # Function decorators
│   ├── 10_generators.py         # Generators and iterators
│   ├── 11_exception_handling.py # Error handling
│   ├── 12_modules_packages.py   # Modules and imports
│   └── 13_advanced_concepts.py  # Lambda, map, filter, reduce
├── examples/                     # Practical examples
│   └── practice_exercises.py    # Exercises to practice concepts
├── README.md                     # This file
└── requirements.txt              # Project dependencies
```

## Concepts Covered

1. **Data Types** - int, float, str, bool, list, tuple, dict, set
2. **Operators** - Arithmetic, comparison, logical, bitwise
3. **Control Flow** - if/elif/else, for loops, while loops, break/continue
4. **Functions** - Definition, parameters, return values, scope
5. **List Comprehensions** - Concise list/dict/set creation
6. **String Operations** - Formatting, methods, slicing
7. **File Handling** - Reading, writing, context managers
8. **OOP** - Classes, objects, inheritance, encapsulation
9. **Decorators** - Function wrapping and modification
10. **Generators** - Lazy evaluation and memory efficiency
11. **Exception Handling** - Try/except/finally blocks
12. **Modules** - Import mechanisms and module organization
13. **Advanced** - Lambda, map, filter, reduce functions
14. **NumPy Basics** - Arrays, operations, broadcasting, statistics
15. **Pandas Basics** - DataFrames, Series, data manipulation
16. **Streamlit Demo** - Web app concepts and widgets
17. **Streamlit App** - Complete data analysis dashboard
18. **NumPy Advanced** - Fancy indexing, ufuncs, structured arrays

## How to Use

1. Navigate to the `src/` directory to learn each concept
2. Each file contains:
   - Concept explanation in comments
   - Basic examples
   - Common use cases
   - Best practices
3. Run individual files to see the output:
   ```bash
   python src/01_data_types.py
   ```
4. Practice with exercises in the `examples/` directory

## Interactive Push Helper

If you want Git to ask which remote and branch to push, use the helper script:

```powershell
cd "c:\AI Learning\python-concepts"
.\git_push.ps1
```

- Leave the remote blank to use `origin`
- Leave the branch blank to use `master`
- The script uses a one-time credential helper override so Git should prompt for credentials for this push only
- It does not clear your stored Git credentials globally

## Running Streamlit Applications

To run the Streamlit demos:

```bash
# Basic Streamlit concepts
streamlit run src/16_streamlit_demo.py

# Complete data analysis dashboard
streamlit run src/17_streamlit_app.py
```

The dashboard includes:
- Data upload and exploration
- Interactive visualizations
- Statistical analysis
- Correlation analysis
- Basic machine learning predictions

## Requirements

- Python 3.7+
- NumPy (for array operations)
- Pandas (for data manipulation)
- Streamlit (for web applications)
- Matplotlib & Seaborn (for plotting)
- Plotly (for interactive visualizations)
- Scikit-learn (for machine learning)

Install all dependencies:
```bash
pip install -r requirements.txt
```

No external dependencies required for core Python concepts (files 01-13).

## Learning Path

Start with:
1. Data types and operators (01-02)
2. Control flow (03)
3. Functions (04)
4. Data structures (05-06)
5. OOP basics (08)
6. Advanced concepts (09-11)
7. NumPy fundamentals (14)
8. Pandas data manipulation (15)
9. Streamlit web apps (16-17)
10. NumPy advanced topics (18)

Then explore specialized topics based on your interests.
