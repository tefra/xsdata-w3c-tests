from output.models.ms_data.errata10.err_a003_xsd.err_a003 import Root
from output.models.ms_data.errata10.err_a003_xsd.err_a003 import TestElement
from xsdata.models.datatype import XmlPeriod


obj = Root(
    test_element=TestElement(
        value=XmlPeriod("--05")
    )
)
