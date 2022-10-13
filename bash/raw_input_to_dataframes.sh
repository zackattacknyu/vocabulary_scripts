export PYTHONPATH="${PYTHONPATH}:${PWD}/src"
python scripts/make_df_from_raw_input.py raw_input/vocab_active_korean_1_2.txt input_dataframes
python scripts/make_df_from_raw_input.py raw_input/vocab_ttmik_1_2.txt input_dataframes
