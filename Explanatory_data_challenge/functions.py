def replace_country(df, dictionary, column1, column2, key1, key2):
    df[column1] = df[column2].map(dictionary.set_index(key1)[key2])



country_codes = {
    'ZZX': 'Mixed-teams 1896-1904',
    'BOH': 'Bohemia',
    'ANZ': 'Australasia',
    'RU1': 'Russian Empire',
    'TCH': 'Czechoslovakia',
    'YUG': 'Yugoslavia',
    'ROU': 'Romania',
    'URS': 'Soviet Union',
    'EUA': 'Unified Team of Germany',
    'BWI': 'British West Indies',
    'GDR': 'East Germany',
    'FRG': 'West Germany',
    'EUN': 'Unified Team',
    'IOP': 'Independent Olympic Participants',
    'SRB': 'Serbia',
    'TTO': 'Trinidad and Tobago',
    'MNE': 'Montenegro',
    'SGP': 'Singapore'
}
