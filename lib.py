from os import pathconf_names
import markdown, codecs, os, zipfile, yaml, platform, time, datetime
class File:
    def unzip(zipfilepath, unzipto): #TODO
        pass
    def md2html(path): 
        input_file = codecs.open(path, mode="r", encoding="utf-8")
        text = input_file.read()
        html = markdown.markdown(text)
        return html
    def replace(path, old_content, new_content):
        content = File.read(path)
        content = content.replace(old_content, new_content)
        File.rewrite(path, content)
    def read(path):
        with open(path, encoding='UTF-8') as f:
            read_all = f.read()
            f.close()
        return read_all
    def rewrite(path, data):
        with open(path, 'w', encoding='UTF-8') as f:
            f.write(data)
            f.close()
class Path:
    def getdirsize(path="."):
        size = 0
        for root, dirs, files in os.walk(path):
            size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
        return size #GB: size / 1024 / 1024 / 1024 / 1024
    def ls(path=".", mode="all"):
        all = os.listdir(path)
        filelist = []
        folderlist = []
        for one in all:
            if os.path.isfile(one):
                filelist.append(one)
            if os.path.isdir(one):
                folderlist.append(one)
        if mode == "all":
            return all
        elif mode == "file":
            return filelist
        elif mode == "folder":
            return folderlist
        else:
            return "unknown"
    def getparentfolder(path):
        of = os.getcwd()
        os.chdir(path)
        os.chdir("..")
        pf = os.getcwd()
        os.chdir(of)
        return pf
    def contrast(path1, path2):
        return os.path.relpath(path1, path2)
    def tree(path=".", mode="all"): #文件树生成(all)
        a = []
        b = []
        c = []
        for root, dirs, files in os.walk(path, topdown=False):
            for name in files:
                a.append(os.path.join(root, name))
                c.append(os.path.join(root, name))
            for name in dirs:
                a.append(os.path.join(root, name))
                b.append(os.path.join(root, name))
        if mode == "all":
            return a
        if mode == "folder":
            return b
        if mode == "file":
            return c
class System:
    os_edition = platform.platform()
    local_time = time.ctime()
    processor_numbers = platform.machine()
    python_version = platform.python_version()
    year = time.strftime("%Y", time.localtime()) 
class Data:
    config_data = yaml.load(File.read("config.yml"), Loader=yaml.FullLoader)