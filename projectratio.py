#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 14:36:05 2020

@author: samantha
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as si
annual_sales = 11379.8
average_receivable = (1880.5+138+1958.5)/2#(1880.5+1958.5)/2 #(????)
COGS = 1955.4 # Cost of sales, excluding amortization and impairment of acquired intangible assets
average_inventory = (804.2+929.9)/2
purchase = 804.2-929.9+COGS
average_trade_payables  = (530.8+ 370.5)/2#先用着account payable因为很多企业把trade payable和account payable合并了#为啥这公司没有呢 no vendor供货商吗
revenue = 14377.9
average_total_asset = (25288.9+27234.3+138)/2
average_net_fixed_assets = (3247.3+3601.2)/2 #PPE
average_working_capital = 8381.8-4863.8+138#CA-CL

###activity ratio/efficiency ratio
receivable_turnover = annual_sales/average_receivable
days_of_sales_outstanding = 365/receivable_turnover
inventory_turnover = COGS/average_inventory
days_of_inventory_on_hand = 365/inventory_turnover
total_asset_turnover = revenue/average_total_asset
fixed_asset_turnover = revenue/average_net_fixed_assets
working_capital_turnover = revenue/average_working_capital
payable_turnover = purchase/average_trade_payables
numbers_of_days_of_payables = 365/payable_turnover

current_asset = 8381.8
current_liability = 4863.8
cash = 2913.7
marketable_securities = 1562.2
account_receivable = 1068.1#1880.5

###liquidity ratio
current_ratio = current_asset/current_liability
quick_ratio = (cash+marketable_securities+account_receivable)/current_liability
cash_ratio = (cash+marketable_securities)/current_liability
cash_conversion_cycle = days_of_sales_outstanding+days_of_inventory_on_hand+numbers_of_days_of_payables

total_debt = 13895.2-4863.8-(2810.8*0.7)#TL-TCL#sum of all long-term liabilities 
total_sharehold_equity = 13343.2+(2810.8*0.3)
total_asset  = 27234.3+5.3-(3232.1-2999.83)
average_total_equity = (13339.1+13031.6)/2
EBIT = 7125.9
interest_payment = 43.3 #last year,今年没有interest payment不合理
lease_payment = 86.7 #in page42

###solvency ratio(financial ratio)
debt_to_equity = total_debt/total_sharehold_equity
debt_to_capital = total_debt/(total_debt+total_sharehold_equity)
debt_to_asset = total_debt/total_asset
financial_leverage = average_total_asset/average_total_equity
interest_coverage = EBIT/interest_payment
fixed_charge_coverage = (EBIT+lease_payment)/(interest_payment+lease_payment) #只对大的航空公司影响大

NI = 5993.3-5*0.16  #用的应该是comprehensive income which effect by avaiable for sales gain and loss
gross_profit = revenue-COGS 
opeating_income = 7078.6 #Net cash flows provided by operating activities
tax_rate = 16.25/100 
average_total_capital = average_total_asset #简单点 = total asset ;total liability#Short Term Debt + Long Term Debt + Shareholder’s Equity
#这家公司没有prefer stock
###profitability ratios
net_profit_margin = NI/revenue
gross_profit_margin = gross_profit/revenue#观察是否能通过来提高收入
operating_profit_margin = opeating_income/revenue#/= EBIT/revenue
ROA = (NI+interest_payment*(1-tax_rate))/(average_total_asset)
operating_return_on_asset = opeating_income/average_total_asset
return_on_total_capital = EBIT/average_total_capital
ROE = NI/average_total_equity

activity_ratio = [receivable_turnover,days_of_sales_outstanding,inventory_turnover,days_of_inventory_on_hand\
                  ,total_asset_turnover,fixed_asset_turnover,working_capital_turnover,payable_turnover,numbers_of_days_of_payables]
liquidity_ratio = [current_ratio,quick_ratio,cash_ratio,cash_conversion_cycle]
solvency_ratio = [debt_to_equity,debt_to_capital,debt_to_asset,financial_leverage,interest_coverage,fixed_charge_coverage]
profitability_ratios = [net_profit_margin,gross_profit_margin,operating_profit_margin,ROA,operating_return_on_asset,return_on_total_capital,ROE]

biogen_ratio = pd.DataFrame()
biogen_ratio['activity_ratio'] = activity_ratio
biogen_ratio['liquidity_ratio']=liquidity_ratio+list(np.zeros(5))
biogen_ratio['solvency_ratio'] = solvency_ratio+list(np.zeros(3))
biogen_ratio['profitability_ratios'] = profitability_ratios+list(np.zeros(2))


'---------------------------------------------------------------------------------------------------------------'
annual_sales = 10886.8
average_receivable = (1787.0+1958.5)/2 #(????)
COGS = 1816.3 # Cost of sales, excluding amortization and impairment of acquired intangible assets
average_inventory = (902.7+929.9)/2
purchase = 804.2-929.9+COGS
average_trade_payables  = (395.5+ 370.5)/2#先用着account payable因为很多企业把trade payable和account payable合并了#为啥这公司没有呢 no vendor供货商吗
revenue = 13452.9
average_total_asset = (25288.9+27234.3)/2
average_net_fixed_assets = (3182.4+3601.2)/2 #PPE
average_working_capital = 7640.9-3295.2#CA-CL

###activity ratio/efficiency ratio
receivable_turnover = annual_sales/average_receivable
days_of_sales_outstanding = 365/receivable_turnover
inventory_turnover = COGS/average_inventory
days_of_inventory_on_hand = 365/inventory_turnover
total_asset_turnover = revenue/average_total_asset
fixed_asset_turnover = revenue/average_net_fixed_assets
working_capital_turnover = revenue/average_working_capital
payable_turnover = purchase/average_trade_payables
numbers_of_days_of_payables = 365/payable_turnover

current_asset = 7640.9
current_liability = 3295.2
cash = 1224.6
marketable_securities = 2313.4
account_receivable = 1058.5#1880.5

###liquidity ratio
current_ratio = current_asset/current_liability
quick_ratio = (cash+marketable_securities+account_receivable)/current_liability
cash_ratio = (cash+marketable_securities)/current_liability
cash_conversion_cycle = days_of_sales_outstanding+days_of_inventory_on_hand+numbers_of_days_of_payables


total_debt = 12257.3-3295.2-(1636.2*0.7)#TL-TCL#sum of all long-term liabilities 
total_sharehold_equity = 13031.6+(1636.2*0.3)
total_asset  = 27234.3+5.3-(1636.2*0.075)
average_total_equity = (12598.1+13031.6)/2
EBIT = 5899.6
interest_payment = 43.3 #last year,今年没有interest payment不合理
lease_payment = 60.2 #in page42

###solvency ratio(financial ratio)
debt_to_equity = total_debt/total_sharehold_equity
debt_to_capital = total_debt/(total_debt+total_sharehold_equity)
debt_to_asset = total_debt/total_asset
financial_leverage = average_total_asset/average_total_equity
interest_coverage = EBIT/interest_payment
fixed_charge_coverage = (EBIT+lease_payment)/(interest_payment+lease_payment) #只对大的航空公司影响大

NI = 4550.1-5*0.16  #用的应该是comprehensive income which effect by avaiable for sales gain and loss
gross_profit = revenue-COGS 
opeating_income = 6187.7 #Net cash flows provided by operating activities
tax_rate = 16.25/100 
average_total_capital = average_total_asset #简单点 = total asset ;total liability#Short Term Debt + Long Term Debt + Shareholder’s Equity
#这家公司没有prefer stock
###profitability ratios
net_profit_margin = NI/revenue
gross_profit_margin = gross_profit/revenue#观察是否能通过来提高收入
operating_profit_margin = opeating_income/revenue#/= EBIT/revenue
ROA = (NI+interest_payment*(1-tax_rate))/(average_total_asset)
operating_return_on_asset = opeating_income/average_total_asset
return_on_total_capital = EBIT/average_total_capital
ROE = NI/average_total_equity


activity_ratio = [receivable_turnover,days_of_sales_outstanding,inventory_turnover,days_of_inventory_on_hand\
                  ,total_asset_turnover,fixed_asset_turnover,working_capital_turnover,payable_turnover,numbers_of_days_of_payables]
liquidity_ratio = [current_ratio,quick_ratio,cash_ratio,cash_conversion_cycle]
solvency_ratio = [debt_to_equity,debt_to_capital,debt_to_asset,financial_leverage,interest_coverage,fixed_charge_coverage]
profitability_ratios = [net_profit_margin,gross_profit_margin,operating_profit_margin,ROA,operating_return_on_asset,return_on_total_capital,ROE]

biogen_ratio = pd.DataFrame()
biogen_ratio['activity_ratio'] = activity_ratio
biogen_ratio['liquidity_ratio']=liquidity_ratio+list(np.zeros(5))
biogen_ratio['solvency_ratio'] = solvency_ratio+list(np.zeros(3))
biogen_ratio['profitability_ratios'] = profitability_ratios+list(np.zeros(2))




