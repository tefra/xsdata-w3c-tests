from output.models.ms_data.wildcards.wild_o002_xsd.wild_o002 import Foo


obj = Foo(
    any_attributes={
        '{http://www.w3.org/2001/XMLSchema-instance}schemaLocation': 'http://foobar wildO002.xsd http://foo wildO002a.xsd',
        '{http://foo}name': 'bar',
    }
)
