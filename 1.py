path_to_zip_file = "datasets.zip" #you can write name of the zip file
directory_to_extract_to = "./11/" # put "" to if the zip file and extracted filein the same directory or else put the location 
import zipfile
zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
zip_ref.extractall(directory_to_extract_to)
zip_ref.close()
#save this file as .py format and execute
