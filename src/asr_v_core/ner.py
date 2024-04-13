# TODO venv for all this
import spacy
import scispacy

# Load a powerful pre-trained NER model (adjust based on your needs)
nlp = spacy.load('en_core_sci_scibert') #("en_core_web_trf") #
  
# return array of String
def handleNerSentence(txt):
    '''
    process a given sentence
    '''
    print('ner',txt)
    doc = nlp(txt)
    result = []
    for entity in doc.ents:
        result.append(entity.text)
    return result
