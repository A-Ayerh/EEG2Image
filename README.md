# EEGStyleGAN-ADA
Implementation of EEGStyleGAN-ADA paper [Accepted in WACV 2024]  [[Paper](https://arxiv.org/abs/2310.16532)]

1. Command to train the GAN is mentioned in the Txt file: cmd_generate.txt.
2. Checkpoints:
   * EEGStyleGAN-ADA-CVPR40 [[link](https://drive.google.com/file/d/1Wk3YRcQ6UMXpPnRfqOuEe2OZdTLLBpQi/view?usp=sharing)]
3. cd into EEGStyleGAN-ADA_CVPR40
4. run python `generate.py --network out/00000-EEGImageCVPR40-cond-mirror-cifar-bgcfnc/network-snapshot-005322.pkl --outdir generated_images/4 --seeds 0 --data=../dataset/eeg_imagenet40_cvpr_2017_raw/test2/*`
   
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
