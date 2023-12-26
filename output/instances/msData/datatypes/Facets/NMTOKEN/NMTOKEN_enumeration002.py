from output.models.ms_data.datatypes.facets.nmtoken.nmtoken_enumeration002_xsd.nmtoken_enumeration002 import FooAttrTest
from output.models.ms_data.datatypes.facets.nmtoken.nmtoken_enumeration002_xsd.nmtoken_enumeration002 import FooType
from output.models.ms_data.datatypes.facets.nmtoken.nmtoken_enumeration002_xsd.nmtoken_enumeration002 import Test


obj = Test(
    foo=FooType.Foo(
        value='special test for datatypes that are attribute only',
        attr_test=FooAttrTest.FOO
    )
)
