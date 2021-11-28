# Audio Mnist Classification/Recognition

- Purpose: practice the ML tech
- Dataset size
    - equips 30,000 audios，60 speakers speak 1~10
    - 9.5  小時，取樣率為48K 16bits
- AudioMNIST Paper: [https://arxiv.org/pdf/1807.03418.pdf](https://arxiv.org/pdf/1807.03418.pdf)


## To DO 
- [ ] Implement an audio classifier with Pytorch 
- [ ] Implement an audio classifier with Pytorch Lightning 



## Resource

- Pytorch-tutorial
    - https://pytorch-lightning.readthedocs.io/en/latest/notebooks/course_UvA-DL/01-introduction-to-pytorch.html
    - https://uvadlc-notebooks.readthedocs.io/en/latest/
    - https://github.com/vahidk/EffectivePyTorch
    - https://github.com/phlippe/uvadlc_notebooks

- How to write the dataset/dataloader with Pytorch?
    - Pytorch Audio Datasets Example, includes gtzan,librispeech,speechcommands,vctk etc....
        - https://github.com/pytorch/audio/tree/main/torchaudio/datasets 
    - Many audio source separation datasets writing examples
        - https://github.com/asteroid-team/asteroid/tree/master/asteroid/data 
    - How did FB/Research write their Dataset/Dataloader for audio processing? 
        -  https://github.com/facebookresearch/denoiser/blob/main/denoiser/audio.py
    - How did SpeechBrain design their Dataset/Dataloader?
        - https://github.com/speechbrain/speechbrain/blob/develop/speechbrain/dataio/dataset.py
    - Writing custom datasets, dataloaders and transformers
        - https://pytorch.org/tutorials/beginner/data_loading_tutorial.html  
    - A detailed example of how to generate your data in parallel with Pytorch?
        - https://stanford.edu/~shervine/blog/pytorch-how-to-generate-data-parallel  
    - Building Efficient Custom Datasets in Pytorch?
        - https://towardsdatascience.com/building-efficient-custom-datasets-in-pytorch-2563b946fd9f

- lighting-hydra template
    - https://github.com/ashleve/lightning-hydra-template
- Pytorch example for speech commands
    [https://pytorch.org/tutorials/intermediate/speech_command_recognition_with_torchaudio.html](https://pytorch.org/tutorials/intermediate/speech_command_recognition_with_torchaudio.html)
    
- [https://stackoverflow.com/questions/21645082/applying-neural-network-to-mfccs-for-variable-length-speech-segments](https://stackoverflow.com/questions/21645082/applying-neural-network-to-mfccs-for-variable-length-speech-segments)
- 若是語音分類，資料長短不同，需要padding 0 再丟入訓練
    - [https://discuss.pytorch.org/t/about-the-variable-length-input-in-rnn-scenario/345/13](https://discuss.pytorch.org/t/about-the-variable-length-input-in-rnn-scenario/345/13)
    - [https://stackoverflow.com/questions/49655891/what-type-of-neural-network-can-handle-variable-input-and-output-sizes](https://stackoverflow.com/questions/49655891/what-type-of-neural-network-can-handle-variable-input-and-output-sizes)
- Google CNN for small footprint Keyword Spotting: [https://static.googleusercontent.com/media/research.google.com/zh-TW//pubs/archive/43969.pdf](https://static.googleusercontent.com/media/research.google.com/zh-TW//pubs/archive/43969.pdf)
- [https://github.com/Mmiglio/SpeechRecognition](https://github.com/Mmiglio/SpeechRecognition)
- CTC-based query-by-example Keyword Spotting: [https://openreview.net/pdf?id=SkMRja6ssQ](https://openreview.net/pdf?id=SkMRja6ssQ)
- 語音識別問題： 關鍵詞識別與遷入識別：[http://www.360doc.com/content/20/0821/10/7673502_931426388.shtml](http://www.360doc.com/content/20/0821/10/7673502_931426388.shtml)

- pytorch lightening 入坑心得：https://medium.com/%E6%95%B8%E5%AD%B8-%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7%E8%88%87%E8%9F%92%E8%9B%87/pytorch-lightning-%E5%85%A5%E5%9D%91%E5%BF%83%E5%BE%97-81af12de9bb7

- 雨林聲音辨識，有人使用多種augmentation (stretch/pitch shifting/arbitrary noise)
可以參考他的notebooks
    - [https://www.kaggle.com/hidehisaarai1213/rfcx-audio-data-augmentation-japanese-english](https://www.kaggle.com/hidehisaarai1213/rfcx-audio-data-augmentation-japanese-english)
