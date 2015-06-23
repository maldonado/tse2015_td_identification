# Information of the dataset
Cross project validation

## Script call

`$ python generate_classification_files.py apache-jmeter jfreechart apache-ant argouml columba password `

## Train 
All defect and without classification comments from Apache Ant, ArgoUml, JfreeChart and Columba

## Test

All defect and without classification comments from Apache Jmeter. 

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

8166 examples in test set

|Classification          | TP |FN |FP |TN  |ACC  | P   |  R  | F1  |
|------------------------|----|---|---|----|-----|-----|-----|-----|
|WITHOUT_CLASSIFICATION: |7950|89 |68 |59  |0.981|0.992|0.989|0.990|
|DEFECT:                 |59  |68 |89 |7950|0.981|0.399|0.465|0.429|

Accuracy/micro-averaged F1: 0.98077
Macro-averaged F1: 0.70966

