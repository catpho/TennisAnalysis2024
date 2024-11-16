from pathlib import Path

import pandas as pd

app_dir = Path(__file__).parent
# load multiple datafiles into app
df = pd.read_csv(app_dir / "ShotStats.csv")
session_summary_df =pd.read_csv(app_dir / "SessionSummaryShotStats.csv")
rally_df =pd.read_csv(app_dir / "RallyStats.csv")
match_df =pd.read_csv(app_dir / "MatchStats.csv")