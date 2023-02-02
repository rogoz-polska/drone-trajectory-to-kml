import json
# import simplekml
import utm
import random
utm_x,utm_y,zone,letter = utm.from_latlon(52.402364, 16.948808)

utm_z=0
x =[]
y=[]
z=[]
x_wgs84 =[]
y_wgs84=[]
z_wgs84=[]

x1_wgs84 =[]
y1_wgs84=[]
z1_wgs84=[]

x2_wgs84 =[]
y2_wgs84=[]
z2_wgs84=[]
wgs84 = []

# f = open('drones/Drone 4/trajectory.json')
# data = json.load(f)

# for i in data['points']:
#     x.append((i[1][0]+utm_x))
#     y.append(i[1][1]+utm_y)
#     z.append(i[1][2])

# f.close()

# for (a,b,c) in zip(x,y,z):
#   a,b = utm.to_latlon(a, b, zone, northern=True)
#   c=c+utm_z
#   z_wgs84.append(c)
#   x_wgs84.append(a)
#   y_wgs84.append(b)
for h in range(20):
  f = open(f'drones/drone_{h+1}/trajectory.json')
  data = json.load(f)
  z2_wgs84 = []
  x2_wgs84 = []
  y2_wgs84 = []
  x = []
  y = []
  z = []
  for i in data['points']:
      x.append((i[1][0]+utm_x))
      y.append(i[1][1]+utm_y)
      z.append(i[1][2])

  f.close()

  for (a,b,c) in zip(x,y,z):
    a,b = utm.to_latlon(a, b, zone, northern=True)
    c=c+utm_z
    z2_wgs84.append(c)
    x2_wgs84.append(a)
    y2_wgs84.append(b)
  wgs84.append([x2_wgs84,y2_wgs84,z2_wgs84])

# print(wgs84)
colors = ["ffff0000","ff00ff00","ff0000ff","ff0ab000","ff0000bb"]
a = f"""<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<kml xmlns=\"http://www.opengis.net/kml/2.2\" xmlns:gx=\"http://www.google.com/kml/ext/2.2\" xmlns:kml=\"http://www.opengis.net/kml/2.2\" xmlns:atom=\"http://www.w3.org/2005/Atom\">
<Document>    
	<name> Line Animation Sample</name>  
	<open>1</open>"""
for t in range(len(wgs84)):
  r = random.randrange(0, 2**8)
  r1 = str(hex(r))
  r1 = r1.replace('0x','')
  if r < 16:
    r1 = "0" + r1
  # print(type(r1))
  g = random.randrange(0, 2**8)
  g1 = str(hex(g)) 
  g1 = g1.replace('0x','')
  if g < 16:
    g1 = "0" + g1
  # print(type(g1))
  b = random.randrange(0, 2**8)
  b1 = str(hex(b))
  b1 = b1.replace('0x','')
  if b < 16:
    b1 = "0" + b1
  # print(type(b1))
  o = random.randrange(0, 2**8)
  o = str(hex(o))
  o = o.replace('0x','')
  color = "ff" + b1 + g1 + r1
  print(color)  
  a +=f"""<Style id=\"line-style{t}\">
      <LineStyle>
        <color>{color}</color>  	<!-- this is the color of your path -->   
        <width>1</width>		<!-- this is the width of your path -->
      </LineStyle>
    </Style>	"""
a +=f"""	<!-- this is the camera view  -->	
	
		<LookAt>
			<longitude>{wgs84[0][1][0] - 0.00066847352015}</longitude>
			<latitude>{wgs84[0][0][0] - 0.00066847352015}</latitude>
			<altitude>0</altitude>
			<heading>-10.36466847352015</heading>
			<tilt>70.96541540083902</tilt>
			<range>200.432628192288</range>
			<gx:altitudeMode>relativeToSeaFloor</gx:altitudeMode>
		</LookAt>
	
<gx:Tour>
	<name>Double-click here to start tour</name>
	<gx:Playlist>

         <gx:Wait> <gx:duration>0.01</gx:duration></gx:Wait>"""

# if x_wgs84>x1_wgs84:
#   k = len(x_wgs84)
# else:
#   k = len(x1_wgs84)

# for c in range(k):
#   a += f"""
#   		<gx:AnimatedUpdate>
# 			<Update>"""
#   print(c)
#   print(len(x_wgs84))
#   print(len(x1_wgs84))
#   # if c < len(x_wgs84):
#   a += f'<Change><Placemark targetId="{c}"><visibility>1</visibility></Placemark></Change>'
#   # if c < len(x1_wgs84):
#     # print("h")
#   a += f'<Change><Placemark targetId="v{c}"><visibility>1</visibility></Placemark></Change>'
  
#   a += f"""</Update>
# 		</gx:AnimatedUpdate>		
		
# <gx:Wait><gx:duration>1</gx:duration></gx:Wait>"""



g = [len(wgs84[p][0]) for p in range(len(wgs84))]
print(g)
for c in range(max(g)):
  a += f"""
  		<gx:AnimatedUpdate>
			<Update>"""
  for r in range(len(wgs84)):
    if (c < len(wgs84[r][0])):
      a += f'<Change><Placemark targetId="{r}v{c}"><visibility>1</visibility></Placemark></Change>'
  a += f"""</Update>
		</gx:AnimatedUpdate>		
<gx:Wait><gx:duration>0.01</gx:duration></gx:Wait>"""

a += f"""	</gx:Playlist>
</gx:Tour>


	<Folder>
		<name>Path segments</name>
		
		<Style>
			<ListStyle>
				<listItemType>checkHideChildren</listItemType>
			</ListStyle>
		</Style>"""


# for i in range(len(x_wgs84)-1):
#   a += f"""<Placemark id=\"{i}\">
# 			<name>1</name><visibility>0</visibility>
# 			<styleUrl>#line-style</styleUrl>
# 			<LineString>
# 				<tessellate>1</tessellate>
#         <altitudeMode>relativeToGround</altitudeMode>
# 				<coordinates>
# 					{y_wgs84[i]},{x_wgs84[i]},{z_wgs84[i]} {y_wgs84[i+1]},{x_wgs84[i+1]},{z_wgs84[i+1]}
# 				</coordinates>
# 			</LineString>
# 	</Placemark>"""
# for j in range(len(x1_wgs84)-1):
#   a += f"""<Placemark id=\"v{j}\">
# 			<name>1</name><visibility>0</visibility>
# 			<styleUrl>#line-style1</styleUrl>
# 			<LineString>
# 				<tessellate>1</tessellate>
#         <altitudeMode>relativeToGround</altitudeMode>
# 				<coordinates>
# 					{y1_wgs84[j]},{x1_wgs84[j]},{z1_wgs84[j]} {y1_wgs84[j+1]},{x1_wgs84[j+1]},{z1_wgs84[j+1]}
# 				</coordinates>
# 			</LineString>
# 	</Placemark>"""
for u in range(len(wgs84)):
  for i in range(len(wgs84[u][0])-3):
    a += f"""<Placemark id=\"{u}v{i}\">
        <name>1</name><visibility>0</visibility>
        <styleUrl>#line-style{u}</styleUrl>
        <LineString>
          <tessellate>1</tessellate>
          <altitudeMode>relativeToGround</altitudeMode>
          <coordinates>
            {wgs84[u][1][i]},{wgs84[u][0][i]},{wgs84[u][2][i]} {wgs84[u][1][i+1]},{wgs84[u][0][i+1]},{wgs84[u][2][i+1]}
          </coordinates>
        </LineString>
    </Placemark>"""

a += f"""
	</Folder>
  </Document>
</kml>
"""

f = open("demofile3.kml", "w")
f.write(a)
f.close()
# print(a)

# kml = simplekml.Kml()
# ls = kml.newlinestring(name="Drone path")

# for i in range (len(x)):
#   ls.coords.addcoordinates([(y_wgs84[i],x_wgs84[i],z_wgs84[i])])
# ls.altitudemode = simplekml.AltitudeMode.relativetoground


# kml.save("trace_of_drone.kml")


