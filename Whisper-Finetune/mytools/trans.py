import subprocess
import os
from tqdm import tqdm


def convert_to_pcm_ffmpeg(input_file, output_file):
    # 使用 ffmpeg 进行转换
    command = ["ffmpeg", "-i", input_file, "-f", "wav", "-acodec", "pcm_s16le", output_file]
    subprocess.run(command)

def convert_all_to_pcm_ffmpeg(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in tqdm(os.listdir(input_folder)):
        if filename.endswith(".wav"):
            input_file = os.path.join(input_folder, filename)
            output_file = os.path.join(output_folder, filename)
            convert_to_pcm_ffmpeg(input_file, output_file)

# 噪音文件夹路径
noise_folder = 'D:\\TALCS_corpus\\项目语音数据\\噪音'
# 处理后的噪音保存文件夹路径
output_folder = 'D:\\TALCS_corpus\\data_aishell\\noise'

convert_all_to_pcm_ffmpeg(noise_folder, output_folder)
