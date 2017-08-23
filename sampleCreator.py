import os
import subprocess

def createInfoDirs(posDir):
    bashCommand = "mkdir info"
    for x in range(0,len(os.listdir(posDir))):
        newinfodirbash = bashCommand + str(x)
        process = subprocess.Popen(newinfodirbash.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        print output


def moveVecFiles():
    mkdirVecDirectoryCommand = 'mkdir vecDirectory'
    mvBashCommmand = 'mv *positives* vecDirectory'
    process = subprocess.Popen(mkdirVecDirectoryCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    process.wait()
    process = subprocess.Popen(mvBashCommmand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    print output


def createSamples(posDir, nSamples):

    for n, pos in enumerate(os.listdir(posDir)):
        infoBashCommand = "opencv_createsamples -img {}/{} -bg bg.txt -info info{}/info.lst -pngoutput info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num {}".format(posDir, pos, str(n), nSamples)
        print infoBashCommand
        process = subprocess.Popen(infoBashCommand.split(), stdout=subprocess.PIPE)

        output, error = process.communicate()
        process.wait()
        print output

        vecFileBashCommand = 'opencv_createsamples -info info{}/info.lst -num 22 -w 20 -h 20 -vec positives{}.vec'.format(n,n)
        print vecFileBashCommand
        process = subprocess.Popen(vecFileBashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        print output
    moveVecFiles()



def thePrinter():
    print "Hey"

