from output.models.ms_data.datatypes.facets.notation.notation_enumeration002_xsd.notation_enumeration002 import FooAttrTest
from output.models.ms_data.datatypes.facets.notation.notation_enumeration002_xsd.notation_enumeration002 import Test


obj = Test(
    foo=FooType.Foo(
        value="special test for datatypes that are attribute only",
        attr_test=FooAttrTest.MPEG
    )
)
