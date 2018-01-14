import os

class Chunkify:
    '''
    A class that performs operations regarding splitting data
    into chunks and processing them.
    '''
    def chunkify(self, text, size):
        '''
        Splits a string into N size chunks and places them in a directory.
        '''
        li = list(text)
        chunks = []
        for i in range(0, len(li), size):
            chunk = li[i:i+size]
            chunks.append(''.join([i for i in chunk]))
        return chunks
    
    def split(self, filepath, size):
        '''
        Splits a file into N size chunks.
        '''
        if '/' in filepath:
            name = filepath.split('/')[-1]
        elif '\\' in filepath:
            name = filepath.split('\\')[-1]
        else:
            name = filepath
        if '.' in name:
            name = name.replace('.', '+_+')
        fd = open(filepath, 'rb')
        data = fd.read()
        fd.close()
        chunks = self.chunkify(data, size)
        os.mkdir(name)
        for i in range(len(chunks)):
            fd = open(name+'/'+str(i), 'w')
            fd.write(chunks[i])
            fd.close()
    def join(self, directory):
        '''
        Joins files in the directory that were splitted by the split function.
        '''
        file_ = ''
        name, ext = directory.split('+_+')
        for i in os.listdir(directory):
            fd = open(directory+'/'+i, 'rb')
            data = fd.read()
            fd.close()
            file_ += data
        fd = open(name+'.'+ext, 'wb')
        fd.write(file_)
        fd.close()
          
