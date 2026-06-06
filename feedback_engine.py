# feedback_engine.py
import os
import json
from google import genai
from google.genai import types

def get_ai_feedback(question, answer):
    """
    Sends the question and user's answer to Gemini to get a structured JSON feedback report.
    """
    # Initialize the Gemini Client (automatically picks up GEMINI_API_KEY environment variable)
    client = genai.Client()
    
    # Craft a strict prompt to ensure JSON output structure
    prompt = f"""
    You are an expert AI Interview Coach. Analyze the candidate's answer to the given question.
    
    Question: {question}
    Candidate's Answer: {answer}
    
    Provide your evaluation strictly in the following JSON format:
    {{
        "score": <integer from 1 to 10>,
        "strengths": "<what the candidate did well>",
        "weaknesses": "<areas where the answer fell short or can be expanded>",
        "suggested_better_answer": "<a model answer incorporating the feedback>"
    }}
    """
    
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config=types.GenerateContentConfig(
                # Force the model to return a valid JSON object
                response_mime_type="application/json"
            ),
        )
        
        # Parse and return the JSON response
        feedback_data = json.loads(response.text)
        return feedback_data, None
        
    except Exception as e:
        return None, f"Failed to generate AI feedback: {str(e)}"

def generate_final_report(history):
    """
    Generates a final overall summary based on the interview history.
    """
    client = genai.Client()
    
    prompt = f"""
    You are an expert AI Interview Coach. Based on the following interview history, generate a final performance report summary.
    
    Interview History:
    {json.dumps(history, indent=2)}
    
    Provide your evaluation strictly in the following JSON format:
    {{
        "overall_score": <average or comprehensive integer score from 1 to 10>,
        "key_improvements": "<bulleted list of 2-3 main areas the candidate must work on>",
        "summary": "<a motivating closing paragraph summarizing their performance>"
    }}
    """
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config=types.GenerateContentConfig(response_mime_type="application/json"),
        )
        return json.loads(response.text), None
    except Exception as e:
        return None, f"Failed to generate final report: {str(e)}"