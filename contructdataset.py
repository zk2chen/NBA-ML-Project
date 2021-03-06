# Importing libraries
import os
import pandas as pd
import numpy as np
from numpy import *

import pickle

#Loading 2018-2019 stats
nba_18_19 = pd.read_pickle(r"C:\Users\zhika\NBA_ML_PROJECT\18-19-nba_stats.pkl")

#adding column name season
nba_18_19.insert(1, 'season', 2019.0, allow_duplicates = True)

#Loading 2017-2018 stats
nba_17_18 = pd.read_pickle(r"C:\Users\zhika\NBA_ML_PROJECT\17-18-nba_stats.pkl")

#adding column name season
nba_17_18.insert(1, 'season', 2018.0, allow_duplicates = True)

#Loading 2016-2017 stats
nba_16_17 = pd.read_pickle(r"C:\Users\zhika\NBA_ML_PROJECT\16-17-nba_stats.pkl")

#adding column name season
nba_16_17.insert(1, 'season', 2017.0, allow_duplicates = True)

#Loading 2015-2016 stats
nba_15_16 = pd.read_pickle(r"C:\Users\zhika\NBA_ML_PROJECT\15-16-nba_stats.pkl")

#adding column name season
nba_15_16.insert(1, 'season', 2016.0, allow_duplicates = True)

#Loading 2014-2015 stats
nba_14_15 = pd.read_pickle(r"C:\Users\zhika\NBA_ML_PROJECT\14-15-nba_stats.pkl")

#adding column name season
nba_14_15.insert(1, 'season', 2015.0, allow_duplicates = True)

#Loading 2013-2014 stats
nba_13_14 = pd.read_pickle(r"C:\Users\zhika\NBA_ML_PROJECT\13-14-nba_stats.pkl")

#adding column name season
nba_13_14.insert(1, 'season', 2014.0, allow_duplicates = True)

#Loading 2012-2013 stats
nba_12_13 = pd.read_pickle(r"C:\Users\zhika\NBA_ML_PROJECT\12-13-nba_stats.pkl")

#adding column name season
nba_12_13.insert(1, 'season', 2013.0, allow_duplicates = True)

#Loading 2011-2012 stats
nba_11_12 = pd.read_pickle(r"C:\Users\zhika\NBA_ML_PROJECT\11-12-nba_stats.pkl")

#adding column name season
nba_11_12.insert(1, 'season', 2012.0, allow_duplicates = True)

#Loading 2010-2011 stats
nba_10_11 = pd.read_pickle(r"C:\Users\zhika\NBA_ML_PROJECT\10-11-nba_stats.pkl")

#adding column name season
nba_10_11.insert(1, 'season', 2011.0, allow_duplicates = True)

#Loading 2009-2010 stats
nba_09_10 = pd.read_pickle(r"C:\Users\zhika\NBA_ML_PROJECT\09-10-nba_stats.pkl")

#adding column name season
nba_09_10.insert(1, 'season', 2010.0, allow_duplicates = True)

#Loading 2008-2009 stats
nba_08_09 = pd.read_pickle(r"C:\Users\zhika\NBA_ML_PROJECT\08-09-nba_stats.pkl")

#adding column name season
nba_08_09.insert(1, 'season', 2009.0, allow_duplicates = True)

#Loading 2007-2008 stats
nba_07_08 = pd.read_pickle(r"C:\Users\zhika\NBA_ML_PROJECT\07-08-nba_stats.pkl")

#adding column name season
nba_07_08.insert(1, 'season', 2008.0, allow_duplicates = True)

#Loading 2006-2007 stats
nba_06_07 = pd.read_pickle(r"C:\Users\zhika\NBA_ML_PROJECT\06-07-nba_stats.pkl")

#adding column name season
nba_06_07.insert(1, 'season', 2007.0, allow_duplicates = True)

#Loading 2005-2006 stats
nba_05_06 = pd.read_pickle(r"C:\Users\zhika\NBA_ML_PROJECT\05-06-nba_stats.pkl")

#adding column name season
nba_05_06.insert(1, 'season', 2006.0, allow_duplicates = True)

#Loading 2004-2005 stats
nba_04_05 = pd.read_pickle(r"C:\Users\zhika\NBA_ML_PROJECT\04-05-nba_stats.pkl")

#adding column name season
nba_04_05.insert(1, 'season', 2005.0, allow_duplicates = True)

#Loading 2003-2004 stats
nba_03_04 = pd.read_pickle(r"C:\Users\zhika\NBA_ML_PROJECT\03-04-nba_stats.pkl")

#adding column name season
nba_03_04.insert(1, 'season', 2004.0, allow_duplicates = True)

#Loading 2002-2003 stats
nba_02_03 = pd.read_pickle(r"C:\Users\zhika\NBA_ML_PROJECT\02-03-nba_stats.pkl")

#adding column name season
nba_02_03.insert(1, 'season', 2003.0, allow_duplicates = True)

#Loading 2001-2002 stats
nba_01_02 = pd.read_pickle(r"C:\Users\zhika\NBA_ML_PROJECT\01-02-nba_stats.pkl")

#adding column name season
nba_01_02.insert(1, 'season', 2002.0, allow_duplicates = True)

#Loading 2000-2001 stats
nba_00_01 = pd.read_pickle(r"C:\Users\zhika\NBA_ML_PROJECT\00-01-nba_stats.pkl")

#adding column name season
nba_00_01.insert(1, 'season', 2001.0, allow_duplicates = True)

#Loading 1999-2000 stats
nba_99_00 = pd.read_pickle(r"C:\Users\zhika\NBA_ML_PROJECT\99-00-nba_stats.pkl")

#adding column name season
nba_99_00.insert(1, 'season', 2000.0, allow_duplicates = True)

#Loading 1998-1999 stats
nba_98_99 = pd.read_pickle(r"C:\Users\zhika\NBA_ML_PROJECT\98-99-nba_stats.pkl")

#adding column name season
nba_98_99.insert(1, 'season', 1999.0, allow_duplicates = True)

#Loading 1997-1998 stats
nba_97_98 = pd.read_pickle(r"C:\Users\zhika\NBA_ML_PROJECT\97-98-nba_stats.pkl")

#adding column name season
nba_97_98.insert(1, 'season', 1998.0, allow_duplicates = True)

#Combining the dataframes together
combined_data = nba_18_19.append(nba_17_18, ignore_index=True)

#Iterate over the array to append all of the dataframes to combined_data
years_array = [nba_16_17, nba_15_16,nba_14_15,nba_13_14,nba_12_13,nba_11_12,nba_10_11,nba_09_10,nba_08_09,
               nba_07_08,nba_06_07,nba_05_06,nba_04_05,nba_03_04,nba_02_03,nba_01_02, nba_00_01, nba_99_00, 
              nba_98_99, nba_97_98]

for year in years_array:
    combined_data = combined_data.append(year, ignore_index=True)

#Make a dataframe of nba players who are playing this year
nbaplayers_in_2018 = combined_data[combined_data['season'] == '18-19']

#Get a list of all active nba players
current_players= nbaplayers_in_2018["player"].tolist()

#Make a new dataframe only active nba players and all the stats from seasons they have played
active_players = combined_data.loc[combined_data['player'].isin(current_players)]
active_players

active_players.to_csv(r'C:\Users\zhika\Desktop\NBAplayerStats.csv')
