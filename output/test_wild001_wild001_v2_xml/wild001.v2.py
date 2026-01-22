from output.models.saxon_data.wild.wild001_xsd.wild001 import Eden


obj = Eden(
    any_attributes={
        'adam': 'm',
        'eve': 'f',
        '{http://genesis.com/}cain': 'm',
        '{http://genesis.com/}abel': 'm',
    }
)
