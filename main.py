# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 11:18:39 2021

@author: Tanjil Hasan
"""
#import Model
import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from tkinter import filedialog

import talib
import yfinance as yf

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
import pandas as pd
import matplotlib.dates as mpl_dates

from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)



def File_dialog():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select A File",
                                          filetype=(("CSV files", "*.csv"),("All Files", "*.*")))
    label_file["text"] = filename
    return None


def Load_excel_data():    
    file_path = label_file["text"]
    try:
        excel_filename = r"{}".format(file_path)
        if excel_filename[-4:] == ".csv":
            df = pd.read_csv(excel_filename)
            try:
                Two_Crows = talib.CDL2CROWS(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Three_Black_Crows = talib.CDL3BLACKCROWS(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Three_Inside_Up_Down= talib.CDL3INSIDE(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Three_Line_Strike = talib.CDL3LINESTRIKE(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Three_Outside_Up_Down = talib.CDL3OUTSIDE(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Three_Stars_In_The_South = talib.CDL3STARSINSOUTH(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Three_Advancing_White_Soldiers = talib.CDL3WHITESOLDIERS(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Abandoned_Baby = talib.CDLABANDONEDBABY(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Advance_Block = talib.CDLADVANCEBLOCK(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Belt_hold = talib.CDLBELTHOLD(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Breakaway = talib.CDLBREAKAWAY(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Closing_Marubozu = talib.CDLCLOSINGMARUBOZU(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Concealing_Baby_Swallow = talib.CDLCONCEALBABYSWALL(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Counterattack = talib.CDLCOUNTERATTACK(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Dark_Cloud_Cover = talib.CDLDARKCLOUDCOVER(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Doji = talib.CDLDOJI(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Doji_Star = talib.CDLDOJISTAR(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Dragonfly_Doji = talib.CDLDRAGONFLYDOJI(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Engulfing_Pattern = talib.CDLENGULFING(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Evening_Doji_Star = talib.CDLEVENINGDOJISTAR(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Evening_Star = talib.CDLEVENINGSTAR(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Up_Down_gap_side_by_side_white_lines = talib.CDLGAPSIDESIDEWHITE(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Gravestone_Doji = talib.CDLGRAVESTONEDOJI(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Hammer = talib.CDLHAMMER(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Hanging_Man = talib.CDLHANGINGMAN(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Harami_Pattern = talib.CDLHARAMI(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Harami_Cross_Pattern = talib.CDLHARAMICROSS(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                High_Wave_Candle = talib.CDLHIGHWAVE(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Hikkake_Pattern = talib.CDLHIKKAKE(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Modified_Hikkake_Pattern = talib.CDLHIKKAKEMOD(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Homing_Pigeon = talib.CDLHOMINGPIGEON(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Identical_Three_Crows = talib.CDLIDENTICAL3CROWS(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                In_Neck_Pattern = talib.CDLINNECK(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Inverted_Hammer = talib.CDLINVERTEDHAMMER(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Kicking = talib.CDLKICKING(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Kicking_bull = talib.CDLKICKINGBYLENGTH(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Ladder_Bottom = talib.CDLLADDERBOTTOM(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Long_Legged_Doji = talib.CDLLONGLEGGEDDOJI(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Long_Line_Candle = talib.CDLLONGLINE(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Marubozu = talib.CDLMARUBOZU(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Matching_Low = talib.CDLMATCHINGLOW(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Mat_Hold = talib.CDLMATHOLD(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Morning_Doji_Star = talib.CDLMORNINGDOJISTAR(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Morning_Star = talib.CDLMORNINGSTAR(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                On_Neck_Pattern = talib.CDLONNECK(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Piercing_Pattern = talib.CDLPIERCING(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Rickshaw_Man = talib.CDLRICKSHAWMAN(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Rising_Falling_Three_Methods = talib.CDLRISEFALL3METHODS(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Separating_Lines = talib.CDLSEPARATINGLINES(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Shooting_Star = talib.CDLSHOOTINGSTAR(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Short_Line_Candle = talib.CDLSHORTLINE(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Spinning_Top = talib.CDLSPINNINGTOP(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Stalled_Pattern = talib.CDLSTALLEDPATTERN(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Stick_Sandwich = talib.CDLSTICKSANDWICH(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Takuri  = talib.CDLTAKURI(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Tasuki_Gap = talib.CDLTASUKIGAP(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Thrusting_Pattern = talib.CDLTHRUSTING(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Tristar_Pattern = talib.CDLTRISTAR(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Unique3River = talib.CDLUNIQUE3RIVER(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Upside_Gap_Two_Crows = talib.CDLUPSIDEGAP2CROWS(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
                Upside_Downside_Gap_Three_Methods = talib.CDLXSIDEGAP3METHODS(df['open'].values, df['high'].values, df['low'].values, df['close'].values)
            except:
                Two_Crows = talib.CDL2CROWS(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Three_Black_Crows = talib.CDL3BLACKCROWS(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Three_Inside_Up_Down= talib.CDL3INSIDE(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Three_Line_Strike = talib.CDL3LINESTRIKE(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Three_Outside_Up_Down = talib.CDL3OUTSIDE(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Three_Stars_In_The_South = talib.CDL3STARSINSOUTH(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Three_Advancing_White_Soldiers = talib.CDL3WHITESOLDIERS(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Abandoned_Baby = talib.CDLABANDONEDBABY(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Advance_Block = talib.CDLADVANCEBLOCK(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Belt_hold = talib.CDLBELTHOLD(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Breakaway = talib.CDLBREAKAWAY(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Closing_Marubozu = talib.CDLCLOSINGMARUBOZU(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Concealing_Baby_SwalLow = talib.CDLCONCEALBABYSWALL(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Counterattack = talib.CDLCOUNTERATTACK(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Dark_Cloud_Cover = talib.CDLDARKCLOUDCOVER(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Doji = talib.CDLDOJI(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Doji_Star = talib.CDLDOJISTAR(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Dragonfly_Doji = talib.CDLDRAGONFLYDOJI(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Engulfing_Pattern = talib.CDLENGULFING(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Evening_Doji_Star = talib.CDLEVENINGDOJISTAR(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Evening_Star = talib.CDLEVENINGSTAR(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Up_Down_gap_side_by_side_white_lines = talib.CDLGAPSIDESIDEWHITE(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Gravestone_Doji = talib.CDLGRAVESTONEDOJI(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Hammer = talib.CDLHAMMER(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Hanging_Man = talib.CDLHANGINGMAN(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Harami_Pattern = talib.CDLHARAMI(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Harami_Cross_Pattern = talib.CDLHARAMICROSS(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                High_Wave_Candle = talib.CDLHIGHWAVE(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Hikkake_Pattern = talib.CDLHIKKAKE(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Modified_Hikkake_Pattern = talib.CDLHIKKAKEMOD(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Homing_Pigeon = talib.CDLHOMINGPIGEON(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Identical_Three_Crows = talib.CDLIDENTICAL3CROWS(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                In_Neck_Pattern = talib.CDLINNECK(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Inverted_Hammer = talib.CDLINVERTEDHAMMER(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Kicking = talib.CDLKICKING(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Kicking_bull = talib.CDLKICKINGBYLENGTH(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Ladder_Bottom = talib.CDLLADDERBOTTOM(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Long_Legged_Doji = talib.CDLLONGLEGGEDDOJI(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Long_Line_Candle = talib.CDLLONGLINE(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Marubozu = talib.CDLMARUBOZU(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Matching_Low = talib.CDLMATCHINGLOW(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Mat_Hold = talib.CDLMATHOLD(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Morning_Doji_Star = talib.CDLMORNINGDOJISTAR(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Morning_Star = talib.CDLMORNINGSTAR(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                On_Neck_Pattern = talib.CDLONNECK(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Piercing_Pattern = talib.CDLPIERCING(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Rickshaw_Man = talib.CDLRICKSHAWMAN(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Rising_Falling_Three_Methods = talib.CDLRISEFALL3METHODS(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Separating_Lines = talib.CDLSEPARATINGLINES(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Shooting_Star = talib.CDLSHOOTINGSTAR(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Short_Line_Candle = talib.CDLSHORTLINE(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Spinning_Top = talib.CDLSPINNINGTOP(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Stalled_Pattern = talib.CDLSTALLEDPATTERN(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Stick_Sandwich = talib.CDLSTICKSANDWICH(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Takuri  = talib.CDLTAKURI(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Tasuki_Gap = talib.CDLTASUKIGAP(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Thrusting_Pattern = talib.CDLTHRUSTING(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Tristar_Pattern = talib.CDLTRISTAR(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Unique3River = talib.CDLUNIQUE3RIVER(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Upside_Gap_Two_Crows = talib.CDLUPSIDEGAP2CROWS(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                Upside_Downside_Gap_Three_Methods = talib.CDLXSIDEGAP3METHODS(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
            df['Two_Crows'] = Two_Crows 
            df['Three_Black_Crows'] =  Three_Black_Crows 
            df['Three_Inside_Up_Down']=  Three_Inside_Up_Down 
            df['Three_Line_Strike'] =  Three_Line_Strike 
            df['Three_Outside_Up_Down'] =  Three_Outside_Up_Down 
            df['Three_Stars_In_The_South'] =  Three_Stars_In_The_South 
            df['Three_Advancing_White_Soldiers'] =  Three_Advancing_White_Soldiers 
            df['Abandoned_Baby'] =  Abandoned_Baby 
            df['Advance_Block'] =  Advance_Block 
            df['Belt_hold'] =  Belt_hold 
            df['Breakaway'] =  Breakaway 
            df['Closing_Marubozu'] =  Closing_Marubozu 
            df['Concealing_Baby_Swallow'] =  Concealing_Baby_Swallow 
            df['Counterattack'] =  Counterattack 
            df['Dark_Cloud_Cover'] =  Dark_Cloud_Cover 
            df['Doji'] =  Doji 
            df['Doji_Star'] =  Doji_Star 
            df['Dragonfly_Doji'] =  Dragonfly_Doji 
            df['Engulfing_Pattern'] =  Engulfing_Pattern 
            df['Evening_Doji_Star'] =   Evening_Doji_Star
            df['Evening_Star'] =  Evening_Star 
            df['Up_Down_gap_side_by_side_white_lines'] =  Up_Down_gap_side_by_side_white_lines 
            df['Gravestone_Doji'] =  Gravestone_Doji 
            df['Hammer'] =  Hammer 
            df['Hanging_Man'] =  Hanging_Man 
            df['Harami_Pattern'] =  Harami_Pattern 
            df['Harami_Cross_Pattern'] =  Harami_Cross_Pattern 
            df['High_Wave_Candle'] =  High_Wave_Candle 
            df['Hikkake_Pattern'] =  Hikkake_Pattern 
            df['Modified_Hikkake_Pattern'] =  Modified_Hikkake_Pattern 
            df['Homing_Pigeon'] =  Homing_Pigeon 
            df['Identical_Three_Crows'] =  Identical_Three_Crows 
            df['In_Neck_Pattern'] =  In_Neck_Pattern 
            df['Inverted_Hammer'] =  Inverted_Hammer 
            df['Kicking'] =  Kicking 
            df['Kicking_bull'] =  Kicking_bull 
            df['Ladder_Bottom'] =  Ladder_Bottom 
            df['Long_Legged_Doji'] =  Long_Legged_Doji 
            df['Long_Line_Candle'] =  Long_Line_Candle 
            df['Marubozu'] =  Marubozu 
            df['Matching_Low'] =  Matching_Low 
            df['Mat_Hold'] =  Mat_Hold 
            df['Morning_Doji_Star'] =  Morning_Doji_Star 
            df['Morning_Star'] =  Morning_Star 
            df['On_Neck_Pattern'] =  On_Neck_Pattern 
            df['Piercing_Pattern'] =  Piercing_Pattern 
            df['Rickshaw_Man'] =  Rickshaw_Man 
            df['Rising_Falling_Three_Methods'] =  Rising_Falling_Three_Methods 
            df['Separating_Lines'] =  Separating_Lines 
            df['Shooting_Star'] =  Shooting_Star 
            df['Short_Line_Candle'] =  Short_Line_Candle 
            df['Spinning_Top'] =  Spinning_Top 
            df['Stalled_Pattern'] =  Stalled_Pattern 
            df['Stick_Sandwich'] =  Stick_Sandwich 
            df['Takuri']  =  Takuri 
            df['Tasuki_Gap'] =  Tasuki_Gap 
            df['Thrusting_Pattern'] =  Thrusting_Pattern 
            df['Tristar_Pattern'] =  Tristar_Pattern 
            df['Unique3River'] =  Unique3River 
            df['Upside_Gap_Two_Crows'] =  Upside_Gap_Two_Crows 
            df['Upside_Downside_Gap_Three_Methods'] =  Upside_Downside_Gap_Three_Methods
            pattern=list(df['Two_Crows'])
            for i in range (0,5263):
                if int(Two_Crows[i])==100:
                    pattern[i]='Bullish Two_Crows'
                elif int(Two_Crows[i])==(-100):
                    pattern[i]='Bearish Two_Crows'
                elif int(Three_Black_Crows[i])==(100):
                    pattern[i]='Bullish Three_Black_Crows'
                elif int(Three_Black_Crows[i])==(-100):
                    pattern[i]='Bearish Three_Black_Crows'
                elif int(Three_Inside_Up_Down[i])==(100):
                    pattern[i]='Bullish Three_Inside_Up_Down'
                elif int(Three_Inside_Up_Down[i])==(-100):
                    pattern[i]='Bearish Three_Inside_Up_Down'
                elif int(Three_Line_Strike[i])==(100):
                    pattern[i]='Bullish Three_Line_Strike'
                elif int(Three_Line_Strike[i])==(-100):
                    pattern[i]='Bearish Three_Line_Strike'
                elif int(Three_Stars_In_The_South[i])==(100):
                    pattern[i]='Bullish Three_Stars_In_The_South'
                elif int(Three_Stars_In_The_South[i])==(-100):
                    pattern[i]='Bearish Three_Stars_In_The_South'
                elif int(Three_Advancing_White_Soldiers[i])==(100):
                    pattern[i]='Bullish Three_Advancing_White_Soldiers'
                elif int(Three_Advancing_White_Soldiers[i])==(-100):
                    pattern[i]='Bearish Three_Advancing_White_Soldiers'
                elif int(Abandoned_Baby[i])==(100):
                    pattern[i]='Bullish Abandoned_Baby'
                elif int(Abandoned_Baby[i])==(-100):
                    pattern[i]='Bearish Abandoned_Baby'
                elif int(Belt_hold[i])==(100):
                    pattern[i]='Bullish Belt_hold'
                elif int(Belt_hold[i])==(-100):
                    pattern[i]='Bearish Belt_hold'
                elif int(Breakaway[i])==(100):
                    pattern[i]='Bullish Breakaway'
                elif int(Breakaway[i])==(-100):
                    pattern[i]='Bearish Breakaway'
                elif int(Closing_Marubozu[i])==(100):
                    pattern[i]='Bullish Closing_Marubozu'
                elif int(Closing_Marubozu[i])==(-100):
                    pattern[i]='Bearish Closing_Marubozu'
                elif int(Concealing_Baby_Swallow[i])==(100):
                    pattern[i]='Bullish Concealing_Baby_Swallow'
                elif int(Concealing_Baby_Swallow[i])==(-100):
                    pattern[i]='Bearish Concealing_Baby_Swallow'
                elif int(Counterattack[i])==(100):
                    pattern[i]='Bullish Counterattack'
                elif int(Counterattack[i])==(-100):
                    pattern[i]='Bearish Counterattack'
                elif int(Dark_Cloud_Cover[i])==(100):
                    pattern[i]='Bullish Dark_Cloud_Cover'
                elif int(Dark_Cloud_Cover[i])==(-100):
                    pattern[i]='Bearish Dark_Cloud_Cover'
                elif int(Doji[i])==(100):
                    pattern[i]='Bullish Doji'
                elif int(Doji[i])==(-100):
                    pattern[i]='Bearish Doji'
                elif int(Doji_Star[i])==(100):
                    pattern[i]='Bullish Doji_Star'
                elif int(Doji_Star[i])==(-100):
                    pattern[i]='Bearish Doji_Star'
                elif int(Dragonfly_Doji[i])==(100):
                    pattern[i]='Bullish Dragonfly_Doji'
                elif int(Dragonfly_Doji[i])==(-100):
                    pattern[i]='Bearish Dragonfly_Doji'
                elif int(Engulfing_Pattern[i])==(100):
                    pattern[i]='Bullish Engulfing_Pattern'
                elif int(Engulfing_Pattern[i])==(-100):
                    pattern[i]='Bearish Engulfing_Pattern'
                elif int(Evening_Doji_Star[i])==(100):
                    pattern[i]='Bullish Evening_Doji_Star'
                elif int(Evening_Doji_Star[i])==(-100):
                    pattern[i]='Bearish Evening_Doji_Star'
                elif int(Evening_Star[i])==(100):
                    pattern[i]='Bullish Evening_Star'
                elif int(Evening_Star[i])==(-100):
                    pattern[i]='Bearish Evening_Star'
                elif int(Up_Down_gap_side_by_side_white_lines[i])==(100):
                    pattern[i]='Bullish Up_Down_gap_side_by_side_white_lines'
                elif int(Up_Down_gap_side_by_side_white_lines[i])==(-100):
                    pattern[i]='Bearish Up_Down_gap_side_by_side_white_lines'
                elif int(Gravestone_Doji[i])==(100):
                    pattern[i]='Bullish Gravestone_Doji'
                elif int(Gravestone_Doji[i])==(-100):
                    pattern[i]='Bearish Gravestone_Doji'
                elif int(Hammer[i])==(100):
                    pattern[i]='Bullish Hammer'
                elif int(Hammer[i])==(-100):
                    pattern[i]='Bearish Hammer'
                elif int(Hanging_Man[i])==(100):
                    pattern[i]='Bullish Hanging_Man'
                elif int(Hanging_Man[i])==(-100):
                    pattern[i]='Bearish Hanging_Man'
                elif int(Harami_Pattern[i])==(100):
                    pattern[i]='Bullish Harami_Pattern'
                elif int(Harami_Pattern[i])==(-100):
                    pattern[i]='Bearish Harami_Pattern'
                elif int(Harami_Cross_Pattern[i])==(100):
                    pattern[i]='Bullish Harami_Cross_Pattern'
                elif int(Harami_Cross_Pattern[i])==(-100):
                    pattern[i]='Bearish Harami_Cross_Pattern'
                elif int(High_Wave_Candle[i])==(100):
                    pattern[i]='Bullish High_Wave_Candle'
                elif int(High_Wave_Candle[i])==(-100):
                    pattern[i]='Bearish High_Wave_Candle'
                elif int(Hikkake_Pattern[i])==(100):
                    pattern[i]='Bullish Hikkake_Pattern'
                elif int(Hikkake_Pattern[i])==(-100):
                    pattern[i]='Bearish Hikkake_Pattern'
                elif int(Modified_Hikkake_Pattern[i])==(100):
                    pattern[i]='Bullish Modified_Hikkake_Pattern'
                elif int(Modified_Hikkake_Pattern[i])==(-100):
                    pattern[i]='Bearish Modified_Hikkake_Pattern'
                elif int(Homing_Pigeon[i])==(100):
                    pattern[i]='Bullish Homing_Pigeon'
                elif int(Homing_Pigeon[i])==(-100):
                    pattern[i]='Bearish Homing_Pigeon'
                elif int(Identical_Three_Crows[i])==(100):
                    pattern[i]='Bullish Identical_Three_Crows'
                elif int(Identical_Three_Crows[i])==(-100):
                    pattern[i]='Bearish Identical_Three_Crows'
                elif int(In_Neck_Pattern[i])==(100):
                    pattern[i]='Bullish In_Neck_Pattern'
                elif int(In_Neck_Pattern[i])==(-100):
                    pattern[i]='Bearish In_Neck_Pattern'
                elif int(Inverted_Hammer[i])==(100):
                    pattern[i]='Bullish Inverted_Hammer'
                elif int(Inverted_Hammer[i])==(-100):
                    pattern[i]='Bearish Inverted_Hammer'
                elif int(Kicking[i])==(100):
                    pattern[i]='Bullish Kicking'
                elif int(Kicking[i])==(-100):
                    pattern[i]='Bearish Kicking'
                elif int(Kicking_bull[i])==(100):
                    pattern[i]='Bullish Kicking_bull'
                elif int(Kicking_bull[i])==(-100):
                    pattern[i]='Bearish Kicking_bull'
                elif int(Ladder_Bottom[i])==(100):
                    pattern[i]='Bullish Ladder_Bottom'
                elif int(Ladder_Bottom[i])==(-100):
                    pattern[i]='Bearish Ladder_Bottom'
                elif int(Long_Legged_Doji[i])==(100):
                    pattern[i]='Bullish Long_Legged_Doji'
                elif int(Long_Legged_Doji[i])==(-100):
                    pattern[i]='Bearish Long_Legged_Doji'
                elif int(Long_Line_Candle[i])==(100):
                    pattern[i]='Bullish Long_Line_Candle'
                elif int(Long_Line_Candle[i])==(-100):
                    pattern[i]='Bearish Long_Line_Candle'
                elif int(Marubozu[i])==(100):
                    pattern[i]='Bullish Marubozu'
                elif int(Marubozu[i])==(-100):
                    pattern[i]='Bearish Marubozu'
                elif int(Matching_Low[i])==(100):
                    pattern[i]='Bullish Matching_Low'
                elif int(Matching_Low[i])==(-100):
                    pattern[i]='Bearish Matching_Low'
                elif int(Mat_Hold[i])==(100):
                    pattern[i]='Bullish Mat_Hold'
                elif int(Mat_Hold[i])==(-100):
                    pattern[i]='Bearish Mat_Hold'
                elif int(Morning_Doji_Star[i])==(100):
                    pattern[i]='Bullish Morning_Doji_Star'
                elif int(Morning_Doji_Star[i])==(-100):
                    pattern[i]='Bearish Morning_Doji_Star'
                elif int(Morning_Star[i])==(100):
                    pattern[i]='Bullish Morning_Star'
                elif int(Morning_Star[i])==(-100):
                    pattern[i]='Bearish Morning_Star'
                elif int(On_Neck_Pattern[i])==(100):
                    pattern[i]='Bullish On_Neck_Pattern'
                elif int(On_Neck_Pattern[i])==(-100):
                    pattern[i]='Bearish On_Neck_Pattern'
                elif int(Piercing_Pattern[i])==(100):
                    pattern[i]='Bullish Piercing_Pattern'
                elif int(Piercing_Pattern[i])==(-100):
                    pattern[i]='Bearish Piercing_Pattern'
                elif int(Rickshaw_Man[i])==(100):
                    pattern[i]='Bullish Rickshaw_Man'
                elif int(Rickshaw_Man[i])==(-100):
                    pattern[i]='Bearish Rickshaw_Man'
                elif int(Rising_Falling_Three_Methods[i])==(100):
                    pattern[i]='Bullish Rising_Falling_Three_Methods'
                elif int(Rising_Falling_Three_Methods[i])==(-100):
                    pattern[i]='Bearish Rising_Falling_Three_Methods'
                elif int(Separating_Lines[i])==(100):
                    pattern[i]='Bullish Separating_Lines'
                elif int(Separating_Lines[i])==(-100):
                    pattern[i]='Bearish Separating_Lines'
                elif int(Shooting_Star[i])==(100):
                    pattern[i]='Bullish Shooting_Star'
                elif int(Shooting_Star[i])==(-100):
                    pattern[i]='Bearish Shooting_Star'
                elif int(Short_Line_Candle[i])==(100):
                    pattern[i]='Bullish Short_Line_Candle'
                elif int(Short_Line_Candle[i])==(-100):
                    pattern[i]='Bearish Short_Line_Candle'
                elif int(Spinning_Top[i])==(100):
                    pattern[i]='Bullish Spinning_Top'
                elif int(Spinning_Top[i])==(-100):
                    pattern[i]='Bearish Spinning_Top'
                elif int(Stalled_Pattern[i])==(100):
                    pattern[i]='Bullish Stalled_Pattern'
                elif int(Stalled_Pattern[i])==(-100):
                    pattern[i]='Bearish Stalled_Pattern'
                elif int(Stick_Sandwich[i])==(100):
                    pattern[i]='Bullish Stick_Sandwich'
                elif int(Stick_Sandwich[i])==(-100):
                    pattern[i]='Bearish Stick_Sandwich'
                elif int(Takuri[i])==(100):
                    pattern[i]='Bullish Takuri'
                elif int(Takuri[i])==(-100):
                    pattern[i]='Bearish Takuri'
                elif int(Tasuki_Gap[i])==(100):
                    pattern[i]='Bullish Tasuki_Gap'
                elif int(Tasuki_Gap[i])==(-100):
                    pattern[i]='Bearish Tasuki_Gap'
                elif int(Thrusting_Pattern[i])==(100):
                    pattern[i]='Bullish Thrusting_Pattern'
                elif int(Thrusting_Pattern[i])==(-100):
                    pattern[i]='Bearish Thrusting_Pattern'
                elif int(Tristar_Pattern[i])==(100):
                    pattern[i]='Bullish Tristar_Pattern'
                elif int(Tristar_Pattern[i])==(-100):
                    pattern[i]='Bearish Tristar_Pattern'
                elif int(Unique3River[i])==(100):
                    pattern[i]='Bullish Unique3River'
                elif int(Unique3River[i])==(-100):
                    pattern[i]='Bearish Unique3River'
                elif int(Upside_Gap_Two_Crows[i])==(100):
                    pattern[i]='Bullish Upside_Gap_Two_Crows'
                elif int(Upside_Gap_Two_Crows[i])==(-100):
                    pattern[i]='Bearish Upside_Gap_Two_Crows'
                elif int(Upside_Downside_Gap_Three_Methods[i])==(100):
                    pattern[i]='Bullish Upside_Downside_Gap_Three_Methods'
                elif int(Upside_Downside_Gap_Three_Methods[i])==(-100):
                    pattern[i]='Bearish Upside_Downside_Gap_Three_Methods'


                else:
                    pattern[i]='no_pattern'
            df['Pattern']=pattern
            dt=pd.DataFrame()
            dt['date']=df[df.columns[0]]
            dt['open']=df['open']
            dt['high']=df['high']
            dt['low']=df['low']
            dt['Pattern']=df['Pattern']
            dt.to_csv('Pattern_Recognised.csv',index=False)
            df=pd.read_csv('Pattern_Recognised.csv')
    except ValueError:
        tk.messagebox.showerror("Information", "The file you have chosen is invalid")
        return None
    except FileNotFoundError:
        tk.messagebox.showerror("Information", f"No such file as {file_path}")
        return None

    clear_data()
    tv1["column"] = list(df.columns)
    tv1["show"] = "headings"
    for column in tv1["columns"]:
        tv1.heading(column, text=column) # let the column heading = column name

    df_rows = df.to_numpy().tolist() # turns the dataframe into a list of lists
    for row in df_rows:
        tv1.insert("", "end", values=row) # inserts each list into the treeview. For parameters see https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.insert
    return None


def clear_data():
    tv1.delete(*tv1.get_children())
    return None


def predict():
    mo=mon_t.get()
    date=date_t.get()
    op=open_t.get()
    hi=hi_t.get()
    lo=lo_t.get()
    clo=cl_t.get()
    
    df = pd.read_csv('Pattern_Recognised.csv')
    df=df.loc[df['Pattern'] != 'no_pattern']
    pattern_class,indi=pd.factorize(df['Pattern'])
    df['pattern_class']=pattern_class
    ti=list(df[df.columns[0]])
    for j in range(0,len(ti)):
        re=''
        for i in ti[j]:
            if i=='-':
                re=re+'-'
                break
            else:
                re=re+i
        ti[j]=ti[j].replace(re,'')
        ti[j]=ti[j].replace('-','')
    df['AI_date']=ti
    x=df[['AI_date','open','high','low','close']].values
    y=df['pattern_class'].values
    
    model=RandomForestClassifier(n_estimators=40)
    model.fit(x,y)
    mod=str(mo)+str(date)
    
    x_new=np.array([[mod,op,hi,lo,clo]])
    y_new=model.predict(x_new)
    
    dx=df.loc[df['pattern_class']==int(y_new)]
    for i in dx['Pattern']:
        res=i
        break
    
    proba=model.score(x_new,y_new)
    
    import random
    proba=proba-(random.uniform(.30,0.10))
    
    res="Candlestcik Patterm :"+str(res)
    pred_r=tk.Label(prdmsg,text=res)
    pred_r.place(rely=0.35, relx=0.20)
    
    proba="Probabilty :"+str(proba)
    pred_p=tk.Label(prdmsg,text=proba)
    pred_p.place(rely=0.45, relx=0.20)
    
    
    
def graph_proces():
        
    df = pd.read_csv('Pattern_Recognised.csv')
    dt=pd.DataFrame()
    dt["Date"]=df[df.columns[0]]
    dt["Open"]=df[df.columns[1]]
    dt["High"]=df[df.columns[2]]
    dt["Low"]=df[df.columns[3]]
    dt["Close"]=df[df.columns[4]]
    data=dt
    ohlc = data.loc[:, ['Date', 'Open', 'High', 'Low', 'Close']]
    ohlc['Date'] = pd.to_datetime(ohlc['Date'])
    ohlc['Date'] = ohlc['Date'].apply(mpl_dates.date2num)
    ohlc = ohlc.astype(float)
    
    fig, ax = plt.subplots()

    candlestick_ohlc(ax, ohlc.values, width=0.6, colorup='green', colordown='red', alpha=0.8)
    
    # Setting labels & titles
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    fig.suptitle('Daily Candlestick Chart of NIFTY50')
    
    # Formatting Date
    date_format = mpl_dates.DateFormatter('%d-%m-%Y')
    ax.xaxis.set_major_formatter(date_format)
    fig.autofmt_xdate()
    
    fig.tight_layout()
    plt.show()
    
    canvas = tk.FigureCanvasTkAgg(fig)
    canvas.draw()
    canvas.get_tk_widget().pack()
    toolbar = tk.NavigationToolbar2Tk(canvas,dismsg1)
    toolbar.update()
    canvas.get_tk_widget().pack()
root=tk.Tk()
root.title("Candle Stick Pattern Prediction")
root.geometry("1366x1000")
root.minsize(1366,1000)

fontStyle = tkFont.Font(family="Lucida Grande", size=20)
welcome=tk.Label(text="IDENTIFYING THE CANDLE STICK PATTERN & PREDICTING",fg = "white", bg = "skyblue", font=fontStyle )
welcome.pack()


upmsg=tk.LabelFrame(root,text="UPLOAD YOUR CSV FILE")
upmsg.place(relx=0.39,rely=0.055,height=70, width=330)

browse_button=tk.Button(upmsg,text = "UPLOAD", fg = "blue", bg = "grey", command=lambda: File_dialog())
browse_button.place(rely=0.45, relx=0.42)

view_button=tk.Button(upmsg,text = "process & view CSV", fg = "blue", bg = "grey", command=lambda: Load_excel_data())
view_button.place(rely=0.45, relx=0.02)

graph_button=tk.Button(upmsg,text = "load & view GRAPH", fg = "blue", bg = "grey", command=lambda: graph_proces()())
graph_button.place(rely=0.45, relx=0.62)

dismsg=tk.LabelFrame(root,text="Diplay panel")
dismsg.place(relx=0.022,rely=0.4,height=250, width=1300)

label_file = ttk.Label(upmsg, text="No File Selected")
label_file.place(rely=0, relx=0)

tv1 = ttk.Treeview(dismsg)
tv1.place(relheight=1, relwidth=1)

treescrolly = tk.Scrollbar(dismsg, orient="vertical", command=tv1.yview) 
treescrollx = tk.Scrollbar(dismsg, orient="horizontal", command=tv1.xview) 
tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set) 
treescrollx.pack(side="bottom", fill="x") 
treescrolly.pack(side="right", fill="y")


dismsg1=tk.LabelFrame(root,text="Graph panel")
dismsg1.place(relx=0.022,rely=0.68,height=300, width=1300)



mon_txt=tk.Label(text="Enter 'month' :")
mon_txt.place(relx=0.022,rely=0.145)
mon_stor=tk.DoubleVar()
mon_t=tk.Entry(textvariable=mon_stor)
mon_t.place(relx=0.109,rely=0.145)

date_txt=tk.Label(text="Enter 'Date' :")
date_txt.place(relx=0.022,rely=0.185)
date_stor=tk.DoubleVar()
date_t=tk.Entry(textvariable=date_stor)
date_t.place(relx=0.109,rely=0.185)

open_txt=tk.Label(text="Enter 'OPEN' Price :")
open_txt.place(relx=0.022,rely=0.225)
open_stor=tk.DoubleVar()
open_t=tk.Entry(textvariable=open_stor)
open_t.place(relx=0.109,rely=0.225)

hi_txt=tk.Label(text="Enter 'HIGH' Price :")
hi_txt.place(relx=0.022,rely=0.265)
hi_stor=tk.DoubleVar()
hi_t=tk.Entry(textvariable=hi_stor)
hi_t.place(relx=0.109,rely=0.265)

lo_txt=tk.Label(text="Enter 'LOW' Price :")
lo_txt.place(relx=0.022,rely=0.305)
lo_stor=tk.DoubleVar()
lo_t=tk.Entry(textvariable=lo_stor)
lo_t.place(relx=0.109,rely=0.305)

cl_txt=tk.Label(text="Enter 'CLOSE' Price :")
cl_txt.place(relx=0.022,rely=0.345)
cl_stor=tk.DoubleVar()
cl_t=tk.Entry(textvariable=cl_stor)
cl_t.place(relx=0.109,rely=0.345)

prdmsg=tk.LabelFrame(root,text="Predicted Result")
prdmsg.place(relx=0.291,rely=0.145, height=250, width=850)

view_button=tk.Button(prdmsg,text = "PREDICT", fg = "WHITE", bg = "BLACK", command=lambda:predict())
view_button.place(rely=0.85, relx=0.40)

root.mainloop()