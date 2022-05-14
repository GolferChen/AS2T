
import pandas as pd

ori_csv = "E:\\Documents\\research\\tdsc-attack\\minor-revision\\human-study\\use\\final-use\\res-16\\Batch_4738919_batch_results.csv"
des_csv = "E:\\Documents\\research\\tdsc-attack\\minor-revision\\human-study\\use\\final-use\\res-16\\Batch_4738919_batch_results_approve_reject.csv"
des_csv_2 = "E:\\Documents\\research\\tdsc-attack\\minor-revision\\human-study\\use\\final-use\\res-16\\Batch_4738919_batch_results_approve.csv"

df = pd.read_csv(ori_csv)
# print(df)

exclude_workers = set()
for i, url in enumerate(list(df["Input.ground_url"])):
    if "test/pair" in url:
        if 'Different' not in list(df["Answer.experiment3-identify-speaker.label"])[i]:
            exclude_workers.add(list(df["WorkerId"])[i])
    
            # print(i, list(df["Answer.experiment3-identify-speaker.label"])[i])

print(exclude_workers, len(exclude_workers))
# print(len(set(list(df["WorkerId"]))))

# df_2 = copy.deepcopy(df)

drop_index = []
for index, row in df.iterrows():
    if row["WorkerId"] not in exclude_workers:
        # row['Approve'] = "x"
        df.loc[index, 'Approve'] = "x"
        # df_2.loc[index, 'Approve'] = "x"
    else:
         # row['Reject'] = 'Failed to pass our concentration test. The answers are randomly choosen.'
        df.loc[index, 'Reject'] = 'Failed to pass our concentration test. The answers are randomly choosen.'
        # df_2.drop(index)
        drop_index.append(index)

df_2 = df.drop(drop_index)

print(df)
print(df_2)

df.to_csv(des_csv, index=False)
df_2.to_csv(des_csv_2, index=False)


