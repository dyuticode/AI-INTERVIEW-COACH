

QUESTIONS = {
    "Technical Interview": [
        "What is the difference between AI, Machine Learning, and Deep Learning?",
        "Explain the main difference between supervised and unsupervised learning.",
        "What is overfitting, and how can it be reduced?",
        "What is underfitting, and how do you fix it?",
        "Why do we split data into training and testing datasets?",
        "What is cross-validation and why is it important?",
        "Can you explain what feature engineering is?",
        "What is the difference between normalization and standardization?",
        "What is data preprocessing, and why is it necessary?",
        "What is an activation function in a neural network?",
        "How does gradient descent work?",
        "What is a confusion matrix, and what metrics can you derive from it?",
        "Explain the trade-off between precision and recall.",
        "What is the F1 score, and when should you use it?",
        "What is the core difference between classification and regression?",
        "How does the K-Means clustering algorithm work?",
        "What is a decision tree, and how does it make splits?",
        "How does a random forest improve upon a standard decision tree?",
        "What are the primary advantages of using Python for data science?",
        "What is the fundamental difference between a list and a tuple in Python?",
        "What is the difference between a list and a dictionary in Python?",
        "What are the main use cases for the NumPy and Pandas libraries?",
        "What is the difference between SQL and NoSQL databases?",
        "What are primary and foreign keys in a relational database?",
        "Can you explain the basic steps of the ETL process?"
    ],
    "HR Interview": [
        "Tell me about yourself.",
        "What are your greatest strengths?",
        "What are your weaknesses, and how are you working on them?",
        "Why should we hire you for this role?",
        "Why are you interested in joining our company?",
        "What motivates you to perform at your best?",
        "Where do you see yourself professionally in five years?",
        "How do you handle high-pressure situations or tight deadlines?",
        "Tell me about a significant challenge you faced and how you overcame it.",
        "Tell me about a past failure and what you learned from it.",
        "Describe a scenario where you demonstrated leadership qualities.",
        "Tell me about a time you worked as part of a team to achieve a goal.",
        "How do you approach resolving conflicts within a team project?",
        "How do you prioritize your tasks when handling multiple responsibilities?",
        "Why did you choose to study Data Science & AI?",
        "What specific skills or knowledge do you hope to gain from this internship?",
        "How do you go about teaching yourself a new technology or framework?",
        "How do you handle constructive criticism or negative feedback?",
        "Describe your ideal working environment.",
        "How do you stay up-to-date with emerging technology trends?",
        "What does personal and professional success mean to you?",
        "What would your peers or professors say is your best quality?",
        "Do you prefer working independently or collaboratively, and why?",
        "Tell me about a time you made a mistake and how you corrected it.",
        "Do you have any questions for us about the role or the team?"
    ]
}

def get_questions_by_type(interview_type):
    """Returns the list of questions for a specific interview type."""
    return QUESTIONS.get(interview_type, [])