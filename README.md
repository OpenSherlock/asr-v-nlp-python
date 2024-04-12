# A Python interface to
- SpaCy
- SciSpacy

For processing paragraphs
## Installation
### Virtual Environment
`pip install virtualenv`

`pip3 install virtualenv`

`python -m venv asrcore`

`python3 -m venv asrcore`

`source asrcore/bin activate`

### Dependencies
Install uvicorn, e.g. `sudo apt install uvicorn`

`pip install starlette`

`pip3 install starlette`

`pip install spacy`

`pip3 install spacy`


`pip install spacy-dbpedia-spotlight`

`pip3 install spacy-dbpedia-spotlight`
## install pytorch as discussed below
#####
## On Silicon Macs, there may be issues installing scispacy
## which ar typically solved with python 3.10 if you have 
##x a moro recent version - create your veenv with 3.10
#####
`pip install scispacy`

`pip3 install scispacy`

`python -m spacy download en_core_web_md`

`python3 -m spacy download en_core_web_md`

######
## Warning
## what follows is a Transformer, which means it will opt for thee cuda-based Torch
## if you do not have cuda, you need to install a CPU-based PyTorch
#####
`pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.4/en_core_sci_scibert-0.5.4.tar.gz`

`pip3 install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.4/en_core_sci_scibert-0.5.4.tar.gz`

`pip install *scispacy model url*`

`pip3 install *scispacy model url*`


where *scispacy model url* is found here: https://allenai.github.io/scispacy/

and model = en_core_sci_lg


### Build everything
`pip install .`

`pip3 install .`

## Running Python

`uvicorn -p 8008 asr_v_core:app`

or

`./run.sh`
### Note
Allow a long time for the system to boot the first time while it fills internal caches with large models downloaded from S3

When everything is loaded,you should see something like:

`2023-10-10 12:55:15 INFO: Done loading processors!
INFO:     Started server process [28842]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8008 (Press CTRL+C to quit)

## Testing
It is advised to run the test as described next to allow a new installation to cach needed libraries.

`cd asr_v_core`

`python test.py`