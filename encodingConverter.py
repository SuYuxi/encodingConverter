import os
import glob

filesPath = '/usr/prj/' #example '/usr/prj/'
saveAsPath = '/usr/prj_new/' #example '/usr/prj_new/'
fileType = ['.h', '.hpp', '.cpp'] #the filename extension to be converted
originEncoding = 'gbk' #current file encoding 'gbk' for Chineses and 'sjis' for Japanesed
targetEncoding = 'utf-8-sig' #convert into utf-8 with signature

for ft in fileType:
    fileDirs = glob.glob(filesPath + '**/*' + ft, recursive = True)
    for path in fileDirs:
        targetDir = os.path.abspath(saveAsPath + os.path.relpath(path, start=filesPath))
        if not os.path.exists(os.path.dirname(targetDir)):
            os.makedirs(os.path.dirname(targetDir))
            print('Create {0}'.format(os.path.dirname(targetDir)))
        try:
            with open(path, encoding=originEncoding, mode='r') as f:
                data = f.read()
            with open(targetDir, encoding=targetEncoding, mode='w') as d:
                d.write(data)
            print('Convert {0} from {1} into {2}'.format(os.path.basename(path), originEncoding, targetEncoding))
        except UnicodeDecodeError:
            print(path + ' file encoding seem not to be \'' + originEncoding + '\'')
print('Save all files into {0}'.format(saveAsPath))