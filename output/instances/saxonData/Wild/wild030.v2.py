from output.models.saxon_data.wild.wild030_xsd.wild030 import QuietComputer
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = DerivedElement(
    qname='computer',
    value=QuietComputer(
        cpu='Intel',
        memory='4Gb',
        monitor='17inch',
        any_element=[
            AnyElement(
                qname='disk',
                text='Seagate'
            ),
            AnyElement(
                qname='mouse',
                text='USB'
            ),
        ]
    ),
    type='quietComputer'
)
