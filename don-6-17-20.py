# Print out all of the strings in the following array that represent a number divisible by 3:
# [
#   "five",
#   "twenty six",
#   "nine hundred ninety nine,
#   "twelve",
#   "eighteen",
#   "one hundred one",
#   "fifty two",
#   "forty one",
#   "seventy seven",
#   "six",
#   "twelve",
#   "four",
#   "sixteen"
# ]
# The expected output for the above input is:
# nine hundred ninety nine
# twelve
# eighteen
# six
# twelve
# You may use whatever programming language you wish.
# Verbalize your thought process as much as possible before writing any code.
#  Run through the UPER problem solving framework while going through your thought process.

# step one iterate through array and translate strings into integers and push to new array

# step two iterate through the new array and using the modulo operater print all elements divisible by 3

from word2number import w2n

array =  [
   "five",
   "twenty six",
   "nine hundred ninety nine",
   "twelve",
   "eighteen",
   "one hundred one",
   "fifty two",
   "forty one",
   "seventy seven",
   "six",
   "twelve",
   "four",
   "sixteen"
]

for word in array:
    if w2n.word_to_num(word) % 3 == 0:
        print(word)