from time import sleep
from hfselect import Dataset, compute_task_ranking
import csv
cnt = 0
with open("../dataset_calls.csv", "r") as f:

    reader = csv.reader(f, delimiter="\t")
    for line in reader:
        print(str(cnt) + "/1396")
        cnt += 1
        subset = None if line[5] == 'None' else line[5]
        text_col = ""
        if "[" in line[2]:
            text_col = eval(line[2])
        else:
            text_col = line[2]

        regression = True if line[4] == "True" else False
        try:
            dataset = Dataset.from_hugging_face(
                name=line[0],
                split=line[1],
                text_col=text_col,
                label_col=line[3],
                is_regression=regression,
                subset=subset,
                num_examples=int(line[6]),
                seed=int(line[7]),
                trust_remote_code = True
            )

            ranking = compute_task_ranking(dataset, "bert-base-multilingual-uncased", device_name="cuda")
            df = ranking.to_pandas()
            name= ""
            if subset is not None:
                name = line[0] +"_"+ subset
                name = name.replace("/", "_")
            else:
                name = line[0]
                name = name.replace("/", "_")
            df.to_csv(name + "_data.scv", index=False)
            with open("dataset_calls_correct", "a", encoding="utf-8") as call_file:
                call_file.write(line[0]+ "\t" + line[1] + "\t" +  line[2]+ "\t" +  line[3]+ "\t" + line[4]+ "\t" + line[5]+ "\t" + line[6]+ "\t" + line[7]+"\n")
            sleep(15)
        except Exception as error:
            with open("error", "a", encoding="utf-8") as error_file:
                error_file.write(line[0]+ "\n" + str(error) + " \n\n")
            with open("dataset_calls_notcorrect", "a", encoding="utf-8") as call_file:
                call_file.write(line[0]+ "\t" + line[1] + "\t" +  line[2]+ "\t" +  line[3]+ "\t" + line[4]+ "\t" + line[5]+ "\t" + line[6]+ "\t" + line[7]+"\n")
            sleep(15)