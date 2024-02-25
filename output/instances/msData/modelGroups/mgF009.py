from output.models.ms_data.model_groups.mg_f009_xsd.mg_f009 import Doc
from output.models.ms_data.model_groups.mg_f009_xsd.mg_f009 import Foo
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    a=1,
    b_or_b2=Foo.B(
        value='I am a stringy string'
    ),
    c=True,
    d='',
    w3_org_1999_xhtml_element=[
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
