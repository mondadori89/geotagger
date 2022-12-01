# Geotagger

Open the terminal on this folder and run:
```
pip install exif
```

## Geotaging images with txt file

The txt file should be like: <br/>
Name: **geotagfile.txt**    <br/>
Format: <br/>
Lat Long Alt

Example:
```
-12.598716360 -44.124049631 961.1079 0 0 0 3 5
-12.598950484 -44.123816338 961.6306 0 0 0 3 5
-12.599246306 -44.123671023 961.5233 0 0 0 3 5
-12.599561691 -44.123649569 961.4831 0 0 0 3 5
-12.599884866 -44.123652585 961.0322 0 0 0 3 5
```

There should be 1 folder with name **flight_images** 
All the images to be geotaged should be on this folder
```
flight_images
```

Open the terminal on this folder and run:
```
py geotagger.py
```

The output will be on the *flight_images_geotag* folder that will be created
<br/>
<br/>
<br/>

# Rename

Create a folder to put the images to be renamed with the name **organizer**
```
organizer
```

Open the terminal on this folder and run:
```
py rename.py
```