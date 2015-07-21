# Information of the dataset
Cross project validation

`$ python generate_classification_files.py columba apache-ant apache-jmeter argouml jfreechart password `

## Train 
All documentation and without classification comments from Apache Ant, Apache Jmeter, JfreeChart and ArgoUml

## Test

All documentation and without classification comments from Columba. 

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
 -prop /Users/evermal/git/npl_tools/datasets/documentation_vs_without_classification/columba_tested/dataset.prop
1.usePrefixSuffixNGrams = true
QNsize = 15
useQN = true
goldAnswerColumn = 0
1.minNGramLeng = 1
trainFile = /Users/evermal/git/npl_tools/datasets/documentation_vs_without_classification/columba_tested/classified_seq.train
tolerance = 1e-4
1.maxNGramLeng = 4
testFile = /Users/evermal/git/npl_tools/datasets/documentation_vs_without_classification/columba_tested/classified_seq.test
sigma = 3
printClassifierParam = 200
displayedColumn = 1
intern = true
useClassFeature = true
1.binnedLengths = 10,20,30
1.useNGrams = true
Reading dataset from /Users/evermal/git/npl_tools/datasets/documentation_vs_without_classification/columba_tested/classified_seq.train ...
WARNING: Number of tab-separated columns in /Users/evermal/git/npl_tools/datasets/documentation_vs_without_classification/columba_tested/classified_seq.train varies between 2 and 23
done [4.3s, 23921 items].
numDatums: 23921
numDatumsPerLabel: {DOCUMENTATION=33.0, WITHOUT_CLASSIFICATION=23888.0}
numLabels: 2 [WITHOUT_CLASSIFICATION, DOCUMENTATION]
numFeatures (Phi(X) types): 95025 [CLASS, 1-#-*, 1-#E- */, 1-#-tuff, 1-#-en, ...]

6280 examples in test set
Cls WITHOUT_CLASSIFICATION: TP=6264 FN=0 FP=16 TN=0; Acc 0.997 P 0.997 R 1.000 F1 0.999
Cls DOCUMENTATION: TP=0 FN=16 FP=0 TN=6264; Acc 0.997 P 1.000 R 0.000 F1 0.000
Accuracy/micro-averaged F1: 0.99745
Macro-averaged F1: 0.49936

8069 examples in test set

|Classification          | TP |FN |FP |TN  |ACC  | P   |  R  | F1  |
|------------------------|----|---|---|----|-----|-----|-----|-----|
|WITHOUT_CLASSIFICATION: |8039|0  |29 |1   |0.996|0.996|1.000|0.998|
|DOCUMENTATION:          |1   |29 |0  |8039|0.996|1.000|0.033|0.065|

Accuracy/micro-averaged F1: 0.99641
Macro-averaged F1: 0.53136

