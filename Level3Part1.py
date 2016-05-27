#!/usr/bin/python

# Import Counter and dictionary
from collections import Counter,defaultdict

def answer(document, searchTerms):
    # Split the document so we can use indices
    doc = document.split(" ")
    # Answer goes here!
    answer = ''
    # A place to store info about where our terms can be found
    window = []
    # Count our searchTerms
    counter = Counter(searchTerms)
    # A place to keep track of indices
    dictionary = defaultdict(list)

    #    reversed
    #        - so that the last window is actually the first in the document
    #    filter
    #        - filter the enumerated doc for searchTerms
    #    lambda
    #        - the conditional for the filter is that the word must be in searchTerms
    for idx, word in reversed( filter(lambda x: x[1] in counter, enumerate(doc)) ):
        # Check if we already have this word in our dictionary
        if len(dictionary[word]) == counter[word]:
            # If we already have the word:
            #   - Remove its current index from dictionary
            #   - Remove it from the window
            window.remove(dictionary[word].pop(-1))
        # Add or update index for current word in dictionary
        dictionary[word].append(idx)
        # Update the window
        window.append(idx)

        # If:
        #   - The window is the same length as the number of serchTerms
        # And:
        #   - answer is empty OR length of the window is smaller than length of answer
        if len(window) == len(searchTerms) and (answer == '' or window[0] - window[-1] < len(answer)):
            # Answer is the window range in the doc
            answer = doc[window[-1]:window[0]+1]
        print dictionary
    # Return the answer as a string
    return ' '.join(answer)


#document = "aa b cc dd aa go le og le fu py th on go og fo le"
#searchTerms = ["go", "le", "og", "le"]

document = "many google employees can program but not all employees are google employees"
searchTerms = ["google", "program"]
print answer(document, searchTerms)
