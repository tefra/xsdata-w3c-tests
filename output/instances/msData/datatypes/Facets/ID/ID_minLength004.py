from output.models.ms_data.datatypes.facets.id.id_min_length004_xsd.id_min_length004 import FooType
from output.models.ms_data.datatypes.facets.id.id_min_length004_xsd.id_min_length004 import Test


obj = Test(
    foo=FooType.Foo(
        value='special test for datatypes that are attribute only',
        attr_test='foofo'
    )
)
