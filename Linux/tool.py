import subprocess
import sys
import json
from urllib import request
from subprocess import check_call,CalledProcessError

from pkg_resources import parse_version

def versions(pkg_name):
    url = f'https://pypi.python.org/pypi/{pkg_name}/json'
    releases = json.loads(request.urlopen(url).read())['releases']
    return sorted(releases, key=parse_version, reverse=True) 


file=open("requirement.txt")
ans=[]
file_read=file.readlines()
for l in file_read:
    arr=l.split('==')
    s = versions(arr[0])
    if arr[1].rstrip('\n') in s:
        try:
            subprocess.check_output('pip install '+ l +' -v')
        except CalledProcessError as e:
            ans.append(l.rstrip('\n'))
    else:
        ans.append(l.rstrip('\n'))
file.close()
if ans:
    for i in ans:
        print(i)
else:
    print("succes")