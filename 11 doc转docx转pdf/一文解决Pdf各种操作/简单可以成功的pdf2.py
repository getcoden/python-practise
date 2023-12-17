import fitz
import PIL

def covert2pic(zoom):
    doc = fitz.open(r"D:\1jieya\2.pdf")
    total = doc.page_count
    for pg in range(total):
        page = doc[pg]
        zoom = int(zoom)            #值越大，分辨率越高，文件越清晰
        rotate = int(0)
        
        trans = fitz.Matrix(zoom / 100.0, zoom / 100.0).prerotate(rotate)
        pm = page.get_pixmap(matrix=trans, alpha=False)
      
        lurl='.pdf/%s.jpg' % str(pg+1)
        pm.save(lurl)
    doc.close()
 
covert2pic(100)