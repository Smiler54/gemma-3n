from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("google/gemma-3n-E4B")
model = AutoModelForCausalLM.from_pretrained("google/gemma-3n-E4B")

import speech_recognition as sr

def transcribe_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Speak now...")
        audio = r.listen(source)
        text = r.recognize_google(audio)
        print("📝 Transcribed:", text)
        return text
    
from PIL import Image

def load_image(image_path):
    image = Image.open(image_path).convert("RGB")
    image = image.resize((224, 224))  # simple resize
    return image

def query_gemma(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=100)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# 
caption = query_gemma("Describe the image of a dog sitting on a beach.")

if __name__ == "__main__":
    spoken = transcribe_speech()
    image = load_image("sample.jpg")
    
    prompt = f"User said: {spoken}\nBased on the image, answer:"
    response = query_gemma(prompt)
    print("🤖 Response:", response)