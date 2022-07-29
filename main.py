import os
import requests
import shutil

print("MinecraftServerDownloader")
print("Author: JakubKonkol")

srvtype = input("What type of server you want to create? example: vannila, bukkit, spigot, paper: \n")
version = input("What server version you want to use? example: 1.19, 1.8:\n")

def download(url: str, dest_folder: str):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)  # create folder if it does not exist

    filename = "server.jar"  # be careful with file names
    file_path = os.path.join(dest_folder, filename)
    r = requests.get(url, stream=True)
    if r.ok:
        print("saving to", os.path.abspath(file_path))
        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 8):
                if chunk:
                    f.write(chunk)
                    f.flush()
                    os.fsync(f.fileno())
    else:  # HTTP status code 4XX/5XX
        print("Download failed: status code {}\n{}".format(r.status_code, r.text))

def main():
    DIRNAME="srv_"+srvtype+"_"+version;
    print("creating directory "+DIRNAME+"...")
    parent_dir = os.getcwd()
    templates = parent_dir
    path = os.path.join(parent_dir, DIRNAME)
    source = parent_dir + '\\templates'
    destination = path
    shutil.copytree(source, destination)
    print("Directory created at "+path)
    url = "https://serverjars.com/api/fetchJar/"+srvtype+"/"+version
    download(url, path)
    print("creating files to start the server....")

    pass


if(srvtype == "bukkit" or srvtype == "vanilla" or srvtype == "spigot" or srvtype == "paper"):
    main()
else:
    print("Provide correct server type! re-run the script")
    pass

