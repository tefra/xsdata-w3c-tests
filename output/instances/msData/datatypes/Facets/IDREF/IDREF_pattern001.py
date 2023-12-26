from output.models.ms_data.datatypes.facets.idref.idref_pattern001_xsd.idref_pattern001 import FooType
from output.models.ms_data.datatypes.facets.idref.idref_pattern001_xsd.idref_pattern001 import Test


obj = Test(
    foo=FooType.Foo(
        value='special test for datatypes that are attribute only',
        attr_test='abc',
        id_attr='abc'
    )
)
