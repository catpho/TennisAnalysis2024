
# Import necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
from shared import df

##IMPORTANT NOTE: games recorded so far are one v. one. When it comes to teams, code will need to adjust
#adding function to avoid hardcoding names into system 
first_player_name = df['Player Name'].iloc[0]

# Filter the data to only include rows where 'Player Name' is 'isaac stahly'
filtered_player_data = df[df['Player Name'].str.lower() == first_player_name.lower()]

# Count the occurrences of each value in the 'Context' column
context_counts = filtered_player_data['Context'].value_counts()

# Plotting the data as a bar chart
plt.figure(figsize=(14, 8))
sns.barplot(x=context_counts.index, y=context_counts.values, palette='viridis')

# Adding plot labels and title
plt.xlabel('Context')
plt.ylabel('Count')
plt.title(f'Distribution of Contexts for {first_player_name}')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.grid(axis='y')

# Show the plot
plt.show()


#####
# Filter the data to only include rows where 'Player Name' is 'isaac stahly' and 'Context' is 'FAULT'
fault_data = df[(df['Player Name'].str.lower() == 'isaac stahly') & (df['Context'] == 'FAULT')]

# Extract the columns needed for the diagram
columns_to_plot = ['Hit (x)', 'Hit (y)']
fault_points = fault_data[columns_to_plot]

# Plotting the 'Hit (x)' and 'Hit (y)' points for faults
plt.figure(figsize=(12, 10))
plt.scatter(fault_points['Hit (x)'], fault_points['Hit (y)'], color='red', s=150, label='Faults', marker='X')

# Adding plot labels and title
plt.xlabel('Hit (X)')
plt.ylabel('Hit (Y)')
plt.title('Hit Points for Faults: Isaac Stahly')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()

#######
# Filter the data to only include rows where 'Player Name' is 'isaac stahly' and 'Context' is 'FAULT'
fault_data = df[(df['Player Name'].str.lower() == 'isaac stahly') & (df['Context'] == 'ERROR')]

# Extract the columns needed for the diagram
columns_to_plot = ['Hit (x)', 'Hit (y)']
fault_points = fault_data[columns_to_plot]

# Plotting the 'Hit (x)' and 'Hit (y)' points for faults
plt.figure(figsize=(12, 10))
plt.scatter(fault_points['Hit (x)'], fault_points['Hit (y)'], color='red', s=150, label='Error', marker='X')

# Adding plot labels and title
plt.xlabel('Hit (X)')
plt.ylabel('Hit (Y)')
plt.title('Hit Points for Error: Isaac Stahly')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
