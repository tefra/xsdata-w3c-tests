from output.models.ms_data.datatypes.facets.id.id_max_length003_xsd.id_max_length003 import FooType
from output.models.ms_data.datatypes.facets.id.id_max_length003_xsd.id_max_length003 import Test


obj = Test(
    foo=FooType.Foo(
        value="special test for datatypes that are attribute only",
        attr_test="foofo"
    )
)
