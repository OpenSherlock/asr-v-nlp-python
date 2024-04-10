# run some sciSpaCy routines on a sentence

def entity_to_json(ent):
  result = {"cid": ent.concept_id,
    "canonical":ent.canonical_name,
    "aliases": ent.aliases,
    "types": ent.types,
    "definition": ent.definition}
  return result

def entDef(ent, linker):
  result = []
  for umls_ent in ent._.kb_ents:
    result.append(entity_to_json(linker.kb.cui_to_entity[umls_ent[0]]))
  return result

def processSentence(txt, nlp, linker):
  doc = nlp(txt)
  #gather POS list
  posx = []
  for word in doc:
    foo = {"txt":  word.text,
      "lemma": word.lemma_,
      "pos": word.pos_,
      "tag": word.tag_,
      "dep": word.dep_}
    posx.append(foo)
  # hearst structures - if any
  hrstx = doc._.hearst_patterns,
  # abbreviations - if any
  abvx = []
  for abc in doc._.abbreviations:
    abvz = {"abvr":  abc.text,
      "strt":  abc.start,
      "term":  abc._.long_form.text}
    abvx.append(abvz)
  # dbpedia
  dbpx = []
  for ent in doc.ents:
    dbpx.append(ent._.dbpedia_raw_result)
  # ents with umls references

  entx = []
  for ent in doc.ents:
    entz = {"name": ent.text,
      "strt":  ent.start,
      "umls":  entDef(ent, linker)
    }
    entx.append(entz)
  return {"sentence":txt, "pos": posx,
    "hearst":hrstx, "abbrev":abvx, "dbp":dbpx,
    "ents":entx
    }
