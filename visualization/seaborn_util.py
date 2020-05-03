import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
def count_plot(df:         pd.DataFrame,
               feature:    pd.Series,
               title:      str = '',
               size:       int = 2
               ):
    _ , ax = plt.subplot(1, 1, figsize=(4*size, 3*size))
    total = float(len(df))
    sns.countplot(df[feature],order = df[feature].value_counts().index, palette='Set2')
    plt.title(title)
    for p in ax.patches:
        height = p.get_height()
        ax.text(p.get_x()+p.get_width()/2.,
                height + 3,
                '{:1.2f}%'.format(100*height/total),
                ha="center")
    plt.show()

