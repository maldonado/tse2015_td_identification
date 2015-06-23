# Information of the dataset
Cross project validation

## Script call

`$ python generate_classification_files.py apache-jmeter jfreechart apache-ant argouml columba password `

## Train 
All documentation and without classification comments from Apache Ant, ArgoUml, JfreeChart and Columba

## Test

All documentation and without classification comments from Apache Jmeter. 

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

8069 examples in test set

|Classification          | TP |FN |FP |TN  |ACC  | P   |  R  | F1  |
|------------------------|----|---|---|----|-----|-----|-----|-----|
|WITHOUT_CLASSIFICATION: |8039|0  |29 |1   |0.996|0.996|1.000|0.998|
|DOCUMENTATION:          |1   |29 |0  |8039|0.996|1.000|0.033|0.065|

Accuracy/micro-averaged F1: 0.99641
Macro-averaged F1: 0.53136

