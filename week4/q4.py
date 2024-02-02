# This function reads lines in a given text file and sends them to _decorator_ to print values
def printStats(filename):
    with open(filename, 'r') as file:
        content = file.read();
        lines = content.split('\n')
        
        for line_number,line in enumerate(lines):
            print(f'\n~~~ LINE NUMBER {line_number+1} ~~~')
            _decorator_(line)

# This function takes a line of numbers, parses them and prints out the stats
def _decorator_(line):
    numbers_read=[]
    numbers_count=0
    numbers_average=0
    numbers_max=0
    # make numbers usable in list
    numbers = line.split(',')
    for num in numbers:
        numbers_read.append(int(num));
        numbers_count+=1
    # Find the max number and average in row
    numbers_max = max(numbers_read)
    numbers_average = sum(numbers_read) / numbers_count
    # Print statistics
    print(f'values: {numbers_read}')
    print(f'number count: {numbers_count}')
    print(f'Average of numbers:{numbers_average}')
    print(f'largest number: {numbers_max}')


printStats('t3.txt');