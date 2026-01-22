from output.models.ms_data.datatypes.facets.idref.idref_max_length003_xsd.idref_max_length003 import FooType
from output.models.ms_data.datatypes.facets.idref.idref_max_length003_xsd.idref_max_length003 import Test


obj = Test(
    foo=FooType.Foo(
        value='special test for datatypes that are attribute only',
        attr_test='foofo',
        id_attr='foofo'
    )
)
