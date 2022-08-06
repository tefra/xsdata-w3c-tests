from output.models.ms_data.datatypes.facets.idrefs.idrefs_min_length004_xsd.idrefs_min_length004 import Foo
from output.models.ms_data.datatypes.facets.idrefs.idrefs_min_length004_xsd.idrefs_min_length004 import Test


obj = Test(
    foo=Foo(
        idrefs_attr=[
            "foofo",
            "more",
        ],
        id1_attr="foofo"
    ),
    id2_attr="more"
)
