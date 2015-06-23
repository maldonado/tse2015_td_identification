# Information of the dataset
Cross project validation

`$ python generate_classification_files.py columba apache-ant apache-jmeter argouml jfreechart password `

## Train 
All design and without classification comments from Apache Ant, Apache Jmeter, JfreeChart and ArgoUml

## Test

All design and without classification comments from Columba. 

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
trainFile = /Users/evermal/git/npl_tools/datasets/design_vs_without_classification/columba_tested/classified_seq.train
tolerance = 1e-4
1.maxNGramLeng = 4
testFile = /Users/evermal/git/npl_tools/datasets/design_vs_without_classification/columba_tested/classified_seq.test
sigma = 3
printClassifierParam = 200
displayedColumn = 1
intern = true
useClassFeature = true
1.binnedLengths = 10,20,30
1.useNGrams = true
Reading dataset from /Users/evermal/git/npl_tools/datasets/design_vs_without_classification/columba_tested/classified_seq.train ...
WARNING: Number of tab-separated columns in /Users/evermal/git/npl_tools/datasets/design_vs_without_classification/columba_tested/classified_seq.train varies between 2 and 23
done [5.1s, 25284 items].
numDatums: 25284
numDatumsPerLabel: {DESIGN=1396.0, WITHOUT_CLASSIFICATION=23888.0}
numLabels: 2 [WITHOUT_CLASSIFICATION, DESIGN]
numFeatures (Phi(X) types): 101590 [CLASS, 1-#-*, 1-#E- */, 1-#-tuff, 1-#-en, ...]
6390 examples in test set
Cls WITHOUT_CLASSIFICATION: TP=6250 FN=14 FP=41 TN=85; Acc 0.991 P 0.993 R 0.998 F1 0.996
Cls DESIGN: TP=85 FN=41 FP=14 TN=6250; Acc 0.991 P 0.859 R 0.675 F1 0.756
Accuracy/micro-averaged F1: 0.99139
Macro-averaged F1: 0.87559

8840 examples in test set

|Classification          | TP |FN |FP |TN  |ACC  | P   |  R  | F1  |
|------------------------|----|---|---|----|-----|-----|-----|-----|
|DESIGN:                 |722 |79 |229|7810|0.965|0.759|0.901|0.824|
|WITHOUT_CLASSIFICATION: |7810|229|79 |722 |0.965|0.990|0.972|0.981|

Accuracy/micro-averaged F1: 0.96516
Macro-averaged F1: 0.90243

