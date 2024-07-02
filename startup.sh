#!/bin/bash
pip install -r requirements.txt
streamlit run main.py --server.port 8000 --server.headless true