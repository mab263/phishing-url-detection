# Phishing URL Detection 🔗

A logistic regression model that predicts whether a URL is phishing or legitimate, using structural features of the URL (length, HTTPS usage, symbol counts, etc.)

## Dataset Notes 📝
- Source: [https://www.kaggle.com/datasets/sunnykusawa/phishing-urls]
- target: 0 = phishing URL, 1 = legitimate URL
- 2,488 rows, 13 features, no missing values
- Class balance: 52.8% legitimate, 47.2% phishing (roughly balanced)