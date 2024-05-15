import os
import shutil
from git import Repo
import datetime as dt
tgl = dt.datetime.now().strftime("%y%m%d_%H%M%S")
os.chdir('../premade')
#import shutil
#shutil.make_archive('HEINZO', 'zip', '/content/images')
full_local_path = "/content/premade"

initt = "/content/init.png"
maskk = "/content/mask.png"
initoutputss = "/content/premade/initmask/" + str(tgl) + "I.png"
maskoutputss = "/content/premade/initmask/" + str(tgl) + "M.png"
shutil.copy(initt, initoutputss)
shutil.copy(maskk, maskoutputss)

repo = Repo(full_local_path)
repo.git.add("-A")
repo.index.commit("initmask")

#repo = Repo(full_local_path)
origin = repo.remote(name="origin")
origin.push()


os.chdir('..')
