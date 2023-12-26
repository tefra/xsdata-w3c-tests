from output.models.sun_data.combined.identity.idc001.idc001_nogen_xsd.idc001_nogen import BookCatalogue


obj = BookCatalogue(
    book=[
        BookCatalogue.Book(
            title='My Life and Times',
            author='Paul McCartney',
            date='1998',
            isbn='94303-12021-43892',
            publisher='McMillin Publishing'
        ),
        BookCatalogue.Book(
            title='Illusions The Adventures of a Reluctant Messiah',
            author='Richard Bach',
            date='1977',
            isbn='0-440-34319-4',
            publisher='Dell Publishing Co.'
        ),
        BookCatalogue.Book(
            title='The First and Last Freedom',
            author='J. Krishnamurti',
            date='1954',
            isbn='0-06-064831-7',
            publisher='Harper & Row'
        ),
    ]
)
