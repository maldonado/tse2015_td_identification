# Information of the dataset
Cross project validation

## Train 
All design and without classification comments from Apache Ant, Apache Jmeter, JfreeChart and Columba

## Test

All design and without classification comments from ArgoUml. 

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

WARNING: Number of tab-separated columns in /Users/evermal/git/npl_tools/datasets/design_vs_without_classification/argo_tested/classified_seq.train varies between 2 and 51
done [3.6s, 22834 items].

numDatums: 22834
numDatumsPerLabel: {DESIGN=721.0, WITHOUT_CLASSIFICATION=22113.0}
numLabels: 2 [DESIGN, WITHOUT_CLASSIFICATION]


8840 examples in test set

|Classification          | TP |FN |FP |TN  |ACC  | P   |  R  | F1  |
|------------------------|----|---|---|----|-----|-----|-----|-----|
|DESIGN:                 |722 |79 |229|7810|0.965|0.759|0.901|0.824|
|WITHOUT_CLASSIFICATION: |7810|229|79 |722 |0.965|0.990|0.972|0.981|

Accuracy/micro-averaged F1: 0.96516
Macro-averaged F1: 0.90243

