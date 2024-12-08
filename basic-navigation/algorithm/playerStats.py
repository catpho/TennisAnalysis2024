# Import necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
from shared import df 

#shot analysis for one of the players 
# Filter the data to only include rows where 'Player Name' is 'isaac stahly'
filtered_data = df[df['Player Name'].str.lower() == 'isaac stahly']

# Extract the columns needed for the diagram
columns_to_plot = ['Direction', 'Shot Type', 'Hit (x)', 'Hit (y)']
data = filtered_data[columns_to_plot]

plt.figure(figsize=(14, 10))
sns.scatterplot(
    x='Hit (x)',
    y='Hit (y)',
    hue='Direction',  # Different colors for each unique direction
    style='Shot Type',  # Different markers for each shot type
    data=data,
    palette='Set1',
    s=100
)

# Adding plot labels and title
plt.xlabel('Hit (X)')
plt.ylabel('Hit (Y)')
plt.title('Shot Analysis for Isaac Stahly: Hit Locations by Direction and Shot Type')
plt.legend(title='Direction and Shot Type')
plt.grid(True)

plt.show()
#Keep in mind that playes swap sides during a match, so locations will show on both sides of the court.

#####
# Filter the data to only include rows where 'Player Name' is 'isaac stahly' and 'Outcome' is not 'IN'
filtered_data = df[(df['Player Name'].str.lower() == 'isaac stahly') & (df['Outcome'] != 'IN')]

# Extract the columns needed for the diagram
columns_to_plot = ['Direction', 'Shot Type', 'Hit (x)', 'Hit (y)']
data = filtered_data[columns_to_plot]

plt.figure(figsize=(14, 10))
sns.scatterplot(
    x='Hit (x)',
    y='Hit (y)',
    hue='Direction',  # Different colors for each unique direction
    style='Shot Type',  # Different markers for each shot type
    data=data,
    palette='Set1',
    s=100
)

# Adding plot labels and title
plt.xlabel('Hit (X)')
plt.ylabel('Hit (Y)')
plt.title('Shot Analysis for Isaac Stahly: Hit Locations by Direction and Shot Type. Shown only when hit not IN')
plt.legend(title='Direction and Shot Type')
plt.grid(True)

plt.show()

######

# Filter the data to only include rows where 'Player Name' is 'isaac stahly'
filtered_data = df[df['Player Name'].str.lower() == 'isaac stahly']

# Select a specific record by its index (update the index or criteria as needed)
record = filtered_data.iloc[0]  # Change the index if you want a different record

# Extract 'Hit (x)', 'Hit (y)', 'Bounce (x)', and 'Bounce (y)' from the record
hit_x = record['Hit (x)']
hit_y = record['Hit (y)']
bounce_x = record['Bounce (x)']
bounce_y = record['Bounce (y)']

# Plotting the data points for 'Hit' and 'Bounce'
plt.figure(figsize=(10, 8))
plt.scatter(hit_x, hit_y, color='blue', label='Hit Point', s=200, marker='o')
plt.scatter(bounce_x, bounce_y, color='red', label='Bounce Point', s=200, marker='X')

# Adding plot labels and title
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.title('Single Record Analysis: Hit and Bounce Points')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()

#####
# Filter the data to only include rows where 'Player Name' is 'isaac stahly'
filtered_data = df[(df['Player Name'].str.lower() == 'isaac stahly') & (df['Outcome'] != 'IN')]

# Select up to 5 records from the filtered data
records = filtered_data.head(5)

# Plotting the 'Hit' and 'Bounce' points
plt.figure(figsize=(12, 10))

for i, record in records.iterrows():
    # Extract 'Hit (x)', 'Hit (y)', 'Bounce (x)', and 'Bounce (y)' from the record
    hit_x = record['Hit (x)']
    hit_y = record['Hit (y)']
    bounce_x = record['Bounce (x)']
    bounce_y = record['Bounce (y)']

    # Plot 'Hit' and 'Bounce' points
    plt.scatter(hit_x, hit_y, color='blue', label=f'Hit Point {i}', s=200, marker='o')
    plt.scatter(bounce_x, bounce_y, color='red', label=f'Bounce Point {i}', s=200, marker='X')

    # Add labels for each point
    plt.text(hit_x, hit_y, f'Hit {i}', fontsize=12, color='blue', ha='right')
    plt.text(bounce_x, bounce_y, f'Bounce {i}', fontsize=12, color='red', ha='right')

# Adding plot labels and title
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.title('Up to 5 Records Analysis: Hit and Bounce Points for Isaac Stahly, where shot was not in')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()