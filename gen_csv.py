
# import numpy as np
# import pandas as pd
# import os

# url_predix = "https://golferchen.github.io/AS2T/"
# info = dict()
# info["ground_url"] = []
# info["audio_url"] = []

# for audio_name in os.listdir("E:\\Documents\\research\\tdsc-attack\\minor-revision\\human-study\\use\\final-use\\res-16\\ori"):
#     url = url_predix + "ori/" + audio_name

#     for eps in ["0-05", "0-01", "0-001", "0-0001"]:
#         url_2 = url_predix + eps + "/" + audio_name
#         info["ground_url"].append(url)
#         info["audio_url"].append(url_2)

# for eps in ["pair-1", "pair-2", "pair-3"]:
#     audio_names = os.listdir("E:\\Documents\\research\\tdsc-attack\\minor-revision\\human-study\\use\\final-use\\res-16\\test\\" + eps)
#     i = np.random.randint(len(audio_names))
#     j = 0  if i == 1 else 1
#     url = url_predix + "test/" + eps + "/" + audio_names[i]
#     url_2 = url_predix + "test/" + eps + "/" + audio_names[j]
#     info["ground_url"].append(url)
#     info["audio_url"].append(url_2)

# df = pd.DataFrame(info)
# print(df)
# df = df.sample(frac=1)
# print(df)
# df.to_csv("E:\\Documents\\research\\tdsc-attack\\minor-revision\\human-study\\use\\final-use\\res-16\\ori_same_text.csv", index=False)



import numpy as np
import pandas as pd
import os

url_predix = "https://golferchen.github.io/AS2T/"
info = dict()
info["ground_url"] = []
info["audio_url"] = []

for audio_name in os.listdir("E:\\Documents\\research\\tdsc-attack\\minor-revision\\human-study\\use\\final-use\\res-16\\ori-differ-text"):
    url = url_predix + "ori-differ-text/" + audio_name

    for eps in ["0-05", "0-01", "0-001", "0-0001"]:
        for audio_name_2 in os.listdir("E:\\Documents\\research\\tdsc-attack\\minor-revision\\human-study\\use\\final-use\\res-16\\" + eps):
            if audio_name_2.split('-')[0] != audio_name.split('-')[0]:
                continue
            url_2 = url_predix + eps + "/" + audio_name_2
            info["ground_url"].append(url)
            info["audio_url"].append(url_2)
    
    for audio_name_2 in os.listdir("E:\\Documents\\research\\tdsc-attack\\minor-revision\\human-study\\use\\final-use\\res-16\\" + 'ori'):
            if audio_name_2.split('-')[0] != audio_name.split('-')[0]:
                continue
            url_2 = url_predix + "ori" + "/" + audio_name_2
            info["ground_url"].append(url)
            info["audio_url"].append(url_2)

for eps in ["pair-1", "pair-2", "pair-3"]:
    audio_names = os.listdir("E:\\Documents\\research\\tdsc-attack\\minor-revision\\human-study\\use\\final-use\\res-16\\test\\" + eps)
    i = np.random.randint(len(audio_names))
    j = 0  if i == 1 else 1
    url = url_predix + "test/" + eps + "/" + audio_names[i]
    url_2 = url_predix + "test/" + eps + "/" + audio_names[j]
    info["ground_url"].append(url)
    info["audio_url"].append(url_2)

for eps in ["pair-1", "pair-2", "pair-3", "pair-4"]:
    audio_names = os.listdir("E:\\Documents\\research\\tdsc-attack\\minor-revision\\human-study\\use\\final-use\\res-16\\other\\" + eps)
    i = np.random.randint(len(audio_names))
    j = 0  if i == 1 else 1
    url = url_predix + "other/" + eps + "/" + audio_names[i]
    url_2 = url_predix + "other/" + eps + "/" + audio_names[j]
    info["ground_url"].append(url)
    info["audio_url"].append(url_2)

df = pd.DataFrame(info)
df.to_csv("E:\\Documents\\research\\tdsc-attack\\minor-revision\\human-study\\use\\final-use\\res-16\\ori_differ_text-unshuffle.csv", index=False)
print(df)
df = df.sample(frac=1)
print(df)
df.to_csv("E:\\Documents\\research\\tdsc-attack\\minor-revision\\human-study\\use\\final-use\\res-16\\ori_differ_text.csv", index=False)

