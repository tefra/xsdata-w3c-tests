from output.models.ms_data.complex_type.test67200_xsd.test67200 import TypeA
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = DerivedElement(
    qname='elt1',
    value=TypeA(
        elt2=''
    ),
    type='typeA'
)
