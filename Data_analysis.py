import shap
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegressionCV
from sklearn.feature_selection import RFE
from sklearn.preprocessing import StandardScaler

import matplotlib.pyplot as plt
import seaborn as sns

from complexity_accuracy import *

def correlation_score(data_name, testcases, codes, feature_selection=0):
    df= compute_complexity(data_name, testcases, codes)
    X = df.drop('accuracy', axis=1)
    y = df['accuracy']
    if feature_selection==0:

        model = LogisticRegression(max_iter=10000, penalty='l2')
        scores = cross_val_score(model, X, y, cv=10, scoring='accuracy')
        return scores.mean

    elif feature_selection == 'L1':
        model_l1 = LogisticRegressionCV(cv=10, penalty='l1', solver='liblinear', max_iter=10000)
        model_l1.fit(X, y)

        coefficients = pd.Series(model_l1.coef_[0], index=X.columns)
        selected_features = coefficients[coefficients != 0].index

        X_selected = X[selected_features]
        model_final = LogisticRegression(max_iter=10000, penalty='l2')

        final_scores = cross_val_score(model_final, X_selected, y, cv=10, scoring='accuracy')
        
        return final_scores.mean()

    elif feature_selection == 'rfe':
        rfe = RFE(model, n_features_to_select=10)  # Select the top 10 features
        rfe.fit(X, y)

        selected_features = X.columns[rfe.support_]

        print("Selected features using RFE:", selected_features)


        X_selected = X[selected_features]
        model_final = LogisticRegression(max_iter=10000, penalty='l2')

        final_scores = cross_val_score(model_final, X_selected, y, cv=10, scoring='accuracy')
        return final_scores.mean()

    elif feature_selection == 'corr':
        correlation_matrix = X.corrwith(y)

        threshold = 0.2 # Define a threshold for correlation coefficient
        selected_features = correlation_matrix[correlation_matrix.abs() > threshold].index

        X_selected = X[selected_features]
        model_final = LogisticRegression(max_iter=10000, penalty='l2')

        final_scores = cross_val_score(model_final, X_selected, y, cv=10, scoring='accuracy')

        return final_scores.mean()
    elif feature_selection == 'shap':
        initial_model = LogisticRegression(max_iter=10000, penalty='l2')
        initial_model.fit(X, y)

        explainer = shap.Explainer(initial_model, X)
        shap_values = explainer(X)
        shap_importance = np.abs(shap_values.values).mean(axis=0)

        top_features_indices = np.argsort(shap_importance)[-5:]  # indices of the 5 most important features
        X_selected = X.iloc[:, top_features_indices]

        model = LogisticRegression(max_iter=10000, penalty='l2')
        scores = cross_val_score(model, X_selected, y, cv=10, scoring='accuracy')

        return scores.mean()

def distribution(data_name, testcases, codes):
    df= compute_complexity(data_name, testcases, codes)
    X = df.drop('accuracy', axis=1)
    y = df['accuracy']

    scaler = StandardScaler()
    X_scaled = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)

    df_scaled = pd.concat([X_scaled, y], axis=1)
    df_scaled

    grouped = df_scaled.groupby('accuracy')
    median_metrics = grouped.median()

    #Calculate the difference between fail (0) and pass (1) cases
    metric_diff = median_metrics.loc[0] - median_metrics.loc[1]

    #Sort by the difference (larger values indicate higher in failed cases)
    metric_diff_sorted = metric_diff.sort_values(ascending=False)

    metric_diff_nonzero = metric_diff_sorted[metric_diff_sorted != 0]

    color = "#D8BFD8"

    plt.figure(figsize=(10, 8))
    metric_diff_nonzero.plot(kind='barh', color=color, edgecolor="black")

    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.show()

    #Box Plot
    '''

    metrics = df_scaled.columns.drop('accuracy')
    for metric in metrics:
        plt.figure(figsize=(8, 6))

        sns.boxplot(x='accuracy', y=metric, data=df_scaled)

        plt.title(f'Distribution of {metric} by Target')
        plt.xlabel('Target (1 = Pass, 0 = Fail)')
        plt.ylabel(metric)

        # Show the plot
        plt.show()
    '''  
