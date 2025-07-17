# gemma-3n

A Python app that listens to your voice, transcribes it, analyzes an image, and returns a caption or answer using Google's Gemma 3n multimodal model.

## Features
- **Speech Recognition**: Captures and transcribes spoken input using your microphone.
- **Image Analysis**: Loads and processes an image for context.
- **Multimodal Reasoning**: Uses the Gemma 3n E4B model to generate answers or captions based on both text and image input.

## Requirements
- Python 3.8+
- [transformers](https://pypi.org/project/transformers/) >= 4.53.1
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) >= 3.14.3
- [pillow](https://pypi.org/project/Pillow/) >= 11.3.0

Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage
1. Place an image file named `sample.jpg` in the project directory (or modify the code to use your own image path).
2. Run the app:
   ```bash
   python main.py
   ```
3. Speak into your microphone when prompted. The app will transcribe your speech, analyze the image, and generate a response using Gemma 3n.

## Example
```
🎙️ Speak now...
📝 Transcribed: What is the dog doing on the beach?
🤖 Response: The dog is sitting on the beach, possibly enjoying the view or resting.
```

## About Gemma 3n
This project uses the [google/gemma-3n-E4B](https://huggingface.co/google/gemma-3n-E4B) model, a state-of-the-art, open, multimodal model from Google DeepMind. Gemma 3n supports text, image, and audio input, and is optimized for efficient execution on a wide range of devices. Learn more in the [official documentation](https://ai.google.dev/gemma/docs/gemma-3n).

## References
- [Gemma 3n Model Card](https://ai.google.dev/gemma/docs/gemma-3n/model_card)
- [Hugging Face: google/gemma-3n-E4B](https://huggingface.co/google/gemma-3n-E4B)
- [SpeechRecognition Library](https://github.com/Uberi/speech_recognition)
- [Pillow (PIL)](https://python-pillow.org/)

## Notes
- The app requires a working microphone and an image file named `sample.jpg` in the project directory.
- For best results, use clear speech and high-quality images.
- The first run may take time as the model downloads weights from Hugging Face.
