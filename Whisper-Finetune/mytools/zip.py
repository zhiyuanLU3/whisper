import os
import zipfile
from tqdm import tqdm

data_directory = "D:\\TALCS_corpus\\data_aishell\\new"
output_directory = "D:\\TALCS_corpus\\data_aishell"

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

wav_files = [f for f in os.listdir(data_directory) if f.endswith('.wav')]

batch_size = 2500
num_batches = len(wav_files) // batch_size

for i in tqdm(range(num_batches)):
    start_index = i * batch_size
    end_index = (i + 1) * batch_size

    batch_files = wav_files[start_index:end_index]

    # 创建 ZIP 文件
    zip_filename = os.path.join(output_directory, f'train{i + 1}.zip')
    with zipfile.ZipFile(zip_filename, 'w') as zip_file:
        # 将每个 WAV 文件添加到 ZIP 文件中
        for wav_file in batch_files:
            wav_path = os.path.join(data_directory, wav_file)
            zip_file.write(wav_path, os.path.basename(wav_path))

print("Data compression and saving completed.")
