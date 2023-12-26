from output.models.ms_data.element.qfe1700c_xsd.qfe1700c import E2
from output.models.ms_data.element.qfe1700c_xsd.qfe1700c import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    e1='abc',
    any_element=AnyElement(
        qname='e2',
        text='abc',
        children=[
            AnyElement(
                qname='e3',
                text=''
            ),
        ],
        attributes={
            '{http://www.w3.org/2001/XMLSchema-instance}nil': 'false',
        }
    ),
    e2=E2(

    )
)
