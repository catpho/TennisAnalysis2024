from shared import df

##IMPORTANT NOTE: games recorded so far are one v. one. When it comes to teams, code will need to adjust
#adding function to avoid hardcoding names into system 
first_player_name = df['Player Name'].iloc[0]

# individual player data based on the first name read
filtered_player_data = df[df['Player Name'].str.lower() == first_player_name.lower()]
# fault data 
fault_data = df[(df['Player Name'].str.lower() == first_player_name.lower()) & (df['Context'] == 'FAULT')]
# error data 
error_data = df[(df['Player Name'].str.lower() == first_player_name.lower()) & (df['Context'] == 'ERROR')]



