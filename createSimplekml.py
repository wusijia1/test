import simplekml
import shutil
import os
LongLatPath="E:\\locationImei\\resultanalysis\\outgpsdisgnss\\"
outPath="E:\\locationImei\\resultanalysis\\outgpsdisgnssKml\\"

if  os.path.exists(outPath):
   shutil.rmtree(outPath)
   os.mkdir(outPath)
else :
    os.mkdir(outPath)


LongLatFile=os.listdir(LongLatPath)
for file in LongLatFile:
    with open(LongLatPath+file, "r") as f:
        lines = f.readlines()
    LongLatList = []
    for line in lines:
        long = float(line.split(",")[-2])
        lat =  float(line.split(",")[-3])
        tup=(long,lat)
        LongLatList.append(tup)

    kml = simplekml.Kml()
    ls = kml.newlinestring(name='A LineString')
    ls.coords =LongLatList
    ls.extrude = 1
    ls.altitudemode = simplekml.AltitudeMode.relativetoground
    ls.style.linestyle.width = 2
    ls.style.linestyle.color = simplekml.Color.red
    print(LongLatPath+file)
    kml.save(outPath+file+".kml")
print("OK!  ^-^  ")