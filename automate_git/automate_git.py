from datetime import datetime
import git


msg = '-m Update {}'.format(datetime.now())


repos = (
    r'D:\Projects\p1',
    r'D:\Projects\p2',
    r'D:\Projects\p3',
    r'D:\Projects\p1',
)

for path in repos:
    print('*'*50)
    print('Updating:', path)
    print('*'*50)
    g = git.cmd.Git(path)
    status = g.status()
    print(status)

    if 'nothing to commit, working tree clean' not in status:
        print(g.add('.'))
        print(g.commit(msg))

        repo = git.Repo(path)
        origin = repo.remote(name='origin')
        print(origin.push('master'))
