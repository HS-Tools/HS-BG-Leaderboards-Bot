REGIONS = ['US', 'EU', 'AP']
REGION_ALIASES = {
    'NA':'US',
    'AMERICA':'US',
    'AMERICAS':'US',
    'ASIA':'AP',
    'EUROPE':'EU'
}

def parseRegion(region):
    region = region.upper()

    region = REGION_ALIASES.get(region, region)
    if region in REGIONS:
        return region
