earth_wt=float(input("enter your earth weight:"))
planet_num=int(input("enter the planet number:"))
if planet_num==1:
  dest_wt = earth_wt * 0.38
  print(dest_wt)
elif planet_num==2:
  dest_wt = earth_wt * 0.91
  print(dest_wt)
elif planet_num==3:
  dest_wt = earth_wt * 0.38
  print(dest_wt)
elif planet_num==4:
  dest_wt=earth_wt*2.53
  print(dest_wt)
elif planet_num==5:
  dest_wt=earth_wt*1.07
  print(dest_wt)
elif planet_num==6:
  dest_wt=earth_wt*0.89
  print(dest_wt)
elif planet_num==7:
  dest_wt=earth_wt*1.14
  print(dest_wt)
else:
  print("Invalid planet number")
