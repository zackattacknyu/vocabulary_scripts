from vocab_tools.ingestion.english_korean_info_ingest import text_block_to_english_hangul_df
import sys


def raw_input_file_to_dataframe(input_file_full_path, output_file_folder):

    file_name = input_file_full_path.split('/')[-1]
    file_name_no_ext = file_name.split('.')[0]

    with open(input_file_full_path, 'r') as f:
        text = f.read()

    out_df = text_block_to_english_hangul_df(text)

    out_df.to_csv(f'{output_file_folder}/{file_name_no_ext}_df.csv', index=False)


if __name__ == '__main__':
    raw_input_file_to_dataframe(sys.argv[1], sys.argv[2])
