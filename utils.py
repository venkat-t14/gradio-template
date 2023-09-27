import pandas as pd


def test_fn():
    df = pd.DataFrame(data={"a": [1, 2, 3], "b": [4, 5, 6]})
    return df_to_table(df)


def df_to_table(df: pd.DataFrame):
    html = '<table class="table is-striped is-hoverable is-fullwidth">'
    html += "<thead><tr>"
    for column in df.columns:
        html += f"<th>{column}</th>"
    html += "</tr></thead><tbody>"
    for i, row in df.iterrows():
        html += "<tr>"
        for cell in row:
            html += f"<td>{cell}</td>"
        html += "</tr>"
    html += "</tbody></table>"
    return html
