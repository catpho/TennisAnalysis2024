from shared import df, session_summary_df, rally_df, match_df
import pandas as pd 


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