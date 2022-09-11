from operator import truediv
from optparse import Values
import re
from subprocess import list2cmdline
import string



STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    with open(file, 'r') as input_file:
        #reads file set to variable contents
        contents = input_file.read()
        
        #changes contents to all lower case
        lower_case = contents.lower()
        
        #removes punctuation from lower case contents
        no_punct = lower_case.translate(str.maketrans("","", string.punctuation))
        
        #split string into separate items in a list
        list_content = no_punct.split()

        #filter out STOP_WORDS form our list
        less_words = [item for item in list_content if item not in STOP_WORDS]
        
        #establish a dictionary
        totals = dict()
        
        #loop through items in our list "list_contnet"
        for word in less_words:
            if word not in totals:
                totals[word] = 1 #put word in dict w/ count 1
            else:
                totals[word] += 1 #increase count if word already present
        
        #sort dictionary into a tupile
        sorted_totals = sorted(totals.items(), key=lambda item: item[1], reverse=True)
        
        #print our tupile keys with their values
        for keys in sorted_totals:
            print(f' {keys[0]: >15} | {keys[1]} {keys[1]*"*"}')


#don't touch
if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)

