# for static testing

from predicatedetector import handleSingleSentence

#### Data
s1=""" 
The microbial communities are in symbiosis with the host, contributing to homeostasis and regulating immune function.
"""

s2=""" 
IL-4 production was inhibited by haloperidol and chlorpromazine, but not by clozapine.
"""

s3=""" 
Microbiome refers to the collection of genomes from all the microorganisms in the environment, which includes not only the community of the microorganisms, but also the microbial structural elements, metabolites, and the environmental conditions.
"""

s4=""" 
The role of microbiota in health and diseases is being highlighted by numerous studies since its discovery.
"""

### Code

json = {
  'text':s1
}
print(json)

result = handleSingleSentence(json)
print(json)
