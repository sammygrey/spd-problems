# Given a string of digits 2 to 9 a user has pressed on a T9 “old school” telephone keypad,
# return a list of all letter combinations they could have been trying to type on the keypad.
# Example execution 1:  t9_letters("23")  ⇒  ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
# Example execution 2:  t9_letters("4663")  ⇒  ["gmmd", …, "gone", …, "good", …, "home", …, "hood", …, "ioof"]

nums = "4663"
results = []
digits = {"2": "abc",
          "3": "def",
          "4": "ghi",
          "5": "jkl",
          "6": "mno",
          "7": "qprs",
          "8": "tuv",
          "9": "wxyz", }


def t9_letters(i=0, currentString=""):
    if len(currentString) == len(nums):
        results.append(currentString)
        return

    for char in digits[nums[i]]:
        t9_letters(i+1, currentString + char)


t9_letters()
print(results)