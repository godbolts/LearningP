from pixboard import *

pildi_maatriks = [[252, 252, 252, 252, 220, 172, 175, 132, 127, 139, 151, 212, 252, 252, 252, 252],
  [252, 252, 251, 163, 215, 195, 124,  99,  95, 119, 139, 155, 135, 243, 252, 252],
  [252, 252, 179, 252, 220,  63,  56, 103, 115,  67,  68,  79, 124, 124, 251, 252],
  [252, 163, 251, 252, 147,  39,  98, 252, 252, 119,  59,  67,  60,  99, 131, 252],
  [212, 212, 252, 252, 128,  36,  84, 252, 252, 104,  51,  63,  59,  55, 100, 204],
  [179, 251, 251, 252, 163,  19,  47,  79,  99,  44,  55,  56,  55,  52,  59, 131],
  [175, 252, 243, 251, 236,  79,  19,  35,  31,  51,  55,  51,  51,  51,  47,  67],
  [148, 252, 244, 236, 244, 235, 143,  67,  50,  28,  28,  43,  44,  43,  43,  52],
  [151, 252, 243, 243, 231, 236, 244, 231, 228, 200,  79,  27,  43,  43,  39,  52],
  [175, 252, 244, 239, 235, 228, 220, 228, 227, 223, 220,  67,  23,  36,  35,  60],
  [179, 243, 252, 239, 235, 228, 235, 171, 103, 196, 215, 152,  19,  35,  35, 116],
  [215, 187, 252, 239, 232, 236, 220,  55,   3, 104, 216, 199,  19,  35,  34, 195],
  [252, 148, 239, 252, 235, 228, 232, 115,  27, 164, 215, 184,  19,  28,  98, 252],
  [252, 244, 167, 243, 251, 235, 227, 227, 207, 212, 231, 115,  12,  59, 244, 252],
  [252, 252, 244, 147, 199, 227, 244, 236, 231, 223, 135,  23,  91, 251, 252, 252],
  [252, 252, 252, 252, 212, 155, 147, 132, 132, 151, 148, 187, 252, 252, 252, 252]]

kõrgus = len(pildi_maatriks) // 2
laius = len(pildi_maatriks[0]) // 2
pilt = [[0] * laius for _ in range(kõrgus)]
ümber_pööratud = [[0] * laius for _ in range(kõrgus)]

for i in range(kõrgus):
  for j in range(laius):
    ümber_pööratud[i][kõrgus - 1 - j] = pildi_maatriks[i][j]

sulatatud_pilt = [[0] * laius for _ in range(kõrgus)]

for i in range(kõrgus):
  for j in range(laius):
    sulatatud_pilt[i][j] = (ümber_pööratud[i][j] + pilt[i][j]) // 2

vastus = sulatatud_pilt

show(vastus)