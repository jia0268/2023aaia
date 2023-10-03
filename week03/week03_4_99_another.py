# 試試看,用f配上大括號
for i in range(1,10):
  for j in range(1,10):
    print(f'{j}x{i}={i*j:2}',end=' ') #{i*j:2}我要他佔兩格
  print()