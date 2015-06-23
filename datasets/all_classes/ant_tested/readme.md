# Information of the dataset
Cross project validation

## Script call

`$ python generate_classification_files.py apache-ant apache-jmeter argouml jfreechart columba password `

## Train 
All comments from ArgoUml, Apache Jmeter, JfreeChart and Columba

## Test

All comments from Apache ant. 

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

.usePrefixSuffixNGrams = true
QNsize = 15
useQN = true
goldAnswerColumn = 0
1.minNGramLeng = 1
trainFile = /Users/evermal/git/npl_tools/datasets/all_classes/ant_tested/classified_seq.train
tolerance = 1e-4
1.maxNGramLeng = 4
testFile = /Users/evermal/git/npl_tools/datasets/all_classes/ant_tested/classified_seq.test
sigma = 3
printClassifierParam = 200
displayedColumn = 1
intern = true
useClassFeature = true
1.binnedLengths = 10,20,30
1.useNGrams = true
Reading dataset from /Users/evermal/git/npl_tools/datasets/all_classes/ant_tested/classified_seq.train ...
WARNING: Number of tab-separated columns in /Users/evermal/git/npl_tools/datasets/all_classes/ant_tested/classified_seq.train varies between 2 and 51
done [5.1s, 28727 items].
numDatums: 28727
numDatumsPerLabel: {DOCUMENTATION=49.0, DESIGN=1427.0, TEST=63.0, WITHOUT_CLASSIFICATION=26185.0, DEFECT=171.0, IMPLEMENTATION=832.0}
numLabels: 6 [DESIGN, WITHOUT_CLASSIFICATION, IMPLEMENTATION, TEST, DEFECT, DOCUMENTATION]
numFeatures (Phi(X) types): 104548 [CLASS, 1-#- F, 1-#E- */, 1-#-ets , 1-#-t , ...]


4101 examples in test set
Cls DESIGN: TP=28 FN=67 FP=34 TN=3972; Acc 0.975 P 0.452 R 0.295 F1 0.357
Cls WITHOUT_CLASSIFICATION: TP=3940 FN=27 FP=85 TN=49; Acc 0.973 P 0.979 R 0.993 F1 0.986
Cls IMPLEMENTATION: TP=4 FN=12 FP=9 TN=4076; Acc 0.995 P 0.308 R 0.250 F1 0.276
Cls TEST: TP=0 FN=10 FP=0 TN=4091; Acc 0.998 P 1.000 R 0.000 F1 0.000
Cls DEFECT: TP=0 FN=13 FP=1 TN=4087; Acc 0.997 P 0.000 R 0.000 F1 0.000
Cls DOCUMENTATION: TP=0 FN=0 FP=0 TN=4101; Acc 1.000 P 1.000 R 1.000 F1 1.000
Accuracy/micro-averaged F1: 0.96854
Macro-averaged F1: 0.43642



