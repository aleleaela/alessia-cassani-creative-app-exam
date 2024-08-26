from transformers import MusicgenProcessor, MusicgenForConditionalGeneration
import scipy.io.wavfile
import numpy as np
import torch
import datetime

model_name = "facebook/musicgen-small"
processor = MusicgenProcessor.from_pretrained(model_name)
model = MusicgenForConditionalGeneration.from_pretrained(model_name)

prompt = ["i have a new black cat in my new house in hamburg! cosa pensi di me caro micio"]
inputs = processor(text=prompt, return_tensors="pt")

with torch.no_grad():
    audio_values = model.generate(**inputs, max_new_tokens=512)

audio_values = audio_values.cpu().numpy()
audio_values = np.int16(audio_values[0, 0] * 32767)

scipy.io.wavfile.write(f"gatto2.wav",
                       rate=model.config.audio_encoder.sampling_rate,
                       data=audio_values)

print("SUCCESS")