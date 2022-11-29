import math
from exif import Image
import os

with open('geotagfile.txt') as geotag_file:
    lines = geotag_file.readlines()

folder_path = 'flight_images'
output_folder = 'flight_images_geotaged'
files_list = os.listdir(folder_path)


for i in range(len(files_list)) :

    # reading each line of the geotag file
    image_geotag = lines[i].split()
    image_lat_decimal = float(image_geotag[0])
    image_long_decimal = float(image_geotag[1])
    image_alt = float(image_geotag[2])

    # transform decimals into minutes
    lat_to_transform = image_lat_decimal
    long_to_transform = image_long_decimal
    lat_NorS = 'N'
    long_EorW = 'E'

    if (image_lat_decimal < 0): 
        lat_to_transform = lat_to_transform * -1
        lat_NorS = 'S'

    if (image_long_decimal < 0): 
        long_to_transform = long_to_transform * -1
        long_EorW = 'W'

    lat_hours = math.floor(lat_to_transform)
    lat_minutes_float = (lat_to_transform - lat_hours) * 60
    lat_minutes = math.floor(lat_minutes_float)
    lat_seconds = (lat_minutes_float - lat_minutes) * 60

    long_hours = math.floor(long_to_transform)
    long_minutes_float = (long_to_transform - long_hours) * 60
    long_minutes = math.floor(long_minutes_float)
    long_seconds = (long_minutes_float - long_minutes) * 60

    # variables to write on the image
    gps_altitude = image_alt
    gps_altitude_ref = 0
    gps_latitude = (lat_hours, lat_minutes, lat_seconds)
    gps_latitude_ref = lat_NorS
    gps_longitude = (long_hours, long_minutes, long_seconds)
    gps_longitude_ref = long_EorW



    # writing on the image 
    img_filename = files_list[i]
    img_path = f'{folder_path}/{img_filename}'

    with open(img_path, 'rb') as img_file:
        img = Image(img_file)

    # Add new attributes
    img.gps_altitude = gps_altitude
    img.gps_altitude_ref = gps_altitude_ref
    img.gps_latitude = gps_latitude
    img.gps_latitude_ref = gps_latitude_ref
    img.gps_longitude = gps_longitude
    img.gps_longitude_ref = gps_longitude_ref

    # Check updated/added metadata
    print(f'gps_latitude: {img.get("gps_latitude")}')

    # Save the new file with metadata
    with open(f'{output_folder}/geotaged_{img_filename}', 'wb') as new_image_file:
        new_image_file.write(img.get_file())
