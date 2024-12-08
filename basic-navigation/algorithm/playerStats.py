from algorithm.playerContext import filtered_player_data, first_player_name
from shared import df

# Extract the columns needed for the diagram
columns_to_plot = ['Direction', 'Shot Type', 'Hit (x)', 'Hit (y)']
shot_data = filtered_player_data[columns_to_plot]
#Keep in mind that playes swap sides during a match, so locations will show on both sides of the court.

#####
# Filter the data for outcomes that are IN
filtered_outcome_data = df[(df['Player Name'].str.lower() == first_player_name.lower()) & (df['Outcome'] != 'IN')]

# Extract the columns needed for the diagram
columns_to_plot = ['Direction', 'Shot Type', 'Hit (x)', 'Hit (y)']
outcome_data = filtered_outcome_data[columns_to_plot]

# Select a specific record by its index (update the index or criteria as needed)
shot_record = filtered_player_data.iloc[0]  # Change the index if you want a different record

#####
# where shots are NOT in
filtered_5_data = df[(df['Player Name'].str.lower() == first_player_name.lower()) & (df['Outcome'] != 'IN')]
five_records = filtered_5_data.head(5) 

