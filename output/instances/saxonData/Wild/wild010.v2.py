from output.models.saxon_data.wild.wild010_xsd.wild010 import Eden
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Eden(
    any_element=AnyElement(
        qname='{http://eve.com/}eve',
        text=''
    )
)
