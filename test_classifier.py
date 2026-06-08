from app.extractors.drivers_license import extract_drivers_license

text = """
Virginia
DRIVER'S
LICENSE

Customer Number
E66031726

KWON
CALVIN SOONHYUK

Date of Birth
04/17/2007

Exp
04/17/2031

12602 HERITAGE FARM LN
HERNDON VA 20171
"""

print(extract_drivers_license(text))
