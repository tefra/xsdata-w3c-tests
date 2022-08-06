from output.models.ms_data.datatypes.facets.notation.notation_enumeration004_xsd.notation_enumeration004 import FooAttrTest
from output.models.ms_data.datatypes.facets.notation.notation_enumeration004_xsd.notation_enumeration004 import Test


obj = Test(
    foo=FooType.Foo(
        value="special test for datatypes that are attribute only",
        attr_test=FooAttrTest.G
    )
)
