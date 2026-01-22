from output.models.ms_data.datatypes.facets.notation.notation_min_length004_xsd.notation_min_length004 import BuildNotation
from output.models.ms_data.datatypes.facets.notation.notation_min_length004_xsd.notation_min_length004 import FooType
from output.models.ms_data.datatypes.facets.notation.notation_min_length004_xsd.notation_min_length004 import Test


obj = Test(
    foo=FooType.Foo(
        value='special test for datatypes that are attribute only',
        attr_test=BuildNotation.MPEG
    )
)
