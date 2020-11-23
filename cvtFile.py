import sys
import  os
import tensorflow as ts;

folder="empty_veri1"
# folder="img/empty_200909/10"
txtPath="txt/"
imgPath=folder+"/"
# imgPath="insuff/"
count=16492
list=os.listdir(txtPath)
imglist=os.listdir(imgPath)

context=""
w = open(folder+".txt", 'w')
def fileConvert():
    avg_width=0
    avg_height=0
    count=0
    for file in list:
        print(file)
        filename=file.split('.')
        print(filename[0]+'.jpeg')
        f = open(txtPath+file)

        st=f.readline()
        if(int(st)==0):
            f.close()
            os.remove(txtPath+file)
            continue

        w.write(imgPath+filename[0]+'.jpeg ')
        # w.write(str(int(st)))
        w.write(str(int(st)))

        for i in range(int(st)):
            br = f.readline()
            ls = br.split()
            w.write(" ")

            w.write(str(int(ls[0]))+" ")
            w.write(str(int(ls[1]))+" ")
            w.write(str(int(ls[2])-int(ls[0]))+" ")
            w.write(str(int(ls[3])-int(ls[1]))+" ")
            count+=1
            avg_width+=int(ls[2])-int(ls[0])
            avg_height+=int(ls[3])-int(ls[1])
        w.write("\n")


    f.close()
    w.close()
    print(avg_width/count,avg_height/count)
removelist=[]

def make_text():
    for imgfile in imglist:
        filename=imgfile.split('.')[0]
        f = open(txtPath+filename+".txt",'w')
        f.write("1\n")
        # f.write("41 82 199 183")
        f.write("160 137 365 256")
        # f.write("180 150 450 300")
        f.close()



def fileConvert2():
    for file in list:
        txt=open(file,"w")
        print(file)
        filename=file.split('.')
        print(filename[0]+'.jpeg')
        f = open(txtPath+file)

        st=f.readline()
        if(int(st)==0):
            f.close()
            os.remove(txtPath+file)
            continue


        # w.write(str(int(st)))
        txt.write(str(int(st)))
        txt.write("\n")



        for i in range(int(st)):
            br = f.readline()
            ls = br.split()

            txt.write(str(int(ls[0])-100)+" ")
            txt.write(str(int(ls[1])-100)+" ")
            txt.write(str(int(ls[2])-100)+" ")
            txt.write(str(int(ls[3])-100)+" ")

            # txt.write(str(int(ls[0]))+" ")
            # txt.write(str(int(ls[1]))+" ")
            # txt.write(str(int(ls[2]))+" ")
            # txt.write(str(int(ls[3]))+" ")
    w.close()
    txt.close()

def file_remove():
    imglist=os.listdir(imgPath)
    txtlist=os.listdir(txtPath)

    # for txtfile in txtlist:
    #     filename=txtfile.split('.')[0]
    #     try:
    #         imgf=open("filled/"+filename+".jpeg")
    #     except Exception as e:
    #         print(e)
    #         os.remove(txtPath+txtfile)



    for imgfile in imglist:
        filename=imgfile.split('.')[0]

        try:
            # print("txt/"+filename+".txt")
            txtf=open("txt/"+filename+".txt")
            if int(txtf.readline())==0:
                # print(imgPath+imgfile +"deleted")
                os.remove(imgPath+imgfile)
            txtf.close()


        except Exception as e:
            # print(imgPath + imgfile + " deleted")
            print(e)
            os.remove(imgPath+imgfile)

            # txtf.close()


    # txtf.close()
    w.close()
def removeblank():
    imglist = os.listdir(imgPath)
    txtlist = os.listdir(txtPath)

    for imgfile in imglist:
        filename = imgfile.split(' ')[0]
        try:
            extends=imgfile.split(' ')[1]
            os.rename(imgPath+imgfile,imgPath+filename+extends)
            print(extends)
        except Exception as e:
            continue

    for txtfile in txtlist:
        filename = txtfile.split(' ')[0]
        try:
                extends = txtfile.split(' ')[1]
                os.rename(txtPath + txtfile, txtPath + filename + extends)
                print(extends)
        except Exception as e:
                continue

        # if imgfile.split(' ')[1]:
        #     os.replace(imgfile,filename[0]+filename[1])



    # txtf.close()



# removeblank()
fileConvert()
file_remove()
# make_text()



#
# import cv2
# count=0
# list=os.listdir("img/insuff")
#
# count =1000
# for file in list :
#     img=cv2.imread("img/insuff/"+file)
#     filename=file.split('.')
#     cv2.imwrite("img/insuff/insuff_"+str(count)+".jpeg",img)
#     os.remove("img/insuff/"+file)
#     count+=1
#     # os.remove("Image/"+file)


