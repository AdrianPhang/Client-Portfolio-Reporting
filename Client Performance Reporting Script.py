import csv
import sys
import pandas as pd
import numpy as np

from datetime import datetime

#Configurables
report_date = "31/12/2015"
input = ["30","4502"]

def zero_if_null(value):
    if (value.strip() == ""):
        return "0"
    else:
        return value


for id in input:
    # Variables
    stock1_name = 0
    stock2_name = 0
    stock3_name = 0
    stock4_name = 0
    stock5_name = 0
    stock6_name = 0
    stock7_name = 0

    stock1_idx = 0
    stock2_idx = 0
    stock3_idx = 0
    stock4_idx = 0
    stock5_idx = 0
    stock6_idx = 0
    stock7_idx = 0

    stock1_units = 0
    stock2_units = 0
    stock3_units = 0
    stock4_units = 0
    stock5_units = 0
    stock6_units = 0
    stock7_units = 0

    stock1_invested = 0
    stock2_invested = 0
    stock3_invested = 0
    stock4_invested = 0
    stock5_invested = 0
    stock6_invested = 0
    stock7_invested = 0

    stock1_curr_price = 0
    stock2_curr_price = 0
    stock3_curr_price = 0
    stock4_curr_price = 0
    stock5_curr_price = 0
    stock6_curr_price = 0
    stock7_curr_price = 0

    stock1_ret = 0
    stock2_ret = 0
    stock3_ret = 0
    stock4_ret = 0
    stock5_ret = 0
    stock6_ret = 0
    stock7_ret = 0

    total_count = 0

    with open("portfolios-2.csv","r") as f:
        for l,i in enumerate(f):
            data = i.split(",")
            if data[0] == id:
                amountInvested = data[2]
                stock1 = data[3]
                stock2 = data[4]
                stock3 = data[5]
                stock4 = data[6]
                stock5 = data[7]
                stock6 = data[8]
                stock7 = data[9]
                
                stocks = []
                stocks.append(stock1)
                stocks.append(stock2)
                stocks.append(stock3)
                stocks.append(stock4)
                stocks.append(stock5)
                stocks.append(stock6)
                stocks.append(stock7)

                stock1_weightage = float(zero_if_null(data[10]))
                stock2_weightage = float(zero_if_null(data[11]))
                stock3_weightage = float(zero_if_null(data[12]))
                stock4_weightage = float(zero_if_null(data[13]))
                stock5_weightage = float(zero_if_null(data[14]))
                stock6_weightage = float(zero_if_null(data[15]))
                stock7_weightage = float(zero_if_null(data[16]))

                datetime_str = data[17]
                end_date = datetime.strptime(report_date, "%d/%m/%Y").date()
                start_date = datetime.strptime(datetime_str.strip(), "%d/%m/%Y").date()
                monthDiff = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
                actualMonth = monthDiff+2
                investPerMonth = data[2] # monthly
                principalAmount = data[1] # initial
                
                stock1_initial_amt = float(stock1_weightage)*float(principalAmount)
                stock2_initial_amt = float(stock2_weightage)*float(principalAmount)
                stock3_initial_amt = float(stock3_weightage)*float(principalAmount)
                stock4_initial_amt = float(stock4_weightage)*float(principalAmount)
                stock5_initial_amt = float(stock5_weightage)*float(principalAmount)
                stock6_initial_amt = float(stock6_weightage)*float(principalAmount)
                stock7_initial_amt = float(stock7_weightage)*float(principalAmount)

                stock1_investment_amt_per_month = float(stock1_weightage)*float(investPerMonth)
                stock2_investment_amt_per_month = float(stock2_weightage)*float(investPerMonth)
                stock3_investment_amt_per_month = float(stock3_weightage)*float(investPerMonth)
                stock4_investment_amt_per_month = float(stock4_weightage)*float(investPerMonth)
                stock5_investment_amt_per_month = float(stock5_weightage)*float(investPerMonth)
                stock6_investment_amt_per_month = float(stock6_weightage)*float(investPerMonth)
                stock7_investment_amt_per_month = float(stock7_weightage)*float(investPerMonth)

                investedDate = pd.date_range(start_date, end_date, freq = 'M') 
                investedDate_rev = []
                for i,x in enumerate(investedDate):
                    investedDate_rev.append((investedDate[len(investedDate) - i - 1]).date())
                investedDate_rev.pop()
                investedDate_rev.append(start_date)
                with open("raw_price_data-2.csv","r") as raw_price_data:
                    for l,i in enumerate(raw_price_data):
                        dataHeader = i.split(",")
                        if l == 0:
                            dataHeaderColumn = i.split(",")
                            for num,value in enumerate(dataHeaderColumn):
                                if value == stock1:
                                    stock1_name = value.strip()
                                    stock1_idx = num
                                elif value == stock2:
                                    stock2_name = value.strip()
                                    stock2_idx = num
                                elif value == stock3:
                                    stock3_name = value.strip()
                                    stock3_idx = num
                                elif value == stock4:
                                    stock4_name = value.strip()
                                    stock4_idx = num
                                elif value == stock5:
                                    stock5_name = value.strip()
                                    stock5_idx = num
                                elif value == stock6:
                                    stock6_name = value.strip()
                                    stock6_idx = num
                                elif value == stock7:
                                    stock7_name = value.strip()
                                    stock7_idx = num
                        break
                    
                    for l,idate in enumerate(investedDate_rev):
                        for ll,prices in enumerate(raw_price_data):
                            if (ll == 0):
                                pass
                            priceArr = prices.split(",")
                            price_date = datetime.strptime(priceArr[0].strip(), "%d/%m/%Y").date()
                            
                            if (l == 0 and ll > 0):
                                if (idate >= price_date): # Latest price
                                    if (stock1_idx > 0):
                                        stock1_curr_price = float(priceArr[stock1_idx])
                                    if (stock2_idx > 0):
                                        stock2_curr_price = float(priceArr[stock2_idx])
                                    if (stock3_idx > 0):
                                        stock3_curr_price = float(priceArr[stock3_idx])
                                    if (stock4_idx > 0):
                                        stock4_curr_price = float(priceArr[stock4_idx])
                                    if (stock5_idx > 0):
                                        stock5_curr_price = float(priceArr[stock5_idx])
                                    if (stock6_idx > 0):
                                        stock6_curr_price = float(priceArr[stock6_idx])
                                    if (stock7_idx > 0):
                                        stock7_curr_price = float(priceArr[stock7_idx])
                                    
                            if (idate >= price_date):
                                if (idate > price_date):
                                    priceArr = prev_price_data
                                    price_date = datetime.strptime(priceArr[0].strip(), "%d/%m/%Y").date()
                                if (idate == start_date):
                                    stock1_investment_amt_per_month_new = stock1_initial_amt
                                    stock2_investment_amt_per_month_new = stock2_initial_amt
                                    stock3_investment_amt_per_month_new = stock3_initial_amt
                                    stock4_investment_amt_per_month_new = stock4_initial_amt
                                    stock5_investment_amt_per_month_new = stock5_initial_amt
                                    stock6_investment_amt_per_month_new = stock6_initial_amt
                                    stock7_investment_amt_per_month_new = stock7_initial_amt
                                else:
                                    stock1_investment_amt_per_month_new = stock1_investment_amt_per_month
                                    stock2_investment_amt_per_month_new = stock2_investment_amt_per_month
                                    stock3_investment_amt_per_month_new = stock3_investment_amt_per_month
                                    stock4_investment_amt_per_month_new = stock4_investment_amt_per_month
                                    stock5_investment_amt_per_month_new = stock5_investment_amt_per_month
                                    stock6_investment_amt_per_month_new = stock6_investment_amt_per_month
                                    stock7_investment_amt_per_month_new = stock7_investment_amt_per_month

                                for idx,stock in enumerate(stocks):
                                    if (stock.strip() != ""):
                                        if stock.strip() == dataHeader[stock1_idx].strip():
                                            stock1_invested += stock1_investment_amt_per_month_new
                                            stock1_units += stock1_investment_amt_per_month_new / float(priceArr[stock1_idx])
                                            #print("Picking invest_date: " + str(idate) + " price_date: " + str(price_date))
                                            #print(str(stock.strip()) + "," + str(price_date) + "," + str(priceArr[stock1_idx]) +"," + str(stock1_investment_amt_per_month / float(priceArr[stock1_idx])))
                                        if stock.strip() == dataHeader[stock2_idx].strip():
                                            stock2_invested += stock2_investment_amt_per_month_new
                                            stock2_units += stock2_investment_amt_per_month_new / float(priceArr[stock2_idx])
                                        if stock.strip() == dataHeader[stock3_idx].strip():
                                            stock3_invested += stock3_investment_amt_per_month_new
                                            stock3_units += stock3_investment_amt_per_month_new / float(priceArr[stock3_idx])
                                        if stock.strip() == dataHeader[stock4_idx].strip():
                                            stock4_invested += stock4_investment_amt_per_month_new
                                            stock4_units += stock4_investment_amt_per_month_new / float(priceArr[stock4_idx])
                                        if stock.strip() == dataHeader[stock5_idx].strip():
                                            stock5_invested += stock5_investment_amt_per_month_new
                                            stock5_units += stock5_investment_amt_per_month_new / float(priceArr[stock5_idx])
                                        if stock.strip() == dataHeader[stock6_idx].strip():
                                            stock6_invested += stock6_investment_amt_per_month_new
                                            stock6_units += stock6_investment_amt_per_month_new / float(priceArr[stock6_idx])
                                        if stock.strip() == dataHeader[stock7_idx].strip():
                                            stock7_invested += stock7_investment_amt_per_month_new
                                            stock7_units += stock7_investment_amt_per_month_new / float(priceArr[stock7_idx])
                                break
                            prev_price_data = priceArr
                            
                # Finally
                stock1_mkt = stock1_units * stock1_curr_price
                stock2_mkt = stock2_units * stock2_curr_price
                stock3_mkt = stock3_units * stock3_curr_price
                stock4_mkt = stock4_units * stock4_curr_price
                stock5_mkt = stock5_units * stock5_curr_price
                stock6_mkt = stock6_units * stock6_curr_price
                stock7_mkt = stock7_units * stock7_curr_price
                
                if (stock1_invested > 0):
                    stock1_ret = (stock1_mkt - stock1_invested) / stock1_invested * 100.0
                if (stock2_invested > 0):
                    stock2_ret = (stock2_mkt - stock2_invested) / stock2_invested * 100.0
                if (stock3_invested > 0):
                    stock3_ret = (stock3_mkt - stock3_invested) / stock3_invested * 100.0
                if (stock4_invested > 0):
                    stock4_ret = (stock4_mkt - stock4_invested) / stock4_invested * 100.0
                if (stock5_invested > 0):
                    stock5_ret = (stock5_mkt - stock5_invested) / stock5_invested * 100.0
                if (stock6_invested > 0):
                    stock6_ret = (stock6_mkt - stock6_invested) / stock6_invested * 100.0
                if (stock7_invested > 0):
                    stock7_ret = (stock7_mkt - stock7_invested) / stock7_invested * 100.0

                portfolio_return = ((stock1_mkt + stock2_mkt + stock3_mkt + stock4_mkt + stock5_mkt + stock6_mkt + stock7_mkt) - (stock1_invested + stock2_invested + stock3_invested + stock4_invested + stock5_invested + stock6_invested + stock7_invested)) / (stock1_invested + stock2_invested + stock3_invested + stock4_invested + stock5_invested + stock6_invested + stock7_invested) * 100.0
                    
                # Report Generation
                print("Report Date      : " + datetime.strptime(report_date, "%d/%m/%Y").date().strftime("%Y-%m-%d"))
                print("Portfolio ID     : " + id)
                print("PC Date          : " + datetime.strptime(datetime_str.strip(), "%d/%m/%Y").date().strftime("%Y-%m-%d"))
                print("Portfolio Return : " + "%.1f%%" % (portfolio_return))
                    
                print("")
                print("             " + "%10s" % "Weight (%)" + " %10s" % "Price ($)" + " %15s" % "Units Invt ($)" + " %13s" % "Mkt Value ($)" + " %10s" % "Return (%)")

                if (stock1_name != 0):
                    print(str(stock1_name) + " " + ("%10.1f" % (stock1_weightage*100)) + " " + ("%10.1f" % (stock1_curr_price)) + " " + ("%6.1f" % (stock1_units)) + " " + ("%8.1f" % (stock1_invested)) + " " + ("%13.1f" % (stock1_mkt)) + " " + ("%10.1f" % (stock1_ret)))
                if (stock2_name != 0):
                    print(str(stock2_name) + " " + ("%10.1f" % (stock2_weightage*100)) + " " + ("%10.1f" % (stock2_curr_price)) + " " + ("%6.1f" % (stock2_units)) + " " + ("%8.1f" % (stock2_invested)) + " " + ("%13.1f" % (stock2_mkt)) + " " + ("%10.1f" % (stock2_ret)))
                if (stock3_name != 0):
                    print(str(stock3_name) + " " + ("%10.1f" % (stock3_weightage*100)) + " " + ("%10.1f" % (stock3_curr_price)) + " " + ("%6.1f" % (stock3_units)) + " " + ("%8.1f" % (stock3_invested)) + " " + ("%13.1f" % (stock3_mkt)) + " " + ("%10.1f" % (stock3_ret)))
                if (stock4_name != 0):
                    print(str(stock4_name) + " " + ("%10.1f" % (stock4_weightage*100)) + " " + ("%10.1f" % (stock4_curr_price)) + " " + ("%6.1f" % (stock4_units)) + " " + ("%8.1f" % (stock4_invested)) + " " + ("%13.1f" % (stock4_mkt)) + " " + ("%10.1f" % (stock4_ret)))
                if (stock5_name != 0):
                    print(str(stock5_name) + " " + ("%10.1f" % (stock5_weightage*100)) + " " + ("%10.1f" % (stock5_curr_price)) + " " + ("%6.1f" % (stock5_units)) + " " + ("%8.1f" % (stock5_invested)) + " " + ("%13.1f" % (stock5_mkt)) + " " + ("%10.1f" % (stock5_ret)))
                if (stock6_name != 0):
                    print(str(stock6_name) + " " + ("%10.1f" % (stock6_weightage*100)) + " " + ("%10.1f" % (stock6_curr_price)) + " " + ("%6.1f" % (stock6_units)) + " " + ("%8.1f" % (stock6_invested)) + " " + ("%13.1f" % (stock6_mkt)) + " " + ("%10.1f" % (stock6_ret)))
                if (stock7_name != 0):
                    print(str(stock7_name) + " " + ("%10.1f" % (stock7_weightage*100)) + " " + ("%10.1f" % (stock7_curr_price)) + " " + ("%6.1f" % (stock7_units)) + " " + ("%8.1f" % (stock7_invested)) + " " + ("%13.1f" % (stock7_mkt)) + " " + ("%10.1f" % (stock7_ret)))
                    
                print("")