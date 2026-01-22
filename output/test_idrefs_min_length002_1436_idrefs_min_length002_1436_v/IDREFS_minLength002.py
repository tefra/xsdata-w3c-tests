from output.models.ms_data.datatypes.facets.idrefs.idrefs_min_length002_xsd.idrefs_min_length002 import Foo
from output.models.ms_data.datatypes.facets.idrefs.idrefs_min_length002_xsd.idrefs_min_length002 import Test


obj = Test(
    foo=Foo(
        idrefs_attr=[
            'more',
            'foofo',
        ],
        id1_attr='foofo'
    ),
    id2_attr='more'
)
