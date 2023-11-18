import os
import random
import numpy as np
from scipy.io.wavfile import read, write
from scipy.signal import spectrogram
from tqdm import tqdm

original_folder = 'D:\\TALCS_corpus\\train'
noise_folder = 'D:\\TALCS_corpus\\data_aishell\\noise'
synthetic_folder = 'D:\\TALCS_corpus\\data_aishell\\new'
snr = 10

original_files = os.listdir(original_folder)
noise_files = os.listdir(noise_folder)

for original_file in tqdm(original_files):
    try:
        original_sample_rate, original_data = read(os.path.join(original_folder, original_file))
        noise_file = random.choice(noise_files)

        noise_sample_rate, noise_data = read(os.path.join(noise_folder, noise_file))

        # Ensure the noise length matches the original length
        if len(noise_data) < len(original_data):
            # Repeat the noise to match the original length
            repeats = len(original_data) // len(noise_data) + 1
            noise_data = np.tile(noise_data, repeats)[:len(original_data)]
        else:
            # Trim the noise to match the original length
            noise_data = noise_data[:len(original_data)]

        f, t, Sxx = spectrogram(original_data, original_sample_rate)

        noise_amplitude = np.abs(Sxx) / (snr * 10 ** (np.mean(Sxx) / 10))

        adjusted_amplitude = noise_amplitude / np.sqrt(np.sum(noise_data ** 2))

        noise_data = noise_data * random.uniform(0.010, 0.020)

        synthetic_data = original_data + noise_data

        if not os.path.exists(synthetic_folder):
            os.makedirs(synthetic_folder)

        write(os.path.join(synthetic_folder, original_file), original_sample_rate, synthetic_data)
    except Exception as e:
        print(f"Error processing file {original_file}: {e}")