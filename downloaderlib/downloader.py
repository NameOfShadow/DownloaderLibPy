from mureq import get as k
from os import mkdir as i
class downloader:
 o="Download"
 def picture(l,o=o):
  r=k(l)
  n=l.split("/")[-1]
  try:i(o),open(f"{o}/picture-{n}","wb").write(r.content)
  except FileExistsError:open(f"{o}/picture-{n}","wb").write(r.content)
 def code(l,o=o):
  r=k(l)
  n=l.split("/")[-1]
  try:i(o),open(f"{o}/code-{n}", "wb").write(r.content)
  except FileExistsError:open(f"{o}/code-{n}","wb").write(r.content)
 def audio(l,o=o):
  r=k(l)
  n=l.split("/")[-1]
  try:i(o),open(f"{o}/audio-{n}","wb").write(r.content)
  except FileExistsError:open(f"{o}/audio-{n}","wb").write(r.content)