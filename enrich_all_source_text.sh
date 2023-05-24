# !/bin/bash
for filename in init_docs/text/*; 
    do python3 entity-enrichment.py "${filename}";
done