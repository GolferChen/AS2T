
import pandas as pd

csv_path = "E:\\Documents\\research\\tdsc-attack\\minor-revision\\human-study\\use\\final-use\\res-16\\Batch_4738919_batch_results_approve.csv"

results = dict()
results['ori'] = {"same": 0, "diff": 0, "not sure": 0}
results['other'] = {"same": 0, "diff": 0, "not sure": 0}
results['0-05'] = {"same": 0, "diff": 0, "not sure": 0}
results['0-01'] = {"same": 0, "diff": 0, "not sure": 0}
results['0-001'] = {"same": 0, "diff": 0, "not sure": 0}
results['0-0001'] = {"same": 0, "diff": 0, "not sure": 0}

df = pd.read_csv(csv_path)

for index, row in df.iterrows():

    if "/ori/" in row["Input.audio_url"]:
        des = "ori"
    elif "/other/" in row["Input.audio_url"]:
        des = "other"
    elif "/0-05/" in row["Input.audio_url"]:
        des = "0-05"
    elif "/0-01/" in row["Input.audio_url"]:
        des = "0-01"
    elif "/0-001/" in row["Input.audio_url"]:
        des = "0-001"
    elif "/0-0001/" in row["Input.audio_url"]:
        des = "0-0001"
    else:
        print("Error: ", row["Input.audio_url"])
        # exit(1)
        continue
    
    if "Same" in row["Answer.experiment3-identify-speaker.label"]:
        results[des]["same"] += 1
    elif "Different" in row["Answer.experiment3-identify-speaker.label"]:
        results[des]["diff"] += 1
    elif "Not Sure" in row["Answer.experiment3-identify-speaker.label"]:
        results[des]["not sure"] += 1
    else:
        print("Error: ", row["Answer.experiment3-identify-speaker.label"])
        exit(1)

for k, v in results.items():
    tol  = v["same"] + v["diff"] + v["not sure"]
    print(k, tol,  v['same'], v['diff'], v['not sure'], v['same'] * 100 / tol, v['diff'] * 100 / tol, v['not sure'] * 100 / tol)