from pydub import AudioSegment
song= AudioSegment.from_wav("d:/voice/test.wav")
first_10_seconds = song[:58*1000]
first_10_seconds.export("d:/voice/out.wav", format="wav")