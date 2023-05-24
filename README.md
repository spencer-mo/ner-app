# ner-app

### Experimental repo on automated training of linguistic models based on dictionaries, vectors, and contextual mapping using spaCy in Python to accept new NER (named-entity recognition) parameters

## entity-analysis.py

#### Utilizes **spaCy** and returns entities of Amazon text snippet

### Expected output:

```
Amazon.com, Inc. ORG
Amazon ORG
American NORP
Seattle GPE
Washington GPE
Jeff Bezos PERSON
July 5, 1994 DATE
second ORDINAL
Alibaba Group ORG
amazon.com ORG
Fire TV ORG
Echo -  LOC
PaaS ORG
Amazon ORG
AmazonBasics ORG
```

## entity-scrubbing.py

#### Utilizes **spaCy** and redacts/scrubs specific entity types from text snippet

### Expected output:

```
[PRIVATE] , doing business as [PRIVATE] , is an American electronic commerce and cloud computing company based in Seattle, Washington, that was founded by [PRIVATE] on July 5, 1994. The tech giant is the largest Internet retailer in the world as measured by revenue and market capitalization, and second largest after [PRIVATE] in terms of total sales. The [PRIVATE] website started as an online bookstore and later diversified to sell video downloads/streaming, MP3 downloads/streaming, audiobook downloads/streaming, software, video games, electronics, apparel, furniture, food, toys, and jewelry. The company also produces consumer electronics - Kindle e-readers, Fire tablets, [PRIVATE] , and Echo - and is the world's largest provider of cloud infrastructure services (IaaS and [PRIVATE] ). [PRIVATE] also sells certain low-end products under its in-house brand [PRIVATE] .
```

## information-extraction.py

#### Utilizes textacy on top of **spaCy** and extracts meaningful information from text using [_semi-structured statement extraction_](https://www.pydoc.io/pypi/textacy-0.5.0/autoapi/extract/index.html#extract.semistructured_statements)

### Expected output:

```
**** Information from Washington's Wikipedia page ****
1 - Statement:  (Washington, is, the capital of the United States of America.[4)
1 - Fact:  the capital of the United States of America.[4
2 - Statement:  (Washington, is, the principal city of the Washington metropolitan area, which has a population of 6,131,977.[6)
2 - Fact:  the principal city of the Washington metropolitan area, which has a population of 6,131,977.[6
3 - Statement:  (Washington, is, home to many national monuments and museums, which are primarily situated on or around the National Mall)
3 - Fact:  home to many national monuments and museums, which are primarily situated on or around the National Mall
```
