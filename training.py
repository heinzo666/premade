import os
from git import Repo
import datetime as dt
tgl = dt.datetime.now().strftime("%y%m%d_%H%M%S")
os.chdir('../premade')
#import shutil
#shutil.make_archive('HEINZO', 'zip', '/content/images')
full_local_path = "/content/premade"

repo = Repo(full_local_path)
repo.git.add("-A")
repo.index.commit("outputs")

#repo = Repo(full_local_path)
origin = repo.remote(name="origin")
origin.push()


os.chdir('..')
