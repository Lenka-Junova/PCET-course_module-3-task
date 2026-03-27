'''
source: processor.py
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
'''
from processor import process_values

from processor import process_values

#Test case 1: All inputs approved
assert process_values("4qfm") == ("4qfm", "")

#Test case 2: Some inputs are rejected
assert process_values("w2fm") == ("fm", "w2")
