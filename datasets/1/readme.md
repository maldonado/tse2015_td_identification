# Information of the dataset
Cross project validation

## Train 
All comments from Apache Ant, Apache Jmeter, JfreeChart and Columba

## Test

All comments from ArgoUml. 

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

9788 examples in test set

|Classification          | TP |FN |FP |TN  |ACC  | P   |  R  | F1  |
|------------------------|----|---|---|----|-----|-----|-----|-----|
|DESIGN:                 |667 |134|622|8365|0.923|0.517|0.833|0.638|
|WITHOUT_CLASSIFICATION: |7807|232|234|1515|0.952|0.971|0.971|0.971|
|BUG_FIX_COMMENT:        |4   |92 |4  |9688|0.990|0.500|0.042|0.077|
|IMPLEMENTATION:         |354 |297|41 |9096|0.965|0.896|0.544|0.677|
|TEST:                   |8   |36 |7  |9737|0.996|0.533|0.182|0.271|
|DEFECT:                 |7   |120|31 |9630|0.985|0.184|0.055|0.085|
|DOCUMENTATION:          |0   |30 |2  |9756|0.997|0.000|0.000|0.000|
|:                       |0   |0  |0  |9788|1.000|1.000|1.000|1.000|

Accuracy/micro-averaged F1: 0.90386
Macro-averaged F1: 0.46489

