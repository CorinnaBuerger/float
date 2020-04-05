# Python implementation of a finite-state machine approach to float parsing,
# as demonstrated by github.com/DanielSchuette.
import sys

def is_digit(char):
    if ord(char) >= ord(str(0)) and ord(char) <= ord(str(9)):
        return True
    return False

def string_into_float(string):
    MODE = "BEFORE_DEC"
    f = 0.0
    divisor = 1.0
    exp = 0.0
    is_neg = False
    exp_is_neg = False

    for pos, char in enumerate(string):
        if MODE == "ERROR":
            raise Exception("Invalid float {}".format(string))
        if MODE == "BEFORE_DEC":
            if char == ".":
                MODE = "AFTER_DEC"
                continue
            if char == "-" and pos == 0:
                is_neg = True
                continue
        if MODE == "AFTER_DEC":
            if char == "e" or char == "E":
                MODE = "AFTER_EXP"
                continue
            divisor = divisor * 10

        if MODE == "BEFORE_DEC" or MODE == "AFTER_DEC":
            if not is_digit(char):
                MODE = "ERROR"
                continue
            f = (f * 10.0) + ord(char) - ord(str(0))

        if MODE == "AFTER_EXP":
            if char == "-":
                exp_is_neg = True
                continue
            exp = (exp * 10.0) + ord(char) - ord(str(0))
    
    if is_neg:
        f = -1 * f
    if exp_is_neg:
        exp = -1 * exp
    f = f / divisor
    f = f * (10**exp)
    
    return f

def test(arr):
    for i in range(len(arr)):
        f = string_into_float(arr[i])
        if float(arr[i]) == f:
            print("Successfully converted {} into {}".format(arr[i], f))
        else:
            print("Conversion failed for {}. {} is the wrong answer!".format(arr[i], f))
            sys.exit(1)

if __name__ == "__main__":
    arr = [
        "1.0", ".0", ".4679087", "21876.", "24198", "1276.19", "34567878654.2345678", 
        "-2163.97", "-.654", "-456.", "-34556", "314.26e3", "56.7E4", ".5e-3"
           ]
    test(arr)