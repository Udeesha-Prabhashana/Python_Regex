"""
This application is designed to match regexes that contain either '^'
    or '$'
    or '.'
    
    '^' - begins with the specified pattern
    '$' - finishes with the specified pattern
    '.' - matches a single character.
    
This program get pattern and text as input by terminal
and the output also give on the terminal  
    
"""

# naive string matching algorithm  
def string_matching(pat, txt):
    m = len(pat)
    n = len(txt)

    i = 0
    while i < n-m+1 :
        j = 0
        while (j<m):
            if (txt[i+j] == pat[j]):
                j += 1
            else:
                break
        
        if (j == m):
            return i
        
        i += 1
    return -1
# Specialized naive string matching algorithm to see if the text begins with the specified pattern   
def che_starts(pat, txt):
    m  = len(pat)
    
    if (txt[0] == pat[0]):
        j=1
        while(j < m):
            if (txt[j] == pat[j]):
                j += 1
            else:
                break
        if (j == m):
            return 0  #if it's true ,that mean 0 index the start index of pattren
    return -1

# Specialized naive string matching algorithm to see if the text ends with the specified pattern 
def che_ends(pat, txt):
    m = len(pat)
    n = len(txt)
    
    i = n - m
    j = 0
    
    while j < m:
        if txt[i + j] == pat[j]:
            j += 1
        else:
            break
    
    if j == m:
        return i
    
    return -1
# Specifically designed naive string matching algorithm to check for patterns containing "."
def che_matching(pat, txt):
    m = len(pat)
    n = len(txt)

    matches = []             #decare the array to get all matched index 

    i = 0
    while i < n-m+1 :
        j = 0
        while (j<m):
            if (txt[i+j] == pat[j]):
                j += 1
            else:
                if pat[j] == '.':  # '.' represents exactly one charater. So we don't have to match, but need to increment the counter
                    j += 1         # increment 
                else:
                    break
        
        if (j == m):
            matches.append(i)    # if it has more than one matches ,that indexs are append to array
        
        i += 1
    if matches:
        return matches      # return index of array
    else:
        return -1
# Preprocess the given regex
# Call the functions using the special charaters
def preprocessor(pat, txt):
    m  = len(pat)
    n = len(txt)
    
    index = -1
    response = ""

    # check whether pattern have '^'
    if '^' in pat:
        index = che_starts(pat[1:], txt) 
 
    # check whether pattern have '$'
    elif '$' in pat:
        pat = pat[:-1]
        index = che_ends(pat, txt)

    # Check whether the pattern have '.'
    elif '.' in pat:
        index = che_matching(pat, txt)
    
    if index == -1:
        response = "no match found"
    else:
        response = f"found at index {index}"   
        
    print(response)  #return response

def main():
    #get the input using terminal
    pat = input("Enter the pattern: ")
    txt = input("Enter the text: ")
    #call the preprocess function
    preprocessor(pat, txt)

if __name__ == "__main__":
    main()