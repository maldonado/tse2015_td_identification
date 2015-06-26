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

WARNING: Number of tab-separated columns in /Users/evermal/git/npl_tools/datasets/design_vs_without_classification/jfreechart_tested/classified_seq.train varies between 2 and 51
done [5.4s, 27291 items].

numDatums: 27291
numDatumsPerLabel: {DESIGN=1338.0, WITHOUT_CLASSIFICATION=25953.0}
numLabels: 2 [WITHOUT_CLASSIFICATION, DESIGN]

4383 examples in test set

|Classification          | TP |FN |FP |TN  |ACC  | P   |  R  | F1  |
|------------------------|----|---|---|----|-----|-----|-----|-----|
|DESIGN:                 |59  |125|39 |4160|0.963|0.602|0.321|0.418|
|WITHOUT_CLASSIFICATION: |4160|39 |125|59  |0.963|0.971|0.991|0.981|

Accuracy/micro-averaged F1: 0.96258
Macro-averaged F1: 0.69955


