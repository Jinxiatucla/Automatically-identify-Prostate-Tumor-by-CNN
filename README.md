# Automatically-identify-Prostate-Tumor-by-CNN
Usage:
* 0, request our data(data is too big to upload, if you need to run on them, please email me at jinxi@g.ucla.edu)
* 1, set up tensorflow.
* 2, change input file path in finetune_alexnet->finetune
* 3, run finetune_alexnet->finetune to see our results.


finetune_alexnet:
* the code of finetune alex model, including three finetune versions we edited for different batch size.
* The model is built on tensorflow.
* The model is downloaded from this website:
* https://github.com/kratzert/finetune_alexnet_with_tensorflow


prune&generate_path:
* prune: Codes we used for pruning the masked images to images only including prostate part.
* generate_image_path: code we used to generate images path and label for training fine-tune Alexnet


unaugmented_DATA:
* original MRI images from Professor Scalzo. and Xinran
* Images and masks predicted from professor Scalzo's data by our segmentation model.



Augmented_DATA:
* dataset3: augmented segmented images from dataset1.(images path are listed in filelist_train and filelist_test.)
* dataset4: augmented segmented images from dataset2 and have been pruned by predicted masks.(images path are listed in filelist_train and filelist_test.)
* dataset5: augmented unsegmented images from dataset2.(images path are listed in filelist_train and filelist_test.)

Data_augmentation:
* code for augmenting data.
