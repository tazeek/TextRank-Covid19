from HybridTheory import HybridTheory

import pandas as pd

covid_scopus_df = pd.read_excel('folder/covid19_scopus.xlsx')

abstract_df = covid_scopus_df['Abstract']
abstract_ser = abstract_df[abstract_df != '[No abstract available]']

# There is a NaN abstract in the list (Checked by manual analysis)
abstract_ser.dropna(inplace=True)

hybrid_analyzer = HybridTheory()

keywords_abstract_list = []

for abstract in abstract_ser:

    hybrid_analyzer.analyze(abstract, candidate_pos = ['NOUN', 'PROPN'], window_size=4, lower=False)

    keywords_list = hybrid_analyzer.get_keywords(5)

    keywords_abstract_list.append({
        'abstract': abstract,
        'keywords': ','.join(keywords_list)
    })

pd.DataFrame(keywords_abstract_list).to_csv('tester.csv', index=False)