from output.models.ms_data.datatypes.facets.notation.notation_max_length001_xsd.notation_max_length001 import BuildNotation
from output.models.ms_data.datatypes.facets.notation.notation_max_length001_xsd.notation_max_length001 import FooType
from output.models.ms_data.datatypes.facets.notation.notation_max_length001_xsd.notation_max_length001 import Test


obj = Test(
    foo=FooType.Foo(
        value="special test for datatypes that are attribute only",
        attr_test=BuildNotation.MPEG
    )
)
