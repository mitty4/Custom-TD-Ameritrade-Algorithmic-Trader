#what tickers to trade?

#under 30 min
thirty = ["BBBY", "GEVO", "FUBO", "CCL", "NNDM", "AMD", "MARA", "FCEL", "SOL", "TSLA", "M", "RIOT", "VVPR", "NCLH", "KODK", "CLF", "OXY", "MAC", "SPWR", "FCX", "X", "SUNW", "SKT", "DDD", "SLB", "UAVS", "NCTY"]

sp = ["AAPL", "ADI", "AES", "AFL", "HES", "AIG", "AMAT", "APA", "IVZ", "AXP", "BAC", "TFC", "BBY", "BEN", "BKR", "BMY", "BSX", "CAT", "CNC", "COF", "COG", "COP", "LUMN", "CVS", "CVX", "DHI", "DHR", "DVN", "EBAY", "EOG", "F", "FCX", "FE", "FITB", "NEE", "FTI", "GILD", "GOOGL", "GPS", "GS", "HBAN", "IFF", "INTC", "JNJ", "JNPR", "JPM", "KEY", "KIM", "KR", "LEN", "LLY", "LOW", "LB", "MET", "MOS", "MRO", "MU", "MS", "NFLX", "NVDA", "NWL", "OKE", "OXY", "PCAR", "PHM", "QCOM", "RF", "SCHW", "SLB", "SPG", "SWKS", "TGT", "TMO", "TXN", "JCI", "VLO", "WBA", "WFC", "XOM", "HFC", "DISCA", "EXPE", "UAA", "VIAC", "HBI", "DISCK", "PBCT", "TSLA", "GM", "KMI", "MPC", "APTV", "ENPH", "PSX", "FANG", "ABBV", "GOOG", "SYF", "CFG", "ETSY"]

# low_pe = ['LEU', 'BBSI', 'PRDO', 'CRAI', 'CRMT', 'EBIX', 'ECPG', 'FLWS', 'FRME', 'HAFC', 'HBAN', 'HIBB', 'HTLF', 'KFRC', 'HOPE', 'NBN', 'NEWT', 'NSIT', 'OZK', 'PFBC', 'PLXS', 'PNFP', 'STLD', 'TBBK', 'UCBI', 'UNTY', 'WLFC', 'WRLD', 'BGFV', 'DISCA', 'VIAC', 'QRTEA', 'COWN', 'PRIM', 'PBCT', 'AMCX', 'SUPN', 'NAVI', 'MIK', 'CHRS', 'FFWM', 'AB', 'ADS', 'MTOR', 'AYI', 'BBY', 'BC', 'BEN', 'BXC', 'BXS', 'BZH', 'CE', 'CFR', 'CMC', 'CYD', 'DHI', 'DRD', 'ATGE', 'EXP', 'FBC', 'FNB', 'GBL', 'TGNA', 'GS', 'GTN', 'HOV', 'HVT', 'JLL', 'KBH', 'KIM', 'MHO', 'MTZ', 'MS', 'NCR', 'STL', 'PHM', 'RF', 'SLG', 'TKR', 'UNFI', 'UNM', 'VHI', 'WHR', 'WSM', 'GLP', 'BMA', 'HBI', 'DAC', 'FLY', 'LL', 'GSL', 'CLW', 'CAI', 'TROX', 'BCEI', 'ALSN', 'CAPL', 'WES', 'TPH', 'SBSW', 'PBFX', 'LPG', 'ENVA', 'HESM', 'SUM', 'KEN', 'NGVT', 'VVV', 'NTB', 'CWH', 'BPMP']

low_pe = ['ABCB', 'AMKR', 'BPOP', 'BSRR', 'CATY', 'PRDO', 'CHY', 'CRMT', 'DISH', 'EBIX', 'ECPG', 'ESCA', 'EWBC', 'FITB', 'FRME', 'HAFC', 'HOLX', 'IIIN', 'KFRC', 'HOPE', 'NCTY', 'OZK', 'PFBC', 'PFG', 'PLUS', 'PRAA', 'STLD', 'STRL', 'TBBK', 'AUB', 'UCBI', 'UFPI', 'VLY', 'WRLD', 'WTFC', 'EFSC', 'VIAC', 'QRTEA', 'COWN', 'PRIM', 'TA', 'SMCI', 'GRBK', 'OPI', 'PBCT', 'IRWD', 'HEAR', 'AMCX', 'FDUS', 'COOP', 'LGIH', 'NMIH', 'NAVI', 'MIK', 'VBTX', 'FFWM', 'MOMO', 'WRI', 'SPB', 'WAL', 'GLP', 'FNF', 'BMA', 'TRTN', 'EVR', 'HBI', 'CS', 'DAC', 'SBH', 'LL', 'GSL', 'CLW', 'STWD', 'SEM', 'CAI', 'TROX', 'BKU', 'NGVC', 'VTOL', 'TPH', 'BCC', 'SBSW', 'TMHC', 'KNOP', 'OMF', 'TPVG', 'TNET', 'CCS', 'BSIG', 'ENVA', 'SUM', 'NGVT', 'ATKR', 'VVV', 'ATH', 'BPMP', 'XBIT', 'NBLX', 'LSXMA', 'FHB', 'ABG', 'AEL', 'AN', 'ARW', 'BC', 'BEN', 'BXC', 'BXS', 'C', 'CFR', 'CMC', 'CNO', 'DKS', 'DVA', 'DX', 'EPD', 'EXP', 'FBC', 'FNB', 'GBL', 'TGNA', 'GPI', 'HZO', 'INT', 'KBH', 'KIM', 'LAD', 'MET', 'MEI', 'MHO', 'MS', 'MYE', 'NCR', 'STL', 'RDN', 'RJF', 'SF', 'SLG', 'STT', 'TKR', 'TOL', 'PAG']

tickers = [x for x in low_pe]




