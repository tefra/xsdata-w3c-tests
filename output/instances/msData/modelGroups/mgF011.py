from output.models.ms_data.model_groups.mg_f011_xsd.mg_f011 import Doc
from output.models.ms_data.model_groups.mg_f011_xsd.mg_f011 import Foo
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    b_or_b2=Foo.B(
        value='I am a stringy string'
    ),
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
    c=True,
    a=1,
    d=''
)
