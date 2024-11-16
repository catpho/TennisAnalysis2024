import seaborn as sns
import pandas as pd


# Import data from shared.py
from shared import df, session_summary_df, rally_df, match_df
from alogorithm import conf_matrix

from shiny.express import input, render, ui

ui.page_opts(title="Tennis Analytics")

ui.nav_spacer()  # Push the navbar items to the right


footer = ui.input_select(
    "var", "Select variable", choices=["Shot Type", "Stroke", "Context","Outcome"]
)
dataframe_select = ui.input_select(
    "dataframe", "Select varible", choices = ["Session Summary","Shot Stats","Rally Stats","Match Stats"]
)

#added function for choosing which dataframe to load 
def get_dataframe():
    selected_df = input.dataframe()

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

with ui.nav_panel("Page 1"):
    with ui.navset_card_underline(title="Data", footer=footer ):
        with ui.nav_panel("Plot"):

            @render.plot
            def hist():
                p = sns.histplot(
                    df, x=input.var(), facecolor="#007bc2", edgecolor="white"
                )
                return p.set(xlabel=None)

        with ui.nav_panel("Table"):

            #FIXME: Make it so in this panel, user can see different tables via the input they choose 
           
            @render.data_frame
            def data():
                #selected_df = get_dataframe
                return render.DataGrid(df)
            
            

######################################################

###############################################
with ui.nav_panel("Page 2"):
    with ui.navset_card_underline(title="Algorithms"):
        with ui.nav_panel("Regression"):
            "Logistic Model Evaluation"
            f"Confusion Matrix: {conf_matrix}"
            
        
