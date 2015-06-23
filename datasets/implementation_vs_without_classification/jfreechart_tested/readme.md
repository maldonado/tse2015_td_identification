# Information of the dataset
Cross project validation

## Script call

`$ python generate_classification_files.py jfreechart apache-ant apache-jmeter argouml columba password `

## Train 
All implementation and without classification comments from Apache Ant, Apache Jmeter, ArgoUml and Columba

## Test

All implementation and without classification comments from Jfreechart. 

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
trainFile = /Users/evermal/git/npl_tools/datasets/implementation_vs_without_classification/jfreechart_tested/classified_seq.train
tolerance = 1e-4
1.maxNGramLeng = 4
testFile = /Users/evermal/git/npl_tools/datasets/implementation_vs_without_classification/jfreechart_tested/classified_seq.test
sigma = 3
printClassifierParam = 200
displayedColumn = 1
intern = true
useClassFeature = true
1.binnedLengths = 10,20,30
1.useNGrams = true
Reading dataset from /Users/evermal/git/npl_tools/datasets/implementation_vs_without_classification/jfreechart_tested/classified_seq.train ...
WARNING: Number of tab-separated columns in /Users/evermal/git/npl_tools/datasets/implementation_vs_without_classification/jfreechart_tested/classified_seq.train varies between 2 and 51
done [4.6s, 26776 items].
numDatums: 26776
numDatumsPerLabel: {WITHOUT_CLASSIFICATION=25953.0, IMPLEMENTATION=823.0}
numLabels: 2 [WITHOUT_CLASSIFICATION, IMPLEMENTATION]
numFeatures (Phi(X) types): 100934 [CLASS, 1-#-*, 1-#E- */, 1-#-tuff, 1-#-en, ...]

4224 examples in test set
Cls WITHOUT_CLASSIFICATION: TP=4196 FN=3 FP=6 TN=19; Acc 0.998 P 0.999 R 0.999 F1 0.999
Cls IMPLEMENTATION: TP=19 FN=6 FP=3 TN=4196; Acc 0.998 P 0.864 R 0.760 F1 0.809
Accuracy/micro-averaged F1: 0.99787
Macro-averaged F1: 0.90372
8690 examples in test set

|Classification          | TP |FN |FP |TN  |ACC  | P   |  R  | F1  |
|------------------------|----|---|---|----|-----|-----|-----|-----|
|WITHOUT_CLASSIFICATION: |7918|121|139|512 |0.970|0.983|0.985|0.984|
|IMPLEMENTATION:         |512 |139|121|7918|0.970|0.809|0.786|0.798|

Accuracy/micro-averaged F1: 0.97008
Macro-averaged F1: 0.89068

