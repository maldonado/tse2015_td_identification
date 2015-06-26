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

WARNING: Number of tab-separated columns in /Users/evermal/git/npl_tools/datasets/design_vs_without_classification/columba_tested/classified_seq.train varies between 2 and 23
done [5.1s, 25284 items].

numDatums: 25284
numDatumsPerLabel: {DESIGN=1396.0, WITHOUT_CLASSIFICATION=23888.0}
numLabels: 2 [WITHOUT_CLASSIFICATION, DESIGN]


Cls WITHOUT |6250|14|41|85  |0.991|0.993|0.998|0.996|
Cls DESIGN: |85  |41|14|6250|0.991|0.859|0.675|0.756|


6390 examples in test set

|Classification          | TP |FN |FP |TN  |ACC  | P   |  R  | F1  |
|------------------------|----|---|---|----|-----|-----|-----|-----|
|DESIGN:                 |85  |41 |14 |6250|0.991|0.859|0.675|0.756|
|WITHOUT_CLASSIFICATION: |6250|14 |41 |85  |0.991|0.993|0.998|0.996|

Accuracy/micro-averaged F1: 0.99139
Macro-averaged F1: 0.87559

