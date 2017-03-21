import os
import shutil
import sys
class organize:
    def organizer(self,newpath,foldername):
        print("newpath :",newpath)
        print("foldername: ",foldername)
        if not os.path.exists(foldername):
                print("folder does not exist")
                return
        if os.listdir(foldername)==[]:
                print("folder is empty")
                return
        files=os.listdir(foldername)
        print(files)
        for file in files:
            if(file.find(".")==-1):

                print("its folder")
                src=foldername+'/'+file
                print(src)
                location,extension=os.path.split(src)
                des=newpath+'/'+extension
                shutil.move(src,des)
            else:
                 extension=file.split(".")[-1]
                 source=foldername+'/'+file
                 destination=newpath+'/'+extension
                 if not os.path.exists(destination):
                    os.makedirs(destination)
                    print("created new folder : "+destination)
                 if not os.path.exists(destination+'/'+file):
                    #print("copying files from ",source," to " ,destination)
                    shutil.move(source,destination)

                 else:
                     print("cannot create "+file+"already exists")

                 print("copied file =  ",source, " to ",destination)


    def clearing_stuff(self,newpath,foldername):
        print("removing the empty directory")
        os.rmdir(foldername)
        print("renaming the destination to source")
        os.rename(newpath,foldername)


def main():
    src=input("enter directory to get classified as file extensions : \n")
    org = organize.organizer("a", "c:/tmp1",src)
    clearing=organize.clearing_stuff("a","c:/tmp1",src)

    #org = organize.organizer("a","c:/tushardata_linuxtp/t","c:/tushardata_linuxtp/pyt")
    #clearing=organize.clearing_stuff("a","c:/tushardata_linuxtp/t","c:/tushardata_linuxtp/pyt")
main()
