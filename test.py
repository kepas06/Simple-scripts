dest_subTypes = [('.pdf', '/documents'), ('.docx', '/documents'),
                ('.txt', '/documents'), ('.md', 'documents'),
                ('.csv', '/documents'), ('.xls', '/doucments'),
                ('.jpg', '/images'), ('.png', 'images'),
                ('.zip', '/packed'), ('.tar.xz', '/packages'),
                ('.deb', '/packages'), ('.tar.gz', '/packages'),
                ('.iso', '/packages')]

for fileFormat, dest in dest_subTypes:
    print("index is", fileFormat)
    print(" and dest ", dest)