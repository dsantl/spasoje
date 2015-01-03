
def avg(lst):
    suma = sum(lst)
    return suma / float(len(lst))


def get_distance_height_pair(img_l, img_r):

    height = img_l.shape[0]
    width = img_l.shape[1]

    d_list_l = [[] for i in xrange(height)]
    d_list_r = [[] for i in xrange(height)]

    
    for i in xrange(height):
        for j in xrange(width):
            if img_l[i, j] == 255:
                d_list_l[i].append(j)
            if img_r[i, j] == 255:
                d_list_r[i].append(j)

    yl = []
    zl = []
    
    B = 100.0
    for i in xrange(height):
        if d_list_l[i] and d_list_r[i]:
            x_l = avg(d_list_l[i])
            x_r = avg(d_list_r[i])
            dx = x_l - x_r
            z = -B/dx
            yl.append(height-i-1)
            zl.append(z)
    
    return (zl, yl)
