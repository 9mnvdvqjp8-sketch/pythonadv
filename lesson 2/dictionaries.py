puntoret={
    "Yll":5000,
  "Leon":4000,
    "Albion":7500,
    "Enes":1000,
}


print(puntoret["Yll"])
puntoret["Yll"]=12000
print(puntoret)
del puntoret["Enes"]
print(puntoret)

print(puntoret.keys())
print(puntoret.values())