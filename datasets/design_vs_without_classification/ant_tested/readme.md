# Information of the dataset
Cross project validation

## Script call

`$ python generate_classification_files.py apache-ant apache-jmeter argouml jfreechart columba password `

## Train 
All design and without classification comments from ArgoUml, Apache Jmeter, JfreeChart and Columba

## Test

All design and without classification comments from Apache ant. 

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


WARNING: Number of tab-separated columns in /Users/evermal/git/npl_tools/datasets/design_vs_without_classification/ant_tested/classified_seq.train varies between 2 and 51
done [5.0s, 27612 items].

numDatums: 27612
numDatumsPerLabel: {DESIGN=1427.0, WITHOUT_CLASSIFICATION=26185.0}
numLabels: 2 [DESIGN, WITHOUT_CLASSIFICATION]


4062 examples in test set

|Classification          | TP |FN |FP |TN  |ACC  | P   |  R  | F1  |
|------------------------|----|---|---|----|-----|-----|-----|-----|
|DESIGN:                 |29  |66 |25 |3942|0.978|0.537|0.305|0.389|
|WITHOUT_CLASSIFICATION: |3942|25 |66 |29  |0.978|0.984|0.994|0.989|

Accuracy/micro-averaged F1: 0.97760
Macro-averaged F1: 0.68893

