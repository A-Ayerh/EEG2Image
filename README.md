# EEGStyleGAN-ADA
Implementation of EEGStyleGAN-ADA paper [Accepted in WACV 2024]  [[Paper](https://arxiv.org/abs/2310.16532)]

1. Command to train the GAN is mentioned in the Txt file.
2. Checkpoints:
   * EEGStyleGAN-ADA-CVPR40 [[link](https://iitgnacin-my.sharepoint.com/:u:/g/personal/19210048_iitgn_ac_in/EXn-8R80rxtHjlMCzPfhL9UBj80opHXyq3MnBBXXE6IsQw?e=Xbt2zO)]
   
## Config

<pre>
conda create -n to1.7 anaconda python=3.8
conda activate to1.7
pip install torch==1.7.0+cu110 torchvision==0.8.1+cu110 torchaudio==0.7.0 -f https://download.pytorch.org/whl/torch_stable.html
pip install opencv-python==4.5.4.58 opencv-contrib-python==4.5.4.58
pip install natsort
</pre>

## Sources
* EEGStyleGAN-ADA [[Link](https://github.com/prajwalsingh/EEGStyleGAN-ADA)]
* StyleGAN2-ADA [[Link](https://github.com/NVlabs/stylegan2-ada-pytorch)]
