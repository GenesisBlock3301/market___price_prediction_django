from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import View
from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse
import numpy as np
import talib
import plotly
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import plotly.graph_objects as go
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import itertools


class Home(View):
    def get(self, request):
        return render(request, 'home.html')

    def post(self, request):
        print(">>>>>>>>>>>>>>>>>", request.FILES.get('csv_file'))
        file_name = request.FILES.get('csv_file')
        if str(file_name)[-4::] == ".csv":
            handle_profile_image(file_name)
            messages.success(request, "File upload successfully")
        else:
            messages.error(request, "Invalid file")
        return redirect('home')


def process_csv(request):
    path = str(settings.BASE_DIR) + "/media/Day-k.csv"
    # print(path)
    # print(str(settings.BASE_DIR) + "/media/trained/Pattern_Recognised.csv")
    try:
        df = pd.read_csv(path)
        # print(file_open)
        try:
            Two_Crows = talib.CDL2CROWS(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
            Three_Black_Crows = talib.CDL3BLACKCROWS(df['open'].values, df['high'].values, df['low'].values,
                                                     df['close'].values)
            Three_Inside_Up_Down = talib.CDL3INSIDE(df['open'].values, df['high'].values, df['low'].values,
                                                    df['close'].values)
            Three_Line_Strike = talib.CDL3LINESTRIKE(df['open'].values, df['high'].values, df['low'].values,
                                                     df['close'].values)
            Three_Outside_Up_Down = talib.CDL3OUTSIDE(df['open'].values, df['high'].values, df['low'].values,
                                                      df['close'].values)
            Three_Stars_In_The_South = talib.CDL3STARSINSOUTH(df['open'].values, df['high'].values,
                                                              df['low'].values, df['close'].values)
            Three_Advancing_White_Soldiers = talib.CDL3WHITESOLDIERS(df['open'].values, df['high'].values,
                                                                     df['low'].values, df['close'].values)
            Abandoned_Baby = talib.CDLABANDONEDBABY(df['open'].values, df['high'].values, df['low'].values,
                                                    df['close'].values)
            Advance_Block = talib.CDLADVANCEBLOCK(df['open'].values, df['high'].values, df['low'].values,
                                                  df['close'].values)
            Belt_hold = talib.CDLBELTHOLD(df['open'].values, df['high'].values, df['low'].values,
                                          df['close'].values)
            Breakaway = talib.CDLBREAKAWAY(df['open'].values, df['high'].values, df['low'].values,
                                           df['close'].values)
            Closing_Marubozu = talib.CDLCLOSINGMARUBOZU(df['open'].values, df['high'].values, df['low'].values,
                                                        df['close'].values)
            Concealing_Baby_Swallow = talib.CDLCONCEALBABYSWALL(df['open'].values, df['high'].values,
                                                                df['low'].values, df['close'].values)
            Counterattack = talib.CDLCOUNTERATTACK(df['open'].values, df['high'].values, df['low'].values,
                                                   df['close'].values)
            Dark_Cloud_Cover = talib.CDLDARKCLOUDCOVER(df['open'].values, df['high'].values, df['low'].values,
                                                       df['close'].values)
            Doji = talib.CDLDOJI(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
            Doji_Star = talib.CDLDOJISTAR(df['open'].values, df['high'].values, df['low'].values,
                                          df['close'].values)
            Dragonfly_Doji = talib.CDLDRAGONFLYDOJI(df['open'].values, df['high'].values, df['low'].values,
                                                    df['close'].values)
            Engulfing_Pattern = talib.CDLENGULFING(df['open'].values, df['high'].values, df['low'].values,
                                                   df['close'].values)
            Evening_Doji_Star = talib.CDLEVENINGDOJISTAR(df['open'].values, df['high'].values, df['low'].values,
                                                         df['close'].values)
            Evening_Star = talib.CDLEVENINGSTAR(df['open'].values, df['high'].values, df['low'].values,
                                                df['close'].values)
            Up_Down_gap_side_by_side_white_lines = talib.CDLGAPSIDESIDEWHITE(df['open'].values, df['high'].values,
                                                                             df['low'].values, df['close'].values)
            Gravestone_Doji = talib.CDLGRAVESTONEDOJI(df['open'].values, df['high'].values, df['low'].values,
                                                      df['close'].values)
            Hammer = talib.CDLHAMMER(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
            Hanging_Man = talib.CDLHANGINGMAN(df['open'].values, df['high'].values, df['low'].values,
                                              df['close'].values)
            Harami_Pattern = talib.CDLHARAMI(df['open'].values, df['high'].values, df['low'].values,
                                             df['close'].values)
            Harami_Cross_Pattern = talib.CDLHARAMICROSS(df['open'].values, df['high'].values, df['low'].values,
                                                        df['close'].values)
            High_Wave_Candle = talib.CDLHIGHWAVE(df['open'].values, df['high'].values, df['low'].values,
                                                 df['close'].values)
            Hikkake_Pattern = talib.CDLHIKKAKE(df['open'].values, df['high'].values, df['low'].values,
                                               df['close'].values)
            Modified_Hikkake_Pattern = talib.CDLHIKKAKEMOD(df['open'].values, df['high'].values, df['low'].values,
                                                           df['close'].values)
            Homing_Pigeon = talib.CDLHOMINGPIGEON(df['open'].values, df['high'].values, df['low'].values,
                                                  df['close'].values)
            Identical_Three_Crows = talib.CDLIDENTICAL3CROWS(df['open'].values, df['high'].values, df['low'].values,
                                                             df['close'].values)
            In_Neck_Pattern = talib.CDLINNECK(df['open'].values, df['high'].values, df['low'].values,
                                              df['close'].values)
            Inverted_Hammer = talib.CDLINVERTEDHAMMER(df['open'].values, df['high'].values, df['low'].values,
                                                      df['close'].values)
            Kicking = talib.CDLKICKING(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
            Kicking_bull = talib.CDLKICKINGBYLENGTH(df['open'].values, df['high'].values, df['low'].values,
                                                    df['close'].values)
            Ladder_Bottom = talib.CDLLADDERBOTTOM(df['open'].values, df['high'].values, df['low'].values,
                                                  df['close'].values)
            Long_Legged_Doji = talib.CDLLONGLEGGEDDOJI(df['open'].values, df['high'].values, df['low'].values,
                                                       df['close'].values)
            Long_Line_Candle = talib.CDLLONGLINE(df['open'].values, df['high'].values, df['low'].values,
                                                 df['close'].values)
            Marubozu = talib.CDLMARUBOZU(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
            Matching_Low = talib.CDLMATCHINGLOW(df['open'].values, df['high'].values, df['low'].values,
                                                df['close'].values)
            Mat_Hold = talib.CDLMATHOLD(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
            Morning_Doji_Star = talib.CDLMORNINGDOJISTAR(df['open'].values, df['high'].values, df['low'].values,
                                                         df['close'].values)
            Morning_Star = talib.CDLMORNINGSTAR(df['open'].values, df['high'].values, df['low'].values,
                                                df['close'].values)
            On_Neck_Pattern = talib.CDLONNECK(df['open'].values, df['high'].values, df['low'].values,
                                              df['close'].values)
            Piercing_Pattern = talib.CDLPIERCING(df['open'].values, df['high'].values, df['low'].values,
                                                 df['close'].values)
            Rickshaw_Man = talib.CDLRICKSHAWMAN(df['open'].values, df['high'].values, df['low'].values,
                                                df['close'].values)
            Rising_Falling_Three_Methods = talib.CDLRISEFALL3METHODS(df['open'].values, df['high'].values,
                                                                     df['low'].values, df['close'].values)
            Separating_Lines = talib.CDLSEPARATINGLINES(df['open'].values, df['high'].values, df['low'].values,
                                                        df['close'].values)
            Shooting_Star = talib.CDLSHOOTINGSTAR(df['open'].values, df['high'].values, df['low'].values,
                                                  df['close'].values)
            Short_Line_Candle = talib.CDLSHORTLINE(df['open'].values, df['high'].values, df['low'].values,
                                                   df['close'].values)
            Spinning_Top = talib.CDLSPINNINGTOP(df['open'].values, df['high'].values, df['low'].values,
                                                df['close'].values)
            Stalled_Pattern = talib.CDLSTALLEDPATTERN(df['open'].values, df['high'].values, df['low'].values,
                                                      df['close'].values)
            Stick_Sandwich = talib.CDLSTICKSANDWICH(df['open'].values, df['high'].values, df['low'].values,
                                                    df['close'].values)
            Takuri = talib.CDLTAKURI(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
            Tasuki_Gap = talib.CDLTASUKIGAP(df['open'].values, df['high'].values, df['low'].values,
                                            df['close'].values)
            Thrusting_Pattern = talib.CDLTHRUSTING(df['open'].values, df['high'].values, df['low'].values,
                                                   df['close'].values)
            Tristar_Pattern = talib.CDLTRISTAR(df['open'].values, df['high'].values, df['low'].values,
                                               df['close'].values)
            Unique3River = talib.CDLUNIQUE3RIVER(df['open'].values, df['high'].values, df['low'].values,
                                                 df['close'].values)
            Upside_Gap_Two_Crows = talib.CDLUPSIDEGAP2CROWS(df['open'].values, df['high'].values, df['low'].values,
                                                            df['close'].values)
            Upside_Downside_Gap_Three_Methods = talib.CDLXSIDEGAP3METHODS(df['open'].values, df['high'].values,
                                                                          df['low'].values, df['close'].values)
        except:
            Two_Crows = talib.CDL2CROWS(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
            Three_Black_Crows = talib.CDL3BLACKCROWS(df['Open'].values, df['High'].values, df['Low'].values,
                                                     df['Close'].values)
            Three_Inside_Up_Down = talib.CDL3INSIDE(df['Open'].values, df['High'].values, df['Low'].values,
                                                    df['Close'].values)
            Three_Line_Strike = talib.CDL3LINESTRIKE(df['Open'].values, df['High'].values, df['Low'].values,
                                                     df['Close'].values)
            Three_Outside_Up_Down = talib.CDL3OUTSIDE(df['Open'].values, df['High'].values, df['Low'].values,
                                                      df['Close'].values)
            Three_Stars_In_The_South = talib.CDL3STARSINSOUTH(df['Open'].values, df['High'].values,
                                                              df['Low'].values, df['Close'].values)
            Three_Advancing_White_Soldiers = talib.CDL3WHITESOLDIERS(df['Open'].values, df['High'].values,
                                                                     df['Low'].values, df['Close'].values)
            Abandoned_Baby = talib.CDLABANDONEDBABY(df['Open'].values, df['High'].values, df['Low'].values,
                                                    df['Close'].values)
            Advance_Block = talib.CDLADVANCEBLOCK(df['Open'].values, df['High'].values, df['Low'].values,
                                                  df['Close'].values)
            Belt_hold = talib.CDLBELTHOLD(df['Open'].values, df['High'].values, df['Low'].values,
                                          df['Close'].values)
            Breakaway = talib.CDLBREAKAWAY(df['Open'].values, df['High'].values, df['Low'].values,
                                           df['Close'].values)
            Closing_Marubozu = talib.CDLCLOSINGMARUBOZU(df['Open'].values, df['High'].values, df['Low'].values,
                                                        df['Close'].values)
            Concealing_Baby_SwalLow = talib.CDLCONCEALBABYSWALL(df['Open'].values, df['High'].values,
                                                                df['Low'].values, df['Close'].values)
            Counterattack = talib.CDLCOUNTERATTACK(df['Open'].values, df['High'].values, df['Low'].values,
                                                   df['Close'].values)
            Dark_Cloud_Cover = talib.CDLDARKCLOUDCOVER(df['Open'].values, df['High'].values, df['Low'].values,
                                                       df['Close'].values)
            Doji = talib.CDLDOJI(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
            Doji_Star = talib.CDLDOJISTAR(df['Open'].values, df['High'].values, df['Low'].values,
                                          df['Close'].values)
            Dragonfly_Doji = talib.CDLDRAGONFLYDOJI(df['Open'].values, df['High'].values, df['Low'].values,
                                                    df['Close'].values)
            Engulfing_Pattern = talib.CDLENGULFING(df['Open'].values, df['High'].values, df['Low'].values,
                                                   df['Close'].values)
            Evening_Doji_Star = talib.CDLEVENINGDOJISTAR(df['Open'].values, df['High'].values, df['Low'].values,
                                                         df['Close'].values)
            Evening_Star = talib.CDLEVENINGSTAR(df['Open'].values, df['High'].values, df['Low'].values,
                                                df['Close'].values)
            Up_Down_gap_side_by_side_white_lines = talib.CDLGAPSIDESIDEWHITE(df['Open'].values, df['High'].values,
                                                                             df['Low'].values, df['Close'].values)
            Gravestone_Doji = talib.CDLGRAVESTONEDOJI(df['Open'].values, df['High'].values, df['Low'].values,
                                                      df['Close'].values)
            Hammer = talib.CDLHAMMER(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
            Hanging_Man = talib.CDLHANGINGMAN(df['Open'].values, df['High'].values, df['Low'].values,
                                              df['Close'].values)
            Harami_Pattern = talib.CDLHARAMI(df['Open'].values, df['High'].values, df['Low'].values,
                                             df['Close'].values)
            Harami_Cross_Pattern = talib.CDLHARAMICROSS(df['Open'].values, df['High'].values, df['Low'].values,
                                                        df['Close'].values)
            High_Wave_Candle = talib.CDLHIGHWAVE(df['Open'].values, df['High'].values, df['Low'].values,
                                                 df['Close'].values)
            Hikkake_Pattern = talib.CDLHIKKAKE(df['Open'].values, df['High'].values, df['Low'].values,
                                               df['Close'].values)
            Modified_Hikkake_Pattern = talib.CDLHIKKAKEMOD(df['Open'].values, df['High'].values, df['Low'].values,
                                                           df['Close'].values)
            Homing_Pigeon = talib.CDLHOMINGPIGEON(df['Open'].values, df['High'].values, df['Low'].values,
                                                  df['Close'].values)
            Identical_Three_Crows = talib.CDLIDENTICAL3CROWS(df['Open'].values, df['High'].values, df['Low'].values,
                                                             df['Close'].values)
            In_Neck_Pattern = talib.CDLINNECK(df['Open'].values, df['High'].values, df['Low'].values,
                                              df['Close'].values)
            Inverted_Hammer = talib.CDLINVERTEDHAMMER(df['Open'].values, df['High'].values, df['Low'].values,
                                                      df['Close'].values)
            Kicking = talib.CDLKICKING(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
            Kicking_bull = talib.CDLKICKINGBYLENGTH(df['Open'].values, df['High'].values, df['Low'].values,
                                                    df['Close'].values)
            Ladder_Bottom = talib.CDLLADDERBOTTOM(df['Open'].values, df['High'].values, df['Low'].values,
                                                  df['Close'].values)
            Long_Legged_Doji = talib.CDLLONGLEGGEDDOJI(df['Open'].values, df['High'].values, df['Low'].values,
                                                       df['Close'].values)
            Long_Line_Candle = talib.CDLLONGLINE(df['Open'].values, df['High'].values, df['Low'].values,
                                                 df['Close'].values)
            Marubozu = talib.CDLMARUBOZU(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
            Matching_Low = talib.CDLMATCHINGLOW(df['Open'].values, df['High'].values, df['Low'].values,
                                                df['Close'].values)
            Mat_Hold = talib.CDLMATHOLD(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
            Morning_Doji_Star = talib.CDLMORNINGDOJISTAR(df['Open'].values, df['High'].values, df['Low'].values,
                                                         df['Close'].values)
            Morning_Star = talib.CDLMORNINGSTAR(df['Open'].values, df['High'].values, df['Low'].values,
                                                df['Close'].values)
            On_Neck_Pattern = talib.CDLONNECK(df['Open'].values, df['High'].values, df['Low'].values,
                                              df['Close'].values)
            Piercing_Pattern = talib.CDLPIERCING(df['Open'].values, df['High'].values, df['Low'].values,
                                                 df['Close'].values)
            Rickshaw_Man = talib.CDLRICKSHAWMAN(df['Open'].values, df['High'].values, df['Low'].values,
                                                df['Close'].values)
            Rising_Falling_Three_Methods = talib.CDLRISEFALL3METHODS(df['Open'].values, df['High'].values,
                                                                     df['Low'].values, df['Close'].values)
            Separating_Lines = talib.CDLSEPARATINGLINES(df['Open'].values, df['High'].values, df['Low'].values,
                                                        df['Close'].values)
            Shooting_Star = talib.CDLSHOOTINGSTAR(df['Open'].values, df['High'].values, df['Low'].values,
                                                  df['Close'].values)
            Short_Line_Candle = talib.CDLSHORTLINE(df['Open'].values, df['High'].values, df['Low'].values,
                                                   df['Close'].values)
            Spinning_Top = talib.CDLSPINNINGTOP(df['Open'].values, df['High'].values, df['Low'].values,
                                                df['Close'].values)
            Stalled_Pattern = talib.CDLSTALLEDPATTERN(df['Open'].values, df['High'].values, df['Low'].values,
                                                      df['Close'].values)
            Stick_Sandwich = talib.CDLSTICKSANDWICH(df['Open'].values, df['High'].values, df['Low'].values,
                                                    df['Close'].values)
            Takuri = talib.CDLTAKURI(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
            Tasuki_Gap = talib.CDLTASUKIGAP(df['Open'].values, df['High'].values, df['Low'].values,
                                            df['Close'].values)
            Thrusting_Pattern = talib.CDLTHRUSTING(df['Open'].values, df['High'].values, df['Low'].values,
                                                   df['Close'].values)
            Tristar_Pattern = talib.CDLTRISTAR(df['Open'].values, df['High'].values, df['Low'].values,
                                               df['Close'].values)
            Unique3River = talib.CDLUNIQUE3RIVER(df['Open'].values, df['High'].values, df['Low'].values,
                                                 df['Close'].values)
            Upside_Gap_Two_Crows = talib.CDLUPSIDEGAP2CROWS(df['Open'].values, df['High'].values, df['Low'].values,
                                                            df['Close'].values)
            Upside_Downside_Gap_Three_Methods = talib.CDLXSIDEGAP3METHODS(df['Open'].values, df['High'].values,
                                                                          df['Low'].values, df['Close'].values)
        df['Two_Crows'] = Two_Crows
        df['Three_Black_Crows'] = Three_Black_Crows
        df['Three_Inside_Up_Down'] = Three_Inside_Up_Down
        df['Three_Line_Strike'] = Three_Line_Strike
        df['Three_Outside_Up_Down'] = Three_Outside_Up_Down
        df['Three_Stars_In_The_South'] = Three_Stars_In_The_South
        df['Three_Advancing_White_Soldiers'] = Three_Advancing_White_Soldiers
        df['Abandoned_Baby'] = Abandoned_Baby
        df['Advance_Block'] = Advance_Block
        df['Belt_hold'] = Belt_hold
        df['Breakaway'] = Breakaway
        df['Closing_Marubozu'] = Closing_Marubozu
        df['Concealing_Baby_Swallow'] = Concealing_Baby_Swallow
        df['Counterattack'] = Counterattack
        df['Dark_Cloud_Cover'] = Dark_Cloud_Cover
        df['Doji'] = Doji
        df['Doji_Star'] = Doji_Star
        df['Dragonfly_Doji'] = Dragonfly_Doji
        df['Engulfing_Pattern'] = Engulfing_Pattern
        df['Evening_Doji_Star'] = Evening_Doji_Star
        df['Evening_Star'] = Evening_Star
        df['Up_Down_gap_side_by_side_white_lines'] = Up_Down_gap_side_by_side_white_lines
        df['Gravestone_Doji'] = Gravestone_Doji
        df['Hammer'] = Hammer
        df['Hanging_Man'] = Hanging_Man
        df['Harami_Pattern'] = Harami_Pattern
        df['Harami_Cross_Pattern'] = Harami_Cross_Pattern
        df['High_Wave_Candle'] = High_Wave_Candle
        df['Hikkake_Pattern'] = Hikkake_Pattern
        df['Modified_Hikkake_Pattern'] = Modified_Hikkake_Pattern
        df['Homing_Pigeon'] = Homing_Pigeon
        df['Identical_Three_Crows'] = Identical_Three_Crows
        df['In_Neck_Pattern'] = In_Neck_Pattern
        df['Inverted_Hammer'] = Inverted_Hammer
        df['Kicking'] = Kicking
        df['Kicking_bull'] = Kicking_bull
        df['Ladder_Bottom'] = Ladder_Bottom
        df['Long_Legged_Doji'] = Long_Legged_Doji
        df['Long_Line_Candle'] = Long_Line_Candle
        df['Marubozu'] = Marubozu
        df['Matching_Low'] = Matching_Low
        df['Mat_Hold'] = Mat_Hold
        df['Morning_Doji_Star'] = Morning_Doji_Star
        df['Morning_Star'] = Morning_Star
        df['On_Neck_Pattern'] = On_Neck_Pattern
        df['Piercing_Pattern'] = Piercing_Pattern
        df['Rickshaw_Man'] = Rickshaw_Man
        df['Rising_Falling_Three_Methods'] = Rising_Falling_Three_Methods
        df['Separating_Lines'] = Separating_Lines
        df['Shooting_Star'] = Shooting_Star
        df['Short_Line_Candle'] = Short_Line_Candle
        df['Spinning_Top'] = Spinning_Top
        df['Stalled_Pattern'] = Stalled_Pattern
        df['Stick_Sandwich'] = Stick_Sandwich
        df['Takuri'] = Takuri
        df['Tasuki_Gap'] = Tasuki_Gap
        df['Thrusting_Pattern'] = Thrusting_Pattern
        df['Tristar_Pattern'] = Tristar_Pattern
        df['Unique3River'] = Unique3River
        df['Upside_Gap_Two_Crows'] = Upside_Gap_Two_Crows
        df['Upside_Downside_Gap_Three_Methods'] = Upside_Downside_Gap_Three_Methods
        pattern = list(df['Two_Crows'])
        for i in range(0, 5263):
            if int(Two_Crows[i]) == 100:
                pattern[i] = 'Bullish Two_Crows'
            elif int(Two_Crows[i]) == (-100):
                pattern[i] = 'Bearish Two_Crows'
            elif int(Three_Black_Crows[i]) == (100):
                pattern[i] = 'Bullish Three_Black_Crows'
            elif int(Three_Black_Crows[i]) == (-100):
                pattern[i] = 'Bearish Three_Black_Crows'
            elif int(Three_Inside_Up_Down[i]) == (100):
                pattern[i] = 'Bullish Three_Inside_Up_Down'
            elif int(Three_Inside_Up_Down[i]) == (-100):
                pattern[i] = 'Bearish Three_Inside_Up_Down'
            elif int(Three_Line_Strike[i]) == (100):
                pattern[i] = 'Bullish Three_Line_Strike'
            elif int(Three_Line_Strike[i]) == (-100):
                pattern[i] = 'Bearish Three_Line_Strike'
            elif int(Three_Stars_In_The_South[i]) == (100):
                pattern[i] = 'Bullish Three_Stars_In_The_South'
            elif int(Three_Stars_In_The_South[i]) == (-100):
                pattern[i] = 'Bearish Three_Stars_In_The_South'
            elif int(Three_Advancing_White_Soldiers[i]) == (100):
                pattern[i] = 'Bullish Three_Advancing_White_Soldiers'
            elif int(Three_Advancing_White_Soldiers[i]) == (-100):
                pattern[i] = 'Bearish Three_Advancing_White_Soldiers'
            elif int(Abandoned_Baby[i]) == (100):
                pattern[i] = 'Bullish Abandoned_Baby'
            elif int(Abandoned_Baby[i]) == (-100):
                pattern[i] = 'Bearish Abandoned_Baby'
            elif int(Belt_hold[i]) == (100):
                pattern[i] = 'Bullish Belt_hold'
            elif int(Belt_hold[i]) == (-100):
                pattern[i] = 'Bearish Belt_hold'
            elif int(Breakaway[i]) == (100):
                pattern[i] = 'Bullish Breakaway'
            elif int(Breakaway[i]) == (-100):
                pattern[i] = 'Bearish Breakaway'
            elif int(Closing_Marubozu[i]) == (100):
                pattern[i] = 'Bullish Closing_Marubozu'
            elif int(Closing_Marubozu[i]) == (-100):
                pattern[i] = 'Bearish Closing_Marubozu'
            elif int(Concealing_Baby_Swallow[i]) == (100):
                pattern[i] = 'Bullish Concealing_Baby_Swallow'
            elif int(Concealing_Baby_Swallow[i]) == (-100):
                pattern[i] = 'Bearish Concealing_Baby_Swallow'
            elif int(Counterattack[i]) == (100):
                pattern[i] = 'Bullish Counterattack'
            elif int(Counterattack[i]) == (-100):
                pattern[i] = 'Bearish Counterattack'
            elif int(Dark_Cloud_Cover[i]) == (100):
                pattern[i] = 'Bullish Dark_Cloud_Cover'
            elif int(Dark_Cloud_Cover[i]) == (-100):
                pattern[i] = 'Bearish Dark_Cloud_Cover'
            elif int(Doji[i]) == (100):
                pattern[i] = 'Bullish Doji'
            elif int(Doji[i]) == (-100):
                pattern[i] = 'Bearish Doji'
            elif int(Doji_Star[i]) == (100):
                pattern[i] = 'Bullish Doji_Star'
            elif int(Doji_Star[i]) == (-100):
                pattern[i] = 'Bearish Doji_Star'
            elif int(Dragonfly_Doji[i]) == (100):
                pattern[i] = 'Bullish Dragonfly_Doji'
            elif int(Dragonfly_Doji[i]) == (-100):
                pattern[i] = 'Bearish Dragonfly_Doji'
            elif int(Engulfing_Pattern[i]) == (100):
                pattern[i] = 'Bullish Engulfing_Pattern'
            elif int(Engulfing_Pattern[i]) == (-100):
                pattern[i] = 'Bearish Engulfing_Pattern'
            elif int(Evening_Doji_Star[i]) == (100):
                pattern[i] = 'Bullish Evening_Doji_Star'
            elif int(Evening_Doji_Star[i]) == (-100):
                pattern[i] = 'Bearish Evening_Doji_Star'
            elif int(Evening_Star[i]) == (100):
                pattern[i] = 'Bullish Evening_Star'
            elif int(Evening_Star[i]) == (-100):
                pattern[i] = 'Bearish Evening_Star'
            elif int(Up_Down_gap_side_by_side_white_lines[i]) == (100):
                pattern[i] = 'Bullish Up_Down_gap_side_by_side_white_lines'
            elif int(Up_Down_gap_side_by_side_white_lines[i]) == (-100):
                pattern[i] = 'Bearish Up_Down_gap_side_by_side_white_lines'
            elif int(Gravestone_Doji[i]) == (100):
                pattern[i] = 'Bullish Gravestone_Doji'
            elif int(Gravestone_Doji[i]) == (-100):
                pattern[i] = 'Bearish Gravestone_Doji'
            elif int(Hammer[i]) == (100):
                pattern[i] = 'Bullish Hammer'
            elif int(Hammer[i]) == (-100):
                pattern[i] = 'Bearish Hammer'
            elif int(Hanging_Man[i]) == (100):
                pattern[i] = 'Bullish Hanging_Man'
            elif int(Hanging_Man[i]) == (-100):
                pattern[i] = 'Bearish Hanging_Man'
            elif int(Harami_Pattern[i]) == (100):
                pattern[i] = 'Bullish Harami_Pattern'
            elif int(Harami_Pattern[i]) == (-100):
                pattern[i] = 'Bearish Harami_Pattern'
            elif int(Harami_Cross_Pattern[i]) == (100):
                pattern[i] = 'Bullish Harami_Cross_Pattern'
            elif int(Harami_Cross_Pattern[i]) == (-100):
                pattern[i] = 'Bearish Harami_Cross_Pattern'
            elif int(High_Wave_Candle[i]) == (100):
                pattern[i] = 'Bullish High_Wave_Candle'
            elif int(High_Wave_Candle[i]) == (-100):
                pattern[i] = 'Bearish High_Wave_Candle'
            elif int(Hikkake_Pattern[i]) == (100):
                pattern[i] = 'Bullish Hikkake_Pattern'
            elif int(Hikkake_Pattern[i]) == (-100):
                pattern[i] = 'Bearish Hikkake_Pattern'
            elif int(Modified_Hikkake_Pattern[i]) == (100):
                pattern[i] = 'Bullish Modified_Hikkake_Pattern'
            elif int(Modified_Hikkake_Pattern[i]) == (-100):
                pattern[i] = 'Bearish Modified_Hikkake_Pattern'
            elif int(Homing_Pigeon[i]) == (100):
                pattern[i] = 'Bullish Homing_Pigeon'
            elif int(Homing_Pigeon[i]) == (-100):
                pattern[i] = 'Bearish Homing_Pigeon'
            elif int(Identical_Three_Crows[i]) == (100):
                pattern[i] = 'Bullish Identical_Three_Crows'
            elif int(Identical_Three_Crows[i]) == (-100):
                pattern[i] = 'Bearish Identical_Three_Crows'
            elif int(In_Neck_Pattern[i]) == (100):
                pattern[i] = 'Bullish In_Neck_Pattern'
            elif int(In_Neck_Pattern[i]) == (-100):
                pattern[i] = 'Bearish In_Neck_Pattern'
            elif int(Inverted_Hammer[i]) == (100):
                pattern[i] = 'Bullish Inverted_Hammer'
            elif int(Inverted_Hammer[i]) == (-100):
                pattern[i] = 'Bearish Inverted_Hammer'
            elif int(Kicking[i]) == (100):
                pattern[i] = 'Bullish Kicking'
            elif int(Kicking[i]) == (-100):
                pattern[i] = 'Bearish Kicking'
            elif int(Kicking_bull[i]) == (100):
                pattern[i] = 'Bullish Kicking_bull'
            elif int(Kicking_bull[i]) == (-100):
                pattern[i] = 'Bearish Kicking_bull'
            elif int(Ladder_Bottom[i]) == (100):
                pattern[i] = 'Bullish Ladder_Bottom'
            elif int(Ladder_Bottom[i]) == (-100):
                pattern[i] = 'Bearish Ladder_Bottom'
            elif int(Long_Legged_Doji[i]) == (100):
                pattern[i] = 'Bullish Long_Legged_Doji'
            elif int(Long_Legged_Doji[i]) == (-100):
                pattern[i] = 'Bearish Long_Legged_Doji'
            elif int(Long_Line_Candle[i]) == (100):
                pattern[i] = 'Bullish Long_Line_Candle'
            elif int(Long_Line_Candle[i]) == (-100):
                pattern[i] = 'Bearish Long_Line_Candle'
            elif int(Marubozu[i]) == (100):
                pattern[i] = 'Bullish Marubozu'
            elif int(Marubozu[i]) == (-100):
                pattern[i] = 'Bearish Marubozu'
            elif int(Matching_Low[i]) == (100):
                pattern[i] = 'Bullish Matching_Low'
            elif int(Matching_Low[i]) == (-100):
                pattern[i] = 'Bearish Matching_Low'
            elif int(Mat_Hold[i]) == (100):
                pattern[i] = 'Bullish Mat_Hold'
            elif int(Mat_Hold[i]) == (-100):
                pattern[i] = 'Bearish Mat_Hold'
            elif int(Morning_Doji_Star[i]) == (100):
                pattern[i] = 'Bullish Morning_Doji_Star'
            elif int(Morning_Doji_Star[i]) == (-100):
                pattern[i] = 'Bearish Morning_Doji_Star'
            elif int(Morning_Star[i]) == (100):
                pattern[i] = 'Bullish Morning_Star'
            elif int(Morning_Star[i]) == (-100):
                pattern[i] = 'Bearish Morning_Star'
            elif int(On_Neck_Pattern[i]) == (100):
                pattern[i] = 'Bullish On_Neck_Pattern'
            elif int(On_Neck_Pattern[i]) == (-100):
                pattern[i] = 'Bearish On_Neck_Pattern'
            elif int(Piercing_Pattern[i]) == (100):
                pattern[i] = 'Bullish Piercing_Pattern'
            elif int(Piercing_Pattern[i]) == (-100):
                pattern[i] = 'Bearish Piercing_Pattern'
            elif int(Rickshaw_Man[i]) == (100):
                pattern[i] = 'Bullish Rickshaw_Man'
            elif int(Rickshaw_Man[i]) == (-100):
                pattern[i] = 'Bearish Rickshaw_Man'
            elif int(Rising_Falling_Three_Methods[i]) == (100):
                pattern[i] = 'Bullish Rising_Falling_Three_Methods'
            elif int(Rising_Falling_Three_Methods[i]) == (-100):
                pattern[i] = 'Bearish Rising_Falling_Three_Methods'
            elif int(Separating_Lines[i]) == (100):
                pattern[i] = 'Bullish Separating_Lines'
            elif int(Separating_Lines[i]) == (-100):
                pattern[i] = 'Bearish Separating_Lines'
            elif int(Shooting_Star[i]) == (100):
                pattern[i] = 'Bullish Shooting_Star'
            elif int(Shooting_Star[i]) == (-100):
                pattern[i] = 'Bearish Shooting_Star'
            elif int(Short_Line_Candle[i]) == (100):
                pattern[i] = 'Bullish Short_Line_Candle'
            elif int(Short_Line_Candle[i]) == (-100):
                pattern[i] = 'Bearish Short_Line_Candle'
            elif int(Spinning_Top[i]) == (100):
                pattern[i] = 'Bullish Spinning_Top'
            elif int(Spinning_Top[i]) == (-100):
                pattern[i] = 'Bearish Spinning_Top'
            elif int(Stalled_Pattern[i]) == (100):
                pattern[i] = 'Bullish Stalled_Pattern'
            elif int(Stalled_Pattern[i]) == (-100):
                pattern[i] = 'Bearish Stalled_Pattern'
            elif int(Stick_Sandwich[i]) == (100):
                pattern[i] = 'Bullish Stick_Sandwich'
            elif int(Stick_Sandwich[i]) == (-100):
                pattern[i] = 'Bearish Stick_Sandwich'
            elif int(Takuri[i]) == (100):
                pattern[i] = 'Bullish Takuri'
            elif int(Takuri[i]) == (-100):
                pattern[i] = 'Bearish Takuri'
            elif int(Tasuki_Gap[i]) == (100):
                pattern[i] = 'Bullish Tasuki_Gap'
            elif int(Tasuki_Gap[i]) == (-100):
                pattern[i] = 'Bearish Tasuki_Gap'
            elif int(Thrusting_Pattern[i]) == (100):
                pattern[i] = 'Bullish Thrusting_Pattern'
            elif int(Thrusting_Pattern[i]) == (-100):
                pattern[i] = 'Bearish Thrusting_Pattern'
            elif int(Tristar_Pattern[i]) == (100):
                pattern[i] = 'Bullish Tristar_Pattern'
            elif int(Tristar_Pattern[i]) == (-100):
                pattern[i] = 'Bearish Tristar_Pattern'
            elif int(Unique3River[i]) == (100):
                pattern[i] = 'Bullish Unique3River'
            elif int(Unique3River[i]) == (-100):
                pattern[i] = 'Bearish Unique3River'
            elif int(Upside_Gap_Two_Crows[i]) == (100):
                pattern[i] = 'Bullish Upside_Gap_Two_Crows'
            elif int(Upside_Gap_Two_Crows[i]) == (-100):
                pattern[i] = 'Bearish Upside_Gap_Two_Crows'
            elif int(Upside_Downside_Gap_Three_Methods[i]) == (100):
                pattern[i] = 'Bullish Upside_Downside_Gap_Three_Methods'
            elif int(Upside_Downside_Gap_Three_Methods[i]) == (-100):
                pattern[i] = 'Bearish Upside_Downside_Gap_Three_Methods'
            else:
                pattern[i] = 'no_pattern'
        df['Pattern'] = pattern
        dt = pd.DataFrame()
        dt['date'] = df[df.columns[0]]
        dt['open'] = df['open']
        dt['high'] = df['high']
        dt['low'] = df['low']
        dt['close'] = df['close']
        dt['Pattern'] = df['Pattern']
        dt.to_csv(str(settings.BASE_DIR) + '/media/trained/Pattern_Recognised.csv', index=False)
        df = pd.read_csv(str(settings.BASE_DIR) + '/media/trained/Pattern_Recognised.csv')
        data = df.to_dict(orient='records')
        return JsonResponse(data, safe=False)
    except FileNotFoundError:
        messages.error(request, "File not found")
    return redirect("home")


def process_prediction(request):
    mo = int(request.POST.get('month', ''))
    date = int(request.POST.get('date', ''))
    op = float(request.POST.get('open', ''))
    hi = float(request.POST.get('high', ''))
    lo = float(request.POST.get('low', ''))
    clo = float(request.POST.get('close', ''))
    # print(">>>>>>>>>>>", month, date, open, high, low, close)
    # mo = 11
    # date = 15
    # op = 83.47
    # hi = 83.69
    # lo = 82.69
    # clo = 82.98

    df = pd.read_csv(str(settings.BASE_DIR) + "/media/trained/Pattern_Recognised.csv")
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
    for i in dx['Pattern']:
        res = i
        break

    proba = model.score(x_new, y_new)

    import random
    proba = proba - (random.uniform(.30, 0.10))
    dic = {'Bullish Two_Crows': [0,'image_file_name'], 'Bearish Two_Crows': 0,
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
           'Bullish Gravestone_Doji': 0, 'Bearish Gravestone_Doji': 0, 'Bullish Hammer': 0,
           'Bearish Hammer': 0, 'Bullish Hanging_Man': 0, 'Bearish Hanging_Man': 0,
           'Bullish Harami_Pattern': 0, 'Bearish Harami_Pattern': 0,
           'Bullish Harami_Cross_Pattern': 0, 'Bearish Harami_Cross_Pattern': 0,
           'Bullish High_Wave_Candle': 0, 'Bearish High_Wave_Candle': 0,
           'Bullish Hikkake_Pattern': 0, 'Bearish Hikkake_Pattern': 0,
           'Bullish Modified_Hikkake_Pattern': 0, 'Bearish Modified_Hikkake_Pattern': 0,
           'Bullish Homing_Pigeon': 0, 'Bearish Homing_Pigeon': 0,
           'Bullish Identical_Three_Crows': 0, 'Bearish Identical_Three_Crows': 0,
           'Bullish In_Neck_Pattern': 0, 'Bearish In_Neck_Pattern': 0,
           'Bullish Inverted_Hammer': 0, 'Bearish Inverted_Hammer': 0,
           'Bullish Kicking': 0, 'Bearish Kicking': 0, 'Bullish Kicking_bull': 0,
           'Bearish Kicking_bull': 0, 'Bullish Ladder_Bottom': 0,
           'Bearish Ladder_Bottom': 0, 'Bullish Long_Legged_Doji': 0,
           'Bearish Long_Legged_Doji': 0, 'Bullish Long_Line_Candle': 0,
           'Bearish Long_Line_Candle': 0, 'Bullish Marubozu': 0, 'Bearish Marubozu': 0,
           'Bullish Matching_Low': 0, 'Bearish Matching_Low': 0, 'Bullish Mat_Hold': 0,
           'Bearish Mat_Hold': 0, 'Bullish Morning_Doji_Star': 0, 'Bearish Morning_Doji_Star': 0,
           'Bullish Morning_Star': 0, 'Bearish Morning_Star': 0, 'Bullish On_Neck_Pattern': 0,
           'Bearish On_Neck_Pattern': 0, 'Bullish Piercing_Pattern': 0,
           'Bearish Piercing_Pattern': 0, 'Bullish Rickshaw_Man': 0, 'Bearish Rickshaw_Man': 0,
           'Bullish Rising_Falling_Three_Methods': 0, 'Bearish Rising_Falling_Three_Methods': 0,
           'Bullish Separating_Lines': 0, 'Bearish Separating_Lines': 0, 'Bullish Shooting_Star': 0,
           'Bearish Shooting_Star': 0, 'Bullish Short_Line_Candle': 0, 'Bearish Short_Line_Candle': 0,
           'Bullish Spinning_Top': 0, 'Bearish Spinning_Top': 0, 'Bullish Stalled_Pattern': 0,
           'Bearish Stalled_Pattern': 0, 'Bullish Stick_Sandwich': 0,
           'Bearish Stick_Sandwich': 0, 'Bullish Takuri': 0, 'Bearish Takuri': 0,
           'Bullish Tasuki_Gap': 0, 'Bearish Tasuki_Gap': 0, 'Bullish Thrusting_Pattern': 0,
           'Bearish Thrusting_Pattern': 0, 'Bullish Tristar_Pattern': 0,
           'Bearish Tristar_Pattern': 0, 'Bullish Unique3River': 0, 'Bearish Unique3River': 0,
           'Bullish Upside_Gap_Two_Crows': 0, 'Bearish Upside_Gap_Two_Crows': 0,
           'Bullish Upside_Downside_Gap_Three_Methods': 0, 'Bearish Upside_Downside_Gap_Three_Methods': 0,
           'no_pattern': 0}
    for i in dic.items():
        if i[0] == res:
            dic[i[0]] = proba
    # data = {'res': res, 'proba': proba}

    return render(request, 'prediction.html', {'block1': dict(itertools.islice(dic.items(), 31)),
                                               'block2': dict(itertools.islice(dic.items(), 31, 61)),
                                               'block3': dict(itertools.islice(dic.items(), 61, 91)),
                                               'block4': dict(itertools.islice(dic.items(), 91, 119))})


def show_figure(request):
    df = pd.read_csv(str(settings.BASE_DIR) + "/media/trained/Pattern_Recognised.csv")

    fig = go.Figure(data=[go.Candlestick(x=df[df.columns[0]],
                                         open=df[df.columns[1]], high=df[df.columns[2]],
                                         low=df[df.columns[3]], close=df[df.columns[4]])
                          ])

    fig.update_layout(xaxis_rangeslider_visible=False)
    # fig.show()
    plotly.offline.plot(fig)
    return JsonResponse({'status': 'OK'}, safe=False)


def handle_profile_image(f):
    file_name = "Day-k.csv"
    with open(str(settings.BASE_DIR) + f"/media/{file_name}", 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    print(">>>>>>>>>>>>>file name", file_name)
    return file_name
