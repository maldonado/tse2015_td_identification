# Information of the dataset
Cross project validation

## Script call

`$ python generate_classification_files.py apache-ant apache-jmeter argouml jfreechart columba password `

## Train 
All test and without classification comments from ArgoUml, Apache Jmeter, JfreeChart and Columba

## Test

All test and without classification comments from Apache ant. 

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
trainFile = /Users/evermal/git/npl_tools/datasets/test_vs_without_classification/ant_tested/classified_seq.train
tolerance = 1e-4
1.maxNGramLeng = 4
testFile = /Users/evermal/git/npl_tools/datasets/test_vs_without_classification/ant_tested/classified_seq.test
sigma = 3
printClassifierParam = 200
displayedColumn = 1
intern = true
useClassFeature = true
1.binnedLengths = 10,20,30
1.useNGrams = true
Reading dataset from /Users/evermal/git/npl_tools/datasets/test_vs_without_classification/ant_tested/classified_seq.train ...
WARNING: Number of tab-separated columns in /Users/evermal/git/npl_tools/datasets/test_vs_without_classification/ant_tested/classified_seq.train varies between 2 and 51
done [5.0s, 26248 items].
numDatums: 26248
numDatumsPerLabel: {TEST=63.0, WITHOUT_CLASSIFICATION=26185.0}
numLabels: 2 [WITHOUT_CLASSIFICATION, TEST]

3977 examples in test set
Cls WITHOUT_CLASSIFICATION: TP=3967 FN=0 FP=10 TN=0; Acc 0.997 P 0.997 R 1.000 F1 0.999
Cls TEST: TP=0 FN=10 FP=0 TN=3967; Acc 0.997 P 1.000 R 0.000 F1 0.000
Accuracy/micro-averaged F1: 0.99749
Macro-averaged F1: 0.49937

8083 examples in test set

|Classification          | TP |FN |FP |TN  |ACC  | P   |  R  | F1  |
|------------------------|----|---|---|----|-----|-----|-----|-----|
|WITHOUT_CLASSIFICATION: |8032|7  |25 |19  |0.996|0.997|0.999|0.998|
|TEST:                   |19  |25 |7  |8032|0.996|0.731|0.432|0.543|

Accuracy/micro-averaged F1: 0.99604
Macro-averaged F1: 0.77043



