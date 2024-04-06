A Python interface to
- SpaCy
- SciSpacy

For processing paragraphs
## Installation
### Virtual Environment
`pip install virtualenv`

`python3 -m venv asrcore`

`source asrcore/bin/activate`

### Dependencies
`pip install spacy`

`pip install spacy-dbpedia-spotlight`

`pip install scispacy`

`python -m spacy download en_core_web_md`

`pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.4/en_core_sci_scibert-0.5.4.tar.gz
`

`pip install *scispacy model url*`

where *scispacy model url* is found here: https://allenai.github.io/scispacy/

and model = en_core_sci_lg


### Build everthing
`pip install .`

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
