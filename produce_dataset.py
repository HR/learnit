from pprint import pprint
import json
import csv
from random import randint

# This .py collects data from a SQuAD JSON dataset and produces around 200k
# quadruples (Context, Question, Answer, Label) in CSV ASCII file, where
# label corresponds to whether the answer to the question is true or false.
# False answers were produced by using true answers in a different context.

#prompt the user for a file to import
filter = "JSON file (*.json)|*.json|All Files (*.*)|*.*||"
filename = "dev-v1.1.json"

#Read JSON data into the datastore variable
with open(filename) as data_file:    
    data = json.load(data_file)

with open('data.csv', 'w') as csvfile:
    fieldnames = ['Context', 'Question', 'Answer', 'Label']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    falseans = []       # contains all answers from a dataset
    #Read JSON data into the datastore variable
    filename = "train-v1.1.json"
    with open(filename) as data_file:    
        data = json.load(data_file)

    # fill a falseans dataset with first dataset
    for a in range(len(data['data'])):
            for c in range(len(data['data'][a]['paragraphs'])):
                    for j in range(len(data['data'][a]['paragraphs'][c]['qas'])):
                            for k in range(len(data['data'][a]['paragraphs'][c]['qas'][j]['answers'])):
                                    falseans.append(data['data'][a]['paragraphs'][c]['qas'][j]['answers'][k]['text'])
                                    
    #Read JSON data into the datastore variable
    filename = "dev-v1.1.json"
    with open(filename) as data_file:
            data = json.load(data_file)

    # fill a falseans dataset with first dataset
    for a in range(len(data['data'])):
            for c in range(len(data['data'][a]['paragraphs'])):
                    for j in range(len(data['data'][a]['paragraphs'][c]['qas'])):
                            for k in range(len(data['data'][a]['paragraphs'][c]['qas'][j]['answers'])):
                                    falseans.append(data['data'][a]['paragraphs'][c]['qas'][j]['answers'][k]['text'])

    # fill quadruples from a first dataset
    for a in range(len(data['data'])): # go through a list (data is a list of dictionaries)
            for c in range(len(data['data'][a]['paragraphs'])):# from the dictionary choose paragraph section, go through a list of paragraphs
            #list of paragraphs has dictionaries with 1 context and 2 qas
                for j in range(len(data['data'][a]['paragraphs'][c]['qas'])):
                    ans = []
                    #print(data['data'][a]['paragraphs'][c]['qas'][j]['question'])
                    for k in range(len(data['data'][a]['paragraphs'][c]['qas'][j]['answers'])):
                        if data['data'][a]['paragraphs'][c]['qas'][j]['answers'][k]['text'] not in ans:
                            ans.append(data['data'][a]['paragraphs'][c]['qas'][j]['answers'][k]['text'])
                            try:
                                    rnumber = randint(0, len(falseans))
                                    while ((rnumber % 2) != 0):
                                            rnumber = randint(0, len(falseans))
                                    while data['data'][a]['paragraphs'][c]['qas'][j]['answers'][k]['text'] == falseans[rnumber]:
                                            rnumber = randint(0, len(falseans))
                                    string1 = data['data'][a]['paragraphs'][c]['context'].encode("ascii", errors="ignore").decode()
                                    string2 = data['data'][a]['paragraphs'][c]['qas'][j]['question'].encode("ascii", errors="ignore").decode()
                                    string3 = data['data'][a]['paragraphs'][c]['qas'][j]['answers'][k]['text'].encode("ascii", errors="ignore").decode()
                                    string4 = falseans[rnumber].encode("ascii", errors="ignore").decode()
                                    #writer.writerow({'Context': data['data'][a]['paragraphs'][c]['context'], 'Question': data['data'][a]['paragraphs'][c]['qas'][j]['question'], 'Answer':falseans[rnumber], 'Label': 0})
                                    #writer.writerow({'Context': data['data'][a]['paragraphs'][c]['context'], 'Question': data['data'][a]['paragraphs'][c]['qas'][j]['question'], 'Answer':data['data'][a]['paragraphs'][c]['qas'][j]['answers'][k]['text'], 'Label': 1})
                                    writer.writerow({'Context': string1, 'Question': string2, 'Answer': string4, 'Label': 0})
                                    writer.writerow({'Context': string1, 'Question': string2, 'Answer': string3, 'Label': 1})
                            except ValueError:
                                    continue

    #Read JSON data into the datastore variable
    filename = "train-v1.1.json"
    with open(filename) as data_file:    
        data = json.load(data_file)

    # fill quadruples from a dataset 2
    for a in range(len(data['data'])): # go through a list (data is a list of dictionaries)
            for c in range(len(data['data'][a]['paragraphs'])):# from the dictionary choose paragraph section, go through a list of paragraphs
            #list of paragraphs has dictionaries with 1 context and 2 qas
                for j in range(len(data['data'][a]['paragraphs'][c]['qas'])):
                    ans = []
                    #print(data['data'][a]['paragraphs'][c]['qas'][j]['question'])
                    for k in range(len(data['data'][a]['paragraphs'][c]['qas'][j]['answers'])):
                        if data['data'][a]['paragraphs'][c]['qas'][j]['answers'][k]['text'] not in ans:
                            ans.append(data['data'][a]['paragraphs'][c]['qas'][j]['answers'][k]['text'])
                            try:
                                    rnumber = randint(0, len(falseans))
                                    while ((rnumber % 2) != 0):
                                            rnumber = randint(0, len(falseans))
                                    while data['data'][a]['paragraphs'][c]['qas'][j]['answers'][k]['text'] == falseans[rnumber]:
                                            rnumber = randint(0, len(falseans))

                                    string1 = data['data'][a]['paragraphs'][c]['context'].encode("ascii", errors="ignore").decode()
                                    string2 = data['data'][a]['paragraphs'][c]['qas'][j]['question'].encode("ascii", errors="ignore").decode()
                                    string3 = data['data'][a]['paragraphs'][c]['qas'][j]['answers'][k]['text'].encode("ascii", errors="ignore").decode()
                                    string4 = falseans[rnumber].encode("ascii", errors="ignore").decode()
                                    #writer.writerow({'Context': data['data'][a]['paragraphs'][c]['context'], 'Question': data['data'][a]['paragraphs'][c]['qas'][j]['question'], 'Answer':falseans[rnumber], 'Label': 0})
                                    #writer.writerow({'Context': data['data'][a]['paragraphs'][c]['context'], 'Question': data['data'][a]['paragraphs'][c]['qas'][j]['question'], 'Answer':data['data'][a]['paragraphs'][c]['qas'][j]['answers'][k]['text'], 'Label': 1})
                                    writer.writerow({'Context': string1, 'Question': string2, 'Answer': string4, 'Label': 0})
                                    writer.writerow({'Context': string1, 'Question': string2, 'Answer': string3, 'Label': 1})
                            
                            except ValueError:
                                    continue
