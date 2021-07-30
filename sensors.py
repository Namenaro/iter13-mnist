import numpy as np

def make_measurement(pic, centerx, centery, radius):
    return np.mean(get_sensory_array(pic, centerx, centery, radius))

def get_sensory_array(pic, centerx, centery, radius):
    XB, YB = get_coords_less_or_eq_raduis(centerx, centery, radius)
    return get_sensory_array_by_coords(pic, XB, YB)

def get_sensory_array_by_coords(pic, XB, YB):
    arr = []
    for i in range(len(XB)):
        x=XB[i]
        y=YB[i]
        xlen = pic.shape[1]
        ylen = pic.shape[0]
        if x >= 0 and y >= 0 and x < xlen and y < ylen:
            arr.append(pic[y,x])
        else:
            arr.append(0)
    return np.array(arr)


def get_coords_less_or_eq_raduis(centerx, centery, radius):
    XB = []
    YB = []
    for r in range(0, radius+1):
        X, Y = get_coords_for_radius(centerx, centery, r)
        XB = XB + X
        YB = YB + Y
    return XB, YB

def get_coords_for_radius(centerx, centery, radius):
    #|x|+|y|=radius ->  |y|=radius-|x|
    # x>0  -> y1 = radius-|x|
    X=[]
    Y=[]

    for modx in range(0,radius+1):
        # x>0
        mody = radius - modx

        X.append(modx+centerx)
        Y.append(mody+centery)

        X.append(modx + centerx)
        Y.append(-mody + centery)
        # x<0
        X.append(-modx + centerx)
        Y.append(mody + centery)

        X.append(-modx + centerx)
        Y.append(-mody + centery)
    return X,Y

def get_size_of_field_by_its_radius(radius):
    X, _ = get_coords_less_or_eq_raduis(centerx=0, centery=0, radius=radius)
    return len(X)





