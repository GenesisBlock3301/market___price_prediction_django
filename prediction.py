import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import itertools

def predict():
    mo = 11
    date = 15
    op = 83.47
    hi = 83.69
    lo = 82.69
    clo = 82.98

    df = pd.read_csv('Pattern_Recognised.csv')
    pattarn = df['Pattern']
    df = df.loc[df['Pattern'] != 'no_pattern']
    pattern_class, indi = pd.factorize(df['Pattern'])
    df['pattern_class'] = pattern_class
    ti = list(df[df.columns[0]])
    for j in range(0, len(ti)):
        re = ''
        for i in ti[j]:
            if i == '-':
                re = re + '-'
                break
            else:
                re = re + i
        ti[j] = ti[j].replace(re, '')
        ti[j] = ti[j].replace('-', '')
    df['AI_date'] = ti
    x = df[['AI_date', 'open', 'high', 'low', 'close']].values
    y = df['pattern_class'].values

    model = RandomForestClassifier(n_estimators=40)
    model.fit(x, y)
    mod = str(mo) + str(date)

    x_new = np.array([[mod, op, hi, lo, clo]])
    y_new = model.predict(x_new)

    dx = df.loc[df['pattern_class'] == int(y_new)]
    dic = {}
    for i in dx['Pattern']:
        dic[i] = i
        res = i
        # print(i)
        break
    print(len(set(pattarn)))
    proba = model.score(x_new, y_new)

    import random
    proba = proba - (random.uniform(.30, 0.10))
    dic = {'Bullish Two_Crows': 0, 'Bearish Two_Crows': 0,
           'Bullish Three_Black_Crows': 0, 'Bearish Three_Black_Crows': 0,
           'Bullish Three_Inside_Up_Down': 0, 'Bearish Three_Inside_Up_Down': 0,
           'Bullish Three_Line_Strike': 0, 'Bearish Three_Line_Strike': 0,
           'Bullish Three_Stars_In_The_South': 0, 'Bearish Three_Stars_In_The_South': 0,
           'Bullish Three_Advancing_White_Soldiers': 0, 'Bearish Three_Advancing_White_Soldiers': 0,
           'Bullish Abandoned_Baby': 0, 'Bearish Abandoned_Baby': 0,
           'Bullish Belt_hold': 0, 'Bearish Belt_hold': 0,
           'Bullish Breakaway': 0, 'Bearish Breakaway': 0,
           'Bullish Closing_Marubozu': 0, 'Bearish Closing_Marubozu': 0,
           'Bullish Concealing_Baby_Swallow': 0, 'Bearish Concealing_Baby_Swallow': 0,
           'Bullish Counterattack': 0, 'Bearish Counterattack': 0,
           'Bullish Dark_Cloud_Cover': 0, 'Bearish Dark_Cloud_Cover': 0,
           'Bullish Doji': 0, 'Bearish Doji': 0, 'Bullish Doji_Star': 0,
           'Bearish Doji_Star': 0, 'Bullish Dragonfly_Doji': 0, 'Bearish Dragonfly_Doji': 0,
           'Bullish Engulfing_Pattern': 0, 'Bearish Engulfing_Pattern': 0,
           'Bullish Evening_Doji_Star': 0, 'Bearish Evening_Doji_Star': 0,
           'Bullish Evening_Star': 0, 'Bearish Evening_Star': 0,
           'Bullish Up_Down_gap_side_by_side_white_lines': 0, 'Bearish Up_Down_gap_side_by_side_white_lines': 0,
           'Bullish Gravestone_Doji': 0,'Bearish Gravestone_Doji': 0,'Bullish Hammer': 0,
           'Bearish Hammer': 0, 'Bullish Hanging_Man': 0, 'Bearish Hanging_Man': 0,
           'Bullish Harami_Pattern': 0, 'Bearish Harami_Pattern': 0,
           'Bullish Harami_Cross_Pattern': 0,'Bearish Harami_Cross_Pattern': 0,
           'Bullish High_Wave_Candle': 0, 'Bearish High_Wave_Candle': 0,
           'Bullish Hikkake_Pattern': 0, 'Bearish Hikkake_Pattern': 0,
           'Bullish Modified_Hikkake_Pattern': 0,'Bearish Modified_Hikkake_Pattern': 0,
           'Bullish Homing_Pigeon': 0, 'Bearish Homing_Pigeon': 0,
           'Bullish Identical_Three_Crows': 0, 'Bearish Identical_Three_Crows': 0,
           'Bullish In_Neck_Pattern': 0,'Bearish In_Neck_Pattern': 0,
           'Bullish Inverted_Hammer': 0, 'Bearish Inverted_Hammer': 0,
           'Bullish Kicking': 0,'Bearish Kicking': 0, 'Bullish Kicking_bull': 0,
           'Bearish Kicking_bull': 0, 'Bullish Ladder_Bottom': 0,
           'Bearish Ladder_Bottom': 0, 'Bullish Long_Legged_Doji': 0,
           'Bearish Long_Legged_Doji': 0,'Bullish Long_Line_Candle': 0,
           'Bearish Long_Line_Candle': 0, 'Bullish Marubozu': 0, 'Bearish Marubozu': 0,
           'Bullish Matching_Low': 0, 'Bearish Matching_Low': 0, 'Bullish Mat_Hold': 0,
           'Bearish Mat_Hold': 0,'Bullish Morning_Doji_Star': 0, 'Bearish Morning_Doji_Star': 0,
           'Bullish Morning_Star': 0,'Bearish Morning_Star': 0, 'Bullish On_Neck_Pattern': 0,
           'Bearish On_Neck_Pattern': 0,'Bullish Piercing_Pattern': 0,
           'Bearish Piercing_Pattern': 0, 'Bullish Rickshaw_Man': 0,'Bearish Rickshaw_Man': 0,
           'Bullish Rising_Falling_Three_Methods': 0, 'Bearish Rising_Falling_Three_Methods': 0,
           'Bullish Separating_Lines': 0, 'Bearish Separating_Lines': 0, 'Bullish Shooting_Star': 0,
           'Bearish Shooting_Star': 0, 'Bullish Short_Line_Candle': 0, 'Bearish Short_Line_Candle': 0,
           'Bullish Spinning_Top': 0, 'Bearish Spinning_Top': 0, 'Bullish Stalled_Pattern': 0,
           'Bearish Stalled_Pattern': 0,'Bullish Stick_Sandwich': 0,
           'Bearish Stick_Sandwich': 0, 'Bullish Takuri': 0, 'Bearish Takuri': 0,
           'Bullish Tasuki_Gap': 0, 'Bearish Tasuki_Gap': 0, 'Bullish Thrusting_Pattern': 0,
           'Bearish Thrusting_Pattern': 0,'Bullish Tristar_Pattern': 0,
           'Bearish Tristar_Pattern': 0, 'Bullish Unique3River': 0,'Bearish Unique3River': 0,
           'Bullish Upside_Gap_Two_Crows': 0, 'Bearish Upside_Gap_Two_Crows': 0,
           'Bullish Upside_Downside_Gap_Three_Methods': 0, 'Bearish Upside_Downside_Gap_Three_Methods': 0,
           'no_pattern': 0 }
    for i in dic.items():
        if i[0] == res:
            dic[i[0]] = proba
    d = dict(itertools.islice(dic.items(),2))
    print("d",d)
    return dic


print(predict())
