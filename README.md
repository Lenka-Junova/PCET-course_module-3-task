# PCET-course_module-3-task
Task from module 3 from course Certified Entry-Level Tester with Python.

Course: Python for Testing 101 (PT101), Python Institute, Module 3 Project

Scenario:
You have joined an electronic device manufacturing company that develops various high-tech devices. 
Your team is tasked with maintaining and improving an existing codebase. 
One of the legacy functions, process_values(), validates outputs from a black box, an internal tool that is still under development.
The black box produces a four-character-long output, which the function processes. 
Each character must match a predefined set based on the character's position. 
These sets are derived from the rows of keys on a typical 'QWERTY' keyboard layout.
Your objective is to refactor the provided function to follow best practices, making it more readable and maintainable while ensuring it passes all unit tests.

Instructions
Source: processor.py
1) write unit tests:
Create a new Python file named test_process_values.py and write unit tests for the legacy function process_values(). 
Use assert statements to verify the function's behavior with the given test data and cover additional edge cases.
2) first refactoring iteration:
Refactor the legacy code to extract the repeated validation logic into a helper function called process_single_value(). 
Verify that the function still passes all the unit tests after this change.
3) second refactoring iteration:
Further refactor the code by introducing a loop to handle the character processing, replacing the repeated function calls. 
Ensure the function continues to pass all tests after this iteration.
4) review and optimize:
Review your refactored code and optimize it for better readability and maintainability.
Ensure all test cases still pass and the code adheres to Pythonic practices
