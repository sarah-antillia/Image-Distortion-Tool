<h2> Image-Distortion-Tool</h2>

 
<h3> 
1 ImageDistorter class
</h3>

This <a href="./ImageDistorter.py">ImageDistorter</a> is a simple python class  to distort an image by using scipy gaussian filter and OpenCV remap.
It is based on the code in the following stackoverflow web-site.<br>
<br>
https://stackoverflow.com/questions/41703210/inverting-a-real-valued-index-grid/78031420#78031420
<br>
<br>
In this class, we use the 
<a href="https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.gaussian_filter.html">scipy gaussian_filter</a>
<pre>
scipy.ndimage.gaussian_filter(input, sigma, order=0, output=None, mode='reflect', cval=0.0, 
   truncate=4.0, *, radius=None, axes=None)[source]
</pre>

This ImageDistorter runs on Python 3.8 or later version. Please install opencv-python and scipy to your Python development enviroment.<br>  
This tool will be used to augment the image and mask files to train an image segmentation model.<br>

<h3>
2 ImageDistorter
</h3> 
To run ImageDistorter, please specify distortion.config as a command parameter
<pre>
>python ImageDistorter distortion.config
</pre>
distortion,config file is a ini file as shown below.<br>
<pre>
[distortion]
; Image input directory
images_dir             = "./images"
; Image output directory
output_dir             = "./distorted"
gaussian_filter_rsigma = 40
gaussian_filter_sigma  = 0.5
;Specify a list of distorition rate
distortions            = [0.01, 0.02, 0.03]
</pre>
<h3>
2.1 Run ImageDistorter with distortion.config
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
<img src="./distorted/distorted_0.01coco-cola.png" width="640" height="auto"><br>
<br>

cranes <br>
<img src="./images/cranes.jpg" width="640" height="auto"><br>
distorted cranes<br>
<img src="./distorted/distorted_0.01cranes.jpg" width="640" height="auto"><br>

road_signs <br>
<img src="./images/road_signs.png" width="640" height="auto"><br>
distorted road_signs<br>
<img src="./distorted/distorted_0.01road_signs.png" width="640" height="auto"><br>


