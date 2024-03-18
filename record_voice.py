import pyaudio
import wave
from openai import OpenAI

def grabar(client):
    chunks = 1024
    sample_format = pyaudio.paInt16
    channels = 1
    fs = 44100
    seconds = 3
    filename = "output.wav"

    p = pyaudio.PyAudio()

    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunks,
                    input=True)

    frames = []

    for i in range(0, int(fs / chunks * seconds)):
        data = stream.read(chunks)
        frames.append(data)

    stream.stop_stream()
    stream.close()

    p.terminate()
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()

    audio_file = open("output.wav", "rb")
    transcript = client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file
    )
    return transcript.text