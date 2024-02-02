#retrives data in a text file _t_ and returns a dictionary where the _keys_ 
# are unique words in the files and the corresponding _values_ 
# are lists of line numbers where the words are found in the text.

def wordCount(filename):
    dictionary={};
    with open(filename, 'r') as file:
        content = file.read();
        lines = content.split('\n')
        
        for line_number,line in enumerate(lines):
            words=line.split(' ')
            for word in words:
                # replace any commas or periods
                word.replace('.','').replace(',','').strip()
                # check if word exists in dict
                if word in dictionary:
                    #if word exists update dict with line number
                    dictionary[word].append(line_number)
                else:
                    #if word does not exist add line number to dict
                    dictionary[word] = [line_number];

    return dictionary;

wordCount('t2.txt');