alien={'x':0,'y':25,'speed':'medium'}
alien['speed']= 'fast'
print("original x: " +str(alien['x']))
if alien['speed'] =='slow':
	x_increment =1
elif alien['speed'] == 'medium':
	x_increment =2
else:
	x_increment =3
alien['x']=alien['x']+x_increment
print("new_x: "+str(alien['x']))
