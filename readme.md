# Random Walk Graph Modeling
Efficiently Vectorize Graphs using Random Walks

## Prerequisites
- Python (v3.6 or later)
- scikit-learn

## Generate datasets
Comment out some lines of `generate.py` and
```
$ python3 generate.py
```

## Run
Classify two kinds of graphs. Specify datasets generated by the process above.
```
$ python3 main.py
```

## Sample
Generate datasets for ER graphs and SB graphs, then classify two.
```
$ echo 'er
sb' | python3 generate.py &&\
echo 'er
sb' | python3 main.py
```
