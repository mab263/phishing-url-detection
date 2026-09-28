# Phishing URL Detection 🔗

A logistic regression model that predicts whether a URL is phishing or legitimate, using structural features of the URL (length, HTTPS usage, symbol counts, etc.)

## Dataset Notes 📝
- Source: [https://www.kaggle.com/datasets/sunnykusawa/phishing-urls]
- target: 0 = phishing URL, 1 = legitimate URL
- 2,488 rows, 13 features, no missing values
- Class balance: 52.8% legitimate, 47.2% phishing (roughly balanced)

## Model Results 📈
- Baseline model: Logistic Regression (scaled features)
- Accuracy: 85.3%
- Phishing recall: 94% (catches most phishing URLs)
- Legitimate recall: 76% (some legitimate URLs flagged as phishing — a deliberate tradeoff, since under-flagging phishing is more costly than over-flagging)

## Key Findings 🔍
- `valid_url` and `url_length` are the strongest indicators of a legitimate URL
- `path_length` and `nb_www` (www occurrences) are the strongest indicators of phishing
- Feature scaling mattered significantly: `url_length` and `path_length` appeared unimportant before scaling but were actually top predictors once feature scale was normalized