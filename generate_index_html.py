
import os
import pandas as pd

html_path = "E:\\Documents\\research\\tdsc-attack\\minor-revision\\human-study\\use\\final-use\\res-16\\index.html"
writer = open(html_path, "w")
writer.write("<!DOCTYPE html>" + "\n")
writer.write("<html>" + "\n")
writer.write("<head>" + "\n")
writer.write("    <title>audios</title>" + "\n")
writer.write("</head>" + "\n")
writer.write("<body>" + "\n")

for audio_name in os.listdir("E:\\Documents\\research\\tdsc-attack\\minor-revision\\human-study\\use\\final-use\\res-16\\ori"):
    url = "ori/" + audio_name
    item = "    <embed src='" + url + "'/>\n"
    writer.write(item)

for audio_name in os.listdir("E:\\Documents\\research\\tdsc-attack\\minor-revision\\human-study\\use\\final-use\\res-16\\ori-differ-text"):
    url = "ori-differ-text/" + audio_name
    item = "    <embed src='" + url + "'/>\n"
    writer.write(item)

for eps in ["0-05", "0-01", "0-001", "0-0001"]:
    for audio_name in os.listdir("E:\\Documents\\research\\tdsc-attack\\minor-revision\\human-study\\use\\final-use\\res-16\\" + eps):
        url = eps + "/" + audio_name
        item = "    <embed src='" + url + "'/>\n"
        writer.write(item)

for eps in ["pair-1", "pair-2", "pair-3"]:
    for audio_name in os.listdir("E:\\Documents\\research\\tdsc-attack\\minor-revision\\human-study\\use\\final-use\\res-16\\test\\" + eps):
        url = 'test' + "/" + eps + "/" + audio_name
        item = "    <embed src='" + url + "'/>\n"
        writer.write(item)

for eps in ["pair-1", "pair-2", "pair-3", "pair-4"]:
    for audio_name in os.listdir("E:\\Documents\\research\\tdsc-attack\\minor-revision\\human-study\\use\\final-use\\res-16\\other\\" + eps):
        url = 'other' + "/" + eps + "/" + audio_name

# exper1_csv = "D:\\Git\\GolferChen.github.io\\adversarialVPR\\human-study\\human-study-pre-test\\amozon-mturk\\exper1.csv"
# data = pd.read_csv(exper1_csv)
# for i in range(len(data)):
#     url = data.ix[i, 0]
#     item = "    <embed src='" + url + "'/>\n"
#     writer.write(item)

# exper3_csv = "D:\\Git\\GolferChen.github.io\\adversarialVPR\\human-study\\human-study-pre-test\\amozon-mturk\\exper3.csv"
# data = pd.read_csv(exper3_csv)
# for i in range(len(data)):
#     url = data.ix[i, 0]
#     item = "    <embed src='" + url + "'/>\n"
#     writer.write(item)

#     url = data.ix[i, 1]
#     item = "    <embed src='" + url + "'/>\n"
#     writer.write(item)

writer.write("</body>" + "\n")
writer.write("</html>" + "\n")
writer.close()