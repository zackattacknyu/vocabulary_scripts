export PYTHONPATH="${PYTHONPATH}:${PWD}/src"
python scripts/add_hanja_column.py \
    input_dataframes/vocab_ttmik_1_2_df.csv \
    hangul_word \
    metadata/hanja_hangul_pairs.csv \
    hangul_word \
    hanja_word \
    input_dataframes_with_hanja/vocab_ttmik_1_2_with_hanja.csv
python scripts/add_hanja_column.py \
    input_dataframes/vocab_active_korean_1_2_df.csv \
    hangul_word \
    metadata/hanja_hangul_pairs.csv \
    hangul_word \
    hanja_word \
    input_dataframes_with_hanja/vocab_active_korean_1_2_with_hanja.csv