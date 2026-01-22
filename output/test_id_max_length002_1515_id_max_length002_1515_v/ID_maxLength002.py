from output.models.ms_data.datatypes.facets.id.id_max_length002_xsd.id_max_length002 import FooType
from output.models.ms_data.datatypes.facets.id.id_max_length002_xsd.id_max_length002 import Test


obj = Test(
    foo=FooType.Foo(
        value='special test for datatypes that are attribute only',
        attr_test='foofo'
    )
)
