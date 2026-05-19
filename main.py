import os
import pandas as pd
from src.data_loader import load_csv
from src.preprocess import clean_text
from src.sentiment_lexicon import get_sentiment

def main():
    # 1. Load data
    input_path = 'data/raw/sample.csv'  # <-- Place your file here
    df = load_csv(input_path)

    # 2. Preprocess text
    df['clean_text'] = df['text'].apply(clean_text)

    # 3. Sentiment Analysis
    df['sentiment'] = df['clean_text'].apply(get_sentiment)

    # 4. Save results
    os.makedirs('data/processed', exist_ok=True)
    df.to_csv('data/processed/sentiment_results.csv', index=False)
    print(df['sentiment'].value_counts())
    print('Results saved to data/processed/sentiment_results.csv')

if __name__ == '__main__':
    main()
