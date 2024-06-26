from output.models.ms_data.model_groups.mg_f010_xsd.mg_f010 import Doc
from output.models.ms_data.model_groups.mg_f010_xsd.mg_f010 import Foo
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    a=1,
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
    ],
    d='',
    c=True,
    b_or_b2=Foo.B(
        value='I am a stringy string'
    )
)
