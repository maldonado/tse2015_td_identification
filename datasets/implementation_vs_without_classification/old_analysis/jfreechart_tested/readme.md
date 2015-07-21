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

WARNING: Number of tab-separated columns in /Users/evermal/git/npl_tools/datasets/implementation_vs_without_classification/jfreechart_tested/classified_seq.train varies between 2 and 51
done [4.6s, 26776 items].

numDatums: 26776
numDatumsPerLabel: {WITHOUT_CLASSIFICATION=25953.0, IMPLEMENTATION=823.0}
numLabels: 2 [WITHOUT_CLASSIFICATION, IMPLEMENTATION]

4224 examples in test set

|Classification          | TP |FN |FP |TN  |ACC  | P   |  R  | F1  |
|------------------------|----|---|---|----|-----|-----|-----|-----|
|WITHOUT_CLASSIFICATION: |4196|3  |6  |19  |0.998|0.999|0.999|0.999|
|IMPLEMENTATION:         |19  |6  |3  |4196|0.998|0.864|0.760|0.809|

Accuracy/micro-averaged F1: 0.99787
Macro-averaged F1: 0.90372

