z = input('File name: ')
z = z.lower()
if '.gif' in z:
    print('image/gif')
elif '.jpg' in z:
    print('image/jpeg')
elif '.jpeg' in z:
    print('image/jpeg')
elif '.png' in z:
    print('image/png')
elif '.pdf' in z:
    print('application/pdf')
elif '.txt' in z:
    print('text/plain')
elif '.zip' in z:
    print('application/zip')
else:
    print('application/octet-stream')
