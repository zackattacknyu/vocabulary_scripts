def prune_hanja_hangul_list(hangul_hanja_df, hangul_col_name, hanja_col_name ):
    res_df = hangul_hanja_df \
        .groupby(hangul_col_name) \
        .agg({hanja_col_name: ['count', 'first']})
    res_df = res_df[res_df[hanja_col_name]['count'] < 2]
    return res_df.loc[:, (hanja_col_name, 'first')].rename(hanja_col_name)


def remove_hada(x):
    if str(x).endswith('하다'):
        return str(x)[:-2]
    else:
        return x


def add_hanja_column_to_df_with_hangul(df_with_hangul, hangul_col_name, pruned_hangul_hanja_series):
    """
    Takes a dataframe with a column of hangul words
        and adds a column with hanja words
    :param df_with_hangul: dataframe with column of hangul
    :param hangul_col_name: name of the hangul column
    :param pruned_hangul_hanja_series: series where index is hangul word and output is a single hanja word
    :return:
    """
    hangul_wo_hada_col_name = f'{hangul_col_name}_wo_hadaa'
    hangul_orig_col_name = f'{hangul_col_name}_original'
    df_with_hangul[hangul_wo_hada_col_name] = df_with_hangul[hangul_col_name].apply(remove_hada)
    df_with_hangul = df_with_hangul.rename(columns={
        hangul_col_name: hangul_orig_col_name
    })
    out_df = df_with_hangul\
        .set_index(hangul_wo_hada_col_name)\
        .join(pruned_hangul_hanja_series)
    return out_df.reset_index().rename(columns={
        'index': hangul_wo_hada_col_name
    })


def add_hanja_col_to_df_and_prune_hangul_hanja(df_with_hangul,
                                               hangul_col_name_in_df,
                                               hangul_hanja_info,
                                               hangul_col_name_in_info,
                                               hanja_col_name_in_info):
    """
    Adds hanja column to dataframe with hangul.
    Also takes in a hangul-hanja dataframe and return a series with only
        the examples where there is a single hanja for a hangul word
    :param df_with_hangul: dataframe with hangul
    :param hangul_col_name_in_df: hangul column name in dataframe
    :param hangul_hanja_info: info dataframe with hanja-hangul pairs
    :param hangul_col_name_in_info: hangul col name in info dataframe
    :param hanja_col_name_in_info: hanja col name in info dataframe
    :return:
    """
    hangul_hanja_series = prune_hanja_hangul_list(hangul_hanja_info,
                                                  hangul_col_name_in_info,
                                                  hanja_col_name_in_info)
    return add_hanja_column_to_df_with_hangul(df_with_hangul,
                                              hangul_col_name_in_df,
                                              hangul_hanja_series)
