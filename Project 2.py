"""
Jesus Zeno Project 2
This program will gather data on sunspots from a .CSV file from the years 1700-1999.
We will then compile, analyze, and present the data in a meaningful manner.
"""
import numpy as np
import matplotlib.pyplot as plt

# read from a file
# skip the first row 'skip_header=1' and import as string
sun_spots_file = np.genfromtxt("sunspots_1700_1999.csv", dtype='str', delimiter=",", skip_header=1)

# Get the total years in array based on the array length and dimensions
total_years = (sun_spots_file.size / sun_spots_file.ndim)

# Get all the sunspot numbers and years and convert them to float/int for later
all_sun_spots = sun_spots_file[:, 1:]
all_sun_spots = all_sun_spots.astype(float)
all_years = sun_spots_file[:, 0:1]
all_years = all_years.astype(int)

# Define time variables
decennial = 10
centennial = 100


# Determine the percent difference in two numbers
def percent_difference(start, end):
    start = float(start)
    end = float(end)
    difference = float(start) - float(end)
    percent_diff = (float(difference) / start) * 100
    percent_diff = format(float(percent_diff), '.2f')
    return percent_diff


# data_compile function will take the time variable and return the various desired data for each time frame.
def data_compile(time):
    # Make empty arrays for the data we will be returning. Also, initialize counter and year.
    time_data_avg = []
    time_data_min = []
    time_data_max = []
    time_data_std = []
    time_data_median = []
    percent_diff_data = []
    time_years = []
    i = 0
    start_year = 1700

    # Allows us to state proper time frame in print out below.
    if time == 10:
        time_frame = "decennial"
    else:
        time_frame = "centennial"

    # Print out important stats for the time frame
    print("\nBelow are some interesting {} stats based on the sunspots from 1700 to 1999:".format(time_frame))

    # Allows me to print desired data for each time frame given in a loop.
    while i < total_years:
        # determine the sunspots and put them in an array for appropriate time frame
        time_sunspots = np.copy(sun_spots_file[i:(i + time), 1:])
        # convert the data to floats
        time_sunspots = time_sunspots.astype(float)

        # Neatly print out pertinent stats
        print("-" * 83)
        print("{}'s:".format(start_year))
        print("Min:", time_sunspots.min())
        print("Max:", time_sunspots.max())
        print("Mean:", format(time_sunspots.mean(), '.2f'))
        print("Standard Deviation:", format(time_sunspots.std(), '.2f'))
        print("Median:", format(np.median(time_sunspots), '.2f'))

        # Put the data in an array to plot later.
        # Mean
        time_data_avg = np.append(time_data_avg, format(time_sunspots.mean(), '.2f'))
        time_data_avg = time_data_avg.astype(float)
        # Min
        time_data_min = np.append(time_data_min, format(time_sunspots.min(), '.2f'))
        time_data_min = time_data_min.astype(float)
        # Max
        time_data_max = np.append(time_data_max, format(time_sunspots.max(), '.2f'))
        time_data_max = time_data_max.astype(float)
        # Standard Deviation
        time_data_std = np.append(time_data_std, format(time_sunspots.std(), '.2f'))
        time_data_std = time_data_std.astype(float)
        # Median
        time_data_median = np.append(time_data_median, format(np.median(time_sunspots), '.2f'))
        time_data_median = time_data_median.astype(float)
        # Add the years to the year_plot array to be used for later
        time_years = np.append(time_years, start_year)
        time_years = time_years.astype(int)

        # Call percent difference function
        if time_data_avg.size > 1:
            print("Percent difference: {}%".format(percent_difference(time_data_avg[-2], time_data_avg[-1])))
            percent_diff_data = np.append(percent_diff_data, percent_difference(time_data_avg[-1], time_data_avg[-2]))
            percent_diff_data = percent_diff_data.astype(float)

        # Increase Counters and start year
        i += time
        start_year += time

    return time_years, time_data_avg, time_data_min, time_data_max, time_data_std, time_data_median, percent_diff_data


# Calculate and print annual min, max, mean, standard deviation, and median of sunspots.
print("\nBelow are some interesting stats based on the sunspots from 1700 to 1999:")
print("-" * 73)
print("Min:", all_sun_spots.min())
print("Max:", all_sun_spots.max())
print("Mean:", format(all_sun_spots.mean(), '.2f'))
print("Standard Deviation:", format(all_sun_spots.std(), '.2f'))
print("Median:", format(np.median(all_sun_spots), '.2f'))
print("-" * 73)


# Create empty arrays for to be later populated with averages in the while loop
decennial_years, decennial_data_avg, decennial_data_min, decennial_data_max, decennial_data_std, \
    decennial_data_median, decennial_percent_diff = data_compile(decennial)

centennial_years, centennial_data_avg, centennial_data_min, centennial_data_max, centennial_data_std, \
    centennial_data_median, centennial_percent_diff = data_compile(centennial)


# Make plot to just graph the sunspots for each year
plt.figure(figsize=(19, 9))
plt.plot(all_years, all_sun_spots,  '.-', color='blue')
plt.xticks(decennial_years, rotation=60)
plt.xlabel("Years")
plt.ylabel("Sunspots")
plt.title("Amount of Sunspots Each Year")
plt.legend(["Sunspots"])
plt.show()


# Scatter plots for decennial and centennial averages
plt.figure(figsize=(17, 9))

# Make scatter plot for decennial averages
plt.subplot(1, 2, 1)
plt.scatter(decennial_years, decennial_data_avg)
plt.xticks(decennial_years, rotation=60)
plt.xlabel("Each Decade")
plt.ylabel("Average Sunspots")
plt.title("Decennial Sun Spots Averages from 1700 to 1999")
plt.legend(["Decennial Sunspots"])

# Make scatter plot for centennial averages
plt.subplot(1, 2, 2)
plt.scatter(centennial_years, centennial_data_avg)
plt.xticks(centennial_years, rotation=60)
plt.xlabel("Each Century")
plt.ylabel("Average Sunspots")
plt.title("Centennial Sun Spots Averages from 1700 to 1999")
plt.legend(["Centennial Sunspots"])

plt.show()


# Make subplots for decennial and centennial min, max, and mean data on same canvas
plt.figure(figsize=(17, 9))

# Decennial subplot
plt.subplot(1, 2, 1)  # Makes it on the left
plt.xticks(decennial_years, rotation=60)
plt.plot(decennial_years, decennial_data_max, 'o-', color='red')  # This is the max line
plt.plot(decennial_years, decennial_data_avg, 'o-', color='blue')  # This is the mean line
plt.plot(decennial_years, decennial_data_min, 'o-', color='green')  # This is the min line
plt.legend(['Maximum', 'Average', 'Minimum'])
plt.xlabel("Each Decade")
plt.ylabel("Sunspots")
plt.title("Decennial Sunspots from 1700 to 1999")

# Centennial subplot
plt.subplot(1, 2, 2)  # Makes it on the right
plt.xticks(centennial_years)
plt.plot(centennial_years, centennial_data_max, 'o-', color='red')  # This is the max line
plt.plot(centennial_years, centennial_data_avg, 'o-', color='blue')  # This is the mean line
plt.plot(centennial_years, centennial_data_min, 'o-', color='green')  # This is the min line
plt.legend(['Maximum', 'Average', 'Minimum'])
plt.xlabel("Each Century")
plt.ylabel("Sunspots")
plt.title("Centennial Sunspots from 1700 to 1999")
plt.tight_layout()

plt.show()


# Make box plots for various data
# Make box plot for overall data
plt.figure(figsize=(17, 9))
plt.subplot(1, 3, 1)
plt.boxplot(all_sun_spots)
plt.ylabel("Sunspot Values")
plt.title("Sunspot Value Data from 1700 to 1999")

# Make box plot for decennial averages data
plt.subplot(1, 3, 2)
plt.boxplot(decennial_data_avg)
plt.ylabel("Sunspot Averages")
plt.title("Sunspot Decennial Averages from 1700 to 1999")

# Make box plot for centennial averages data
plt.subplot(1, 3, 3)
plt.boxplot(centennial_data_avg)
plt.ylabel("Sunspot Averages")
plt.title("Sunspot Centennial Averages from 1700 to 1999")
plt.tight_layout()

plt.show()


# Plot the percent difference between current and previous time period
# First the decade average
plt.figure(figsize=(17, 9))
plt.subplot(1, 2, 1)
plt.xticks(decennial_years, rotation=60)
plt.plot(decennial_years, decennial_data_avg, 'o-', color='blue')  # This is the mean line
plt.legend(['Average'])
plt.xlabel("Each Decade")
plt.ylabel("Average Sunspots")
plt.title("Decennial Sunspots from 1700 to 1999")

# Second the percent difference over each decade
plt.subplot(1, 2, 2)
plt.plot(decennial_years[1:], decennial_percent_diff)
plt.xticks(decennial_years[1:], rotation=60)
plt.xlabel("Each Decade")
plt.ylabel("Percent Difference")
plt.title("Percent Difference Between Decades")
plt.legend(["Decade Over Decade Percent Difference"])
plt.tight_layout()
plt.show()
