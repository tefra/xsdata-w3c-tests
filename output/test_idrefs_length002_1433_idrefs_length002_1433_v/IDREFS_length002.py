from output.models.ms_data.datatypes.facets.idrefs.idrefs_length002_xsd.idrefs_length002 import Foo
from output.models.ms_data.datatypes.facets.idrefs.idrefs_length002_xsd.idrefs_length002 import Test


obj = Test(
    foo=Foo(
        idrefs_attr=[
            'foofo',
            'more',
        ],
        id1_attr='foofo'
    ),
    id2_attr='more'
)
