path_to_zip_file = "datasets.zip"
directory_to_extract_to = "./11/"
import zipfile
zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
zip_ref.extractall(directory_to_extract_to)
zip_ref.close()