# !/bin/bash
for filename in ./training-data/*;
do python3 train-ner.py "${filename}";
done