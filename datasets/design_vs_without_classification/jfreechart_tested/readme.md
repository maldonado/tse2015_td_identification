# Information of the dataset
Cross project validation

## Script call

`$ python generate_classification_files.py jfreechart apache-ant apache-jmeter argouml columba password `

## Train 
All design and without classification comments from Apache Ant, Apache Jmeter, ArgoUml and Columba

## Test

All design and without classification comments from Jfreechart. 

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
trainFile = /Users/evermal/git/npl_tools/datasets/design_vs_without_classification/jfreechart_tested/classified_seq.train
tolerance = 1e-4
1.maxNGramLeng = 4
testFile = /Users/evermal/git/npl_tools/datasets/design_vs_without_classification/jfreechart_tested/classified_seq.test
sigma = 3
printClassifierParam = 200
displayedColumn = 1
intern = true
useClassFeature = true
1.binnedLengths = 10,20,30
1.useNGrams = true
Reading dataset from /Users/evermal/git/npl_tools/datasets/design_vs_without_classification/jfreechart_tested/classified_seq.train ...
WARNING: Number of tab-separated columns in /Users/evermal/git/npl_tools/datasets/design_vs_without_classification/jfreechart_tested/classified_seq.train varies between 2 and 51
done [5.4s, 27291 items].
numDatums: 27291
numDatumsPerLabel: {DESIGN=1338.0, WITHOUT_CLASSIFICATION=25953.0}
numLabels: 2 [WITHOUT_CLASSIFICATION, DESIGN]
numFeatures (Phi(X) types): 106084 [CLASS, 1-#-*, 1-#E- */, 1-#-tuff, 1-#-en, ...]
4383 examples in test set
Cls WITHOUT_CLASSIFICATION: TP=4160 FN=39 FP=125 TN=59; Acc 0.963 P 0.971 R 0.991 F1 0.981
Cls DESIGN: TP=59 FN=125 FP=39 TN=4160; Acc 0.963 P 0.602 R 0.321 F1 0.418
Accuracy/micro-averaged F1: 0.96258
Macro-averaged F1: 0.69955

8840 examples in test set

|Classification          | TP |FN |FP |TN  |ACC  | P   |  R  | F1  |
|------------------------|----|---|---|----|-----|-----|-----|-----|
|DESIGN:                 |722 |79 |229|7810|0.965|0.759|0.901|0.824|
|WITHOUT_CLASSIFICATION: |7810|229|79 |722 |0.965|0.990|0.972|0.981|

Accuracy/micro-averaged F1: 0.96516
Macro-averaged F1: 0.90243

