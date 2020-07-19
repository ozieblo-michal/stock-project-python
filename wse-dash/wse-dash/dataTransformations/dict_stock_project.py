'''
name_abbreviation_mWIG40_dict - values: full name of the company, keys: its shortcut

sectors_mWIG40_dict - values: shortcut of the companys' full name, keys: market cluster

Market clusters are picked subjectively, based on market knowledge.

mWIG40 included additionally, used next as the index benchmark.
'''

name_abbreviation_mWIG40_dict = {
    'mWIG40': 'mWIG40',
    '11_bit_studios': '11B',
    'Asseco_Poland': 'ACP',
    'Amica': 'AMC',
    'Grupa_Azoty': 'ATT',
    'Budimex': 'BDX',
    'Benefit_Systems': 'BFT',
    'Bank_Handlowy_w_Warszawie': 'BHW',
    'BNP_Paribas_Bank_Polska': 'BNP',
    'Boryszew': 'BRS',
    'Inter_Cars': 'CAR',
    'Ciech': 'CIE',
    'CI_Games': 'CIG',
    'Celon_Pharma': 'CLN',
    'Comarch': 'CMR',
    'Develia': 'DVL',
    'AmRest_Holdings': 'EAT',
    'Echo_Investment': 'ECH',
    'Enea': 'ENA',
    'Energa': 'ENG',
    'Eurocash': 'EUR',
    'Fabryka_Maszyn_Famur': 'FMF',
    'Fabryki_Mebli_Forte': 'FTE',
    'Giełda_Papierów_Wartościowych_w_Warszawie': 'GPW',
    'Globe_Trade_Centre': 'GTC',
    'Getin_Holding': 'GTN',
    'ING_Bank_Śląski': 'ING',
    'Kernel_Holding': 'KER',
    'Kruk': 'KRU',
    'Grupa_Kęty': 'KTY',
    'LiveChat_Software': 'LVC',
    'Lubelski_Węgiel_Bogdanka': 'LWB',
    'Mabion': 'MAB',
    'Bank_Millennium': 'MIL',
    'Orbis': 'ORB',
    'PKP_Cargo': 'PKP',
    'PlayWay': 'PLW',
    'Stalprodukt': 'STP',
    'Ten_Square_Games': 'TEN',
    'VRG': 'VRG',
    'Wirtualna_Polska_Holding': 'WPL'
}

sectors_mWIG40_dict = {
    'mWIG40':'MARKET INDICATOR',
    '11B':'GAMING',
    'ACP':'IT',
    'AMC':'AGD',
    'ATT':'CHEMICALS',
    'BDX':'INFRASTRUCTURE',
    'BFT':'SERVICES',
    'BHW':'BANK',
    'BNP':'BANK',
    'BRS':'CHEMICALS AND CAR PARTS',
    'CAR':'CAR PARTS',
    'CIE':'CHEMICALS',
    'CIG':'GAMING',
    'CLN':'BIOTECH',
    'CMR':'IT',
    'DVL':'CONSTRUCTION DEVELOPER',
    'EAT':'FOOD INDUSTRY',
    'ECH':'CONSTRUCTION DEVELOPER',
    'ENA':'ENERGETICS',
    'ENG':'ENERGETICS',
    'EUR':'FOOD INDUSTRY',
    'FMF':'MINING INDUSTRY',
    'FTE':'FURNITURE',
    'GPW':'STOCK EXCHANGE',
    'GTC':'CONSTRUCTION DEVELOPER',
    'GTN':'BANK',
    'ING':'BANK',
    'KER':'FOOD INDUSTRY',
    'KRU':'VINDICATION',
    'KTY':'METAL PROCESSING',
    'LVC':'IT',
    'LWB':'MINING INDUSTRY',
    'MAB':'BIOTECH',
    'MIL':'BANK',
    'ORB':'HOSPITALITY',
    'PKP':'RAILWAYS',
    'PLW':'GAMING',
    'STP':'METAL PROCESSING',
    'TEN':'GAMING',
    'VRG':'CLOTHES',
    'WPL':'IT'
}

print('Number of market clusters in dataset: ', len(set(sectors_mWIG40_dict.values())))
# 22 market sectors