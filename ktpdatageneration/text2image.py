from PIL import Image, ImageFont, ImageDraw 
from glob import glob
import cv2
# define the paths to your input images and to where you want to put the output images    
out_dir = 'ktp_fake_tif'
out_dir_gt = 'ktp_fake_gt'
file_postfix = '_laku'

# read an input image

# open font
NIK_font = ImageFont.truetype('data/fonts/ocraextended.ttf', 45)
rest_font = ImageFont.truetype('data/fonts/arial.ttf', 25)

# nikList = open("data/NIKs.txt", "r")
# nameList = open("data/NAMEs.txt", "r")
# lahirList = open("data/LAHIRs.txt", "r")
# jenisKelList = open("data/KELAMs.txt", "r")
# golDarahList = open("data/GOLs.txt", "r")
# alamatList = open("data/ALAMs.txt", "r")
# rtList = open("data/RTs.txt", "r")
# kelDesList = open("data/KELDESs.txt", "r")
# kecamatanList = open("data/KECs.txt", "r")
# agamaList = open("data/AGAMs.txt", "r")
# kawinList = open("data/KAWINs.txt", "r")
# pekerjaanList = open("data/KERJAs.txt", "r")
# kewarganegaraanList = open("data/KEWARGAs.txt", "r")
berlakuList = open("data/LAKUs.txt", "r")


for fn in range(0, 50, 1):
    print('processing %s...' % fn)
    
    my_image = Image.open("ktp_template/ktp_template_laku.png")

    # drawable image
    image_editable = ImageDraw.Draw(my_image)

    # nik = nikList.readline()
    # name = nameList.readline()
    # lahir = lahirList.readline()
    # jenisKel = jenisKelList.readline()
    # golDarah = golDarahList.readline()
    # alamat = alamatList.readline()[0:38]
    # rt = rtList.readline()
    # kelDes = kelDesList.readline()
    # kecamatan = kecamatanList.readline()
    # agama = agamaList.readline()
    # kawin = kawinList.readline()
    # pekerjaan = pekerjaanList.readline()
    # kewarganegaraan = kewarganegaraanList.readline()
    berlaku = berlakuList.readline()

    # draw (horizontal, vertical)
    # image_editable.text((205,0), nik, (0, 0, 0), font=NIK_font)
    # image_editable.text((220,0), name, (0, 0, 0), font=rest_font)
    # image_editable.text((220,0), lahir, (0, 0, 0), font=rest_font)
    # image_editable.text((220,0), jenisKel, (0, 0, 0), font=rest_font)
    # image_editable.text((630,0), golDarah, (0, 0, 0), font=rest_font)
    # image_editable.text((220,2), alamat, (0, 0, 0), font=rest_font)
    # image_editable.text((220,0), rt, (0, 0, 0), font=rest_font)
    # image_editable.text((240,2.5), kelDes, (0, 0, 0), font=rest_font)
    # image_editable.text((240,1.75), kecamatan, (35, 36, 46), font=rest_font)
    # image_editable.text((240,2), agama, (35, 36, 50), font=rest_font)
    # image_editable.text((240,2.5), kawin, (39, 36, 46), font=rest_font)
    # image_editable.text((240,0.5), pekerjaan, (32, 40, 46), font=rest_font)
    # image_editable.text((240,2), kewarganegaraan, (41, 32, 46), font=rest_font)
    image_editable.text((240,2), berlaku, (37, 32, 40), font=rest_font)

    # write the result to disk in the previously created output directory
    my_image.save(out_dir+"/fake_ktp_"+str(fn)+file_postfix+".tif")

    # blur image
    im_blur = cv2.imread(out_dir+"/fake_ktp_"+str(fn)+file_postfix+".tif")
    im_blur = cv2.blur(im_blur,(3,4))
    cv2.imwrite(out_dir+"/fake_ktp_"+str(fn)+file_postfix+".tif", im_blur)

    # write file.
    f = open(out_dir_gt+"/fake_ktp_"+str(fn)+file_postfix+".gt.txt", "w")
    # f.write("NIK : "+nik.replace("\n", ""))
    # f.write("Nama : "+name.replace("\n", ""))
    # f.write("Tempat/Tgl Lahir : "+lahir.replace("\n", ""))
    # f.write("Jenis Kelamin : "+jenisKel.replace("\n", "")+" Gol Darah : "+golDarah.replace("\n", ""))
    # f.write("Alamat : "+alamat.replace("\n", "")+"\n")
    # f.write("RT/RW : "+rt.replace("\n", ""))
    # f.write("Kel/Desa : "+kelDes.replace("\n", ""))
    # f.write("Kecamatan : "+kecamatan.replace("\n", ""))
    # f.write("Agama : "+agama.replace("\n", ""))
    # f.write("Status Perkawinan : "+kawin.replace("\n", ""))
    # f.write("Pekerjaan : "+pekerjaan.replace("\n", ""))
    # f.write("Kewarganegaraan : "+kewarganegaraan.replace("\n", ""))
    f.write("Berlaku Hingga : "+berlaku.replace("\n", ""))
    
    f.close()