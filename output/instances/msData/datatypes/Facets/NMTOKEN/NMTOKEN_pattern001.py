from output.models.ms_data.datatypes.facets.nmtoken.nmtoken_pattern001_xsd.nmtoken_pattern001 import FooType
from output.models.ms_data.datatypes.facets.nmtoken.nmtoken_pattern001_xsd.nmtoken_pattern001 import Test


obj = Test(
    foo=FooType.Foo(
        value="special test for datatypes that are attribute only",
        attr_test="abc"
    )
)
