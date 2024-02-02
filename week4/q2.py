
import matplotlib.pyplot as plt

ranges = []
counts=[];

def graphSnowfall(filename):
# receive file info from _t_.txt
# establish ranges of 10cm
# Open and read the entire content of a text file
    values=[];
    with open(filename, 'r') as file:
        content = file.read();
        values = content.split('\n')
        values = [int(value) for value in values]
        max_range = round(max(values));
        counts = [0] * int(max_range // 10 + 1);
        current_range = 0;
        # create the ranges
        while current_range < max_range:
            ranges.append(f'{current_range}-{current_range+10}cm')
            current_range+=10;
    # count occurrence
    for i in values:
        # get the quotient
        counts[int(i) // 10] +=1;
    fig,ax = plt.subplots();
    bar_container = ax.bar(ranges, counts)
    ax.set(ylabel='Temperature occurrence',xlabel="Amount of snow in cm", title='Occurrences by Temperature Range')


    plt.show()

graphSnowfall('_t_.txt');

