# Information of the dataset
Cross project validation

`$ python generate_classification_files.py columba apache-ant apache-jmeter argouml jfreechart password `

## Train 
All implementation and without classification comments from Apache Ant, Apache Jmeter, JfreeChart and ArgoUml

## Test

All implementation and without classification comments from Columba. 

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

WARNING: Number of tab-separated columns in /Users/evermal/git/npl_tools/datasets/implementation_vs_without_classification/columba_tested/classified_seq.train varies between 2 and 23
done [5.1s, 24602 items].

numDatums: 24602
numDatumsPerLabel: {WITHOUT_CLASSIFICATION=23888.0, IMPLEMENTATION=714.0}
numLabels: 2 [WITHOUT_CLASSIFICATION, IMPLEMENTATION]

6398 examples in test set

|Classification          | TP |FN |FP |TN  |ACC  | P   |  R  | F1  |
|------------------------|----|---|---|----|-----|-----|-----|-----|
|WITHOUT_CLASSIFICATION: |6252|12 |9  |125 |0.997|0.999|0.998|0.998|
|IMPLEMENTATION:         |125 |9  |12 |6252|0.997|0.912|0.933|0.923|

Accuracy/micro-averaged F1: 0.99672
Macro-averaged F1: 0.96042