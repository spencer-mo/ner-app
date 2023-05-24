# coding: utf-8
import spacy
import sys

def get_newest_model():
    import subprocess
    return subprocess.check_output([sys.executable, "get_newest_model.py"]).decode('ascii').strip()
                    
print("Using: " + get_newest_model() + "...\n")

### Load spaCy's English NLP model
nlp = spacy.load(get_newest_model())

doc_len = 0

# START contextual enrichment code
def get_adjacent_tokens(token, idx, isRight = True):
    temp = []
    _range = range(1, min((doc_len - idx), 11)) if isRight else range(min(idx, 11), 0, -1)
    for n in _range:
        token_val = token.nbor(n).string if isRight else token.nbor(n*-1).string
        temp.append(token_val)
    return "".join(temp)

def strip_common_escape_chars(token_string):
    if "\n" in token_string:
        token_string = token_string.replace('\n','')
    if "\t" in token_string:
        token_string = token_string.replace('\t','')
    return token_string


def get_entity_tuples(i_token):
    i, token = i_token

    if token.ent_iob != 0 and token.ent_type_ != "":
        right = strip_common_escape_chars(get_adjacent_tokens(token, i)) if (i < doc_len - 1) else ""
        left = strip_common_escape_chars(get_adjacent_tokens(token, i, False)) if (i > 0) else ""
        token_value = token.string.strip()
        if token_value == "":
            return None

        return (left, token.ent_type_, token_value, right)
    else:
        return None

def enrich(text):
    doc = nlp(text)
    for ent in doc.ents:
        ent.merge()
    global doc_len
    doc_len = len(doc)
    tokens = map(get_entity_tuples, enumerate(doc))
    tokens = [t for t in tokens if t != None]
    return tokens

import os

filename = sys.argv[1]

base_name = os.path.basename(filename)
filename_wo_ext = os.path.splitext(base_name)[0].replace(' ', '_')

file = open(filename, 'r')
text = file.read().strip()
file.close()

print("Enriching " + filename + "...\n")

output = enrich(text)

import xml.etree.ElementTree as ET

ent = ET.Element('assure:document', { 'xmlns:assure': "http://assure.com/assure" })

for left, ent_type, ent_val, right in output:
    ent_wrapper = ET.SubElement(ent, 'assure-entity')
    ent_body = ET.SubElement(ent_wrapper, 'entity:' + ent_type.lower().replace('_', '-'), { 
        "xmlns:entity": "http://marklogic.com/entity" 
    })
    ent_body.text = ent_val
    ent_left = ET.SubElement(ent_wrapper, 'left')
    ent_left.text = left
    ent_right = ET.SubElement(ent_wrapper, 'right')
    ent_right.text = right
    
tree = ET.ElementTree(ent)

outputfile = "./init_docs/enriched/" + filename_wo_ext + ".xml"

tree.write(outputfile, xml_declaration=True, encoding="utf-8")

print('The contents of "' + filename + '" have been outputted as enriched entity data to "./' + outputfile + '"\n')