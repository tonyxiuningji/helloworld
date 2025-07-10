import akshare as ak

# stock_sse_summary_df = ak.stock_sse_summary()
# print(stock_sse_summary_df)

# stock_szse_summary_df = ak.stock_szse_summary(date="20250704")
# print(stock_szse_summary_df)


# stock_szse_sector_summary_df = ak.stock_szse_sector_summary(symbol="当年", date="202506")
# print(stock_szse_sector_summary_df)

# stock_szse_sector_summary_df = ak.stock_szse_sector_summary(symbol="行业", date="202506")
# print(stock_szse_sector_summary_df)

#个股信息查询-东财
# stock_individual_info_em_df = ak.stock_individual_info_em(symbol="002810")
# print(stock_individual_info_em_df)

# 个股信息查询-雪球
# stock_individual_basic_info_xq_df = ak.stock_individual_basic_info_xq(symbol="SH601127")
# print(stock_individual_basic_info_xq_df)

# 实时行情数据-东财
# stock_zh_a_spot_em_df = ak.stock_zh_a_spot_em()
# print(stock_zh_a_spot_em_df)

# # 沪 A 股
# stock_sh_a_spot_em_df = ak.stock_sh_a_spot_em()
# print(stock_sh_a_spot_em_df)
# # 深 A 股
# stock_sz_a_spot_em_df = ak.stock_sz_a_spot_em()
# print(stock_sz_a_spot_em_df)
# # 京 A 股
# stock_bj_a_spot_em_df = ak.stock_bj_a_spot_em()
# print(stock_bj_a_spot_em_df)
# # 新股
# stock_new_a_spot_em_df = ak.stock_new_a_spot_em()
# print(stock_new_a_spot_em_df)

# # 创业板
# stock_cy_a_spot_em_df = ak.stock_cy_a_spot_em()
# print(stock_cy_a_spot_em_df)

# # 科创板
# stock_kc_a_spot_em_df = ak.stock_kc_a_spot_em()
# print(stock_kc_a_spot_em_df)

# 实时行情数据-雪球
# stock_individual_spot_xq_df = ak.stock_individual_spot_xq(symbol="SZ002810")
# print(stock_individual_spot_xq_df)

# 历史行情数据-东财
stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol="002810", period="daily", start_date="20250701", end_date='20250710', adjust="")
print(stock_zh_a_hist_df)

# stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol="000001", period="daily", start_date="20170301", end_date='20240528', adjust="qfq")
# print(stock_zh_a_hist_df)