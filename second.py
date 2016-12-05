# Create a function that takes a filename and a string as parameter,
# And writes the string got as second parameter into the file 10 times.
# If the writing succeeds, the function should return True.
# If any problem raises with the file output, the function should not break, but return False.
# Example: when called with the following two parameters: "tree.txt", "apple",
# the function should write "appleappleapple" to the file "tree.txt", and return True.

def string_to_file(filename, input_string):
    try:
        fw = open(filename, 'w')
        fw.write(input_string*5)
        fw.close()
    except:
        return False
    return True
