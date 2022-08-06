from output.models.ms_data.datatypes.facets.idref.idref_enumeration004_xsd.idref_enumeration004 import FooAttrTest
from output.models.ms_data.datatypes.facets.idref.idref_enumeration004_xsd.idref_enumeration004 import Test


obj = Test(
    foo=FooType.Foo(
        value="special test for datatypes that are attribute only",
        attr_test=FooAttrTest.FOO,
        id_attr="foo"
    )
)
