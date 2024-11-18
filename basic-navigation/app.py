import seaborn as sns
import pandas as pd
from shared import df, session_summary_df, rally_df, match_df
from alogorithm import conf_matrix
from shiny import App, ui, render, reactive

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
            "Page 1",
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
            "Page 2",
            ui.h3("Logistic Model Evaluation"),
            ui.p(f"Confusion Matrix: {conf_matrix}")
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

# Create and run the app
app = App(app_ui, server)
