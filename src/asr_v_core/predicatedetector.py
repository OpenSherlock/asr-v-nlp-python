import spacy
import json
import time
from scispacy.linking import EntityLinker
from scispacy.hyponym_detector import HyponymDetector
from scispacy.abbreviation import AbbreviationDetector

import antecedents #import antecedents
import predicates # import predicates
import scxspacy #import processSentence

from spacy.matcher import PhraseMatcher
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_md")
import spacy_dbpedia_spotlight

import ner #import handleSingleNerSentence

# Note: opentapioca is not all that accurate
# plus which the repo uses the wrong api URL
#nlx = spacy.blank("en")
#nlx.add_pipe("opentapioca")

snlp = spacy.load("en_core_sci_lg")

snlp.add_pipe("scispacy_linker", config={"resolve_abbreviations": True, "linker_name": "umls"})
snlp.add_pipe("hyponym_detector", last=True, config={"extended": False})
snlp.add_pipe("abbreviation_detector")
snlp.add_pipe("dbpedia_spotlight")
linker = snlp.get_pipe("scispacy_linker")

suchMatcher = Matcher(nlp.vocab)
suchMatcher.add("suchas", [[{"POS":"NOUN"}, {"TEXT":"such"}, {"TEXT":"as"}],
  [{"POS":"NOUN"}, {"TEXT":","}, {"TEXT":"such"}, {"TEXT":"as"}]])
antMatcher = PhraseMatcher(nlp.vocab)
predMatcher = PhraseMatcher(nlp.vocab)
antPatterns = [nlp.make_doc(term) for term in antecedents.antecedents]
predPatterns = [nlp.make_doc(term) for term in predicates.predicates]
antMatcher.add("prelist", antPatterns)
predMatcher.add("predlist", predPatterns)
conjMatcher = Matcher(nlp.vocab)
conjMatcher.add("ConJ", [[{"POS": "CCONJ","TEXT":"and" }],
                         [{"POS": "PUNCT", "TEXT":","}]])
disjMatcher = Matcher(nlp.vocab) 
disjMatcher.add("DisJ", [[{"POS": "CCONJ","TEXT":"or" }]])

xMatcher = Matcher(nlp.vocab)
xMatcher.add("X", [[{"POS":"NOUN"}, {"TEXT":"of"}],[{"POS":"NOUN"}, {"TEXT":"that"}], [{"POS":"NOUN"}, {"TEXT":"which"}]])

def current_milli_time():
    return round(time.time() * 1000)

def handleSentences(json):
  '''
    for a given array of sentences
    return an array of spacy and scispacy results
  '''
  result = [] # array of sentence objects
  sentencearray = json.sentences
  print('AAA',sentencearray)
  for s in sentencearray:
    result.append(handleSentence(s))
  return result

def handleSingleSentence(json):
  return handleSentence(json['text'])
  
def handleSentence(txt):
  '''
    process a given sentence
  '''
  print(txt)
  startTime = current_milli_time()

  scinlp  = scxspacy.processSentence(txt, snlp, linker)

  doc = nlp(txt)
  jsn = {}

  #Wikidata
  # ignoring for now
  wkds = []

  #for edx in wdx.ents:
  #  txt = edx.text
  #  kid = edx.kb_id_
  #  lbl = edx.label_
  #  dsc = edx._.description
  #  wkds.append((txt, kid, lbl,dsc))
  #suchas
  suchMatches  = suchMatcher(doc)
  suchs = []
  for mid, start, end in suchMatches:
    tok = doc[start:end]
    jsn = {"strt": start, "enx":end, "txt": tok.text }
    suchs.append(jsn)
  #Predicates
  antMatches = antMatcher(doc)
  predMatches = predMatcher(doc)

  data = []
  ants = []
  #Antecedents to predicates
  for mid, start, end in antMatches:
    tok = doc[start:end]
    jsn = {"strt": start, "enx":end, "txt": tok.text }
    ants.append(jsn)
  print("ANTECENTS", ants)
  data.append(ants)

  preds = []
  for mid, start, end in predMatches:
    tok = doc[start:end]
    jsn = {"strt": start, "enx":end, "txt": tok.text }
    preds.append(jsn)
  print("PREDICATES", preds)
  data.append(preds)
  print("DATAX", data)
  #Nouns and verbs
  nmatcher = Matcher(nlp.vocab)
  nmatcher.add("Nouns", [[{"POS": "NOUN"}]])
  nns = nmatcher(doc)
  #print("FOO", nns)
  nnx = []
  pnmatcher = Matcher(nlp.vocab)
  pnmatcher.add("ProperNouns", [[{"POS": "PROPN"}]])
  pnns = pnmatcher(doc)
  #print("BAR", pnns)
  pnnx = []
  vmatcher = Matcher(nlp.vocab)
  vmatcher.add("Verbs", [[{"POS": "VERB"}]])
  vbs = vmatcher(doc)
  vbx = []
  #print("BAH", vbs)
  for mid, start, end in nns:
    tok = doc[start]
    jsn = {"strt": start,"txt": tok.text }
    nnx.append(jsn)
 # print("NNN", nnx)
  for mid, start, end in pnns:
    tok = doc[start]
    jsn = {"strt": start,"txt": tok.text }
    pnnx.append(jsn)
  #print('PNN', pnnx)
  for mid, start, end in vbs:
    tok = doc[start]
    jsn = {"strt": start,"txt": tok.text }
    vbx.append(jsn)
  #print("VRB", vbx)
  #conjunctions
  conjX = conjMatcher(doc)
  conjM = []
  for mid, start, end in conjX:
    tok = doc[start]
    jsn = {"strt": start,"txt": tok.text }
    conjM.append(jsn)
  #disjunctions
  disjX = disjMatcher(doc)
  disjM = []
  for mid, start, end in disjX:
    tok = doc[start]
    jsn = {"strt": start,"txt": tok.text }
    disjM.append(jsn)

  xX = xMatcher(doc)
  xx = []
  for mid, start, end in xX:
    tok = doc[start:end]
    jsn = {"strt": start,"txt": tok.text }
    xx.append(jsn)
  print("XXX", xx)

  nex = ner.handleSentence(txt)

  return {
    "data":data, # []
     "wkd":wkds, # []
    "nns":nnx, # []
    "pnns":pnnx, # []
    "vrbs":vbx, # []
    "conj":conjM, # []
    "disj":disjM, # []
    "noms":xx, # []
    "suchs":suchs, # []
    "scispcy":scinlp, # []
    "ner":nex,# []
    "time":(current_milli_time()-startTime)/1000
    }

  