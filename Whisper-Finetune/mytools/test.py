from scipy.io import wavfile
import numpy as np

sample_rate, sig = wavfile.read("D:\\TALCS_corpus\\data_aishell\\noise\\_rec_19_20200525_093854.wav")
print("sample rate: %d" % sample_rate)
print(sig)

if sig.dtype == np.int16:
    print("PCM16 integer")
if sig.dtype == np.float32:
    print("PCM32 float")