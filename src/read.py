import os;

#Creating a file at ../files/ and writing into it
def createfile(file_name, inp):
    try:
        if not (os.path.isdir('..\\files')): #directory files is created in parent if it does not exist
            os.mkdir('..\\files')
        inp_file = open('..\\files\\' + file_name,'w')#file opened in write mode where file is created if it does not exist
        if(inp_file):#checking if file is created sucessfully
            print 'created file at ' + '..\\files\\' + file_name
        else:
            print 'error creating file'
        inp_file.write(inp)#writing text to the file
    except Exception, e :#printing out exceptions if any
        print e
    finally:#file is closed at the end
        inp_file.close()

#reading the file and printing out its contents
def readfile(file_name):
    try:
        out_file = open('..\\files\\' + file_name,'r')#file opened in read mode
        if out_file:#checking if file read sucessfully
            print 'opened file ' + '..\\files\\' + file_name
        else:
            print 'error opening file'

        for line in out_file.readlines():#reading out all the lines in the file and printing it out on the screen
            print line,#printing out lines without adding anyy additional new line characters
    except Exception, e :#printing out exceptions if any
        print e
    finally:#file is closed at the end
        out_file.close()

fileName = str(raw_input('enter file name : '))#file name is taken as an input from the user
text_input = str(raw_input("enter text : "))#text which is to be written into the file is taken as input from the user
createfile(fileName, text_input)
readfile(fileName)