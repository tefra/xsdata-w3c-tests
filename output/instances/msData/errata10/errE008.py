from output.models.ms_data.errata10.err_e008_xsd.err_e008 import Root
from output.models.ms_data.errata10.err_e008_xsd.err_e008 import TestToken


obj = Root(
    test_token=TestToken(
        value='test\rdata'
    )
)
