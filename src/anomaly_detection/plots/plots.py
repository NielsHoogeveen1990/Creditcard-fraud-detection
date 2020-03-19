import seaborn as sns
import matplotlib.pyplot as plt


def create_distplots(df, cols=4):
    num_vars = df.select_dtypes('number').columns

    if (len(num_vars) // cols) != 0:
        rows = (len(num_vars) // cols) + 1
    else:
        rows = (len(num_vars) // cols)

    fig, ax = plt.subplots(rows, cols, figsize=(20, 10))
    for variable, subplot in zip(num_vars.tolist(), ax.flatten()):
        sns.distplot(df[variable], ax=subplot)
        for label in subplot.get_xticklabels():
            label.set_rotation(90)


def create_boxplots(df, cols=2):
    cat_vars = df.select_dtypes('object').columns

    if (len(cat_vars) // cols) != 0:
        rows = (len(cat_vars) // cols) + 1
    else:
        rows = (len(cat_vars) // cols)

    fig, ax = plt.subplots(rows, cols, figsize=(20, 10))
    for variable, subplot in zip(cat_vars.tolist(), ax.flatten()):
        sns.countplot(df[variable], ax=subplot)
        for label in subplot.get_xticklabels():
            label.set_rotation(90)