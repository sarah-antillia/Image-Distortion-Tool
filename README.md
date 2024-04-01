<h2> Image-Distortion-Tool (Updated: 2024/04/01)</h2>

<li>2024/04/01: Modified the output file name to be a format of "distorted_{ratio}_rsigma{rsigma}_sigma{sigma}_{origina_filename}". </li>
<li>2024/04/01: Added Distortion Example of MultipleMyeloma Dataset. </li>
<br>
<a href="#1">1, ImageDistorter</a><br>
<a href="#2">2, Run ImageDistorter</a><br>
<a href="#3">3. Seeing Is Believing</a><br>
<a href="#4">4. MultipleMyeloma Dataset Distortion</a><br>
<br>
<h3> 
<a id="1">1. ImageDistorter</a>
</h3>

This is a simple python class <a href="./ImageDistorter.py">ImageDistorter</a> to distort an image by using scipy gaussian filter and OpenCV remap.
It is based on the code in the following stackoverflow web-site.<br>
<br>
https://stackoverflow.com/questions/41703210/inverting-a-real-valued-index-grid/78031420#78031420
<br>
<br>
Distortion Example by ImageDistorter<br>
<img src="./distorted3/distorted_0.02_rsigma0.5_sigma40_MeshedPicture.png" width="640" height="auto"><br>

<br>
In this class, we use the 
<a href="https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.gaussian_filter.html">scipy gaussian_filter</a>
<pre>
scipy.ndimage.gaussian_filter(input, sigma, order=0, output=None, mode='reflect', cval=0.0, 
   truncate=4.0, *, radius=None, axes=None)[source]
</pre>

This ImageDistorter runs on Python 3.8 or later version. Please install opencv-python and scipy to your Python development enviroment.<br>  
This tool can be used to augment the image and mask files to train an image segmentation model.
Please refer to <a href="#4">4. MultipleMyeloma Dataset Distortion</a>, which is a typical example of offline augmentation.<br>
You can use the ImageDistorter class to train a segmentation model for your online dataset augmentation tool.
Image distortion can be time-consuming when used for online dataset augmentation, which will slow down the training-speed.
<br>
<h3>
<a id="2">2. Run ImageDistorter</a>
</h3> 
To run ImageDistorter, please specify a <i>distortion.config</i> as a command-line parameter as shown below.
<pre>
>python ImageDistorter distortion.config
</pre>
distortion.config file takes a typical ini file format.<br>
<pre>
[distortion]
; Image input directory
images_dir             = "./images"
; Image output directory
output_dir             = "./distorted"
gaussian_filter_rsigma = 40
gaussian_filter_sigma  = 0.5
;Specify a list of distortion rate which is less than 1.
distortions            = [0.01, 0.02, 0.03]
</pre>

<h3>
2.1 Run ImageDistorter with a distortion.config
</h3> 

Please run the following command.
<pre>
>python ImageDistorter distortion.config
</pre>
, where distortion.config is the following.<br>
<pre>
;distortion.config
[distortion]
images_dir             = "./images"
output_dir             = "./distorted"
gaussian_filter_rsigma = 40
gaussian_filter_sigma  = 0.5
distortions            = [0.01]
</pre>
By running the command above, each image in images_dir will be read, distorted by the parameters in [distortion] section, and
saved to output_dir.<br>

<br>
Original <br>
<img src="./asset/images.png" width="1024" height="auto"><br>
<br>
Distorted <br>
<img src="./asset/distorted.png" width="1024" height="auto"><br>

<br>
Enlarged sample images<br>
coca-cola <br>
<img src="./images/coco-cola.png" width="640" height="auto"><br>
distorted coco-cola<br>
<img src="./distorted/distorted_0.01_rsigma0.5_sigma40_coco-cola.png" width="640" height="auto"><br>
<br>
<br>
cranes <br>
<img src="./images/cranes.jpg" width="640" height="auto"><br>
distorted cranes<br>
<img src="./distorted/distorted_0.01_rsigma0.5_sigma40_cranes.jpg" width="640" height="auto"><br>
<br>
MeshedNioh <br>
<img src="./images/MeshedNioh.png" width="640" height="auto"><br>
distorted MeshedNioh<br>
<img src="./distorted/distorted_0.01_rsigma0.5_sigma40_MeshedNioh.png" width="640" height="auto"><br>
<br>
road_signs <br>
<img src="./images/road_signs.png" width="640" height="auto"><br>
distorted road_signs<br>
<img src="./distorted/distorted_0.01_rsigma0.5_sigma40_road_signs.png" width="640" height="auto"><br>


<h3>
<a id="3">3. Seeing Is Believing</a>
</h3> 
Please run the following command to visualize clearly the distortion effects of this tool, <br>
<pre>
>python ImageDistorter distortion3.config
</pre>
, where distortion.config is the following.<br>
<pre>
;distortion3.config
; 2024/03/30
[distortion]
images_dir             = "./meshed_images"
output_dir             = "./distorted3"
gaussian_filter_rsigma = 40
gaussian_filter_sigma  = 0.5
distortions            = [0.01, 0.02, 0.03]
</pre>
Please note that there are three elements in distortions list as shown above.<br>
By this example, you can easily see the distortion effects by those parameters.

<br>
MeshedPicture <br>
<img src="./meshed_images/MeshedPicture.png" width="640" height="auto"><br>
<br>
Distorted rate=0.01 <br>
<img src="./distorted3/distorted_0.01_rsigma0.5_sigma40_MeshedPicture.png" width="640" height="auto"><br>
Distorted rate=0.02 <br>
<img src="./distorted3/distorted_0.02_rsigma0.5_sigma40_MeshedPicture.png" width="640" height="auto"><br>
Distorted rate=0.03 <br>
<img src="./distorted3/distorted_0.015_rsigma0.5_sigma40_MeshedPicture.png" width="640" height="auto"><br>


<h3>
<a id="4">4. MultipleMyeloma Dataset Distortion</a>
</h3>

<h3>4.1 MultipleMyeloma Dataset</h3>

For a pratical dataset distortion, we have applied this tool to augment MultipleMyeloma Dataset.<br>
<a href="https://drive.google.com/file/d/1QiGah4_0yY-5B7s2kIZ2AjbEVu2ejB3G/view?usp=sharing">MultipleMyeloma-ImageMask-Dataset_V2_X.zip</a>
<br>
On that dataset, please see also <a href="https://github.com/sarah-antillia/MultipleMyeloma-ImageMask-Dataset">MultipleMyeloma-ImageMask-Dataset</a>
<br>
Please expand the downloaded ImageMaskDataset and place them under <b>./</b> folder to be

<pre>
./MultipleMyeloma
 ├─test
 │  ├─images
 │  └─masks
 ├─train
 │  ├─images
 │  └─masks
 └─valid
     ├─images
     └─masks
</pre>
 
Dataset statistics<br>
<img src="./_MultipleMyeloma_.png" width="540" height="auto"><br>

<h3>4.2 Distort MultipleMyeloma Dataset</h3>
Please run the following command.<br>
<pre>
>python ImageDistorter.py distortion_multiplemyeloma.config
</pre>
, where distortion_multiplemyeloma.config is the following.
<pre>
;distortion_multiplemyeloma.config
; 2024/04/01 (C) antillia.com
[distortion]
images_dir             = "./MultipleMyeloma/train"
output_dir             = "./Distorted-MultipleMyeloma/train"
gaussian_filter_rsigma = 40
gaussian_filter_sigma  = 0.5
distortions            = [0.02, 0.03]
</pre>
As shown above, we apply this distortion tool to the train dataset of MultipleMyeloma.<br>
By running the command above, the following directories will be created.<br>
<pre>
./Distorted-MultipleMyeloma
└─train
    ├─images
    └─masks
</pre>
Distorted images<br>
<img src="./asset/Distorted-MultipleMyeloma-train-images.png" width="1024" height="auto"><br><br>
Distorted masks  <br>
<img src="./asset/Distorted-MultipleMyeloma-train-mask.png"  width="1024" height="auto"><br><br>
<br>

By merging the generated "./Distorted-MultipleMyeloma/train" and the original "./MultipleMyeloma" folders, we have finally created
"Distorted-MultipleMyeloma-ImageMask-Dataset".<br>
Statistics :<br>
<img src="./_Distorted-MultipleMyeloma-ImageMask-Dataset_.png" width="540" height="auto"><br>
<br>

We have uploaded this dataset to the google drive
<a href="https://drive.google.com/file/d/1uH8c9zOsglFHKhFDU697NO0Hwnb7S9X6/view?usp=sharing">Distorted-MultipleMyeloma-ImageMask-Dataset.zip</a>
<br>


<h3>Dataset Citation</h3>
The original dataset used here has been take from the following  web site:<br><br>
<b>SegPC-2021-dataset</b><br>
SegPC-2021: Segmentation of Multiple Myeloma Plasma Cells in Microscopic Images<br>
<pre>
https://www.kaggle.com/datasets/sbilab/segpc2021dataset
</pre>

<b>Citation:</b><br>

<pre>
Anubha Gupta, Ritu Gupta, Shiv Gehlot, Shubham Goswami, April 29, 2021, "SegPC-2021: Segmentation of Multiple Myeloma Plasma Cells 
in Microscopic Images", IEEE Dataport, doi: https://dx.doi.org/10.21227/7np1-2q42.

BibTex
@data{segpc2021,
doi = {10.21227/7np1-2q42},
url = {https://dx.doi.org/10.21227/7np1-2q42},
author = {Anubha Gupta; Ritu Gupta; Shiv Gehlot; Shubham Goswami },
publisher = {IEEE Dataport},
title = {SegPC-2021: Segmentation of Multiple Myeloma Plasma Cells in Microscopic Images},
year = {2021} }

IMPORTANT:
If you use this dataset, please cite below publications-
1. Anubha Gupta, Rahul Duggal, Shiv Gehlot, Ritu Gupta, Anvit Mangal, Lalit Kumar, Nisarg Thakkar, and Devprakash Satpathy, 
 "GCTI-SN: Geometry-Inspired Chemical and Tissue Invariant Stain Normalization of Microscopic Medical Images," 
 Medical Image Analysis, vol. 65, Oct 2020. DOI: 
 (2020 IF: 11.148)
2. Shiv Gehlot, Anubha Gupta and Ritu Gupta, 
 "EDNFC-Net: Convolutional Neural Network with Nested Feature Concatenation for Nuclei-Instance Segmentation,"
 ICASSP 2020 - 2020 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 
 Barcelona, Spain, 2020, pp. 1389-1393.
3. Anubha Gupta, Pramit Mallick, Ojaswa Sharma, Ritu Gupta, and Rahul Duggal, 
 "PCSeg: Color model driven probabilistic multiphase level set based tool for plasma cell segmentation in multiple myeloma," 
 PLoS ONE 13(12): e0207908, Dec 2018. DOI: 10.1371/journal.pone.0207908

License
CC BY-NC-SA 4.0
</pre>


