python3 -W ignore main.py $1 $2 \
--feature-min-max-scale price \
--feature-binarize parking \
--feature-remove airconditioning \
--feature-anonymize area \
--feature-fill stories 2

