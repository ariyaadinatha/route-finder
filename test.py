import os

# Cari file root
# path_parent = os.path.dirname(os.getcwd())
#os.chdir(path_parent)
namaFile ="ea"
print("path : ", end="")
uploadDir=(str(os.getcwd())+"/upload/")
eek = os.path.join(uploadDir, "(profile.filename)")
print(eek)