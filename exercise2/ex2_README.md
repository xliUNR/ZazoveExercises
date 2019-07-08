# Readme file for exercise 2

## Python Package Dependencies 
* unittest
* sys
* argparse

## File Descriptions
* __exercise2.py__ is the main file.
* __coptionsFunctions.py__ is the module file containing functions for invalid input checking.
* __OptionsClass.py__ contains the Options, Call, and Put classes and all methods for them. Call and Put inherit from Options base class.
* __ex2_unittestScript.py__ is the file containing all unit tests for exercise 2.

## Execution instructions from terminal. Make sure files have correct permissions. 
* `./exercise2.py --opt-type <C or P> -k <strike price> -s <starting stock price> -t <days until option expiration> -u <size of upward movement> -r <risk-free rate>`
* `./exercise2.py -h (or --help)` will print out help message to explain inputs. Please refer to this for format of inputs.
* Output will be printed to console to 4 decimal places.

## Execution instructions for unit tests
* `./ex1_unittestScript.py`
* Output will be printed to console
