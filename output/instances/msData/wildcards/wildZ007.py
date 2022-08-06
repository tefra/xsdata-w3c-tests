from output.models.ms_data.wildcards.wild_z007_xsd.wild_z007 import Stylesheet
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Stylesheet(
    any_element=AnyElement(
        qname="e",
        text="",
        tail=None,
        children=[],
        attributes={
            "{http://www.w3.org/1999/XSL/Transform}use-attribute-sets": "foo",
        }
    )
)
