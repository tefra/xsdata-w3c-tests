from output.models.ms_data.model_groups.mg_i011_xsd.mg_i011 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    choice=[
        AnyElement(
            qname='{http://www.w3.org/1999/xhtml}html',
            text='',
            children=[
                AnyElement(
                    qname='{http://www.w3.org/1999/xhtml}body',
                    text='\nHey this is html\n'
                ),
            ]
        ),
    ]
)
