#coding:utf-8

def saveFile(file,filename):
    try:
        with open(filename, "wb") as f:
            for chunk in file.chunks(chunk_size=1024):
                f.write(chunk)
    except Exception as e:
        result = str(e)
    else:
        result = "success"
    return result
