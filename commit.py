import git

r = git.Repo()
origin = r.remote('origin')

r.git.add('--all')
r.index.commit("making new commit")
origin.pull()
origin.push()
