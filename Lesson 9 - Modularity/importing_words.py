# different ways of using import

# case 1

import words_refactoring_1

print(words_refactoring_1.fetch_words())

# case 2

from words_refactoring_1 import fetch_words

print(fetch_words())

# case 3
# not use if there is not name collisions in the module

from words_refactoring_1 import fetch_words as f_words

print(f_words())