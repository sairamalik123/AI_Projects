x = object()
y = object()

x_list = [x,x,x,x,x,x,x,x,x,x]
y_list = [y,y,y,y,y,y,y,y,y,y]

concat_list = x_list + y_list

print("X List contains {} objects" .format(len(x_list)))
print("Y List contains {} objects" .format(len(y_list)))
print("Concat List contains {} objects" .format(len(concat_list)))