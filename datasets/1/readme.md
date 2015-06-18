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
Cls DESIGN:                 TP=667  FN=134 FP=622 TN=8365; Acc 0.923 P 0.517 R 0.833 F1 0.638
Cls WITHOUT_CLASSIFICATION: TP=7807 FN=232 FP=234 TN=1515; Acc 0.952 P 0.971 R 0.971 F1 0.971
Cls BUG_FIX_COMMENT:        TP=4    FN=92  FP=4   TN=9688; Acc 0.990 P 0.500 R 0.042 F1 0.077
Cls IMPLEMENTATION:         TP=354  FN=297 FP=41  TN=9096; Acc 0.965 P 0.896 R 0.544 F1 0.677
Cls TEST:                   TP=8    FN=36  FP=7   TN=9737; Acc 0.996 P 0.533 R 0.182 F1 0.271
Cls DEFECT:                 TP=7    FN=120 FP=31  TN=9630; Acc 0.985 P 0.184 R 0.055 F1 0.085
Cls DOCUMENTATION:          TP=0    FN=30  FP=2   TN=9756; Acc 0.997 P 0.000 R 0.000 F1 0.000
Cls :                       TP=0    FN=0   FP=0   TN=9788; Acc 1.000 P 1.000 R 1.000 F1 1.000
Accuracy/micro-averaged F1: 0.90386
Macro-averaged F1: 0.46489

