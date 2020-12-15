from PIL import Image
img=Image.open('./class/image/samp.jpg')
img.show()

img.save("./class/image/sample_bmp.bmp")
img.save("./class/image/sample_png.png")
img.save("./class/image/sample_gif.gif")


r,g,b = img.split()
con_img=Image.merge("RGB",(b,g,r))
con_img.save('./class/image/rgb_to_bgr.jpg')
con_img.show()

bw=img.convert('1')
bw.show()
bw.save('./class/image/sample_bw.jpg')

grey=img.convert("L")
grey.show()
grey.save('./class/image/sample_grey.jpg')

img.transpose(Image.ROTATE_90).show()
img.transpose(Image.ROTATE_90).save('./class/image/rotate_90.jpg')