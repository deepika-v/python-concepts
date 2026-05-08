"""
Python Exception Handling Concepts

This module demonstrates:
- Try-except blocks
- Multiple exceptions
- Else clause with try
- Finally clause
- Raising exceptions
- Custom exceptions
"""

# ============================================================================
# BASIC TRY-EXCEPT
# ============================================================================

print("=" * 60)
print("BASIC TRY-EXCEPT")
print("=" * 60)

try:
    x = 10 / 2
    print(f"Result: {x}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero")

# Another example with error
print("\nWith error:")
try:
    x = 10 / 0
    print(f"Result: {x}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero")

# ============================================================================
# CATCHING EXCEPTIONS BY NAME
# ============================================================================

print("\n" + "=" * 60)
print("CATCHING EXCEPTIONS BY NAME")
print("=" * 60)

try:
    # Try to convert string to integer
    number = int("abc")
    print(f"Number: {number}")
except ValueError:
    print("Error: Could not convert string to integer")

# Try to access list index
try:
    my_list = [1, 2, 3]
    print(my_list[10])
except IndexError:
    print("Error: List index out of range")

# Try to access dictionary key
try:
    my_dict = {"name": "John"}
    print(my_dict["age"])
except KeyError:
    print("Error: Key not found in dictionary")

# ============================================================================
# MULTIPLE EXCEPT BLOCKS
# ============================================================================

print("\n" + "=" * 60)
print("MULTIPLE EXCEPT BLOCKS")
print("=" * 60)

def process_data(data_type, value):
    """Function that handles different exceptions."""
    try:
        if data_type == "int":
            return int(value)
        elif data_type == "list":
            return [1, 2, 3][int(value)]
        elif data_type == "dict":
            return {"a": 1}[value]
    except ValueError:
        print(f"ValueError: Could not convert '{value}' to integer")
    except IndexError:
        print(f"IndexError: Index out of range for value {value}")
    except KeyError:
        print(f"KeyError: Key '{value}' not found")

print("Test 1 - ValueError:")
process_data("int", "not_a_number")

print("\nTest 2 - IndexError:")
process_data("list", 10)

print("\nTest 3 - KeyError:")
process_data("dict", "b")

# ============================================================================
# CATCHING MULTIPLE EXCEPTIONS IN ONE BLOCK
# ============================================================================

print("\n" + "=" * 60)
print("CATCHING MULTIPLE EXCEPTIONS IN ONE BLOCK")
print("=" * 60)

def risky_operation(operation):
    """Function that can raise multiple exceptions."""
    try:
        if operation == "divide":
            return 10 / 0
        elif operation == "index":
            return [1, 2, 3][5]
        elif operation == "convert":
            return int("abc")
    except (ValueError, ZeroDivisionError, IndexError) as e:
        print(f"Error: {type(e).__name__} - {e}")

risky_operation("divide")
risky_operation("index")
risky_operation("convert")

# ============================================================================
# GENERIC EXCEPTION HANDLER
# ============================================================================

print("\n" + "=" * 60)
print("GENERIC EXCEPTION HANDLER")
print("=" * 60)

try:
    unknown_operation()  # This will cause NameError
except Exception as e:
    print(f"An error occurred: {type(e).__name__}")
    print(f"Error message: {e}")

# ============================================================================
# ELSE CLAUSE WITH TRY
# ============================================================================

print("\n" + "=" * 60)
print("ELSE CLAUSE WITH TRY")
print("=" * 60)

print("Successful operation:")
try:
    x = 10 / 2
    print(f"Division: {x}")
except ZeroDivisionError:
    print("Error: Division by zero")
else:
    print("No errors occurred")

print("\nFailed operation:")
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero")
else:
    print("No errors occurred")

# ============================================================================
# FINALLY CLAUSE
# ============================================================================

print("\n" + "=" * 60)
print("FINALLY CLAUSE - ALWAYS EXECUTES")
print("=" * 60)

print("With exception:")
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero")
finally:
    print("Finally block always executes!")

print("\nWithout exception:")
try:
    x = 10 / 2
    print(f"Result: {x}")
except ZeroDivisionError:
    print("Error: Division by zero")
finally:
    print("Finally block always executes!")

# ============================================================================
# FILE HANDLING WITH TRY-EXCEPT-FINALLY
# ============================================================================

print("\n" + "=" * 60)
print("FILE HANDLING WITH EXCEPTION")
print("=" * 60)

# Using try-finally for file operations
try:
    print("Opening file...")
    # file = open("nonexistent.txt", "r")  # Would raise FileNotFoundError
    print("File would be read here")
except FileNotFoundError:
    print("Error: File not found")
finally:
    print("File operations complete")

# Better approach using context manager (with statement)
print("\nUsing context manager (preferred):")
try:
    with open("example.txt", "w") as f:
        f.write("Hello, World!")
    print("File written successfully")
except IOError:
    print("Error: Could not write to file")

# ============================================================================
# RAISING EXCEPTIONS
# ============================================================================

print("\n" + "=" * 60)
print("RAISING EXCEPTIONS")
print("=" * 60)

def validate_age(age):
    """Function that raises exceptions."""
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return f"Valid age: {age}"

# Valid input
try:
    print(validate_age(25))
except (TypeError, ValueError) as e:
    print(f"Error: {e}")

# Invalid input
print("\nWith invalid input:")
try:
    print(validate_age(-5))
except (TypeError, ValueError) as e:
    print(f"Error: {e}")

# ============================================================================
# CUSTOM EXCEPTIONS
# ============================================================================

print("\n" + "=" * 60)
print("CUSTOM EXCEPTIONS")
print("=" * 60)

class InsufficientFundsError(Exception):
    """Custom exception for insufficient funds."""
    pass

class NegativeAmountError(Exception):
    """Custom exception for negative amounts."""
    pass

class BankAccount:
    """Bank account with custom exceptions."""
    
    def __init__(self, balance):
        self.balance = balance
    
    def withdraw(self, amount):
        """Withdraw with custom exception handling."""
        if amount < 0:
            raise NegativeAmountError("Amount cannot be negative")
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Insufficient funds: {self.balance}, Requested: {amount}"
            )
        self.balance -= amount
        return f"Withdrawn: {amount}, Balance: {self.balance}"

account = BankAccount(1000)

# Valid withdrawal
try:
    print(account.withdraw(200))
except (InsufficientFundsError, NegativeAmountError) as e:
    print(f"Transaction failed: {e}")

# Insufficient funds
print("\nInsufficient funds:")
try:
    print(account.withdraw(2000))
except (InsufficientFundsError, NegativeAmountError) as e:
    print(f"Transaction failed: {e}")

# Negative amount
print("\nNegative amount:")
try:
    print(account.withdraw(-100))
except (InsufficientFundsError, NegativeAmountError) as e:
    print(f"Transaction failed: {e}")

# ============================================================================
# EXCEPTION HIERARCHY
# ============================================================================

print("\n" + "=" * 60)
print("EXCEPTION HIERARCHY")
print("=" * 60)

print("""
Built-in Exception Hierarchy:
    BaseException
    ├── SystemExit
    ├── KeyboardInterrupt
    ├── GeneratorExit
    └── Exception
        ├── StopIteration
        ├── ArithmeticError
        │   ├── FloatingPointError
        │   ├── OverflowError
        │   └── ZeroDivisionError
        ├── AssertionError
        ├── AttributeError
        ├── BufferError
        ├── EOFError
        ├── ImportError
        ├── LookupError
        │   ├── IndexError
        │   └── KeyError
        ├── NameError
        ├── OSError
        ├── RuntimeError
        ├── SyntaxError
        ├── SystemError
        ├── TypeError
        └── ValueError
""")

# ============================================================================
# SUMMARY
# ============================================================================

print("\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)
print("""
1. try: Block of code that might raise exception
2. except: Handles specific exception
3. else: Executes if no exception in try block
4. finally: Always executes, use for cleanup
5. raise: Manually raise an exception
6. Multiple except blocks: Handle different exception types
7. Multiple exceptions in one block: (ExcType1, ExcType2) as e
8. Generic except: Catch all exceptions (less specific)
9. Custom exceptions: Create domain-specific exceptions
10. as e: Access exception object for error message
11. Use context managers (with statement) for resources
12. Never use bare except: or Exception as generic catch-all
""")
