# Copyright 2024 antillia.com Toshiyuki Arai
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# ImageDistoter.py

# The code used here is based on the following stakoverflow web-site
#https://stackoverflow.com/questions/41703210/inverting-a-real-valued-index-grid/78031420#78031420

import os
import sys
import cv2
import glob 
from scipy import ndimage as ndi
from scipy.ndimage.filters import gaussian_filter
import numpy as np
import shutil
from ConfigParser import ConfigParser

import traceback

"""
We use the following gaussian_filter
https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.gaussian_filter.html
scipy.ndimage.gaussian_filter
scipy.ndimage.gaussian_filter(input, sigma, order=0, output=None, mode='reflect', cval=0.0, 
   truncate=4.0, *, radius=None, axes=None)[source]

"""

DISTORTION      = "distortion"

"""
;distortion.config
[distortion]
images_dir             = "./images"
output_dir             = "./distorted"
gaussian_filter_rsigma = 40
gaussian_filter_sigma  = 0.5
distortions            = [0.01, 0.02]


"""

class ImageDistorter:

  def __init__(self, config_file):
    self.config = ConfigParser(config_file)

    self.images_dir = self.config.get(DISTORTION, "images_dir", dvalue="./images")
    if not os.path.exists(self.images_dir):
      error = "Not found " + self.images_dir
      raise Exception(error)

    self.output_dir = self.config.get(DISTORTION, "output_dir", dvalue="./distorted") 

    if os.path.exists(self.output_dir):
      shutil.rmtree(self.output_dir)
    if not os.path.exists(self.output_dir):
      os.makedirs(self.output_dir)

    self.gaussina_filer_rsigma = self.config.get(DISTORTION, "gaussian_filter_rsigma", dvalue=40)
    self.gaussina_filer_sigma  = self.config.get(DISTORTION, "gaussian_filter_sigma",  dvalue=0.5)
    self.distortions           = self.config.get(DISTORTION, "distortions",  dvalue=[0.01, 0.02])
    np.random.seed(137)
  
  
  def distort(self):
    image_files  = glob.glob(self.images_dir + "/*.jpg")
    image_files += glob.glob(self.images_dir + "/*.png")
    image_files += glob.glob(self.images_dir + "/*.bmp")
    image_files += glob.glob(self.images_dir + "/*.tif")
    if len(image_files) == 0:
      print("Not found image_files "+ self.images_dir)
      return
    for image_file in image_files:
      self.distort_one(image_file, self.output_dir)

  def distort_one(self, image_file, output_dir):
    print("--- distort_one {}".format(image_file))
    img  = cv2.imread(image_file)
    basename = os.path.basename(image_file)
  
    shape = (img.shape[1], img.shape[0])
    (w, h) = shape
    xsize = w
    if h>w:
      xsize = h
    # Resize original img to a square image
    resized = cv2.resize(img, (xsize, xsize))
 
    shape   = (xsize, xsize)
 
    t = np.random.normal(size = shape)
    for size in self.distortions:
      filename = "distorted_" + str(size) + basename
      output_file = os.path.join(output_dir, filename)    
      dx = gaussian_filter(t, self.gaussina_filer_rsigma, order =(0,1))
      dy = gaussian_filter(t, self.gaussina_filer_rsigma, order =(1,0))
      sizex = int(xsize*size)
      sizey = int(xsize*size)
      dx *= sizex/dx.max()
      dy *= sizey/dy.max()

      img = gaussian_filter(img, self.gaussina_filer_sigma)

      yy, xx = np.indices(shape)
      xmap = (xx-dx).astype(np.float32)
      ymap = (yy-dy).astype(np.float32)

      distorted = cv2.remap(resized, xmap, ymap, cv2.INTER_LINEAR)
      distorted = cv2.resize(distorted, (w, h))
      cv2.imwrite(output_file, distorted)
      print("=== Saved deformed image file{}".format(output_file))

  
if __name__ == "__main__":
  try:
    config_file = "./distortion.config"
    if len(sys.argv) == 2:
      config_file = sys.argv[1]
    
    if not os.path.exists(config_file):
       error = "Not found " + config_file
       raise Exception(error)

    distorter = ImageDistorter(config_file)
   
    distorter.distort()

  except:
    traceback.print_exc()
