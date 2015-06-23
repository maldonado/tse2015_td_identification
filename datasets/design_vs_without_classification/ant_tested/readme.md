# Information of the dataset
Cross project validation

## Script call

`$ python generate_classification_files.py apache-ant apache-jmeter argouml jfreechart columba password `

## Train 
All design and without classification comments from ArgoUml, Apache Jmeter, JfreeChart and Columba

## Test

All design and without classification comments from Apache ant. 

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
usePrefixSuffixNGrams = true
QNsize = 15
useQN = true
goldAnswerColumn = 0
1.minNGramLeng = 1
trainFile = /Users/evermal/git/npl_tools/datasets/design_vs_without_classification/ant_tested/classified_seq.train
tolerance = 1e-4
1.maxNGramLeng = 4
testFile = /Users/evermal/git/npl_tools/datasets/design_vs_without_classification/ant_tested/classified_seq.test
sigma = 3
printClassifierParam = 200
displayedColumn = 1
intern = true
useClassFeature = true
1.binnedLengths = 10,20,30
1.useNGrams = true
Reading dataset from /Users/evermal/git/npl_tools/datasets/design_vs_without_classification/ant_tested/classified_seq.train ...
WARNING: Number of tab-separated columns in /Users/evermal/git/npl_tools/datasets/design_vs_without_classification/ant_tested/classified_seq.train varies between 2 and 51
done [5.0s, 27612 items].
numDatums: 27612
numDatumsPerLabel: {DESIGN=1427.0, WITHOUT_CLASSIFICATION=26185.0}
numLabels: 2 [DESIGN, WITHOUT_CLASSIFICATION]
numFeatures (Phi(X) types): 101794 [CLASS, 1-#- F, 1-#E- */, 1-#-ets , 1-#-t , ...]

4062 examples in test set
Cls DESIGN: TP=29 FN=66 FP=25 TN=3942; Acc 0.978 P 0.537 R 0.305 F1 0.389
Cls WITHOUT_CLASSIFICATION: TP=3942 FN=25 FP=66 TN=29; Acc 0.978 P 0.984 R 0.994 F1 0.989
Accuracy/micro-averaged F1: 0.97760
Macro-averaged F1: 0.68893

8840 examples in test set

|Classification          | TP |FN |FP |TN  |ACC  | P   |  R  | F1  |
|------------------------|----|---|---|----|-----|-----|-----|-----|
|DESIGN:                 |722 |79 |229|7810|0.965|0.759|0.901|0.824|
|WITHOUT_CLASSIFICATION: |7810|229|79 |722 |0.965|0.990|0.972|0.981|

Accuracy/micro-averaged F1: 0.96516
Macro-averaged F1: 0.90243

