from output.models.sun_data.wildcard.ns_constraint.ns_constraint00301m.ns_constraint00301m1_xsd.ns_constraint00301m1 import A
from xsdata.formats.dataclass.models.generics import AnyElement


obj = A(
    ns_test1_ns_test2_element=[
        AnyElement(
            qname="{ns_test1}date",
            text="2002-04-29"
        ),
        AnyElement(
            qname="{ns_test2}time",
            text="15:15:00"
        ),
    ]
)
