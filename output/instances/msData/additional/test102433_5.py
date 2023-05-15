from output.models.ms_data.additional.test102433_xsd.test102433 import Bar
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Bar(
    any_element=AnyElement(
        qname="{ns}baz",
        text=""
    )
)
