# Information of the dataset
Cross project validation

## Script call

`$ python generate_classification_files.py apache-ant apache-jmeter argouml jfreechart columba password `

## Train 
All defect and without classification comments from ArgoUml, Apache Jmeter, JfreeChart and Columba

## Test

All defect and without classification comments from Apache ant. 

## Parameters
###Features

useClassFeature=true
1.useNGrams=true
1.usePrefixSuffixNGrams=true
1.maxNGramLeng=4
1.minNGramLeng=1
1.binnedLengths=10,20,30

###Printing

printClassifier=HighWeight
printClassifierParam=200

###Mapping

goldAnswerColumn=0
displayedColumn=1

###Optimization

intern=true
sigma=3
useQN=true
QNsize=15
tolerance=1e-4

## Results
1.usePrefixSuffixNGrams = true
QNsize = 15
useQN = true
goldAnswerColumn = 0
1.minNGramLeng = 1
trainFile = /Users/evermal/git/npl_tools/datasets/defect_vs_without_classification/ant_tested/classified_seq.train
tolerance = 1e-4
1.maxNGramLeng = 4
testFile = /Users/evermal/git/npl_tools/datasets/defect_vs_without_classification/ant_tested/classified_seq.test
sigma = 3
printClassifierParam = 200
displayedColumn = 1
intern = true
useClassFeature = true
1.binnedLengths = 10,20,30
1.useNGrams = true
Reading dataset from /Users/evermal/git/npl_tools/datasets/defect_vs_without_classification/ant_tested/classified_seq.train ...
WARNING: Number of tab-separated columns in /Users/evermal/git/npl_tools/datasets/defect_vs_without_classification/ant_tested/classified_seq.train varies between 2 and 51
done [4.2s, 26356 items].
numDatums: 26356
numDatumsPerLabel: {WITHOUT_CLASSIFICATION=26185.0, DEFECT=171.0}

3980 examples in test set
Cls WITHOUT_CLASSIFICATION: TP=3966 FN=1 FP=13 TN=0; Acc 0.996 P 0.997 R 1.000 F1 0.998
Cls DEFECT: TP=0 FN=13 FP=1 TN=3966; Acc 0.996 P 0.000 R 0.000 F1 0.000
Accuracy/micro-averaged F1: 0.99648
Macro-averaged F1: 0.49912

8166 examples in test set

|Classification          | TP |FN |FP |TN  |ACC  | P   |  R  | F1  |
|------------------------|----|---|---|----|-----|-----|-----|-----|
|WITHOUT_CLASSIFICATION: |7950|89 |68 |59  |0.981|0.992|0.989|0.990|
|DEFECT:                 |59  |68 |89 |7950|0.981|0.399|0.465|0.429|

Accuracy/micro-averaged F1: 0.98077
Macro-averaged F1: 0.70966

