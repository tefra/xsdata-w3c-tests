from output.models.ms_data.datatypes.facets.idrefs.idrefs_min_length001_xsd.idrefs_min_length001 import Foo
from output.models.ms_data.datatypes.facets.idrefs.idrefs_min_length001_xsd.idrefs_min_length001 import Test


obj = Test(
    foo=Foo(
        idrefs_attr=[
            "foofo",
        ],
        id1_attr="foofo"
    ),
    id2_attr="more"
)
