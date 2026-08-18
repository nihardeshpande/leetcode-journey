"""Write a function reverse_string that takes a string and returns it reversed —
 without using [::-1] or any built-in reverse function. Use a loop."""
def reverse_string(s):
    revstr  = ""
    for i in range(len(s) - 1 , -1 , -1):
        revstr += s[i]
    return revstr

print(reverse_string("hello"))   # should print "olleh"


"""Write a function count_vowels that takes a string and returns how many vowels 
(a, e, i, o, u — lowercase only, don't worry about uppercase for now) it contains."""

def count_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in s:
        if char in vowels:
            count+=1
    return count
print(count_vowels("hello world"))   # should print 3