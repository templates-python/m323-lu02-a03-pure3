"""Durchschnitt von Zahlen.

Aufgabenstellung: https://wiki.bzz.ch/modul/m323/learningunits/lu02/aufgaben/pure3
"""

# your code for function average goes here
def average(numbers):
    if len(numbers) > 0:
        return sum(numbers) / len(numbers)
    else:
        return 0


if __name__ == "__main__":
    demo_numbers = [10, 20, 30, 40, 50]
    # and here
