from output.models.ms_data.model_groups.mg_f013_xsd.mg_f013 import Doc
from output.models.ms_data.model_groups.mg_f013_xsd.mg_f013 import Foo
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    d='',
    b_or_b2=Foo.B(
        value='I am a stringy string'
    ),
    c=True,
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
    ]
)
