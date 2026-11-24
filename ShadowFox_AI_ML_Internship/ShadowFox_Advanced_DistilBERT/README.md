
# DistilBERT Sentiment Analysis

## ShadowFox AI/ML Engineer Internship – Advanced Task

### Project Overview
This project implements a pretrained DistilBERT language model
for sentiment analysis using Python and Hugging Face Transformers.

The model classifies text into two categories:
- POSITIVE
- NEGATIVE

An interactive sentiment analysis application is developed using Gradio.

### Objectives
- Understand pretrained transformer-based language models.
- Implement DistilBERT using Hugging Face Transformers.
- Explore tokenization and attention masks.
- Test different text inputs.
- Evaluate model performance.
- Develop an interactive Gradio application.
- Study model strengths, limitations, and ethical considerations.

### Technologies Used
- Python
- Google Colab
- Hugging Face Transformers
- PyTorch
- DistilBERT
- Gradio
- Pandas
- Scikit-learn
- Matplotlib

### Pretrained Model
Model: distilbert/distilbert-base-uncased-finetuned-sst-2-english

Model Configuration:
- Transformer Layers: 6
- Attention Heads: 12
- Hidden Size: 768
- Vocabulary Size: 30,522
- Number of Labels: 2
- Total Parameters: 66,955,010

### Project Implementation
1. Loaded the pretrained DistilBERT model.
2. Explored text tokenization.
3. Examined input IDs and attention masks.
4. Tested positive and negative sentences.
5. Tested challenging sentences involving sarcasm and mixed sentiment.
6. Developed a Gradio application.
7. Saved prediction results in CSV files.
8. Examined model configuration and parameters.
9. Evaluated performance using accuracy, precision, recall,
   F1-score, and a confusion matrix.
10. Tested custom user inputs.
11. Studied strengths and limitations.
12. Explored ethical considerations.

### Performance Evaluation
The model was evaluated using a small manually labelled
dataset containing 10 sentences.

Results on this test set:
- Accuracy: 100%
- Precision: 1.00
- Recall: 1.00
- F1-score: 1.00

Note: These results apply only to the selected 10 test examples
and do not establish general real-world performance.

### Gradio Application
The application:
- Accepts user-provided text.
- Predicts positive or negative sentiment.
- Displays the predicted sentiment.
- Displays a confidence score.

### Strengths
- Lightweight compared with BERT.
- Fast inference.
- Easy implementation using Hugging Face.
- Useful for binary sentiment classification.

### Limitations
- Does not provide a neutral sentiment category.
- May struggle with sarcasm.
- May misunderstand mixed opinions.
- Confidence scores do not guarantee correctness.
- May be affected by biases in training data.

### Ethical Considerations
- Avoid biased interpretations.
- Protect users' private information.
- Communicate prediction limitations.
- Use predictions responsibly.
- Include human judgment in important decisions.

### Project Structure
- notebooks: Completed DistilBERT notebook
- reports: CSV evaluation and prediction results
- app: Gradio application Python file
- screenshots: Project screenshots

### Conclusion
This project provided practical experience in Natural Language
Processing using a pretrained transformer-based model.
It demonstrated how DistilBERT can perform sentiment
classification and how to develop an interactive application.

### Internship
Organization: ShadowFox
Role: AI/ML Engineer Intern
Task Level: Advanced
