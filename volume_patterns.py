import numpy as np

def find_volume_patterns(data, pattern):
    conditions = pattern.split(',')
    volumes = data['Volume'].values
    opens = data['Open'].values
    closes = data['Close'].values
    highs = data['High'].values
    lows = data['Low'].values

    # Dictionary to map the variable names to the actual data
    variable_mapping = {
        'cv': volumes, 'pv': np.roll(volumes, 1), 'pv1': np.roll(volumes, 2), 'pv2': np.roll(volumes, 3),
        'pv3': np.roll(volumes, 4), 'pv4': np.roll(volumes, 5), 'pv5': np.roll(volumes, 6), 'pv6': np.roll(volumes, 7),
        'pv7': np.roll(volumes, 8), 'pv8': np.roll(volumes, 9), 'pv9': np.roll(volumes, 10), 'pv10': np.roll(volumes, 11),
        'pv11': np.roll(volumes, 12), 'pv12': np.roll(volumes, 13), 'fv1': np.roll(volumes, -1), 'fv2': np.roll(volumes, -2),
        'fv3': np.roll(volumes, -3), 'fv4': np.roll(volumes, -4), 'fv5': np.roll(volumes, -5), 'co': opens, 'cc': closes,
        'fo1': np.roll(opens, -1), 'fc1': np.roll(closes, -1), 'fo2': np.roll(opens, -2), 'fc2': np.roll(closes, -2),
        'fo3': np.roll(opens, -3), 'fc3': np.roll(closes, -3), 'fo4': np.roll(opens, -4), 'fc4': np.roll(closes, -4),
        'fo5': np.roll(opens, -5), 'fc5': np.roll(closes, -5), 'po': np.roll(opens, 1), 'po1': np.roll(opens, 2),
        'po2': np.roll(opens, 3), 'po3': np.roll(opens, 4), 'po4': np.roll(opens, 5), 'po5': np.roll(opens, 6),
        'po6': np.roll(opens, 7), 'po7': np.roll(opens, 8), 'po8': np.roll(opens, 9), 'po9': np.roll(opens, 10),
        'po10': np.roll(opens, 11), 'po11': np.roll(opens, 12), 'po12': np.roll(opens, 13), 'pc': np.roll(closes, 1),
        'pc1': np.roll(closes, 2), 'pc2': np.roll(closes, 3), 'pc3': np.roll(closes, 4), 'pc4': np.roll(closes, 5),
        'pc5': np.roll(closes, 6), 'pc6': np.roll(closes, 7), 'pc7': np.roll(closes, 8), 'pc8': np.roll(closes, 9),
        'pc9': np.roll(closes, 10), 'pc10': np.roll(closes, 11), 'pc11': np.roll(closes, 12), 'pc12': np.roll(closes, 13),
        'cl': lows, 'pl': np.roll(highs, 1), 'pl1': np.roll(highs, 2), 'pl2': np.roll(highs, 3), 'pl3': np.roll(highs, 4),
        'pl4': np.roll(highs, 5), 'pl5': np.roll(highs, 6), 'pl6': np.roll(highs, 7), 'pl7': np.roll(highs, 8),
        'pl8': np.roll(highs, 9), 'pl9': np.roll(highs, 10), 'pl10': np.roll(highs, 11), 'pl11': np.roll(highs, 12),
        'pl12': np.roll(highs, 13), 'ch': highs, 'ph': np.roll(highs, 1), 'ph1': np.roll(highs, 2), 'ph2': np.roll(highs, 3),
        'ph3': np.roll(highs, 4), 'ph4': np.roll(highs, 5), 'ph5': np.roll(highs, 6), 'ph6': np.roll(highs, 7),
        'ph7': np.roll(highs, 8), 'ph8': np.roll(highs, 9), 'ph9': np.roll(highs, 10), 'ph10': np.roll(highs, 11),
        'ph11': np.roll(highs, 12), 'ph12': np.roll(highs, 13),
        'fl1': np.roll(lows, 1), 'fl2': np.roll(lows, 2), 'fl3': np.roll(lows, 3), 'fl4': np.roll(lows, 4), 'fl5': np.roll(lows, 5),
        'fh1': np.roll(highs, 1), 'fh2': np.roll(highs, 2), 'fh3': np.roll(highs, 3), 'fh4': np.roll(highs, 4), 'fh5': np.roll(highs, 5)
    }

    condition_results = []
    for condition in conditions:
        # Split the condition into its components (variable, operator, variable)
        parts = condition.replace(" ", "").split('<')
        if len(parts) == 2:
            left_var, right_var = parts
            condition_result = variable_mapping[left_var] < variable_mapping[right_var]
        else:
            parts = condition.replace(" ", "").split('>')
            left_var, right_var = parts
            condition_result = variable_mapping[left_var] > variable_mapping[right_var]

        condition_results.append(condition_result)

    pattern_found = np.logical_and.reduce(condition_results)
    return data.index[pattern_found]

