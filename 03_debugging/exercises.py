# ============================================================
# DEBUGGING MODULE — FULLY ANNOTATED FOR LEARNING
# ============================================================

"""
BLOCK 1 — TRY / EXCEPT BASICS
Purpose:
- Demonstrate how Python handles runtime errors.
- Show how exceptions are caught.
"""

# try: tells Python “attempt this block”
try:
    result = 10/5
except AssertionError:
    print("Error: Division by zero")


"""
BLOCK 2 — ASSERTIONS
Purpose:
- Assertions are internal sanity checks.
- If the condition is false → AssertionError is raised.
"""

assert 2+2 == 5, "math is broken"

# ------------------------------------------------------------
# LINE-BY-LINE + LETTER BREAKDOWN
# ------------------------------------------------------------
# assert
#  - a s s e r t: keyword
#  - tells Python: “this must be true”

# 2+2 == 5

#  → 2+2 == 5 evaluates to False → triggers AssertionError

# "math is broken"
#  - string message attached to the assertion


"""
BLOCK 3 — LOGGING SETUP
Purpose:
- Logging is superior to print() for automation.
- Allows levels: DEBUG, INFO, WARNING, ERROR, CRITICAL.
"""

import logging

# logging.basicConfig configures the logging system
logging.basicConfig(
    level=logging.DEBUG,   # lowest level → logs everything
)

# ------------------------------------------------------------
# LINE-BY-LINE + LETTER BREAKDOWN
# ------------------------------------------------------------
# import logging
#  - import: keyword
#  - logging: module name

# logging.basicConfig(
#  - logging: module
#  - .basicConfig: function call
#  - (: open parenthesis for arguments

# level=logging.DEBUG
#  - level: parameter name
#  - = assignment inside function call
#  - logging.DEBUG: constant representing debug level


"""
BLOCK 4 — LOGGING MESSAGES
Purpose:
- Demonstrate each logging level.
"""

logging.debug("This is a debug message")       # lowest level
logging.info("This is an info message")        # general info
logging.warning("This is a warning message")   # something unexpected
logging.error("This is an error message")      # something failed
logging.critical("This is a critical message") # system failure

# ------------------------------------------------------------
# LINE-BY-LINE + LETTER BREAKDOWN
# ------------------------------------------------------------
# logging.debug("...")
#  - logging: module
#  - .debug: method
#  - ("..."): message string

# Same structure for info(), warning(), error(), critical()

