from output.models.saxon_data.open.open035_xsd.open035 import BookStore


obj = BookStore(
    book=[
        BookStore.Book(
            id='b1',
            title='T',
            author='A',
            date='date',
            isbn='is',
            publisher='Pub'
        ),
    ]
)
