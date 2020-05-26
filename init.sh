#!/bin/bash
echo "Installing Requirements"
pip3 install -r requirements.txt
echo "Install SpaCy download: Standard English model"
python3 -m spacy download en_core_web_sm
echo "Done"