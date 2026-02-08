from PIL import Image
filename = "test.jpg" #HERE PUT IN A NAME OF THE FILE
with Image.open(filename) as img:
    img.load()
type(img) 
isinstance(img, Image.Image)

palette = [(0, 32, 46, 255),       #HERE PUT YOUR PALETTE IN FORM OF RGBA, LAST PATAMETER IS ALWAYS 255
           (32, 1, 93, 255), 
           (44, 72, 117, 255), 
           (138, 80, 143, 255), 
           (188, 80, 144, 255), 
           (255, 99, 97, 255), 
           (255, 133, 49, 255), 
           (255, 166, 0, 255)]

resized_img = img.reduce(4) #ITERATIONS OF REDUCTION, BIGGER NUMBER = SMALER IMAGE

img_step1 = resized_img.convert(mode = "P", matrix = None, dither = None, palette = "JPEG", colors = 8)
img_finale = img_step1.convert("L").convert("RGBA")

w, h = img_finale.size

for i in range(w):
    for j in range(h):
        print(int(((i * h + j) / (w * h)) * 100), "%")
        temp = int(img_finale.getpixel((i, j))[0] // 31.875)
        if temp == 8:
            img_finale.putpixel((i, j), (255, 255, 255, 255))
        else:
            img_finale.putpixel((i, j), palette[temp])


print(f"Done!")
img_finale.show()

img_finale.save("output.png") #SHOWS NOT A SAVED IMAGE, IT IS SAVED IN THE FOLDER WITH THE CODE
