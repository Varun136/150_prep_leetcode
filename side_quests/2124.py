""" 
QUESTION:
    Given a string s consisting of only the characters 'a' and 'b', return true if every 'a' 
    appears before every 'b' in the string. Otherwise, return false.
"""

def check_string(s: str) -> bool:
    """
    Alphabets are used for logical operators based on their 
    ASCII value.
    """

    for i in range(len(s)-1):
        if s[i] > s[i+1]:
            return False
        
    return True


if __name__ == "__main__":
    string = "abb"
    print(check_string(string))