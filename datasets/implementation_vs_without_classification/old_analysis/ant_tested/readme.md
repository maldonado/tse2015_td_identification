# Information of the dataset
Cross project validation

## Script call

`$ python generate_classification_files.py apache-ant apache-jmeter argouml jfreechart columba password `

## Train 
All implementation and without classification comments from ArgoUml, Apache Jmeter, JfreeChart and Columba

## Test

All implementation and without classification comments from Apache ant. 

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
  
WARNING: Number of tab-separated columns in /Users/evermal/git/npl_tools/datasets/implementation_vs_without_classification/ant_tested/classified_seq.train varies between 2 and 51
done [5.2s, 27017 items].

numDatums: 27017
numDatumsPerLabel: {WITHOUT_CLASSIFICATION=26185.0, IMPLEMENTATION=832.0}
numLabels: 2 [WITHOUT_CLASSIFICATION, IMPLEMENTATION]

Cls WITHO     |3965|2 |11|5   |0.997|0.997|0.999|0.998|
Cls IMPLETAT: |5   |11|2 |3965|0.997|0.714|0.312|0.435|


3983 examples in test set

|Classification          | TP |FN |FP |TN  |ACC  | P   |  R  | F1  |
|------------------------|----|---|---|----|-----|-----|-----|-----|
|WITHOUT_CLASSIFICATION: |3965|2  |11 |5   |0.997|0.997|0.999|0.998|
|IMPLEMENTATION:         |5   |11 |2  |3965|0.997|0.714|0.312|0.435|

Accuracy/micro-averaged F1: 0.99674
Macro-averaged F1: 0.71657

