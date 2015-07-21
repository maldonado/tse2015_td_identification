# Information of the dataset
Cross project validation

## Script call

`$ python generate_classification_files.py argouml apache-jmeter apache-ant jfreechart columba password `

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

ColumnDataClassifier invoked on Tue Jun 23 11:54:23 EDT 2015 with arguments:
   -prop /Users/evermal/git/npl_tools/datasets/all_classes/argo_tested/dataset.prop
1.usePrefixSuffixNGrams = true
QNsize = 15
useQN = true
goldAnswerColumn = 0
1.minNGramLeng = 1
trainFile = /Users/evermal/git/npl_tools/datasets/all_classes/argo_tested/classified_seq.train
tolerance = 1e-4
1.maxNGramLeng = 4
testFile = /Users/evermal/git/npl_tools/datasets/all_classes/argo_tested/classified_seq.test
sigma = 3
printClassifierParam = 200
displayedColumn = 1
intern = true
useClassFeature = true
1.binnedLengths = 10,20,30
1.useNGrams = true
Reading dataset from /Users/evermal/git/npl_tools/datasets/all_classes/argo_tested/classified_seq.train ...
WARNING: Number of tab-separated columns in /Users/evermal/git/npl_tools/datasets/all_classes/argo_tested/classified_seq.train varies between 2 and 51
done [3.5s, 23136 items].
numDatums: 23136
numDatumsPerLabel: {DOCUMENTATION=19.0, DESIGN=721.0, TEST=29.0, WITHOUT_CLASSIFICATION=22113.0, DEFECT=57.0, IMPLEMENTATION=197.0}
numLabels: 6 [DESIGN, WITHOUT_CLASSIFICATION, IMPLEMENTATION, TEST, DEFECT, DOCUMENTATION]
numFeatures (Phi(X) types): 94820 [CLASS, 1-#- F, 1-#E- */, 1-#-ets , 1-#-t , ...]

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





