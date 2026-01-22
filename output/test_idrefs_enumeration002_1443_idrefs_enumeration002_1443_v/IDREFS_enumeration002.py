from output.models.ms_data.datatypes.facets.idrefs.idrefs_enumeration002_xsd.idrefs_enumeration002 import Foo
from output.models.ms_data.datatypes.facets.idrefs.idrefs_enumeration002_xsd.idrefs_enumeration002 import FooIdrefsAttr
from output.models.ms_data.datatypes.facets.idrefs.idrefs_enumeration002_xsd.idrefs_enumeration002 import Test


obj = Test(
    foo=Foo(
        idrefs_attr=FooIdrefsAttr.FOO,
        id_attr='foo'
    )
)
