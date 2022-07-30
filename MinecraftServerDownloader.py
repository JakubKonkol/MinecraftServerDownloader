import os
import requests
import shutil

print("MinecraftServerDownloader")
print("Author: JakubKonkol")

srvtype = input("What type of server you want to create? example: vannila, bukkit, spigot, paper: \n")
version = input("What server version you want to use? example: 1.19, 1.8:\n")


def download(url: str, dest_folder: str):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    filename = "server.jar"
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
    else:
        raise RuntimeError("Download failed")
        pass


def main():
    dirname = "srv_" + srvtype + "_" + version
    print("creating directory " + dirname + "...")
    parent_dir = os.getcwd()
    path = os.path.join(parent_dir, dirname)
    source = parent_dir + '\\templates'
    shutil.copytree(source, path)
    print("Directory created at " + path)
    url = "https://serverjars.com/api/fetchJar/" + srvtype + "/" + version
    try:
        download(url, path)
    except RuntimeError:
        print("There is a error when trying to download file...")
        print("Maybe there is no such server version?")
        shutil.rmtree(path)
        input()
    else:
        print("DONE!")
        pass


if srvtype == "bukkit" or srvtype == "vanilla" or srvtype == "spigot" or srvtype == "paper":
    main()
else:
    print("Provide correct server type! re-run the script")
    pass
