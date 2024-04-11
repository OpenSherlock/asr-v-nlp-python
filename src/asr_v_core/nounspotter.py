# deprecated - here for reference and experiments
import spacy
import json
from scispacy.linking import EntityLinker
from scispacy.hyponym_detector import HyponymDetector
from scispacy.abbreviation import AbbreviationDetector
nlp = spacy.load("en_core_sci_lg")

nlp.add_pipe("scispacy_linker", config={"resolve_abbreviations": True, "linker_name": "umls"})
nlp.add_pipe("hyponym_detector", last=True, config={"extended": False})
nlp.add_pipe("abbreviation_detector")
linker = nlp.get_pipe("scispacy_linker")


txt = "When George Washington crossed the Delaware River, he had Leukemia"
txt2 = "Sir Francis Drake was an English explorer and privateer best known for his circumnavigation of the world in a single expedition"
txt3 = "I'm a researcher in theoretical cosmology with extensive experience in coming up with theoretical models, making statistical forecasts, and working with numerical simulations. At the moment, I am working primarily on making better scientific software tools, as well as making forecasts and applying machine learning techniques for upcoming galaxy surveys. I enjoy solving complex problems, building maintainable and customizable software, and automating tasks using command-line tools. Currently on the lookout for new opportunities in a more applied setting, either in research (development of scientific software), or industry (backend or data analysis/engineering)."
txt4 = "The three fruits were mixed to form a supercoagulant (a milk coagulant mixture of the extracts at a ratio of 1:1:1), and the milk coagulation time was measured. The milk was coagulated by the supercoagulant, and thus fortified curd was tested for its ability to inhibit α-glucosidase and α-amylase activities. Then, the fortified curd was fed daily to streptozotocin-induced diabetic rats and their biochemical markers such as blood glucose level, aspartate aminotransferase, alanine transaminase, etc. as well as histopathology of their liver and kidney tissues were compared with the untreated diabetic rats and normal rats."
txt5 = "Some scientists believe that other scientists believe that carbon dioxide causes climate change"
txt6 = "Spinal and bulbar muscular atrophy (SBMA) is an \
           inherited motor neuron disease caused by the expansion \
           of a polyglutamine tract within the androgen receptor (AR). \
           SBMA can be caused by this easily."
txt7 = "The pandemic of obesity, type 2 diabetes mellitus (T2DM) and nonalcoholic fatty liver disease (NAFLD) has frequently been associated with dietary intake of saturated fats (1) and specifically with dietary palm oil (PO) (2)."
txt8 = "Trifluoperazine (tfp) might be an interesting candidate for treating Wilms' Tumor because tfp it antagonizes CALM1 (a protein target). CALM1 regulates an inflammatory gene, IL-6. Lastly we know that IL-6 is associated with Wilms' Tumor."
txt9 = "Vegetarianism in any of its various forms, particularly veganism, has been increasing in popularity over the past few years, especially among the young population in the United States. While several studies have shown that a vegan diet (VD) decreases the risk of cardiometabolic diseases, such as cardiovascular disease, type 2 diabetes mellitus, obesity, and non-alcoholic fatty liver disease, veganism has been associated with adverse health outcomes, namely, nervous, skeletal, and immune system impairments, hematological disorders, as well as mental health problems due to the potential for micro and macronutrient deficits. The goal of this review article is to discuss the current literature on the impact and long-term consequences of veganism on vulnerable populations, including children, adolescents, pregnant and breastfeeding women, and fetal outcomes in strict vegan mothers. It also focuses on the many deficiencies of the vegan diet, especially vitamin B12, and the related increased risk of malignancies."
s12 = "Microbiota describes the living microorganisms found in a defined environment, such as oral and gut microbiota."
#failed to spot "such as" in s12
doc = nlp(s12) #scispacy
#adoc = alp(s12) #spacy
#nounPatterns = [alp.make_doc(term) for term in nnx]
bigOutput = {}
bigOutput['hearst'] = doc._.hearst_patterns
#anmatcher.add("Nouns", nounPatterns)
#matches = anmatcher(adoc)
#nns = nmatcher(doc)mmm = []
mmm=[]
jx={}
#for  start,  in matches:
#TODO
#print(mmm)
#print('\n')
abvx = []

for abc in doc._.abbreviations:
    jx = {}
    jx["abvr"] = abc.text
    jx["strt"] = abc.start
    jx["term"] = abc._.long_form.text
    abvx.append(jx)
jx = {}
bigOutput["abbrev"] = abvx

#print(abvx)
#print('\n')
nnx = []
xyz = []
for ent in doc.ents:
  jx = {}
  jx["name"] = ent.text
  jx["strt"] = ent.start
  for umls_ent in ent._.kb_ents:
    xyz.append(linker.kb.cui_to_entity[umls_ent[0]])
  jx["umls"] = xyz
  nnx.append(jx)
bigOutput["ents"] = nnx
#print(nnx)
#print('\n')
nnxx = []
sx = []
# Grabbing mesh identifiers
# which do not look significantly different from
# umls collected above
# TODO
# consider taking the time to look for duplicates
# generated below against above.
# discard those and write the novel hits into the final record
#for ent in doc.ents:
#  jx = {}
#  jx['name'] = ent
#  jx['strt'] = ent.start
#  for mesh_ent in ent._.kb_ents:
#    jx['mesh'] = linker.kb.cui_to_entity[mesh_ent[0]]
#    nnxx.append(jx)
#bigOutput['ents2'] = nnxx
bigOutput['sentence'] =s12

print(bigOutput)
# To print to an output file rather than console:
# add '> output.json' to the commandline
