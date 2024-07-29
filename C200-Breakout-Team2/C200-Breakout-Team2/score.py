def get_high_score():
    # Default high score
    high_score = 0
 
    # Try to read the high score from a file
    try:
        high_score_file = open("high_score.txt", "r")
        high_score = int(high_score_file.read())
        high_score_file.close()
        print("The high score is", high_score)
    except Error:
        # Error reading the file, no high score
        print("There is no high score yet.")
    except ValueError:
        # There's a file there, but it doesn't understand the number.
        print("I'm confused. Starting with no high score.")
 
    return high_score
