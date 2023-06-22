import sys
import argparse
import pickle
import os
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

# Load dataset
def load_data(dataset=".data/yes.csv"):
    df = pd.read_csv(dataset, encoding = 'utf-8-sig')
    df = df.dropna(how='all')

    jk_map = {"Laki-Laki": 1, "Perempuan": 0}
    df["jenis_kelamin"] = df["jenis_kelamin"].map(jk_map)

    feature_col_names = ["nama"]
    predicted_class_names = ["jenis_kelamin"]
    X = df[feature_col_names].values
    y = df[predicted_class_names].values

    return (X, y)

# Predict using Naive Bayes
def predict_nb(names, dataset):
    if os.path.isfile("./data/pipe_nb.pkl") and dataset is None:
        file_nb = open('./data/pipe_nb.pkl', 'rb')
        pipe_nb = pickle.load(file_nb)
    else:
        file_nb = open('./data/pipe_nb.pkl', 'wb')
        pipe_nb = Pipeline([
            ('vect', CountVectorizer(analyzer='char_wb', ngram_range=(2, 6))),
            ('tfidf', TfidfTransformer()),
            ('clf', MultinomialNB())
        ])
        # Train and dump to file
        X, y = load_data(dataset)
        pipe_nb = pipe_nb.fit(X.ravel(), y.ravel())
        pickle.dump(pipe_nb, file_nb)

    return pipe_nb.predict(names)

# Predict using Logistic Regression
def predict_lg(names, dataset):
    if os.path.isfile("./data/pipe_lg.pkl") and dataset is None:
        file_lg = open('./data/pipe_lg.pkl', 'rb')
        pipe_lg = pickle.load(file_lg)
    else:
        file_lg = open('./data/pipe_lg.pkl', 'wb')
        pipe_lg = Pipeline([
            ('vect', CountVectorizer(analyzer='char_wb', ngram_range=(2, 6))),
            ('tfidf', TfidfTransformer()),
            ('clf', LogisticRegression())
        ])
        X, y = load_data(dataset)
        pipe_lg = pipe_lg.fit(X.ravel(), y.ravel())
        pickle.dump(pipe_lg, file_lg)

    return pipe_lg.predict(names)

# Predict using Random Forest
def predict_rf(names, dataset):
    if os.path.isfile("./data/pipe_rf.pkl") and dataset is None:
        file_rf = open('./data/pipe_rf.pkl', 'rb')
        pipe_rf = pickle.load(file_rf)
    else:
        file_rf = open('./data/pipe_rf.pkl', 'wb')
        pipe_rf = Pipeline([
            ('vect', CountVectorizer(analyzer='char_wb', ngram_range=(2, 6))),
            ('tfidf', TfidfTransformer()),
            ('clf', RandomForestClassifier(n_estimators=10, n_jobs=-1))
        ])
        X, y = load_data(dataset)
        pipe_rf = pipe_rf.fit(X.ravel(), y.ravel())
        pickle.dump(pipe_rf, file_rf)

    return pipe_rf.predict(names)

# Main function
def main(args):
    names_df = pd.read_csv(args.names, header=None)
    names = names_df[0].values
    dataset = args.dataset

    if args.ml == 'LG':
        results = predict_lg(names, dataset)
        ml_type = 'Logistic Regression'
    elif args.ml == 'RF':
        results = predict_rf(names, dataset)
        ml_type = 'Random Forest'
    else:
        results = predict_nb(names, dataset)
        ml_type = 'Naive Bayes'

    output_df = pd.DataFrame({'Nama': names, 'Jenis Kelamin': results})
    output_df.to_excel(args.output, index=False)
    print("Prediction results saved to", args.output)
    print("Prediksi jenis kelamin dengan", ml_type, ":")

# Argument parsing
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Menentukan jenis kelamin berdasarkan nama Bahasa Indonesia")
    parser.add_argument("names", help="CSV file containing names for prediction")
    parser.add_argument("-ml", help="NB=Naive Bayes (default); LG=Logistic Regression; RF=Random Forest",
                        choices=["NB", "LG", "RF"], default="NB")
    parser.add_argument("-d", "--dataset", help="Training dataset in CSV format", default="data/yes.csv")
    parser.add_argument("-o", "--output", help="Output file name for the prediction results in XLSX format",
                        default="prediction_results.xlsx")
    args = parser.parse_args()

    main(args)

#run with python mumet.py (yourfile.csv) -ml (ml, lg, lb) -d data.yes.csv - o (your preddiction).xlsx