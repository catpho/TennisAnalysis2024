from algorithm.confmatrix import conf_matrix
from utils.helper import get_dataframe
from algorithm.cluster import filtered_df
from algorithm.playerContext import filtered_player_data, first_player_name
import seaborn as sns
import matplotlib.pyplot as plt
from shiny import render, reactive


# Define server logic
def server(input, output, session):
    # Reactive expression for the selected dataframe
    @reactive.Calc
    def selected_dataframe():
        return get_dataframe(input.dataframe())

    
    
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
    def conf_matrix_heatmap():
        plt.imshow(conf_matrix, cmap="Blues")
        plt.colorbar()
        plt.title("Confusion Matrix")
        plt.xlabel("Predicted")
        plt.ylabel("Actual")
        return plt.gca()
    
    