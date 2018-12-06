import git
import whatthepatch

# git hash-object -t tree /dev/null
EMPTY_TREE_SHA = "4b825dc642cb6eb9a060e54bf8d69288fbee4904"

repo = git.Repo(".")

commits = list(repo.iter_commits())
commits.reverse()


# first commit hack
patch = commits[0].diff(EMPTY_TREE_SHA, create_patch=True)[0].diff
for diff in whatthepatch.parse_patch(patch):
	for (i,d,t) in diff.changes:
		print (d,i,t)
		
print(commits[0].author.name,commits[0].message)


for i, c in enumerate(commits):

	if i==0: continue;

	patch = commits[i-1].diff(c, create_patch=True)[0].diff

	for diff in whatthepatch.parse_patch(patch):
		for (d,i,t) in diff.changes:
			if d==None or i==None:
				print(d,i,t)

	print(c.author.name,c.message)


