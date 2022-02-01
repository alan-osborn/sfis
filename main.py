from lib import *

version = "v0.1.0"
indexhtml = File.read("./default/index.html")
welcomehtml = File.read("./default/welcome.html")
overviewhtml = File.read("./default/overview.html")
static_path = os.getcwd()
config = Data.config_data

def overview():
    size = str(round(round(Path.getdirsize("./files/") / 1024, 3) / 1024, 3)) + " MB" #GB
    print(size)
    File.rewrite("overview.html", overviewhtml)
    File.replace("overview.html", "$title", config["title"])
    File.replace("overview.html", "$used_space", size)
    File.replace("overview.html", "$os_edition", System.os_edition)
    File.replace("overview.html", "$cpu_version", System.processor_numbers)
    File.replace("overview.html", "$local_time", System.local_time)
    File.replace("overview.html", "$python_version", System.python_version) 
    File.replace("overview.html", "$sfis_version", version) 
    File.replace("overview.html", "$copyright", "<li>&copy " + System.year + " " + config["owner"] + "</li>")
    if config["about"] == True:
        File.replace("overview.html", "$about", "<li>Based on <a href = 'https://github.com/david-ajax/sfis'>SFIS Project</a></li>")
def create(one):
    os.chdir(one)
    print(os.getcwd())
    filelist = Path.ls(".", "file")
    folderlist = Path.ls(".", "folder")
    alllist = ""
    for one in folderlist:
        alllist = alllist + "<br><a href='" + one + "'>" + one + "/</a>"
    for one in filelist:
        if one == "index.html" or one == "":
            continue
        else:
            alllist = alllist + "<br><a href='" + one + "'>" + one + "</a>"
    File.rewrite("index.html", indexhtml)
    File.replace("index.html", "$title", config["title"])
    File.replace("index.html", "$path", Path.contrast(os.getcwd(), static_path))
    File.replace("index.html", "$list", alllist)
    if os.path.exists("README.md") and os.path.isfile("README.md") and config["preview_readme_md"] == True:
        readmemd = File.md2html("README.md")
        File.replace("index.html", "$readme", readmemd)
    else:
        File.replace("index.html", "$readme", "Nothing Here")
    File.replace("index.html", "$ad", config["ad_code"])
    File.replace("index.html", "$copyright", "<li>&copy " + System.year + " " + config["owner"] + "</li>")
    if config["about"] == True:
        File.replace("index.html", "$about", "<li>Based on <a href = 'https://github.com/david-ajax/sfis'>SFIS Project</a></li>")
    os.chdir(static_path)
def welcome():
    File.rewrite("index.html", welcomehtml)
    File.replace("index.html", "$title", config["title"])
    File.replace("index.html", "$owner", config["owner"])
    File.replace("index.html", "$email", config["email"])
    File.replace("index.html", "$ad", config["ad_code"])
    File.replace("index.html", "$copyright", "<li>&copy " + System.year + " " + config["owner"] + "</li>")
    if config["about"] == True:
        File.replace("index.html", "$about", "<li>Based on <a href = 'https://github.com/david-ajax/sfis'>SFIS Project</a></li>")

if __name__ == "__main__":
    welcome()
    p = ["files"]
    for one in Path.tree("files", "folder"):
        p.append(one)
    for one in p:
        create(one)
    overview()
