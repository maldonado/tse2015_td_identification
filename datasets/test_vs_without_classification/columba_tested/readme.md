# Information of the dataset
Cross project validation

`$ python generate_classification_files.py columba apache-ant apache-jmeter argouml jfreechart password `

## Train 
All test and without classification comments from Apache Ant, Apache Jmeter, JfreeChart and ArgoUml

## Test

All test and without classification comments from Columba. 

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

.usePrefixSuffixNGrams = true
QNsize = 15
useQN = true
goldAnswerColumn = 0
1.minNGramLeng = 1
trainFile = /Users/evermal/git/npl_tools/datasets/test_vs_without_classification/columba_tested/classified_seq.train
tolerance = 1e-4
1.maxNGramLeng = 4
testFile = /Users/evermal/git/npl_tools/datasets/test_vs_without_classification/columba_tested/classified_seq.test
sigma = 3
printClassifierParam = 200
displayedColumn = 1
intern = true
useClassFeature = true
1.binnedLengths = 10,20,30
1.useNGrams = true
Reading dataset from /Users/evermal/git/npl_tools/datasets/test_vs_without_classification/columba_tested/classified_seq.train ...
WARNING: Number of tab-separated columns in /Users/evermal/git/npl_tools/datasets/test_vs_without_classification/columba_tested/classified_seq.train varies between 2 and 23
done [5.4s, 23955 items].
numDatums: 23955
numDatumsPerLabel: {TEST=67.0, WITHOUT_CLASSIFICATION=23888.0}
numLabels: 2 [WITHOUT_CLASSIFICATION, TEST]
numFeatures (Phi(X) types): 95264 [CLASS, 1-#-*, 1-#E- */, 1-#-tuff, 1-#-en, ...]

6270 examples in test set
Cls WITHOUT_CLASSIFICATION: TP=6264 FN=0 FP=6 TN=0; Acc 0.999 P 0.999 R 1.000 F1 1.000
Cls TEST: TP=0 FN=6 FP=0 TN=6264; Acc 0.999 P 1.000 R 0.000 F1 0.000
Accuracy/micro-averaged F1: 0.99904
Macro-averaged F1: 0.49976

8083 examples in test set

|Classification          | TP |FN |FP |TN  |ACC  | P   |  R  | F1  |
|------------------------|----|---|---|----|-----|-----|-----|-----|
|WITHOUT_CLASSIFICATION: |8032|7  |25 |19  |0.996|0.997|0.999|0.998|
|TEST:                   |19  |25 |7  |8032|0.996|0.731|0.432|0.543|

Accuracy/micro-averaged F1: 0.99604
Macro-averaged F1: 0.77043



