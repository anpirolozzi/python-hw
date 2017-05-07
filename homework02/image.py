import png

def create(iw,ih,c):
    image = []
    for _ in range(ih):
        row = []
        for _ in range(iw):
            row.append(c)
        image.append(row)
    return image

def save(filename, img):
    png_img = []
    for row in img:
        png_row = []
        for c in row:
            png_row += c
        png_img.append(png_row)
    with open(filename,'wb') as f:
        png.Writer(len(img[0]),len(img)).write(f,png_img)

def load(filename):
    with open(filename,'rb') as f:
        iw, ih, png_img, _ = png.Reader(file=f).asRGB8()
        png_img = [ [ v for v in png_row ] for png_row in png_img ]
    img = []
    for png_row in png_img:
        row = []
        for i in range(0,len(png_row),3):
            row.append( (png_row[i+0],png_row[i+1],png_row[i+2]) )
        img.append( row )
    return img

