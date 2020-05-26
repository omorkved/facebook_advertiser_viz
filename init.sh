#!/bin/bash
echo "Installing Requirements"
pip install -r requirements.txt
echo "Install SpaCy download: Standard English model"
python -m spacy download en_core_web_sm
echo "Done"