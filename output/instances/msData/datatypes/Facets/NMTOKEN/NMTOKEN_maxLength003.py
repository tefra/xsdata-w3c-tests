from output.models.ms_data.datatypes.facets.nmtoken.nmtoken_max_length003_xsd.nmtoken_max_length003 import FooType
from output.models.ms_data.datatypes.facets.nmtoken.nmtoken_max_length003_xsd.nmtoken_max_length003 import Test


obj = Test(
    foo=FooType.Foo(
        value="special test for datatypes that are attribute only",
        attr_test="foofo"
    )
)
