# Information of the dataset
Cross project validation

## Script call

`$ python generate_classification_files.py apache-jmeter jfreechart apache-ant argouml columba password `

## Train 
All design and without classification comments from Apache Ant, ArgoUml, JfreeChart and Columba

## Test

All design and without classification comments from Apache Jmeter. 

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

WARNING: Number of tab-separated columns in /Users/evermal/git/npl_tools/datasets/design_vs_without_classification/jmeter_tested/classified_seq.train varies between 2 and 51
done [4.6s, 23675 items].

numDatums: 23675
numDatumsPerLabel: {DESIGN=1206.0, WITHOUT_CLASSIFICATION=22469.0}
numLabels: 2 [WITHOUT_CLASSIFICATION, DESIGN]

7999 examples in test set

|Classification          | TP |FN |FP |TN  |ACC  | P   |  R  | F1  |
|------------------------|----|---|---|----|-----|-----|-----|-----|
|DESIGN:                 |199 |117|41 |7642|0.980|0.829|0.630|0.716|
|WITHOUT_CLASSIFICATION: |7642|41 |117| 199|0.980|0.985|0.995|0.990|

Accuracy/micro-averaged F1: 0.98025
Macro-averaged F1: 0.85280

