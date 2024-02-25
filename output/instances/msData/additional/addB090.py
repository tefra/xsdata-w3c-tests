from output.models.ms_data.additional.add_b090_xsd.add_b090 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    foo_element=[
        AnyElement(
            qname='{foo}test',
            text=''
        ),
    ],
    c1_or_c2=Doc.C1(

    )
)
