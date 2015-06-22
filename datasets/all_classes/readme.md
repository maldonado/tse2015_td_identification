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

9692 examples in test set

|Classification          | TP |FN |FP |TN  |ACC  | P   |  R  | F1  |
|------------------------|----|---|---|----|-----|-----|-----|-----|
|DESIGN:                 |668 |133|602|8289|0.924|0.526|0.834|0.645|
|WITHOUT_CLASSIFICATION: |7810|229|167|1486|0.959|0.979|0.972|0.975|
|IMPLEMENTATION:         |351 |300|39 |9002|0.965|0.900|0.539|0.674|
|TEST:                   |8   |36 |6  |9642|0.996|0.571|0.182|0.276|
|DEFECT:                 |9   |118|30 |9535|0.985|0.231|0.071|0.108|
|DOCUMENTATION:          |0   |30 |2  |9660|0.997|0.000|0.000|0.000|

Accuracy/micro-averaged F1: 0.91271
Macro-averaged F1: 0.44650





