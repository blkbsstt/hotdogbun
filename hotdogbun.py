import sys
from PyPDF2 import PdfFileWriter, PdfFileReader
from pgmagick import Image

def split(paperpdf, splitpdf):
    output = PdfFileWriter()

    with open(paperpdf, "rb") as l:
        with open(paperpdf, "rb") as r:
            # I know... I know.
            # We have to do this because PyPDF2 kind of sucks.
            left = PdfFileReader(l)
            right = PdfFileReader(r)

            pagecount = left.getNumPages()
            print("%s has %s pages to split." % (paperpdf,pagecount))

            images = [Image(paperpdf + "[%d]" % i) for i in range(0, pagecount)]
            left_margin, left_gutter, right_margin, right_gutter = get_average_margins(images)
            gutter_width = left_gutter + right_gutter

            for num in range(0, pagecount):
                left_page = left.getPage(num)
                right_page = right.getPage(num)
                midpoint = (
                        left_page.mediaBox.getUpperRight_x() / 2,
                        left_page.mediaBox.getUpperRight_y()
                        )

                left_page.mediaBox.upperRight = (midpoint[0] + left_gutter, midpoint[1])
                left_page.mediaBox.upperLeft = (left_margin - gutter_width, midpoint[1])
                output.addPage(left_page)

                right_page.mediaBox.upperRight = (right_page.mediaBox.getWidth() - right_margin + gutter_width , midpoint[1])
                right_page.mediaBox.upperLeft = (midpoint[0] - right_gutter, midpoint[1])
                output.addPage(right_page)

            print("Writing %s pages to %s" % (output.getNumPages(), splitpdf))
            with open(splitpdf, "wb") as s:
                output.write(s)

def avg(l):
    if len(l) > 0:
        return sum(l)/len(l)
    else:
        return 0;

def get_margins(image):
    return image.boundingBox().xOff(), image.size().width() - (image.boundingBox().xOff() + image.boundingBox().width())

def get_average_margins(images):
    margins = [get_margins(im) for im in images]
    left_margin = min([m[0] for m in margins])
    right_margin = min([m[1] for m in margins])

    left_split = []
    right_split = []

    for num in range(0, len(images)):
        page = images[num]
        geom = page.size()
        geom.width(geom.width()/2)
        left_split.append(Image(page))
        left_split[-1].crop(geom)
        geom.xOff(geom.width())
        right_split.append(Image(page))
        right_split[-1].crop(geom)

    right_gutters = [get_margins(im)[1] for im in left_split]
    left_gutters = [get_margins(im)[0] for im in right_split]

    right_gutter = avg([m for m in right_gutters if m > 0])
    left_gutter = avg([m for m in left_gutters if m > 0])

    return left_margin, left_gutter, right_margin, right_gutter

def main(argv):
    # options are for suckers
    pdfs = argv[1:]

    for original in pdfs:
        if original.endswith('.pdf'):
            splitpdf = original[:-4] + '-split.pdf'
        else:
            splitpdf = original + '-split.pdf'

        split(original, splitpdf)

if __name__ == '__main__':
    main(sys.argv)
