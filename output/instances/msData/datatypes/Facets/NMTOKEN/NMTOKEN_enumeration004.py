from output.models.ms_data.datatypes.facets.nmtoken.nmtoken_enumeration004_xsd.nmtoken_enumeration004 import FooAttrTest
from output.models.ms_data.datatypes.facets.nmtoken.nmtoken_enumeration004_xsd.nmtoken_enumeration004 import FooType
from output.models.ms_data.datatypes.facets.nmtoken.nmtoken_enumeration004_xsd.nmtoken_enumeration004 import Test


obj = Test(
    foo=FooType.Foo(
        value='special test for datatypes that are attribute only',
        attr_test=FooAttrTest.FOO
    )
)
