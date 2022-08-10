from subprocess import list2cmdline


STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

import string

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    with open(file, 'r') as input_file:
        #reads file set to variable contents
        contents = input_file.read()
        #changes contents to all lower case
        lower_case = contents.lower()
        #removes punctuation from lower case contents
        no_punct = lower_case.translate(str.maketrans('', '', string.punctuation))
        #split string into separate items in a list
        list_content = no_punct.split(" ")
        #establish a dictionary
        totals = dict()
        #loop through items in our list "list_contnet"
        for word in list_content:
            if word not in totals:
                totals[word] = 1 #put word in dict w/ count 
            else:
                totals[word] += 1 #increase count if word already present
        print(totals)


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

