import pandas as pd


df = pd.read_csv('Submissions.csv')
teamids = df['TeamId'].unique()
counts = []
for teamid in teamids:
    count = 0
    df_temp = df[df['TeamId']==teamid]
    PrivateScoreFullPrecision_best = df_temp['PrivateScoreFullPrecision'].values[0]
    for PrivateScoreFullPrecision in df_temp['PrivateScoreFullPrecision'][1:]:
        if PrivateScoreFullPrecision > PrivateScoreFullPrecision_best:
            count += 1
            PrivateScoreFullPrecision_best = PrivateScoreFullPrecision

    counts.append(count)
df_result = pd.DataFrame()
df_result['TeamId'] = teamids
df_result['counts'] = counts
print(df_result.head())
df_result.to_csv('result.csv', index=False)

