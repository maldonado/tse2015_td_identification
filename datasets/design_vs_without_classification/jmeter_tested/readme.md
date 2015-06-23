# Information of the dataset
Cross project validation

## Script call

`$ python generate_classification_files.py apache-jmeter jfreechart apache-ant argouml columba password `

## Train 
All design and without classification comments from Apache Ant, ArgoUml, JfreeChart and Columba

## Test

All design and without classification comments from Apache Jmeter. 

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
trainFile = /Users/evermal/git/npl_tools/datasets/design_vs_without_classification/jmeter_tested/classified_seq.train
tolerance = 1e-4
1.maxNGramLeng = 4
testFile = /Users/evermal/git/npl_tools/datasets/design_vs_without_classification/jmeter_tested/classified_seq.test
sigma = 3
printClassifierParam = 200
displayedColumn = 1
intern = true
useClassFeature = true
1.binnedLengths = 10,20,30
1.useNGrams = true
Reading dataset from /Users/evermal/git/npl_tools/datasets/design_vs_without_classification/jmeter_tested/classified_seq.train ...
WARNING: Number of tab-separated columns in /Users/evermal/git/npl_tools/datasets/design_vs_without_classification/jmeter_tested/classified_seq.train varies between 2 and 51
done [4.6s, 23675 items].
numDatums: 23675
numDatumsPerLabel: {DESIGN=1206.0, WITHOUT_CLASSIFICATION=22469.0}
numLabels: 2 [WITHOUT_CLASSIFICATION, DESIGN]
numFeatures (Phi(X) types): 99937 [CLASS, 1-#-,, 1-#--, 1-#-/, 1-#-0, ...]

8840 examples in test set

7999 examples in test set
Cls WITHOUT_CLASSIFICATION: TP=7642 FN=41 FP=117 TN=199; Acc 0.980 P 0.985 R 0.995 F1 0.990
Cls DESIGN: TP=199 FN=117 FP=41 TN=7642; Acc 0.980 P 0.829 R 0.630 F1 0.716
Accuracy/micro-averaged F1: 0.98025
Macro-averaged F1: 0.85280

|Classification          | TP |FN |FP |TN  |ACC  | P   |  R  | F1  |
|------------------------|----|---|---|----|-----|-----|-----|-----|
|DESIGN:                 |722 |79 |229|7810|0.965|0.759|0.901|0.824|
|WITHOUT_CLASSIFICATION: |7810|229|79 |722 |0.965|0.990|0.972|0.981|

Accuracy/micro-averaged F1: 0.96516
Macro-averaged F1: 0.90243

