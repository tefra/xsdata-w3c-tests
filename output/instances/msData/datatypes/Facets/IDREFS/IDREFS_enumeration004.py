from output.models.ms_data.datatypes.facets.idrefs.idrefs_enumeration004_xsd.idrefs_enumeration004 import Foo
from output.models.ms_data.datatypes.facets.idrefs.idrefs_enumeration004_xsd.idrefs_enumeration004 import FooIdrefsAttr
from output.models.ms_data.datatypes.facets.idrefs.idrefs_enumeration004_xsd.idrefs_enumeration004 import Test


obj = Test(
    foo=Foo(
        idrefs_attr=FooIdrefsAttr.FOO123,
        id_attr="foo123"
    )
)
