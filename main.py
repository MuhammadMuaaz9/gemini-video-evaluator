import os
import google.generativeai as genai
from pathlib import Path
from dotenv import load_dotenv
from prompts import base_prompt_responding
import json

load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-1.5-flash')


def summarize_video(video_path):

    response_struct_listening = json.dumps({
    "listeningEvaluation": {
        "Eye Contact": {
            "score": "integer (1-5)",
            "explanation": "string"
        },
        "Facial Expressions": {
            "score": "integer (1-5)",
            "explanation": "string"
        },
        "Head and Shoulders Alignment": {
            "score": "integer (1-5)",
            "explanation": "string"
        },
        "Micro Gestures": {
            "score": "integer (1-5)",
            "explanation": "string"
        }
    },
    "overallScore": "integer (1-5)",
    "starRating": "string (★★☆☆☆)",
    "strengths": "string",
    "improvements": "string"
})
    
    prompt_text = f"\nPlease return response in json of format {response_struct_listening}\n"
    
    # Extract system prompt from base_prompt_responding
    system_prompt = ""
    user_prompt = ""
    
    for message in base_prompt_responding:
        if message.get('role') == 'system':
            system_prompt = message.get('content', '')
        elif message.get('role') == 'user':
            for content in message.get('content', []):
                if content.get('type') == 'text':
                    user_prompt += content.get('text', '') + "\n"
    
    # Combine all prompts
    combined_prompt = f"{system_prompt}\n\n{user_prompt}\n\n{prompt_text}"

    try:
        print(f"Processing video: {video_path}")
        
        with open(video_path, "rb") as video_file:
            video_data = video_file.read()

        
        
        # Configure generation settings
        generation_config = {
            "temperature": 0.3,
            "max_output_tokens": 2000,
        }
        
        # Generate summary using Gemini
        response = model.generate_content([
            combined_prompt,
            {"mime_type": "video/mp4", "data": video_data}
        ], generation_config=generation_config)
        
        return response.text
        
    except Exception as e:
        return f"Error processing video {video_path}: {str(e)}"



def process_single_video(video_path):

    summary = summarize_video(video_path)
    
    return {
        "video_path": video_path,
        "video_name": Path(video_path).name,
        "summary": summary
    }


if __name__ == "__main__":
    
    video = "good_response.mp4"
    
    if os.path.exists(video):
        print("Processing single video...")
        
        result = process_single_video(video)
        print(f"Summary: {result['summary']}")