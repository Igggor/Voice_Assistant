import os
path = r"C:\\"
def search(str):
    it = 0
    for root, dirs, files in os.walk(path):
        it += 1
        for file in files:
            if file.endswith(str):
                path_file = os.path.join(root, file)
                return (path_file)
                break
        if it > 100_000:
            return 'NF'
            break
chrome_path = search("chrome.exe")
steam_path = "C:\Program Files (x86)\Steam\Steam.exe"

