# Information of the dataset
Cross project validation

`$ python generate_classification_files.py columba apache-ant apache-jmeter argouml jfreechart password `

## Train 
All comments from Apache Ant, Apache Jmeter, JfreeChart and ArgoUml

## Test

All comments from Columba. 

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
ColumnDataClassifier invoked on Tue Jun 23 11:55:10 EDT 2015 with arguments:
   -prop /Users/evermal/git/npl_tools/datasets/all_classes/columba_tested/dataset.prop
1.usePrefixSuffixNGrams = true
QNsize = 15
useQN = true
goldAnswerColumn = 0
1.minNGramLeng = 1
trainFile = /Users/evermal/git/npl_tools/datasets/all_classes/columba_tested/classified_seq.train
tolerance = 1e-4
1.maxNGramLeng = 4
testFile = /Users/evermal/git/npl_tools/datasets/all_classes/columba_tested/classified_seq.test
sigma = 3
printClassifierParam = 200
displayedColumn = 1
intern = true
useClassFeature = true
1.binnedLengths = 10,20,30
1.useNGrams = true
Reading dataset from /Users/evermal/git/npl_tools/datasets/all_classes/columba_tested/classified_seq.train ...
WARNING: Number of tab-separated columns in /Users/evermal/git/npl_tools/datasets/all_classes/columba_tested/classified_seq.train varies between 2 and 23
done [5.0s, 26269 items].
numDatums: 26269
numDatumsPerLabel: {DOCUMENTATION=33.0, DESIGN=1396.0, TEST=67.0, WITHOUT_CLASSIFICATION=23888.0, DEFECT=171.0, IMPLEMENTATION=714.0}
numLabels: 6 [WITHOUT_CLASSIFICATION, DESIGN, TEST, DEFECT, IMPLEMENTATION, DOCUMENTATION]
numFeatures (Phi(X) types): 104981 [CLASS, 1-#-*, 1-#E- */, 1-#-tuff, 1-#-en, ...]


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

6559 examples in test set
Cls WITHOUT_CLASSIFICATION: TP=6247 FN=17 FP=48 TN=247; Acc 0.990 P 0.992 R 0.997 F1 0.995
Cls DESIGN: TP=68 FN=58 FP=53 TN=6380; Acc 0.983 P 0.562 R 0.540 F1 0.551
Cls TEST: TP=1 FN=5 FP=0 TN=6553; Acc 0.999 P 1.000 R 0.167 F1 0.286
Cls DEFECT: TP=3 FN=10 FP=3 TN=6543; Acc 0.998 P 0.500 R 0.231 F1 0.316
Cls IMPLEMENTATION: TP=107 FN=27 FP=29 TN=6396; Acc 0.991 P 0.787 R 0.799 F1 0.793
Cls DOCUMENTATION: TP=0 FN=16 FP=0 TN=6543; Acc 0.998 P 1.000 R 0.000 F1 0.000
Accuracy/micro-averaged F1: 0.97972
Macro-averaged F1: 0.48992



