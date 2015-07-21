# Information of the dataset
Cross project validation

## Script call

`$ python generate_classification_files.py jfreechart apache-ant apache-jmeter argouml columba password `

## Train 
All comments from Apache Ant, Apache Jmeter, ArgoUml and Columba

## Test

All comments from Jfreechart. 

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
ColumnDataClassifier invoked on Tue Jun 23 11:56:43 EDT 2015 with arguments:
   -prop /Users/evermal/git/npl_tools/datasets/all_classes/jfreechart_tested/dataset.prop
1.usePrefixSuffixNGrams = true
QNsize = 15
useQN = true
goldAnswerColumn = 0
1.minNGramLeng = 1
trainFile = /Users/evermal/git/npl_tools/datasets/all_classes/jfreechart_tested/classified_seq.train
tolerance = 1e-4
1.maxNGramLeng = 4
testFile = /Users/evermal/git/npl_tools/datasets/all_classes/jfreechart_tested/classified_seq.test
sigma = 3
printClassifierParam = 200
displayedColumn = 1
intern = true
useClassFeature = true
1.binnedLengths = 10,20,30
1.useNGrams = true
Reading dataset from /Users/evermal/git/npl_tools/datasets/all_classes/jfreechart_tested/classified_seq.train ...
WARNING: Number of tab-separated columns in /Users/evermal/git/npl_tools/datasets/all_classes/jfreechart_tested/classified_seq.train varies between 2 and 51
done [5.2s, 28410 items].
numDatums: 28410
numDatumsPerLabel: {DOCUMENTATION=49.0, DESIGN=1338.0, TEST=72.0, WITHOUT_CLASSIFICATION=25953.0, DEFECT=175.0, IMPLEMENTATION=823.0}
numLabels: 6 [WITHOUT_CLASSIFICATION, DESIGN, TEST, DEFECT, IMPLEMENTATION, DOCUMENTATION]
numFeatures (Phi(X) types): 109464 [CLASS, 1-#-*, 1-#E- */, 1-#-tuff, 1-#-en, ...]

4418 examples in test set
Cls WITHOUT_CLASSIFICATION: TP=4157 FN=42 FP=126 TN=93; Acc 0.962 P 0.971 R 0.990 F1 0.980
Cls DESIGN: TP=40 FN=144 FP=40 TN=4194; Acc 0.958 P 0.500 R 0.217 F1 0.303
Cls TEST: TP=0 FN=1 FP=0 TN=4417; Acc 1.000 P 1.000 R 0.000 F1 0.000
Cls DEFECT: TP=0 FN=9 FP=14 TN=4395; Acc 0.995 P 0.000 R 0.000 F1 0.000
Cls IMPLEMENTATION: TP=19 FN=6 FP=22 TN=4371; Acc 0.994 P 0.463 R 0.760 F1 0.576
Cls DOCUMENTATION: TP=0 FN=0 FP=0 TN=4418; Acc 1.000 P 1.000 R 1.000 F1 1.000
Accuracy/micro-averaged F1: 0.95428
Macro-averaged F1: 0.47650


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





