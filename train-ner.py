# train named entity recognition
import json
import os
from __future__ import unicode_literals, print_function

import plac
import random
from pathlib import Path
import spacy
from spacy.util import minibatch, compounding
import time
import sys


def get_newest_model():
    import subprocess
    return subprocess.check_output([sys.executable, "get_newest_model.py"]).decode('ascii').strip()


# Load spaCy's English NLP model
nlp = spacy.load(get_newest_model())


def enhance_training_data(text_data=[]):
    '''iterate through and update training data using existing model to prevent "catastrophic forgetting"'''

    iter_text = text_data.copy()

    def check_tokens(token):
        if token.ent_iob != 0 and token.ent_type_ != "":
            if token.string.strip() == "":
                return None
            return (token.ent_type_, token.string.strip())
        else:
            return None

    def get_entity_tuples(text):
        doc = nlp(text)
        for ent in doc.ents:
            ent.merge()
        tokens = map(check_tokens, doc)
        tokens = [t for t in tokens if t != None]
        return tokens

    for idx, obj in enumerate(iter_text):
        text, label_def = obj
        entities = label_def['entities']
        if len(entities) > 0:
            label_record = entities[0]
            fidx, lidx, label = label_record
            target = text[fidx:lidx]
            output = get_entity_tuples(text)
            for ent in output:
                ent_type, ent_val = ent
                if target != ent_val:
                    if ent_val in target or target in ent_val:
                        offset = (ent_val, {
                            'entities': []
                        })

                        if offset not in text_data:
                            text_data.append(offset)

                    elif ent_val not in target.split(" "):
                        _fidx = text.index(ent_val)
                        _lidx = _fidx + len(ent_val)
                        text_data[idx][1]['entities'].append(
                            (_fidx, _lidx, ent_type))
    return text_data


# read in json data file

data_file = sys.argv[1]

base = os.path.basename(data_file)
LABEL = os.path.splitext(base)[0].upper()

data = None

# read in json file
with open(data_file) as json_file:
    data = json.load(json_file)

# initialize training data as empty list
TRAIN_DATA = []

# populate training data from json file read as array of tuples containing a string, and a dictionary object
for entity in data['entities']:
    _text, _entities = entity.items()
    v1, text = _text
    v2, entities = _entities
    ents = []
    for ent in entities:
        fi, la = ent
        ents.append((int(fi), int(la), LABEL))
    TRAIN_DATA.append((text, {
        'entities': ents
    }))

# enhance training data accounting for offsets and existing entity types
TRAIN_DATA = enhance_training_data(TRAIN_DATA)


@plac.annotations(
    model=("Model name. Defaults to blank 'en' model.", "option", "m", str),
    new_model_name=("New model name for model meta.", "option", "nm", str),
    output_dir=("Optional output directory", "option", "o", Path),
    n_iter=("Number of training iterations", "option", "n", int))
def main(model=str(get_newest_model()), new_model_name=LABEL.lower(), output_dir='custom-models', n_iter=10):
    """Set up the pipeline and entity recognizer, and train the new entity."""
    if model is not None:
        nlp = spacy.load(model)  # load existing spaCy model
        print("Loaded model '%s'" % model)
    else:
        nlp = spacy.blank('en')  # create blank Language class
        print("Created blank 'en' model")
    # Add entity recognizer to model if it's not in the pipeline
    # nlp.create_pipe works for built-ins that are registered with spaCy
    if 'ner' not in nlp.pipe_names:
        ner = nlp.create_pipe('ner')
        nlp.add_pipe(ner)
    # otherwise, get it, so we can add labels to it
    else:
        ner = nlp.get_pipe('ner')

    ner.add_label(LABEL)   # add new entity label to entity recognizer
    if model is None:
        optimizer = nlp.begin_training()
    else:
        # Note that 'begin_training' initializes the models, so it'll zero out
        # existing entity types.
        optimizer = nlp.entity.create_optimizer()

    # get names of other pipes to disable them during training
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
    with nlp.disable_pipes(*other_pipes):  # only train NER
        for itn in range(n_iter):
            random.shuffle(TRAIN_DATA)
            losses = {}
            # batch up the examples using spaCy's minibatch
            batches = minibatch(TRAIN_DATA, size=compounding(4., 32., 1.001))
            for batch in batches:
                texts, annotations = zip(*batch)
                nlp.update(texts, annotations, sgd=optimizer, drop=0.35,
                           losses=losses)
            print('Losses', losses)

    # test the trained model with test_text provided by secondary script exec argument; defaulting to a very basic test
    test_text = "This is " + new_model_name.replace('_', ' ').title() + "."
    if len(sys.argv) >= 3 and sys.argv[2] != "":
        test_text = sys.argv[2]

    doc = nlp(test_text)
    print("Entities in '%s'" % test_text)
    for ent in doc.ents:
        print(ent.label_, ent.text)

    # save model to output directory
    if output_dir is not None:
        millis = int(round(time.time() * 1000))
        output_dir = Path(output_dir + '/' + str(millis) +
                          "-" + new_model_name)
        if not output_dir.exists():
            output_dir.mkdir()
        nlp.meta['name'] = new_model_name  # rename model
        nlp.to_disk(output_dir)
        print("Saved model to", output_dir)

        # test the saved model
        print("Loading from", output_dir)
        nlp2 = spacy.load(output_dir)
        doc2 = nlp2(test_text)
        for ent in doc2.ents:
            print(ent.label_, ent.text)


# if __name__ == '__main__':
#     plac.call(main)

# Run our Function
print("\nTraining for " + LABEL + "...\n")
main()
