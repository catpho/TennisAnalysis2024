import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from shared import df, session_summary_df, rally_df, match_df
from alogorithm import conf_matrix, accuracy, mse, mae, r2, SVR_mae, SVR_mse, SVR_r2, RFR_mae ,RFR_mse,RFR_r2
from shiny import App, ui, render, reactive
from cluster import filtered_df

# Helper function to get selected dataframe
def get_dataframe(selected_df):
    if selected_df == "Shot Stats":
        return df
    elif selected_df == "Session Summary":
        return session_summary_df
    elif selected_df == "Rally Stats":
        return rally_df
    elif selected_df == "Match Stats":
        return match_df
    else:
        return pd.DataFrame()

# Define UI
app_ui = ui.page_fluid(
    ui.navset_tab(
        # Page 1
        ui.nav_panel(
            "Tennis Data",
            ui.layout_sidebar(
                ui.sidebar(
                    ui.input_select(
                        "dataframe", "Select Dataframe", 
                        choices=["Session Summary", "Shot Stats", "Rally Stats", "Match Stats"]
                    ),
                    ui.input_select(
                        "var", "Select Variable", 
                        choices=["Shot Type", "Stroke", "Context", "Outcome"]
                    )
                ),
                
                    ui.navset_tab(
                        ui.nav_panel(
                            "Plot",
                            ui.output_plot("hist_plot")
                        ),
                        ui.nav_panel(
                            "Table",
                            ui.output_data_frame("data_table")
                        )
                    )
                
            )
        ),
        # Page 2
        ui.nav_panel(
            "Algorithms",
            ui.h3(f"Accuracy: {accuracy * 100:.2f}"),
            ui.output_plot("conf_matrix_heatmap"),
                               
                ui.navset_tab(
                        ui.nav_panel(
                            "Logistic Model Evaluation",
                            ui.p(f"Means Squared Error: {mse:.2f}"),
                            ui.p(f"Means Absolute Error: {mae:.2f}"),
                            ui.p(f"R-squared: {r2:.2f}")
                        ),
                        ui.nav_panel(
                            "SVR Model Evaluation",
                            ui.p(f"Means Squared Error: {SVR_mse:.2f}"),
                            ui.p(f"Means Absolute Error: {SVR_mae:.2f}"),
                            ui.p(f"R-squared: {SVR_r2:.2f}")
                        ),
                        ui.nav_panel(
                            "Random Forest Regressor Model Evaluation",
                            ui.p(f"Means Squared Error: {RFR_mse:.2f}"),
                            ui.p(f"Means Absolute Error: {RFR_mae:.2f}"),
                            ui.p(f"R-squared: {RFR_r2:.2f}")
                        )
                )
            
        ),
        ui.nav_panel(
            "Exploratory",
            ui.h3(f"Decision Tree of Shot Statistics"),
            ui.output_plot("decision_tree_plot")
                
            
        )
    )
)




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
    def conf_matrix_heatmap():
        # Assuming conf_matrix is a 2D array or DataFrame
        plt.figure(figsize=(8, 6))
        sns.heatmap(conf_matrix, annot=True, fmt='g', cmap="Blues", cbar=False, 
                    xticklabels=True, yticklabels=True)
        plt.title("Confusion Matrix")
        plt.xlabel("Predicted")
        plt.ylabel("Actual")
        return plt.gca()
    
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


# Create and run the app
app = App(app_ui, server)
