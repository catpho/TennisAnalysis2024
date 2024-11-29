from pathlib import Path

import pandas as pd

#FIXME: the files and cvs are hard coded into the code. make it possible for any similar type of file to be uploded and have that file be automatically processed. 

app_dir = Path(__file__).parent
# load multiple datafiles into app
df = pd.read_csv("cs_files/ShotStats.csv")
session_summary_df =pd.read_csv( "cs_files/SessionSummaryShotStats.csv")
rally_df =pd.read_csv("cs_files/RallyStats.csv")
match_df =pd.read_csv("cs_files/MatchStats.csv")