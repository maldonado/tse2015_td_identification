# Information of the dataset
Cross project validation

## Train 
All defect and without classification comments from Apache Ant, Apache Jmeter, JfreeChart and Columba

## Test

All defect and without classification comments from ArgoUml. 

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
ColumnDataClassifier invoked on Tue Jun 23 12:02:32 EDT 2015 with arguments:
   -prop /Users/evermal/git/npl_tools/datasets/defect_vs_without_classification/argo_tested/dataset.prop
1.usePrefixSuffixNGrams = true
QNsize = 15
useQN = true
goldAnswerColumn = 0
1.minNGramLeng = 1
trainFile = /Users/evermal/git/npl_tools/datasets/defect_vs_without_classification/argo_tested/classified_seq.train
tolerance = 1e-4
1.maxNGramLeng = 4
testFile = /Users/evermal/git/npl_tools/datasets/defect_vs_without_classification/argo_tested/classified_seq.test
sigma = 3
printClassifierParam = 200
displayedColumn = 1
intern = true
useClassFeature = true
1.binnedLengths = 10,20,30
1.useNGrams = true
Reading dataset from /Users/evermal/git/npl_tools/datasets/defect_vs_without_classification/argo_tested/classified_seq.train ...
WARNING: Number of tab-separated columns in /Users/evermal/git/npl_tools/datasets/defect_vs_without_classification/argo_tested/classified_seq.train varies between 2 and 51
done [3.2s, 22170 items].
numDatums: 22170
numDatumsPerLabel: {WITHOUT_CLASSIFICATION=22113.0, DEFECT=57.0}
numLabels: 2 [WITHOUT_CLASSIFICATION, DEFECT]
numFeatures (Phi(X) types): 90595 [CLASS, 1-Len-0-10, 1-#B-//?, 1-#-//??, 1-#B-//??, ...]

8166 examples in test set
Cls WITHOUT_CLASSIFICATION: TP=7950 FN=89 FP=68 TN=59; Acc 0.981 P 0.992 R 0.989 F1 0.990
Cls DEFECT: TP=59 FN=68 FP=89 TN=7950; Acc 0.981 P 0.399 R 0.465 F1 0.429
Accuracy/micro-averaged F1: 0.98077
Macro-averaged F1: 0.70966

8166 examples in test set

|Classification          | TP |FN |FP |TN  |ACC  | P   |  R  | F1  |
|------------------------|----|---|---|----|-----|-----|-----|-----|
|WITHOUT_CLASSIFICATION: |7950|89 |68 |59  |0.981|0.992|0.989|0.990|
|DEFECT:                 |59  |68 |89 |7950|0.981|0.399|0.465|0.429|

2560 examples in test set
Cls IMPLEMENTATION: TP=15 FN=49 FP=3 TN=2493; Acc 0.980 P 0.833 R 0.234 F1 0.366
Cls WITHOUT_CLASSIFICATION: TP=2493 FN=3 FP=49 TN=15; Acc 0.980 P 0.981 R 0.999 F1 0.990
Accuracy/micro-averaged F1: 0.97969
Macro-averaged F1: 0.67777



Accuracy/micro-averaged F1: 0.98077
Macro-averaged F1: 0.70966

