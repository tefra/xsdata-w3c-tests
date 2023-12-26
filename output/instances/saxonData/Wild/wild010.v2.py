from output.models.saxon_data.wild.wild012_xsd.wild012inc import Eden
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Eden(
    any_element=AnyElement(
        qname='{http://eve.com/}eve',
        text=''
    )
)
