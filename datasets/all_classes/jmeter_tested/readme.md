# Information of the dataset
Cross project validation

## Script call

`$ python generate_classification_files.py apache-jmeter jfreechart apache-ant argouml columba password `

## Train 
All comments from Apache Ant, ArgoUml, JfreeChart and Columba

## Test

All comments from Apache Jmeter. 

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
ColumnDataClassifier invoked on Tue Jun 23 11:57:50 EDT 2015 with arguments:
   -prop /Users/evermal/git/npl_tools/datasets/all_classes/jmeter_tested/dataset.prop
1.usePrefixSuffixNGrams = true
QNsize = 15
useQN = true
goldAnswerColumn = 0
1.minNGramLeng = 1
trainFile = /Users/evermal/git/npl_tools/datasets/all_classes/jmeter_tested/classified_seq.train
tolerance = 1e-4
1.maxNGramLeng = 4
testFile = /Users/evermal/git/npl_tools/datasets/all_classes/jmeter_tested/classified_seq.test
sigma = 3
printClassifierParam = 200
displayedColumn = 1
intern = true
useClassFeature = true
1.binnedLengths = 10,20,30
1.useNGrams = true
Reading dataset from /Users/evermal/git/npl_tools/datasets/all_classes/jmeter_tested/classified_seq.train ...
WARNING: Number of tab-separated columns in /Users/evermal/git/npl_tools/datasets/all_classes/jmeter_tested/classified_seq.train varies between 2 and 51
done [4.9s, 24770 items].
numDatums: 24770
numDatumsPerLabel: {DOCUMENTATION=46.0, DESIGN=1206.0, TEST=61.0, WITHOUT_CLASSIFICATION=22469.0, DEFECT=162.0, IMPLEMENTATION=826.0}
numLabels: 6 [WITHOUT_CLASSIFICATION, DESIGN, DEFECT, IMPLEMENTATION, TEST, DOCUMENTATION]
numFeatures (Phi(X) types): 103406 [CLASS, 1-#-,, 1-#--, 1-#-/, 1-#-0, ...]

8058 examples in test set
Cls WITHOUT_CLASSIFICATION: TP=7634 FN=49 FP=133 TN=242; Acc 0.977 P 0.983 R 0.994 F1 0.988
Cls DESIGN: TP=156 FN=160 FP=53 TN=7689; Acc 0.974 P 0.746 R 0.494 F1 0.594
Cls DEFECT: TP=1 FN=21 FP=17 TN=8019; Acc 0.995 P 0.056 R 0.045 F1 0.050
Cls IMPLEMENTATION: TP=4 FN=18 FP=53 TN=7983; Acc 0.991 P 0.070 R 0.182 F1 0.101
Cls TEST: TP=3 FN=9 FP=3 TN=8043; Acc 0.999 P 0.500 R 0.250 F1 0.333
Cls DOCUMENTATION: TP=1 FN=2 FP=0 TN=8055; Acc 1.000 P 1.000 R 0.333 F1 0.500
Accuracy/micro-averaged F1: 0.96786
Macro-averaged F1: 0.42785

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





