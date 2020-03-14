#インポおと
import random

#グロ変
nepal =["ビザOK","入国OK","ビザNG","入国拒否"]
mission =["ビザ取得ミッション","フライトチェンジミッション","パスポートミッション","入国ミッション"]


def plan():
  print("Namaste number dinuss")
  print("コロナウイルスによって人生ハードモードになりましたひひひ")
  print()

def travel():
  for bbb in mission:
    print(bbb)
  print()



def flight_cancel():
  input('祈りながらプレスエニーキー')
  result = random.randint(0,3)
  if result == 0 or result == 1:
    print(nepal[0])
  else:
    print(f'あなたは{nepal[2]}のため、{nepal[3]}になりましたひひひひ')
  

plan()
travel()
flight_cancel()
