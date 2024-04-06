# TODO venv for all this
import spacy
import scispacy

# Load a powerful pre-trained NER model (adjust based on your needs)
nlp = spacy.load('en_core_sci_scibert') #("en_core_web_trf") #

def handleSingleNerSentence(json):
    return handleSentence(json['text'])
  
# return array of String
def handleSentence(txt):
    '''
    process a given sentence
    '''
    print(txt)
    doc = nlp(p1)
    result = []
    for entity in doc.ents:
        result.append(entity.text)
    return reesult
