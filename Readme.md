# Gemini Video Evaluator

Gemini Video Evaluator is a Python application that uses Google Gemini AI to analyze video recordings of customer service or staff interactions. It generates detailed evaluation reports based on non-verbal listening and responding skills, following customizable rubrics.

## Features

- Evaluates non-verbal listening and responding skills from video frames.
- Uses Google Gemini API for advanced video analysis.
- Customizable rubrics for feedback and scoring.
- Outputs structured JSON and human-readable summaries.

## Project Structure

```
prompts.py
main.py
```

- `main.py`: Main script to process videos and generate evaluation reports.
- `prompts.py`: Contains prompt templates and rubrics for Gemini.
- `.env`: Stores API keys for Gemini and Google.
- `good_response.mp4`, `short.mp4`: Example video files for testing.

## Setup

1. **Clone the repository**  
   ```
   git clone https://github.com/MuhammadMuaaz9/gemini-video-evaluator.git
   cd Gemini-Video-Evaluator
   ```

2. **Install dependencies**  
   ```
   pip install -r requirements.txt
   ```

3. **Configure API keys**  
   - Add your Gemini and Google API keys to the `.env` file.

4. **Run the application**  
   ```
   python main.py
   ```

## Usage

- Place your video file (e.g., `good_response.mp4`) in the project directory.
- Run `main.py` to process the video and print the evaluation summary.

## Customization

- Modify rubrics and prompts in [`prompts.py`] to fit your evaluation needs.

**Note:** This project requires access to the Google Gemini API. Make sure your API key has the necessary