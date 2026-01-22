from output.models.ms_data.element.elem_z014_xsd.elem_z014 import CtypeFoo
from output.models.ms_data.element.elem_z014_xsd.elem_z014 import RootElem
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = RootElem(
    any_element=DerivedElement(
        qname='myelem',
        value=CtypeFoo(
            a='hello'
        ),
        type='{urn-klondike-test}ctype_foo'
    )
)
