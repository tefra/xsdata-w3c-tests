from output.models.ms_data.model_groups.mg_f014_xsd.mg_f014 import Doc
from output.models.ms_data.model_groups.mg_f014_xsd.mg_f014 import Foo
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
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
    b_or_b2=Foo.B(
        value='I am a stringy string'
    ),
    a=1,
    c=True
)
