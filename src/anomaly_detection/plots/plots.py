import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def create_distplots(df, cols=4):
    num_vars = df.select_dtypes('number').columns

    if (len(num_vars) // cols) != 0:
        rows = (len(num_vars) // cols) + 1
    else:
        rows = (len(num_vars) // cols)

    fig, ax = plt.subplots(rows, cols, figsize=(20, 10))
    for variable, subplot in zip(num_vars.tolist(), ax.flatten()):
        sns.distplot(df[variable], ax=subplot)

    plt.tight_layout()
    plt.show()


def create_countplots(df, cols=2):
    cat_vars = df.select_dtypes('object').columns

    if (len(cat_vars) // cols) != 0:
        rows = (len(cat_vars) // cols) + 1
    else:
        rows = (len(cat_vars) // cols)

    fig, ax = plt.subplots(rows, cols, figsize=(20, 10))
    for variable, subplot in zip(cat_vars.tolist(), ax.flatten()):
        sns.countplot(df[variable], ax=subplot, palette='Set2')

    plt.tight_layout()
    plt.show()



def boxplots_numerical_target(df, target, cols=2):
    """
    This function plots box plots in order to see the relationship between categorical features and a numerical target.
    :param df: dataframe
    :param target: numerical target variable
    :param cols: amount of columns in the subplot
    :return: subplots of box plots
    """
    cat_vars = df.select_dtypes('object').columns

    if (len(cat_vars) // cols) != 0:
        rows = (len(cat_vars) // cols) + 1
    else:
        rows = (len(cat_vars) // cols)

    fig, ax = plt.subplots(rows, cols, figsize=(20, 10))
    for variable, subplot in zip(cat_vars.tolist(), ax.flatten()):
        sns.boxplot(x=variable,
                    y=target,
                    data=df,
                    ax=subplot,
                    palette='Set2')

    plt.tight_layout()
    plt.show()


def plot_categorical_relations_categorical_target(df):
    # caplot with count
    #sns.catplot(x="F", hue="Target", kind="count", data=df)
    # stacked count plot?

    # Stacked Column chart is a useful graph to visualize the relationship between two
    # categorical variables.It compares the percentage that each category from one variable contributes
    # to a total across categories of the second variable.

    # normalized stacked barplot with sample number and percentage using Python and matplotlib.pyplot
    #TODO
    pass


def plot_distributions_categorical_target(df, target, cols=4, bins=50, alpha=0.3):
    num_vars = df.select_dtypes('number').columns

    if (len(num_vars) // cols) != 0:
        rows = (len(num_vars) // cols) + 1
    else:
        rows = (len(num_vars) // cols)

    target_uniques = np.unique(df[target].values)
    palette = sns.husl_palette(len(target_uniques))
    palette_dict = dict(zip(target_uniques, palette))

    fig, ax = plt.subplots(rows, cols, figsize=(20, 10))
    for variable, subplot in zip(num_vars.tolist(), ax.flatten()):
        for target_unique in target_uniques:
            sns.distplot(df.loc[lambda d: d[target] == target_unique][variable],
                         ax=subplot,
                         bins=bins,
                         color=palette_dict[target_unique],
                         hist_kws=dict(alpha=alpha))

    fig.legend(labels=target_uniques)
    plt.tight_layout()
    plt.show()


def plot_kde_categorical_target(df, target, cols=4):
    #TODO title and legend
    num_vars = df.select_dtypes('number').columns

    if (len(num_vars) // cols) != 0:
        rows = (len(num_vars) // cols) + 1
    else:
        rows = (len(num_vars) // cols)

    target_uniques = np.unique(df[target].values)
    palette = sns.husl_palette(len(target_uniques))
    palette_dict = dict(zip(target_uniques, palette))

    fig, ax = plt.subplots(rows, cols, figsize=(20, 10))
    for variable, subplot in zip(num_vars.tolist(), ax.flatten()):
        for target_unique in target_uniques:
            sns.kdeplot(df.loc[lambda d: d[target] == target_unique][variable],
                        ax=subplot,
                        shade=True,
                        color=palette_dict[target_unique])

    fig.legend(labels=target_uniques)
    plt.tight_layout()
    plt.show()


def plot_scatter_plots(df):
    # scatter plot for relation between numerical features and numerical target
    pass