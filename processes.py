import numpy as np

def feature_engineer(data):
    ρmatrix, ρfluid = 2.65, 1.0

    data['FRR'] = data['ILD'] / data['MSFL']
    data['RD'] = data['ILD'] - data['ILM']
    data['PHID'] = (ρmatrix - data['RHOB']) - (ρmatrix - ρfluid) 
    data['PHIT'] = (data['NPHI'] + data['PHID']) / 2
    data['SW'] = pow((1 / data['ILD'] * pow(data['PHIT'], 2)), 1/2)

    GR_clean = min(data['GR'])
    GR_shale = max(data['GR'])

    data['VSH'] = (data['GR'] - GR_clean) / GR_shale - GR_clean
    data['SHC'] = 1 - data['SW']
    data['AI'] = data['RHOB'] * (1/data['DT'])
    data['BI'] = (min(data['RHOB']) - data['RHOB']) / (min(data['RHOB']) - max(data['RHOB']))
    data['BVW'] = data['PHIT'] * data['SW']
    data['PHIFR'] = data['PHIT'] - data['PHID']
    data['LITHI'] = (data['CALI'] - min(data['CALI'])) / (max(data['CALI']) - min(data['CALI']))


    # data['AI'] == np.inf
    data['AI'].replace(np.inf, 0, inplace=True)

    return data


def wrangle(data):
    # Remove Missing Data - Drop rows with -999
    data = data[~data.isin([-999.25]).any(axis=1)]

    return data