from output.models.ms_data.datatypes.facets.notation.notation_min_length002_xsd.notation_min_length002 import BuildNotation
from output.models.ms_data.datatypes.facets.notation.notation_min_length002_xsd.notation_min_length002 import Test


obj = Test(
    foo=FooType.Foo(
        value="special test for datatypes that are attribute only",
        attr_test=BuildNotation.MPEG
    )
)