# I will change it into proper format later

instruction = {
    "demo": """
<span style="color: red;">
    This demo uses a free tier server and free API with strict request limits and limited capabilities for some models. For a significantly better experience, run the service locally. The demo performance is worse than of a locally running service (slow, buggy, robotic voice, too short messages, etc.). If some model is unavailable, please wait a minute before retrying. Persistent unavailability might mean that the request limit has been reached and demo is unavailable for a while. 
</span>
    """,
    "introduction": """
# Welcome to the AI Mock Interviewer!

This tool is designed to help you practice coding interviews by simulating the real interview experience. Here you can brush your interview skills in a realistic setting, although it’s not intended to replace thorough preparations like studying algorithms or practicing coding problems.

## Key Features

- **Speech-First Interface**: Talk to the AI just like you would with a real interviewer. This makes your practice sessions feel more realistic.
- **Various AI Models**: The tool uses three types of AI models:
  - **LLM (Large Language Model)**: Acts as the interviewer.
  - **Speech-to-Text and Text-to-Speech Models**: These help mimic real conversations by converting spoken words to text and vice versa.
- **Model Flexibility**: The tool works with many different models, including those from OpenAI and open-source models from Hugging Face.

## Planned Updates

This is just the first beta version, and I'm working on enhancing this tool. Planned updates include:
1. **More Interview Types**: Adding simulations like Systems Design, Machine Learning System Design, Math and Logic, Behavioral Interviews, and Theory Tests.
2. **Streaming Mode for Models**: Updating the models to provide faster responses during interviews.
3. **Testing More Models**: Exploring additional open-source models to enhance the tool’s performance and flexibility.
4. **Improving the User Interface**: Making it easier to navigate and use, ensuring a better experience for all users.
    """,
    "quick_start": """
# Running the AI Tech Interviewer Simulator

To get the real experience you should run the service locally and use your own API key or local model.

## Initial Setup

### Clone the Repository

First, clone the project repository to your local machine with the following commands:

```bash
git clone https://huggingface.co/spaces/IliaLarchenko/interviewer
cd interviewer
```

### Configure the Environment

Create a `.env` file from the provided Open AI example and edit it to include your OpenAI API key (learn how to get it here: https://platform.openai.com/api-keys):

```bash
cp .env.openai.example .env
nano .env  # You can use any text editor
```

If you want to use any other model, follow the instructions in Models Configuration section.

### Build and Run the Docker Container

To build and start the Docker container:

```bash
docker-compose build
docker-compose up
```

The application will be accessible at `http://localhost:7860`.

### Running Locally (alternative)

Set up a Python environment and install dependencies to run the application locally:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

The application should now be accessible at `http://localhost:7860`.
    """,
    "interface": """
# Interview Interface Overview

This tool will support different types of interviews, but currently focusing on coding interviews only. Here's how to navigate the interface:

### Setting
Configure the interview settings such as difficulty, topic, and any specific requirements. Start the interview by clicking the **"Generate a problem"** button.

### Problem Statement
The AI will present a coding problem after you initiate the session.

### Solution
This section is where the interaction happens:
- **Code Area**: On the left side, you will find a space to write your solution. You can use any programming language, although syntax highlighting is only available for Python currently.
- **Communication Area**: On the right, this area includes:
  - **Chat History**: Displays the entire dialogue history, showing messages from both you and the AI interviewer.
  - **Audio Record Button**: Use this button to record your responses. Press to start recording, speak your thoughts, and press stop to send your audio. Your message will be transcribed and added to the chat, along with a snapshot of your code. For code-only messages, type your code and record a brief message like "Check out my code."

Engage with the AI as you would with a real interviewer. Provide concise responses and frequent updates rather than long monologues. Your interactions, including any commentary on your code, will be recorded and the AI's responses will be read aloud and displayed in the chat. Follow the AI's instructions and respond to any follow-up questions as they arise.

Once the interview is completed, or if you decide to end it early, click the **"Finish the interview"** button.

### Feedback
Detailed feedback will be provided in this section, helping you understand your performance and areas for improvement.  
    """,
    "models": """
# Models Configuration

This tool utilizes three types of AI models: a Large Language Model (LLM) for simulating interviews, a Speech-to-Text (STT) model for audio processing, and a Text-to-Speech (TTS) model for auditory feedback. You can configure each model separately to tailor the experience based on your preferences and available resources.

## Flexible Model Integration

You can connect various models from different sources to the tool. Whether you are using models from OpenAI, Hugging Face, or even locally hosted models, the tool is designed to be compatible with a range of APIs. Here’s how you can configure each type:

### Large Language Model (LLM)

- **OpenAI Models**: You can use models like GPT-3.5-turbo or GPT-4 provided by OpenAI. Set up is straightforward with your OpenAI API key.
- **Hugging Face Models**: Models like Meta-Llama from Hugging Face can also be integrated. Make sure your API key has appropriate permissions.
- **Local Models**: If you have the capability, you can run models locally. Ensure they are compatible with the Hugging Face API for seamless integration.

### Speech-to-Text (STT)

- **OpenAI Whisper**: Available via OpenAI, this model supports multiple languages and dialects. It is also available in an open-source version on Hugging Face, giving you the flexibility to use it either through the OpenAI API or as a locally hosted version.
- **Other OS models**: Can be used too but can require a specific wrapper to align with API requirements.

### Text-to-Speech (TTS)

- **OpenAI Models**: The "tts-1" model from OpenAI is fast and produces human-like results, making it quite convenient for this use case.
- **Other OS models**: Can be used too but can require a specific wrapper to align with API requirements. In my experience, OS models sound more robotic than OpenAI models.

## Configuration via .env File

The tool uses a `.env` file for environment configuration. Here’s a breakdown of how this works:

- **API Keys**: Whether using OpenAI, Hugging Face, or other services, your API key must be specified in the `.env` file. This key should have the necessary permissions to access the models you intend to use.
- **Model URLs and Types**: Specify the API endpoint URLs for each model and their type (e.g., `OPENAI_API` for OpenAI models, `HF_API` for Hugging Face or local APIs).
- **Model Names**: Set the specific model name, such as `gpt-3.5-turbo` or `whisper-1`, to tell the application which model to interact with.

### Example Configuration

OpenAI LLM:
```plaintext
OPENAI_API_KEY=sk-YOUR_OPENAI_API_KEY
LLM_URL=https://api.openai.com/v1
LLM_TYPE=OPENAI_API
LLM_NAME=gpt-3.5-turbo
```

Hugging face TTS:
```plaintext
HF_API_KEY=hf_YOUR_HUGGINGFACE_API_KEY
TTS_URL=https://api-inference.huggingface.co/models/facebook/mms-tts-eng
TTS_TYPE=HF_API
TTS_NAME=Facebook-mms-tts-eng
```

Local STT:
```plaintext
HF_API_KEY=None
STT_URL=http://127.0.0.1:5000/transcribe
STT_TYPE=HF_API
STT_NAME=whisper-base.en
```

You can configure each models separately. Find more examples in the `.env.example` files provided.

    """,
    "acknowledgements": """
# Acknowledgements

The service is powered by Gradio, and the demo version is hosted on HuggingFace Spaces.

Even though the service can be used with great variety of models I want to specifially acknowledge a few of them:
- **OpenAI**: For models like GPT-3.5, GPT-4, Whisper, and TTS-1. More details on their models and usage policies can be found at [OpenAI's website](https://www.openai.com).
- **Meta**: For the Llama models, particularly the Meta-Llama-3-70B-Instruct, as well as Facebook-mms-tts-eng model. Visit [Meta AI](https://ai.facebook.com) for more information.
- **HuggingFace**: For a wide range of models and APIs that greatly enhance the flexibility of this tool. For specific details on usage, refer to [Hugging Face's documentation](https://huggingface.co).

Please ensure to review the specific documentation and follow the terms of service for each model and API you use, as this is crucial for responsible and compliant use of these technologies.
    """,
}

if __name__ == "__main__":
    spaces_config = """---
title: Interviewer
emoji: 📚
colorFrom: pink
colorTo: yellow
sdk: gradio
sdk_version: 4.27.0
app_file: app.py
pinned: true
license: apache-2.0
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

"""
    with open("README.md", "w") as f:
        f.write(spaces_config)

        for key in ("introduction", "quick_start", "interface", "models", "acknowledgements"):
            f.write(instruction[key])
            f.write("\n\n")