from algorithm.confmatrix import conf_matrix
from utils.helper import get_dataframe
from algorithm.cluster import filtered_df
from algorithm.playerContext import filtered_player_data, first_player_name, fault_data, error_data
from algorithm.playerStats import shot_data, outcome_data, five_records, shot_record
import seaborn as sns
import matplotlib.pyplot as plt
from shiny import render, reactive
import pandas as pd
from pathlib import Path
app_dir = Path(__file__).parent
uploaded_df = None

# Define server logic
def server(input, output, session):
    # Reactive expression for the selected dataframe
    @reactive.Calc
    def selected_dataframe():
        return get_dataframe(input.dataframe())


##this is the possible input for other files to be uploaded into the system. The system itself has a few issues with saving but it can read and upload the file
##cont: when it comes to using the read csv, it may be helpful only when doing the algorithms in real time. 

    @reactive.file_reader
    def read_csv():
        if input.file1():
            return pd.read_csv(input.file1()["datapath"])
        return None
    
    @reactive.Effect
    @reactive.event(input.save)
    def save_data():
        df = read_csv()
        if df is not None:
            try:
              df.to_csv("saved_data.csv", index = False)
              print("Data saved successfully.")
            except Exception as e:
                 print(f"Error saving data: {e}")
    
    # Render histogram plot
    @output
    @render.plot
    def hist_plot():
        data = selected_dataframe()
        var = input.var()
        if var in data.columns:
            plot = sns.histplot(data, x=var, color="#007bc2", edgecolor="white")
            plot.set(xlabel=None)
            return plot
        return None

    # Render data table
    @output
    @render.data_frame
    def data_table():
        return selected_dataframe()
    
      # Render confusion matrix as a heatmap
  
    
    @output
    @render.plot 
    def decision_tree_plot():
        from sklearn.tree import DecisionTreeClassifier, plot_tree

        x = filtered_df.drop(columns=['Cluster'])
        y = filtered_df['Cluster']
        tree = DecisionTreeClassifier(max_depth=3, random_state=42)
        tree.fit(x,y)

        plt.figure(figsize=(12,8))
        plot_tree(tree, 
                  feature_names=x.columns,
                  class_names=[str(i) for i in y.unique()],
                    filled=True)
        plt.title("Decision Tree")
        return plt.gca()
    
    @output
    @render.plot
    def conf_matrix_heatmap():
        plt.imshow(conf_matrix, cmap="Blues")
        plt.colorbar()
        plt.title("Confusion Matrix")
        plt.xlabel("Predicted")
        plt.ylabel("Actual")
        return plt.gca()
    
    @output
    @render.plot
    def player_bar_chart():
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

        return plt.gca()
    
    @output
    @render.plot
    def player_fault_pos():
        # Extract the columns needed for the diagram
        columns_to_plot = ['Hit (x)', 'Hit (y)']
        fault_points = fault_data[columns_to_plot]

        # Plotting the 'Hit (x)' and 'Hit (y)' points for faults
        plt.figure(figsize=(12, 10))
        plt.scatter(fault_points['Hit (x)'], fault_points['Hit (y)'], color='red', s=150, label='Faults', marker='X')

        # Adding plot labels and title
        plt.xlabel('Hit (X)')
        plt.ylabel('Hit (Y)')
        plt.title(f'Hit Points for Faults: {first_player_name.lower()}')
        plt.legend()
        plt.grid(True)
        return plt.gca()
    
    @output
    @render.plot
    def player_error_pos():
        # Extract the columns needed for the diagram
        columns_to_plot = ['Hit (x)', 'Hit (y)']
        error_points = error_data[columns_to_plot]

        # Plotting the 'Hit (x)' and 'Hit (y)' points for faults
        plt.figure(figsize=(12, 10))
        plt.scatter(error_points['Hit (x)'], error_points['Hit (y)'], color='red', s=150, label='Error', marker='X')

        # Adding plot labels and title
        plt.xlabel('Hit (X)')
        plt.ylabel('Hit (Y)')
        plt.title(f'Hit Points for Errors: {first_player_name.lower()}')
        plt.legend()
        plt.grid(True)
        return plt.gca()

    @output
    @render.plot
    def player_shot_pos():
        plt.figure(figsize=(14, 10))
        sns.scatterplot(
            x='Hit (x)',
        y='Hit (y)',
        hue='Direction',  # Different colors for each unique direction
        style='Shot Type',  # Different markers for each shot type
        data= shot_data,
        palette='Set1',
        s=100
        )

        # Adding plot labels and title
        plt.xlabel('Hit (X)')
        plt.ylabel('Hit (Y)')
        plt.title(f'Shot Analysis for {first_player_name.lower()}: Hit Locations by Direction and Shot Type')
        plt.legend(title='Direction and Shot Type')
        plt.grid(True)
        return plt.gca()
    
    
    @output
    @render.plot
    def player_outcome():    
        plt.figure(figsize=(14, 10))
        sns.scatterplot(
            x='Hit (x)',
            y='Hit (y)',
            hue='Direction',  # Different colors for each unique direction
            style='Shot Type',  # Different markers for each shot type
            data=outcome_data,
            palette='Set1',
            s=100
        )

        # Adding plot labels and title
        plt.xlabel('Hit (X)')
        plt.ylabel('Hit (Y)')
        plt.title(f'Shot Analysis for {first_player_name.lower()}: Hit Locations by Direction and Shot Type. Shown only when hit not IN')
        plt.legend(title='Direction and Shot Type')
        plt.grid(True)
        return plt.gca()
  
        
        
    @output
    @render.plot
    def single_shot_analysis():
        # Extract 'Hit (x)', 'Hit (y)', 'Bounce (x)', and 'Bounce (y)' from the record
        hit_x = shot_record['Hit (x)']
        hit_y = shot_record['Hit (y)']
        bounce_x = shot_record['Bounce (x)']
        bounce_y = shot_record['Bounce (y)']

        # Plotting the data points for 'Hit' and 'Bounce'
        plt.figure(figsize=(10, 8))
        plt.scatter(hit_x, hit_y, color='blue', label='Hit Point', s=200, marker='o')
        plt.scatter(bounce_x, bounce_y, color='red', label='Bounce Point', s=200, marker='X')

        # Adding plot labels and title
        plt.xlabel('X Coordinate')
        plt.ylabel('Y Coordinate')
        plt.title(f'Single Record Analysis: Hit and Bounce Points for {first_player_name}')
        plt.legend()
        plt.grid(True)
        return plt.gca()

    
    