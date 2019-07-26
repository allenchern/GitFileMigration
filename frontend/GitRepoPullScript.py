#!/usr/bin/env python3

import os
import git
import shutil
import tempfile

# Define the localhost you want to save those Repos for future Confluence POST"
destination = '/Users/allen.chen/PythonScript/git-python/tmp/newfolder'
#destination = '/../../'

# Create temp dir

resource = tempfile.mkdtemp()

# Clone into temp dir

git.Repo.clone_from('git@github.com:railcore/railcore.github.io.git', resource, branch='master', depth=1)

#git.Repo.clone_from('git@github.com:/XXX.git', resource, branch='master', depth=1)

# Copy desired file from temporary dir

for src_dir, dirs, files in os.walk(resource):
    dst_dir = src_dir.replace(resource, destination, 1)
    #print (dst_dir);
    #if not os.path.exists(resource):
     #   os.makedirs(destination)
    for file in files:
        src_file = os.path.join(resource, file)
        #print (src_file);
        dst_file = os.path.join(destination, file)
        #print (dst_file);
        if os.path.exists(dst_file):
           # in case of the src and dst are the same file
           if os.path.samefile(src_file,dst_file):
              continue
           os.remove(dst_file)
        shutil.move(src_file,dst_dir)
    for fdir in dirs:
        src_dir = os.path.join(resource, fdir)
        #print (src_dir);
        dst_dir = os.path.join(destination, fdir)
        #print (dst_dir);
        if not os.path.exists(resource):
            os.makedirs(destination)
        shutil.move(src_dir,dst_dir)
