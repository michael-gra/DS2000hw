"""
Grace Michael
DS2000: Programming with Data
HW 7
"""

import matplotlib.pyplot as plt


# Question 1

# read the file
def read_file(filename):
    y = 0
    m = 0
    d = 0
    yi = 0
    mi = 0
    data = []
    # open the file
    with open(filename, 'r') as f:
        # skip the header line
        next(f)
        for row in f:
            # get rid of -
            row = row.replace('-', ' ')
            # get rid of \t and \
            row = row.split()
            data.append(row)
    print(data)
    return data

# seperate the dates
def process_filename(data):
    months = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
    date_list = []
    for date in data:
        d = int(date[0])
        y = int(date[2])
        r = date[3]
        # convert into fractioned minutes
        min, secs = r.split(':')
        total_time = int(min) + (float(secs) / 60)
        temp = int(date[4])
        m = months[date[1]]
                # list date as numbers
        date_list.append((y, m, d, total_time, temp))
    print(date_list)
    return date_list


# determine julien date
def julien(y, m, d):
    # following instructions from PDF
    A = 0
    B = 0
    C = 0
    D = 0
    if m == 1 or m == 2:
        yi = y - 1
        mi = m + 12
    else:
        yi = y
        mi = m
    # nothing earlier than 15 October 1582
    if (y > 1582) or (y == 1582 and m > 10) or (y == 1582 and m == 10 and d >= 15):
        A = int(yi / 100)
        B = 2 - A + int(A / 4)
    else:
        B = 0
    C = int(365.25 * yi)
    D = int(30.6001 * (mi + 1))
    # Julien Date
    JD = B + C + D + d + 1720994.5

    # Julien Day
    Book_A = (JD + 1.5) / 7
    JD_Day = round((Book_A % 1) * 7)
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    return days[JD_Day]

# Question 2

def plot_days(data):
    days_week = {'Sun':0, 'Mon':0, 'Tue':0, 'Wed':0, 'Thu':0, 'Fri':0, 'Sat':0}

    for dates in data:
        # add one to dict everytime julien results day
        days_week[julien(dates[0], dates[1], dates[2])] += 1

    # label our axes, title
    plt.xlabel('Day')
    plt.ylabel('Number of Runs')
    plt.title("Number of Runs per Day of Week")
    plt.bar(days_week.keys(), days_week.values())
    # Save to computer
    plt.savefig("bar_graph.pdf", bbox_inches='tight')
    plt.show()

# Question 3

def plot_months(data2):
    months = {'Jul':0, 'Aug':0, 'Sep':0}
    july = []
    august = []
    sept = []
    for dates in data2:
        if dates[1] == 7:
            july.append(dates[3])

        if dates[1] == 8:
            august.append(dates[3])

        if dates[1] == 9:
            sept.append(dates[3])

    print(july, august, sept)

    # label our axes, title
    plt.xlabel('Month')
    plt.ylabel('Number of Minutes')
    plt.title('Total Number of Minutes Ran')
    plt.bar(months.keys(), sum(months.values()))
    # Save to computer
    plt.savefig("bar_graph2.pdf", bbox_inches='tight')
    plt.show()

# Question 4

def line_plot(data):
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

    data = read_file('running.log')
    y1 = []
    y2 = []
    for date in data:
        # add times to respective months
        if date[1] == "Jul":
            time = date[3]
            min, secs = time.split(':')
            total_time = int(min) + (float(secs) / 60)
            y1.append(total_time)
        if date[1] == "Aug":
            time = date[3]
            min, secs = time.split(':')
            total_time = int(min) + (float(secs) / 60)
            y2.append(total_time)

    # make two lines on the plot
    plt.plot(x, y1, label='July')
    plt.plot(x, y2, label='August')


    # label our axes, title
    plt.xlabel("Number of Runs")
    plt.ylabel("Run Times")
    plt.title("Number of Runs vs Run Times Between July and August")

    # differentiate lines
    plt.legend()

    # Save to computer
    plt.savefig("line_graph.pdf", bbox_inches='tight')
    plt.show()

# Question 5

def plot_temp(data):
    run_times = []
    for date in data:
        time = date[3]
        run_times.append(time)
    print(run_times)
        #run_times.sort()
    temperature = []
    for number in data:
        temp = number[4]
        temperature.append(temp)
    print(temperature)


    plt.scatter(temperature, run_times, marker="s")

# label our axes, title
    plt.xlabel("Temperature")
    plt.ylabel("Run Times")
    plt.title("Run Times Depending on Temperature")
    # Save to computer
    plt.savefig("scatter_plot.pdf", bbox_inches='tight')
    plt.show()


# trying to be organized
def main():
    data1 = read_file('running.log')
    data2 = process_filename(data1)
    plot_days(data2)
    plot_months(data2)
    line_plot(data1)
    plot_temp(data2)



main()
