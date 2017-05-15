from pdfrw import PdfReader, PdfWriter, PdfObject


def main():
    thesis = PdfReader('thesis.pdf')

    for i, _ in enumerate(thesis.pages):
        try:
            im_keys = thesis.pages[i].Resources.XObject.keys()

            for key in im_keys:
                thesis.pages[i].Resources.XObject[key].Interpolate = PdfObject('false')
                thesis.pages[i].Resources.XObject[key].SMask.Interpolate = PdfObject('false')

        except:
            print('This page does not have images: {}'.format(i))

    PdfWriter().write('thesis_out.pdf', thesis)


if __name__ == '__main__':
    main()
