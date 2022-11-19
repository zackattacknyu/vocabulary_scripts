import sys

import pandas as pd

from vocab_tools.grouping.grouping_tools import add_hanja_col_to_df_and_prune_hangul_hanja


def add_hanja_to_csv_with_hangul(csv_with_hangul_path,
                                 csv_with_hangul__hangul_col_name,
                                 hangul_hanja_csv_path,
                                 hangul_hanja_csv__hangul_col_name,
                                 hangul_hanja_csv__hanja_col_name,
                                 output_csv_path):
    csv_with_hangul = pd.read_csv(csv_with_hangul_path)
    hangul_hanja_csv = pd.read_csv(hangul_hanja_csv_path)
    out_df = add_hanja_col_to_df_and_prune_hangul_hanja(csv_with_hangul,
                                                        csv_with_hangul__hangul_col_name,
                                                        hangul_hanja_csv,
                                                        hangul_hanja_csv__hangul_col_name,
                                                        hangul_hanja_csv__hanja_col_name)
    out_df.to_csv(output_csv_path, index=False)


if __name__ == '__main__':
    add_hanja_to_csv_with_hangul(*sys.argv[1:])
