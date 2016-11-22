#!/usr/bin/env python
# This file was generated using test_runner.py

# import libs
import sys
import math
from flamedb import db
from xmmlreader import agentdata

# load model data
model = agentdata("/media/sander/DataStorage1/GIT/GitLab/ABM@ECB/ABM_at_ECB/code/Financial_Fragility_Network_Model_2.0/eurace_model.xml")
# load database
data  = db("/media/sander/DataStorage-2/Housing_Market_Dataset/sandbox/validation/results/data_input_1600/db/allvars_every20/v1/set_1_run_1_iters.db", model)

C_RED   = ""
C_GREEN = ""
C_END   = ""

def print_equation_evaluation(lhs, rhs, op, passed):
    global C_RED, C_GREEN, C_END
    
    OP_INVERSE = {}
    OP_INVERSE["=="] = "!="
    OP_INVERSE["!="] = "=="
    OP_INVERSE["<"]  = ">="
    OP_INVERSE[">"]  = "<="
    OP_INVERSE["<="] = ">"
    OP_INVERSE[">="] = "<"
    
    if passed: C_START = C_GREEN
    else: C_START = C_RED
    
    L = float(lhs)
    R = float(rhs)
    S = L + R
    LP = "%.4f%%" % (abs(L / S) * 100)
    RP = "%.4f%%" % (abs(R / S) * 100)
    
    if not passed: op = OP_INVERSE[op]
    
    print "                     LHS                         RHS"
    print "    ----------------------------------------------------"
    print "    %20s      %s%s%s %20s" % (lhs, C_START, op, C_END, rhs)
    print "                %8s                     %8s   " % (LP, RP)
    print "    ----------------------------------------------------"
failed = 0
total  = 33
sums = {}
# user generated variables
sums["igfirm_interest_payment"] = data.get_sum_per_iteration("IGFirm","igfirm_outflows_calendar.total_interest_payment")
sums["ecb_bank_deposits"] = data.get_sum_per_iteration("CentralBank","ecb_inflows_calendar.bank_deposits")
sums["gov_debt_installment"] = data.get_sum_per_iteration("Government","gov_outflows_calendar.debt_installment")
sums["bank_total_liabilities"] = data.get_sum_per_iteration("Bank","bank_stocks_calendar.total_liabilities")
sums["bank_cash_day_20"] = data.get_sum_per_iteration("Bank","bank_stocks_calendar.cash_day_20")
sums["firm_energy_costs"] = data.get_sum_per_iteration("Firm","firm_outflows_calendar.energy_costs")
sums["firm_active"] = data.get_sum_per_iteration("Firm","active")
sums["bank_received_interest_payment"] = data.get_sum_per_iteration("Bank","bank_inflows_calendar.firm_interest_payments")
sums["ecb_bank_debt_installment"] = data.get_sum_per_iteration("CentralBank","ecb_inflows_calendar.bank_debt_installment")
sums["gov_total_expenses"] = data.get_sum_per_iteration("Government","gov_outflows_calendar.total_expenses")
sums["igfirm_value_local_inventory"] = data.get_sum_per_iteration("IGFirm","igfirm_stocks_calendar.total_value_local_inventory")
sums["bank_new_ecb_debt"] = data.get_sum_per_iteration("Bank","bank_inflows_calendar.new_ecb_debt")
sums["firm_revenue"] = data.get_sum_per_iteration("Firm","firm_inflows_calendar.cum_revenue")
sums["household_asset_sales"] = data.get_sum_per_iteration("Household","household_inflows_calendar.asset_sales")
sums["bank_total_credit"] = data.get_sum_per_iteration("Bank","bank_stocks_calendar.total_credit")
sums["igfirm_total_debt"] = data.get_sum_per_iteration("IGFirm","igfirm_stocks_calendar.total_debt")
sums["gov_transfer_household"] = data.get_sum_per_iteration("Government","gov_outflows_calendar.transfer_payment_household")
sums["igfirm_outstanding_shares"] = data.get_sum_per_iteration("IGFirm","igfirm_stocks_calendar.current_shares_outstanding")
sums["bank_net_inflow"] = data.get_sum_per_iteration("Bank","bank_inflows_calendar.net_inflow")
sums["firm_new_loans"] = data.get_sum_per_iteration("Firm","firm_inflows_calendar.new_loans")
sums["firm_interest_payment"] = data.get_sum_per_iteration("Firm","firm_outflows_calendar.total_interest_payment")
sums["gov_total_assets"] = data.get_sum_per_iteration("Government","gov_stocks_calendar.total_assets")
sums["igfirm_total_expenses"] = data.get_sum_per_iteration("IGFirm","igfirm_outflows_calendar.total_expenses")
sums["bank_firm_loan_issues"] = data.get_sum_per_iteration("Bank","bank_outflows_calendar.firm_loan_issues")
sums["gov_payment_account_day_1"] = data.get_sum_per_iteration("Government","gov_stocks_calendar.payment_account_day_1")
sums["gov_ecb_debt"] = data.get_sum_per_iteration("Government","gov_stocks_calendar.ecb_money")
sums["bank_total_assets"] = data.get_sum_per_iteration("Bank","bank_stocks_calendar.total_assets")
sums["household_portfolio_value"] = data.get_sum_per_iteration("Household","household_stocks_calendar.portfolio_value")
sums["ecb_fiat_money_banks"] = data.get_sum_per_iteration("CentralBank","ecb_stocks_calendar.fiat_money_banks")
sums["gov_net_inflow"] = data.get_sum_per_iteration("Government","gov_inflows_calendar.net_inflow")
sums["gov_payment_account"] = data.get_sum_per_iteration("Government","gov_stocks_calendar.payment_account")
sums["bank_cash_day_1"] = data.get_sum_per_iteration("Bank","bank_stocks_calendar.cash_day_1")
sums["firm_debt_installment"] = data.get_sum_per_iteration("Firm","firm_outflows_calendar.total_debt_installment_payment")
sums["gov_subsidy_household"] = data.get_sum_per_iteration("Government","gov_outflows_calendar.subsidy_payment_household")
sums["firm_payment_account"] = data.get_sum_per_iteration("Firm","firm_stocks_calendar.payment_account")
sums["household_tax_payment"] = data.get_sum_per_iteration("Household","household_outflows_calendar.tax_payment")
sums["firm_capital_costs"] = data.get_sum_per_iteration("Firm","firm_outflows_calendar.capital_costs")
sums["firm_net_inflow"] = data.get_sum_per_iteration("Firm","firm_inflows_calendar.net_inflow")
sums["bank_outstanding_shares"] = data.get_sum_per_iteration("Bank","bank_stocks_calendar.current_shares_outstanding")
sums["igfirm_value_repurchased_shares"] = data.get_sum_per_iteration("IGFirm","igfirm_outflows_calendar.value_of_repurchased_shares")
sums["igfirm_payment_account_day_20"] = data.get_sum_per_iteration("IGFirm","igfirm_stocks_calendar.payment_account_day_20")
sums["ecb_gov_deposits"] = data.get_sum_per_iteration("CentralBank","ecb_inflows_calendar.gov_deposits")
sums["firm_value_local_inventory"] = data.get_sum_per_iteration("Firm","firm_stocks_calendar.total_value_local_inventory")
sums["household_unemployment_benefit"] = data.get_sum_per_iteration("Household","household_inflows_calendar.unemployment_benefit")
sums["household_asset_purchases"] = data.get_sum_per_iteration("Household","household_outflows_calendar.asset_purchases")
sums["igfirm_energy_costs"] = data.get_sum_per_iteration("IGFirm","igfirm_outflows_calendar.energy_costs")
sums["household_payment_account_day_20"] = data.get_sum_per_iteration("Household","household_stocks_calendar.payment_account_day_20")
sums["bank_equity"] = data.get_sum_per_iteration("Bank","bank_stocks_calendar.equity")
sums["gov_restitution_payment"] = data.get_sum_per_iteration("Government","gov_inflows_calendar.restitution_payment")
sums["firm_equity"] = data.get_sum_per_iteration("Firm","firm_stocks_calendar.equity")
sums["bank_deposit_inflow"] = data.get_sum_per_iteration("Bank","bank_inflows_calendar.deposit_inflow")
sums["ecb_total_assets"] = data.get_sum_per_iteration("CentralBank","ecb_stocks_calendar.total_assets")
sums["firm_total_sold_quantity_volume"] = data.get_sum_per_iteration("Firm","sold_quantity_in_calendar_month")
sums["gov_total_liabilities"] = data.get_sum_per_iteration("Government","gov_stocks_calendar.total_liabilities")
sums["household_payment_account"] = data.get_sum_per_iteration("Household","household_stocks_calendar.payment_account")
sums["firm_total_debt"] = data.get_sum_per_iteration("Firm","firm_stocks_calendar.total_debt")
sums["firm_labour_costs"] = data.get_sum_per_iteration("Firm","firm_outflows_calendar.labour_costs")
sums["household_total_assets"] = data.get_sum_per_iteration("Household","household_stocks_calendar.total_assets")
sums["gov_value_bonds_outstanding"] = data.get_sum_per_iteration("Government","gov_stocks_calendar.value_bonds_outstanding")
sums["eurostat_gdp"] = data.get_sum_per_iteration("Eurostat","gdp")
sums["firm_value_capital_stock"] = data.get_sum_per_iteration("Firm","firm_stocks_calendar.total_value_capital_stock")
sums["igfirm_dividend_payment"] = data.get_sum_per_iteration("IGFirm","igfirm_outflows_calendar.total_dividend_payment")
sums["bank_mortgage_payments"] = data.get_sum_per_iteration("Bank","bank_inflows_calendar.mortgage_payments")
sums["eurostat_sold_quantity"] = data.get_sum_per_iteration("Eurostat","monthly_sold_quantity")
sums["bank_deposits"] = data.get_sum_per_iteration("Bank","bank_stocks_calendar.deposits")
sums["bank_reserves"] = data.get_sum_per_iteration("Bank","bank_stocks_calendar.reserves")
sums["bank_tax_payment"] = data.get_sum_per_iteration("Bank","bank_outflows_calendar.tax_payment")
sums["ecb_nr_gov_bonds"] = data.get_sum_per_iteration("CentralBank","ecb_stocks_calendar.nr_gov_bonds")
sums["household_payment_account_day_1"] = data.get_sum_per_iteration("Household","household_stocks_calendar.payment_account_day_1")
sums["igfirm_net_inflow"] = data.get_sum_per_iteration("IGFirm","igfirm_inflows_calendar.net_inflow")
sums["firm_outstanding_shares"] = data.get_sum_per_iteration("Firm","firm_stocks_calendar.current_shares_outstanding")
sums["household_restitution_payment"] = data.get_sum_per_iteration("Household","household_outflows_calendar.restitution_payment")
sums["eurostat_investment_value"] = data.get_sum_per_iteration("Eurostat","monthly_investment_value")
sums["bank_mortgage_loan_issues"] = data.get_sum_per_iteration("Bank","bank_outflows_calendar.mortgage_loan_issues")
sums["household_total_dividends"] = data.get_sum_per_iteration("Household","household_inflows_calendar.total_dividends")
sums["firm_value_repurchased_shares"] = data.get_sum_per_iteration("Firm","firm_outflows_calendar.value_of_repurchased_shares")
sums["firm_payment_account_day_20"] = data.get_sum_per_iteration("Firm","firm_stocks_calendar.payment_account_day_20")
sums["igfirm_capital_costs"] = data.get_sum_per_iteration("IGFirm","igfirm_outflows_calendar.capital_costs")
sums["gov_nr_bonds_oustanding"] = data.get_sum_per_iteration("Government","gov_stocks_calendar.nr_bonds_outstanding")
sums["household_nr_assets"] = data.get_sum_per_iteration("Household","assetsowned.units")
sums["igfirm_equity"] = data.get_sum_per_iteration("IGFirm","igfirm_stocks_calendar.equity")
sums["firm_value_of_issued_share"] = data.get_sum_per_iteration("Firm","firm_inflows_calendar.value_of_issued_shares")
sums["ecb_bank_fiat_money"] = data.get_sum_per_iteration("CentralBank","ecb_outflows_calendar.bank_fiat_money")
sums["ecb_bank_interest"] = data.get_sum_per_iteration("CentralBank","ecb_inflows_calendar.bank_interest")
sums["bank_debt_installment_to_ecb"] = data.get_sum_per_iteration("Bank","bank_outflows_calendar.debt_installment_to_ecb")
sums["firm_total_expenses"] = data.get_sum_per_iteration("Firm","firm_outflows_calendar.total_expenses")
sums["household_total_income"] = data.get_sum_per_iteration("Household","household_inflows_calendar.total_income")
sums["gov_money_financing"] = data.get_sum_per_iteration("Government","gov_inflows_calendar.total_money_financing")
sums["household_wage"] = data.get_sum_per_iteration("Household","household_inflows_calendar.wage")
sums["household_subsidies"] = data.get_sum_per_iteration("Household","household_inflows_calendar.subsidies")
sums["ecb_payment_account_govs"] = data.get_sum_per_iteration("CentralBank","ecb_stocks_calendar.payment_account_govs")
sums["gov_benefit_payment"] = data.get_sum_per_iteration("Government","gov_outflows_calendar.benefit_payment")
sums["igfirm_payment_account_day_1"] = data.get_sum_per_iteration("IGFirm","igfirm_stocks_calendar.payment_account_day_1")
sums["bank_net_deposit_inflow"] = data.get_sum_per_iteration("Bank","bank_inflows_calendar.net_deposit_inflow")
sums["ecb_payment_account_banks"] = data.get_sum_per_iteration("CentralBank","ecb_stocks_calendar.payment_account_banks")
sums["gov_bond_interest_payment"] = data.get_sum_per_iteration("Government","gov_outflows_calendar.bond_interest_payment")
sums["eurostat_active_firms"] = data.get_sum_per_iteration("Eurostat","no_active_firms")
sums["bank_ecb_interest_payment"] = data.get_sum_per_iteration("Bank","bank_outflows_calendar.ecb_interest_payment")
sums["igfirm_revenue"] = data.get_sum_per_iteration("IGFirm","igfirm_inflows_calendar.cum_revenue")
sums["bank_cash"] = data.get_sum_per_iteration("Bank","bank_stocks_calendar.cash")
sums["household_gov_interest"] = data.get_sum_per_iteration("Household","household_inflows_calendar.gov_interest")
sums["gov_bond_financing"] = data.get_sum_per_iteration("Government","gov_inflows_calendar.total_bond_financing")
sums["bank_total_income"] = data.get_sum_per_iteration("Bank","bank_inflows_calendar.total_income")
sums["gov_bond_repurchase"] = data.get_sum_per_iteration("Government","gov_outflows_calendar.total_bond_repurchase")
sums["igfirm_tax_payment"] = data.get_sum_per_iteration("IGFirm","igfirm_outflows_calendar.tax_payment")
sums["igfirm_total_income"] = data.get_sum_per_iteration("IGFirm","igfirm_inflows_calendar.total_income")
sums["gov_tax_revenue"] = data.get_sum_per_iteration("Government","gov_inflows_calendar.tax_revenues")
sums["gov_transfer_firm"] = data.get_sum_per_iteration("Government","gov_outflows_calendar.transfer_payment_firm")
sums["household_net_inflow"] = data.get_sum_per_iteration("Household","household_inflows_calendar.net_inflow")
sums["igfirm_value_of_issued_share"] = data.get_sum_per_iteration("IGFirm","igfirm_inflows_calendar.value_of_issued_shares")
sums["ecb_cash"] = data.get_sum_per_iteration("CentralBank","ecb_stocks_calendar.cash")
sums["firm_dividend_payment"] = data.get_sum_per_iteration("Firm","firm_outflows_calendar.total_dividend_payment")
sums["gov_payment_account_day_20"] = data.get_sum_per_iteration("Government","gov_stocks_calendar.payment_account_day_20")
sums["ecb_total_liabilities"] = data.get_sum_per_iteration("CentralBank","ecb_stocks_calendar.total_liabilities")
sums["bank_dividend_payment"] = data.get_sum_per_iteration("Bank","bank_outflows_calendar.dividend_payment")
sums["household_transfer"] = data.get_sum_per_iteration("Household","household_inflows_calendar.transfer")
sums["igfirm_payment_account"] = data.get_sum_per_iteration("IGFirm","igfirm_stocks_calendar.payment_account")
sums["gov_equity"] = data.get_sum_per_iteration("Government","gov_stocks_calendar.equity")
sums["igfirm_active"] = data.get_sum_per_iteration("IGFirm","active")
sums["firm_total_assets"] = data.get_sum_per_iteration("Firm","firm_stocks_calendar.total_assets")
sums["ecb_fiat_money"] = data.get_sum_per_iteration("CentralBank","ecb_stocks_calendar.fiat_money")
sums["bank_deposit_outflow"] = data.get_sum_per_iteration("Bank","bank_outflows_calendar.deposit_outflow")
sums["igfirm_new_loans"] = data.get_sum_per_iteration("IGFirm","igfirm_inflows_calendar.new_loans")
sums["firm_total_income"] = data.get_sum_per_iteration("Firm","firm_inflows_calendar.total_income")
sums["ecb_total_expenses"] = data.get_sum_per_iteration("CentralBank","ecb_outflows_calendar.total_expenses")
sums["household_total_expenses"] = data.get_sum_per_iteration("Household","household_outflows_calendar.total_expenses")
sums["igfirm_value_capital_stock"] = data.get_sum_per_iteration("IGFirm","igfirm_stocks_calendar.total_value_capital_stock")
sums["firm_tax_payment"] = data.get_sum_per_iteration("Firm","firm_outflows_calendar.tax_payment")
sums["gov_ecb_dividend"] = data.get_sum_per_iteration("Government","gov_inflows_calendar.ecb_dividend")
sums["bank_total_expenses"] = data.get_sum_per_iteration("Bank","bank_outflows_calendar.total_expenses")
sums["ecb_gov_interst"] = data.get_sum_per_iteration("CentralBank","ecb_inflows_calendar.gov_interest")
sums["firm_subsidy"] = data.get_sum_per_iteration("Firm","firm_inflows_calendar.subsidy")
sums["ecb_gov_bond_purchase"] = data.get_sum_per_iteration("CentralBank","ecb_outflows_calendar.gov_bond_purchase")
sums["ecb_net_inflow"] = data.get_sum_per_iteration("CentralBank","ecb_inflows_calendar.net_inflow")
sums["gov_consumption_expenditure"] = data.get_sum_per_iteration("Government","gov_outflows_calendar.consumption_expenditure")
sums["bank_ecb_debt"] = data.get_sum_per_iteration("Bank","bank_stocks_calendar.ecb_debt")
sums["igfirm_subsidy"] = data.get_sum_per_iteration("IGFirm","igfirm_inflows_calendar.subsidy")
sums["eurostat_no_firms"] = data.get_sum_per_iteration("Eurostat","no_firms")
sums["ecb_equity"] = data.get_sum_per_iteration("CentralBank","ecb_stocks_calendar.equity")
sums["firm_payment_account_day_1"] = data.get_sum_per_iteration("Firm","firm_stocks_calendar.payment_account_day_1")
sums["ecb_fiat_money_govs"] = data.get_sum_per_iteration("CentralBank","ecb_stocks_calendar.fiat_money_govs")
sums["bank_loan_loss_reserve"] = data.get_sum_per_iteration("Bank","bank_stocks_calendar.loan_loss_reserve")
sums["household_consumption_expenditure"] = data.get_sum_per_iteration("Household","household_outflows_calendar.consumption_expenditure")
sums["igfirm_total_assets"] = data.get_sum_per_iteration("IGFirm","igfirm_stocks_calendar.total_assets")
sums["ecb_dividend_payment"] = data.get_sum_per_iteration("CentralBank","ecb_outflows_calendar.dividend_payment")
sums["gov_investment_expenditure"] = data.get_sum_per_iteration("Government","gov_outflows_calendar.investment_expenditure")
sums["igfirm_labour_costs"] = data.get_sum_per_iteration("IGFirm","igfirm_outflows_calendar.labour_costs")
sums["igfirm_total_liabilities"] = data.get_sum_per_iteration("IGFirm","igfirm_stocks_calendar.total_liabilities")
sums["bank_received_loan_installment"] = data.get_sum_per_iteration("Bank","bank_inflows_calendar.firm_loan_installments")
sums["ecb_gov_bond_holdings"] = data.get_sum_per_iteration("CentralBank","ecb_stocks_calendar.gov_bond_holdings")
sums["eurostat_no_firm_deaths"] = data.get_sum_per_iteration("Eurostat","no_firm_deaths")
sums["firm_total_liabilities"] = data.get_sum_per_iteration("Firm","firm_stocks_calendar.total_liabilities")
sums["ecb_total_income"] = data.get_sum_per_iteration("CentralBank","ecb_inflows_calendar.total_income")
sums["gov_subsidy_firm"] = data.get_sum_per_iteration("Government","gov_outflows_calendar.subsidy_payment_firm")
sums["gov_total_income"] = data.get_sum_per_iteration("Government","gov_inflows_calendar.total_income")
sums["igfirm_debt_installment"] = data.get_sum_per_iteration("IGFirm","igfirm_outflows_calendar.total_debt_installment_payment")


def test_rule_1_of_33():
    global failed
    success = True
    print ""    
    print " %s" % ("."*76)
    print ""
    print "RULE 1 : abs (  firm_payment_account  +  firm_value_local_inventory  +  firm_value_capital_stock  -  firm_total_debt  -  firm_equity )  <  PRECISION"
    for i in data.get_list_of_iterations():
        print ""
        print ""
        print "              ---- [ Iteration %d : " % i,
        if abs ( sums['firm_payment_account'][i] + sums['firm_value_local_inventory'][i] + sums['firm_value_capital_stock'][i] - sums['firm_total_debt'][i] - sums['firm_equity'][i] ) < 1.000000: 
            print "OK ] ----"
        else:
            success = False
            print "FAIL ] ----"
        lhs = eval("abs ( sums['firm_payment_account'][i] + sums['firm_value_local_inventory'][i] + sums['firm_value_capital_stock'][i] - sums['firm_total_debt'][i] - sums['firm_equity'][i] )")
        rhs = eval("1.000000")
        print ""
        print_equation_evaluation(lhs, rhs, "<", success)
        print ""

        maxintlen = 10
        vv = eval("sums['firm_payment_account'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    firm_payment_account              = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['firm_value_local_inventory'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    firm_value_local_inventory        = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['firm_value_capital_stock'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    firm_value_capital_stock          = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['firm_total_debt'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    firm_total_debt                   = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['firm_equity'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    firm_equity                       = %s%f" % ((" " * spacer),vv)
    if not success: failed += 1


def test_rule_2_of_33():
    global failed
    success = True
    print ""    
    print " %s" % ("."*76)
    print ""
    print "RULE 2 : abs (  igfirm_payment_account  +  igfirm_value_local_inventory  +  igfirm_value_capital_stock  -  igfirm_total_debt  -  igfirm_equity )  <  PRECISION"
    for i in data.get_list_of_iterations():
        print ""
        print ""
        print "              ---- [ Iteration %d : " % i,
        if abs ( sums['igfirm_payment_account'][i] + sums['igfirm_value_local_inventory'][i] + sums['igfirm_value_capital_stock'][i] - sums['igfirm_total_debt'][i] - sums['igfirm_equity'][i] ) < 1.000000: 
            print "OK ] ----"
        else:
            success = False
            print "FAIL ] ----"
        lhs = eval("abs ( sums['igfirm_payment_account'][i] + sums['igfirm_value_local_inventory'][i] + sums['igfirm_value_capital_stock'][i] - sums['igfirm_total_debt'][i] - sums['igfirm_equity'][i] )")
        rhs = eval("1.000000")
        print ""
        print_equation_evaluation(lhs, rhs, "<", success)
        print ""

        maxintlen = 10
        vv = eval("sums['igfirm_payment_account'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    igfirm_payment_account            = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['igfirm_value_local_inventory'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    igfirm_value_local_inventory      = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['igfirm_value_capital_stock'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    igfirm_value_capital_stock        = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['igfirm_total_debt'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    igfirm_total_debt                 = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['igfirm_equity'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    igfirm_equity                     = %s%f" % ((" " * spacer),vv)
    if not success: failed += 1


def test_rule_3_of_33():
    global failed
    success = True
    print ""    
    print " %s" % ("."*76)
    print ""
    print "RULE 3 : abs (  bank_cash  +  bank_reserves  +  bank_total_credit  -  bank_deposits  -  bank_ecb_debt  -  bank_equity  -  bank_loan_loss_reserve )  <  PRECISION"
    for i in data.get_list_of_iterations():
        print ""
        print ""
        print "              ---- [ Iteration %d : " % i,
        if abs ( sums['bank_cash'][i] + sums['bank_reserves'][i] + sums['bank_total_credit'][i] - sums['bank_deposits'][i] - sums['bank_ecb_debt'][i] - sums['bank_equity'][i] - sums['bank_loan_loss_reserve'][i] ) < 1.000000: 
            print "OK ] ----"
        else:
            success = False
            print "FAIL ] ----"
        lhs = eval("abs ( sums['bank_cash'][i] + sums['bank_reserves'][i] + sums['bank_total_credit'][i] - sums['bank_deposits'][i] - sums['bank_ecb_debt'][i] - sums['bank_equity'][i] - sums['bank_loan_loss_reserve'][i] )")
        rhs = eval("1.000000")
        print ""
        print_equation_evaluation(lhs, rhs, "<", success)
        print ""

        maxintlen = 10
        vv = eval("sums['bank_cash'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    bank_cash                         = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['bank_reserves'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    bank_reserves                     = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['bank_total_credit'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    bank_total_credit                 = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['bank_deposits'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    bank_deposits                     = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['bank_ecb_debt'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    bank_ecb_debt                     = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['bank_equity'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    bank_equity                       = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['bank_loan_loss_reserve'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    bank_loan_loss_reserve            = %s%f" % ((" " * spacer),vv)
    if not success: failed += 1


def test_rule_4_of_33():
    global failed
    success = True
    print ""    
    print " %s" % ("."*76)
    print ""
    print "RULE 4 : abs (  gov_payment_account  -  gov_value_bonds_outstanding  -  gov_ecb_debt  -  gov_equity )  <  PRECISION"
    for i in data.get_list_of_iterations():
        print ""
        print ""
        print "              ---- [ Iteration %d : " % i,
        if abs ( sums['gov_payment_account'][i] - sums['gov_value_bonds_outstanding'][i] - sums['gov_ecb_debt'][i] - sums['gov_equity'][i] ) < 1.000000: 
            print "OK ] ----"
        else:
            success = False
            print "FAIL ] ----"
        lhs = eval("abs ( sums['gov_payment_account'][i] - sums['gov_value_bonds_outstanding'][i] - sums['gov_ecb_debt'][i] - sums['gov_equity'][i] )")
        rhs = eval("1.000000")
        print ""
        print_equation_evaluation(lhs, rhs, "<", success)
        print ""

        maxintlen = 10
        vv = eval("sums['gov_payment_account'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    gov_payment_account               = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['gov_value_bonds_outstanding'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    gov_value_bonds_outstanding       = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['gov_ecb_debt'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    gov_ecb_debt                      = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['gov_equity'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    gov_equity                        = %s%f" % ((" " * spacer),vv)
    if not success: failed += 1


def test_rule_5_of_33():
    global failed
    success = True
    print ""    
    print " %s" % ("."*76)
    print ""
    print "RULE 5 : abs (  ecb_cash  +  ecb_gov_bond_holdings  +  ecb_fiat_money_banks  -  ecb_payment_account_banks  -  ecb_payment_account_govs  -  ecb_fiat_money  -  ecb_equity )  <  PRECISION"
    for i in data.get_list_of_iterations():
        print ""
        print ""
        print "              ---- [ Iteration %d : " % i,
        if abs ( sums['ecb_cash'][i] + sums['ecb_gov_bond_holdings'][i] + sums['ecb_fiat_money_banks'][i] - sums['ecb_payment_account_banks'][i] - sums['ecb_payment_account_govs'][i] - sums['ecb_fiat_money'][i] - sums['ecb_equity'][i] ) < 1.000000: 
            print "OK ] ----"
        else:
            success = False
            print "FAIL ] ----"
        lhs = eval("abs ( sums['ecb_cash'][i] + sums['ecb_gov_bond_holdings'][i] + sums['ecb_fiat_money_banks'][i] - sums['ecb_payment_account_banks'][i] - sums['ecb_payment_account_govs'][i] - sums['ecb_fiat_money'][i] - sums['ecb_equity'][i] )")
        rhs = eval("1.000000")
        print ""
        print_equation_evaluation(lhs, rhs, "<", success)
        print ""

        maxintlen = 10
        vv = eval("sums['ecb_cash'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    ecb_cash                          = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['ecb_gov_bond_holdings'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    ecb_gov_bond_holdings             = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['ecb_fiat_money_banks'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    ecb_fiat_money_banks              = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['ecb_payment_account_banks'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    ecb_payment_account_banks         = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['ecb_payment_account_govs'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    ecb_payment_account_govs          = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['ecb_fiat_money'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    ecb_fiat_money                    = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['ecb_equity'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    ecb_equity                        = %s%f" % ((" " * spacer),vv)
    if not success: failed += 1


def test_rule_6_of_33():
    global failed
    success = True
    print ""    
    print " %s" % ("."*76)
    print ""
    print "RULE 6 : abs (  firm_net_inflow  -  firm_payment_account_day_20  +  firm_payment_account_day_1 )  <  PRECISION"
    for i in data.get_list_of_iterations():
        print ""
        print ""
        print "              ---- [ Iteration %d : " % i,
        if abs ( sums['firm_net_inflow'][i] - sums['firm_payment_account_day_20'][i] + sums['firm_payment_account_day_1'][i] ) < 1.000000: 
            print "OK ] ----"
        else:
            success = False
            print "FAIL ] ----"
        lhs = eval("abs ( sums['firm_net_inflow'][i] - sums['firm_payment_account_day_20'][i] + sums['firm_payment_account_day_1'][i] )")
        rhs = eval("1.000000")
        print ""
        print_equation_evaluation(lhs, rhs, "<", success)
        print ""

        maxintlen = 10
        vv = eval("sums['firm_net_inflow'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    firm_net_inflow                   = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['firm_payment_account_day_20'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    firm_payment_account_day_20       = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['firm_payment_account_day_1'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    firm_payment_account_day_1        = %s%f" % ((" " * spacer),vv)
    if not success: failed += 1


def test_rule_7_of_33():
    global failed
    success = True
    print ""    
    print " %s" % ("."*76)
    print ""
    print "RULE 7 : abs (  igfirm_net_inflow  -  igfirm_payment_account_day_20  +  igfirm_payment_account_day_1 )  <  PRECISION"
    for i in data.get_list_of_iterations():
        print ""
        print ""
        print "              ---- [ Iteration %d : " % i,
        if abs ( sums['igfirm_net_inflow'][i] - sums['igfirm_payment_account_day_20'][i] + sums['igfirm_payment_account_day_1'][i] ) < 1.000000: 
            print "OK ] ----"
        else:
            success = False
            print "FAIL ] ----"
        lhs = eval("abs ( sums['igfirm_net_inflow'][i] - sums['igfirm_payment_account_day_20'][i] + sums['igfirm_payment_account_day_1'][i] )")
        rhs = eval("1.000000")
        print ""
        print_equation_evaluation(lhs, rhs, "<", success)
        print ""

        maxintlen = 10
        vv = eval("sums['igfirm_net_inflow'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    igfirm_net_inflow                 = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['igfirm_payment_account_day_20'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    igfirm_payment_account_day_20     = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['igfirm_payment_account_day_1'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    igfirm_payment_account_day_1      = %s%f" % ((" " * spacer),vv)
    if not success: failed += 1


def test_rule_8_of_33():
    global failed
    success = True
    print ""    
    print " %s" % ("."*76)
    print ""
    print "RULE 8 : abs (  household_net_inflow  -  household_payment_account_day_20  +  household_payment_account_day_1 )  <  PRECISION"
    for i in data.get_list_of_iterations():
        print ""
        print ""
        print "              ---- [ Iteration %d : " % i,
        if abs ( sums['household_net_inflow'][i] - sums['household_payment_account_day_20'][i] + sums['household_payment_account_day_1'][i] ) < 1.000000: 
            print "OK ] ----"
        else:
            success = False
            print "FAIL ] ----"
        lhs = eval("abs ( sums['household_net_inflow'][i] - sums['household_payment_account_day_20'][i] + sums['household_payment_account_day_1'][i] )")
        rhs = eval("1.000000")
        print ""
        print_equation_evaluation(lhs, rhs, "<", success)
        print ""

        maxintlen = 10
        vv = eval("sums['household_net_inflow'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    household_net_inflow              = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['household_payment_account_day_20'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    household_payment_account_day_20  = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['household_payment_account_day_1'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    household_payment_account_day_1   = %s%f" % ((" " * spacer),vv)
    if not success: failed += 1


def test_rule_9_of_33():
    global failed
    success = True
    print ""    
    print " %s" % ("."*76)
    print ""
    print "RULE 9 : abs (  bank_net_inflow  -  bank_cash_day_20  +  bank_cash_day_1 )  <  PRECISION"
    for i in data.get_list_of_iterations():
        print ""
        print ""
        print "              ---- [ Iteration %d : " % i,
        if abs ( sums['bank_net_inflow'][i] - sums['bank_cash_day_20'][i] + sums['bank_cash_day_1'][i] ) < 1.000000: 
            print "OK ] ----"
        else:
            success = False
            print "FAIL ] ----"
        lhs = eval("abs ( sums['bank_net_inflow'][i] - sums['bank_cash_day_20'][i] + sums['bank_cash_day_1'][i] )")
        rhs = eval("1.000000")
        print ""
        print_equation_evaluation(lhs, rhs, "<", success)
        print ""

        maxintlen = 10
        vv = eval("sums['bank_net_inflow'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    bank_net_inflow                   = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['bank_cash_day_20'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    bank_cash_day_20                  = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['bank_cash_day_1'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    bank_cash_day_1                   = %s%f" % ((" " * spacer),vv)
    if not success: failed += 1


def test_rule_10_of_33():
    global failed
    success = True
    print ""    
    print " %s" % ("."*76)
    print ""
    print "RULE 10 : abs (  gov_net_inflow  -  gov_payment_account_day_20  +  gov_payment_account_day_1 )  <  PRECISION"
    for i in data.get_list_of_iterations():
        print ""
        print ""
        print "              ---- [ Iteration %d : " % i,
        if abs ( sums['gov_net_inflow'][i] - sums['gov_payment_account_day_20'][i] + sums['gov_payment_account_day_1'][i] ) < 1.000000: 
            print "OK ] ----"
        else:
            success = False
            print "FAIL ] ----"
        lhs = eval("abs ( sums['gov_net_inflow'][i] - sums['gov_payment_account_day_20'][i] + sums['gov_payment_account_day_1'][i] )")
        rhs = eval("1.000000")
        print ""
        print_equation_evaluation(lhs, rhs, "<", success)
        print ""

        maxintlen = 10
        vv = eval("sums['gov_net_inflow'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    gov_net_inflow                    = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['gov_payment_account_day_20'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    gov_payment_account_day_20        = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['gov_payment_account_day_1'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    gov_payment_account_day_1         = %s%f" % ((" " * spacer),vv)
    if not success: failed += 1


def test_rule_11_of_33():
    global failed
    success = True
    print ""    
    print " %s" % ("."*76)
    print ""
    print "RULE 11 : abs (  firm_payment_account_day_20  +  igfirm_payment_account_day_20  +  household_payment_account_day_20  -  bank_deposits )   <  PRECISION"
    for i in data.get_list_of_iterations():
        print ""
        print ""
        print "              ---- [ Iteration %d : " % i,
        if abs ( sums['firm_payment_account_day_20'][i] + sums['igfirm_payment_account_day_20'][i] + sums['household_payment_account_day_20'][i] - sums['bank_deposits'][i] ) < 1.000000: 
            print "OK ] ----"
        else:
            success = False
            print "FAIL ] ----"
        lhs = eval("abs ( sums['firm_payment_account_day_20'][i] + sums['igfirm_payment_account_day_20'][i] + sums['household_payment_account_day_20'][i] - sums['bank_deposits'][i] )")
        rhs = eval("1.000000")
        print ""
        print_equation_evaluation(lhs, rhs, "<", success)
        print ""

        maxintlen = 10
        vv = eval("sums['firm_payment_account_day_20'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    firm_payment_account_day_20       = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['igfirm_payment_account_day_20'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    igfirm_payment_account_day_20     = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['household_payment_account_day_20'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    household_payment_account_day_20  = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['bank_deposits'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    bank_deposits                     = %s%f" % ((" " * spacer),vv)
    if not success: failed += 1


def test_rule_12_of_33():
    global failed
    success = True
    print ""    
    print " %s" % ("."*76)
    print ""
    print "RULE 12 : abs (  bank_total_credit  -  firm_total_debt  -  igfirm_total_debt  )   <  PRECISION"
    for i in data.get_list_of_iterations():
        print ""
        print ""
        print "              ---- [ Iteration %d : " % i,
        if abs ( sums['bank_total_credit'][i] - sums['firm_total_debt'][i] - sums['igfirm_total_debt'][i] ) < 1.000000: 
            print "OK ] ----"
        else:
            success = False
            print "FAIL ] ----"
        lhs = eval("abs ( sums['bank_total_credit'][i] - sums['firm_total_debt'][i] - sums['igfirm_total_debt'][i] )")
        rhs = eval("1.000000")
        print ""
        print_equation_evaluation(lhs, rhs, "<", success)
        print ""

        maxintlen = 10
        vv = eval("sums['bank_total_credit'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    bank_total_credit                 = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['firm_total_debt'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    firm_total_debt                   = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['igfirm_total_debt'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    igfirm_total_debt                 = %s%f" % ((" " * spacer),vv)
    if not success: failed += 1


def test_rule_13_of_33():
    global failed
    success = True
    print ""    
    print " %s" % ("."*76)
    print ""
    print "RULE 13 : abs (  firm_net_inflow  +  igfirm_net_inflow  +  household_net_inflow  -  bank_net_deposit_inflow )   <  PRECISION"
    for i in data.get_list_of_iterations():
        print ""
        print ""
        print "              ---- [ Iteration %d : " % i,
        if abs ( sums['firm_net_inflow'][i] + sums['igfirm_net_inflow'][i] + sums['household_net_inflow'][i] - sums['bank_net_deposit_inflow'][i] ) < 1.000000: 
            print "OK ] ----"
        else:
            success = False
            print "FAIL ] ----"
        lhs = eval("abs ( sums['firm_net_inflow'][i] + sums['igfirm_net_inflow'][i] + sums['household_net_inflow'][i] - sums['bank_net_deposit_inflow'][i] )")
        rhs = eval("1.000000")
        print ""
        print_equation_evaluation(lhs, rhs, "<", success)
        print ""

        maxintlen = 10
        vv = eval("sums['firm_net_inflow'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    firm_net_inflow                   = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['igfirm_net_inflow'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    igfirm_net_inflow                 = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['household_net_inflow'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    household_net_inflow              = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['bank_net_deposit_inflow'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    bank_net_deposit_inflow           = %s%f" % ((" " * spacer),vv)
    if not success: failed += 1


def test_rule_14_of_33():
    global failed
    success = True
    print ""    
    print " %s" % ("."*76)
    print ""
    print "RULE 14 : abs (  firm_debt_installment  +  igfirm_debt_installment  -  bank_received_loan_installment )   <  PRECISION"
    for i in data.get_list_of_iterations():
        print ""
        print ""
        print "              ---- [ Iteration %d : " % i,
        if abs ( sums['firm_debt_installment'][i] + sums['igfirm_debt_installment'][i] - sums['bank_received_loan_installment'][i] ) < 1.000000: 
            print "OK ] ----"
        else:
            success = False
            print "FAIL ] ----"
        lhs = eval("abs ( sums['firm_debt_installment'][i] + sums['igfirm_debt_installment'][i] - sums['bank_received_loan_installment'][i] )")
        rhs = eval("1.000000")
        print ""
        print_equation_evaluation(lhs, rhs, "<", success)
        print ""

        maxintlen = 10
        vv = eval("sums['firm_debt_installment'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    firm_debt_installment             = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['igfirm_debt_installment'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    igfirm_debt_installment           = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['bank_received_loan_installment'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    bank_received_loan_installment    = %s%f" % ((" " * spacer),vv)
    if not success: failed += 1


def test_rule_15_of_33():
    global failed
    success = True
    print ""    
    print " %s" % ("."*76)
    print ""
    print "RULE 15 : abs (  firm_interest_payment  +  igfirm_interest_payment  -  bank_received_interest_payment )   <  PRECISION"
    for i in data.get_list_of_iterations():
        print ""
        print ""
        print "              ---- [ Iteration %d : " % i,
        if abs ( sums['firm_interest_payment'][i] + sums['igfirm_interest_payment'][i] - sums['bank_received_interest_payment'][i] ) < 1.000000: 
            print "OK ] ----"
        else:
            success = False
            print "FAIL ] ----"
        lhs = eval("abs ( sums['firm_interest_payment'][i] + sums['igfirm_interest_payment'][i] - sums['bank_received_interest_payment'][i] )")
        rhs = eval("1.000000")
        print ""
        print_equation_evaluation(lhs, rhs, "<", success)
        print ""

        maxintlen = 10
        vv = eval("sums['firm_interest_payment'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    firm_interest_payment             = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['igfirm_interest_payment'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    igfirm_interest_payment           = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['bank_received_interest_payment'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    bank_received_interest_payment    = %s%f" % ((" " * spacer),vv)
    if not success: failed += 1


def test_rule_16_of_33():
    global failed
    success = True
    print ""    
    print " %s" % ("."*76)
    print ""
    print "RULE 16 : abs (  firm_dividend_payment  +  igfirm_dividend_payment  +  bank_dividend_payment  -  household_total_dividends )   <  PRECISION"
    for i in data.get_list_of_iterations():
        print ""
        print ""
        print "              ---- [ Iteration %d : " % i,
        if abs ( sums['firm_dividend_payment'][i] + sums['igfirm_dividend_payment'][i] + sums['bank_dividend_payment'][i] - sums['household_total_dividends'][i] ) < 1.000000: 
            print "OK ] ----"
        else:
            success = False
            print "FAIL ] ----"
        lhs = eval("abs ( sums['firm_dividend_payment'][i] + sums['igfirm_dividend_payment'][i] + sums['bank_dividend_payment'][i] - sums['household_total_dividends'][i] )")
        rhs = eval("1.000000")
        print ""
        print_equation_evaluation(lhs, rhs, "<", success)
        print ""

        maxintlen = 10
        vv = eval("sums['firm_dividend_payment'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    firm_dividend_payment             = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['igfirm_dividend_payment'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    igfirm_dividend_payment           = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['bank_dividend_payment'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    bank_dividend_payment             = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['household_total_dividends'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    household_total_dividends         = %s%f" % ((" " * spacer),vv)
    if not success: failed += 1


def test_rule_17_of_33():
    global failed
    success = True
    print ""    
    print " %s" % ("."*76)
    print ""
    print "RULE 17 : abs (  firm_capital_costs  -  igfirm_revenue )   <  PRECISION"
    for i in data.get_list_of_iterations():
        print ""
        print ""
        print "              ---- [ Iteration %d : " % i,
        if abs ( sums['firm_capital_costs'][i] - sums['igfirm_revenue'][i] ) < 1.000000: 
            print "OK ] ----"
        else:
            success = False
            print "FAIL ] ----"
        lhs = eval("abs ( sums['firm_capital_costs'][i] - sums['igfirm_revenue'][i] )")
        rhs = eval("1.000000")
        print ""
        print_equation_evaluation(lhs, rhs, "<", success)
        print ""

        maxintlen = 10
        vv = eval("sums['firm_capital_costs'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    firm_capital_costs                = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['igfirm_revenue'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    igfirm_revenue                    = %s%f" % ((" " * spacer),vv)
    if not success: failed += 1


def test_rule_18_of_33():
    global failed
    success = True
    print ""    
    print " %s" % ("."*76)
    print ""
    print "RULE 18 : abs (  household_wage  -  firm_labour_costs  -  igfirm_labour_costs )   <  PRECISION"
    for i in data.get_list_of_iterations():
        print ""
        print ""
        print "              ---- [ Iteration %d : " % i,
        if abs ( sums['household_wage'][i] - sums['firm_labour_costs'][i] - sums['igfirm_labour_costs'][i] ) < 1.000000: 
            print "OK ] ----"
        else:
            success = False
            print "FAIL ] ----"
        lhs = eval("abs ( sums['household_wage'][i] - sums['firm_labour_costs'][i] - sums['igfirm_labour_costs'][i] )")
        rhs = eval("1.000000")
        print ""
        print_equation_evaluation(lhs, rhs, "<", success)
        print ""

        maxintlen = 10
        vv = eval("sums['household_wage'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    household_wage                    = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['firm_labour_costs'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    firm_labour_costs                 = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['igfirm_labour_costs'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    igfirm_labour_costs               = %s%f" % ((" " * spacer),vv)
    if not success: failed += 1


def test_rule_19_of_33():
    global failed
    success = True
    print ""    
    print " %s" % ("."*76)
    print ""
    print "RULE 19 : abs (  household_consumption_expenditure  -  firm_revenue )   <  PRECISION"
    for i in data.get_list_of_iterations():
        print ""
        print ""
        print "              ---- [ Iteration %d : " % i,
        if abs ( sums['household_consumption_expenditure'][i] - sums['firm_revenue'][i] ) < 1.000000: 
            print "OK ] ----"
        else:
            success = False
            print "FAIL ] ----"
        lhs = eval("abs ( sums['household_consumption_expenditure'][i] - sums['firm_revenue'][i] )")
        rhs = eval("1.000000")
        print ""
        print_equation_evaluation(lhs, rhs, "<", success)
        print ""

        maxintlen = 10
        vv = eval("sums['household_consumption_expenditure'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    household_consumption_expenditure = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['firm_revenue'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    firm_revenue                      = %s%f" % ((" " * spacer),vv)
    if not success: failed += 1


def test_rule_20_of_33():
    global failed
    success = True
    print ""    
    print " %s" % ("."*76)
    print ""
    print "RULE 20 : abs (  eurostat_gdp  -  eurostat_investment_value  -  household_consumption_expenditure  -  gov_consumption_expenditure  )   <  PRECISION"
    for i in data.get_list_of_iterations():
        print ""
        print ""
        print "              ---- [ Iteration %d : " % i,
        if abs ( sums['eurostat_gdp'][i] - sums['eurostat_investment_value'][i] - sums['household_consumption_expenditure'][i] - sums['gov_consumption_expenditure'][i] ) < 1.000000: 
            print "OK ] ----"
        else:
            success = False
            print "FAIL ] ----"
        lhs = eval("abs ( sums['eurostat_gdp'][i] - sums['eurostat_investment_value'][i] - sums['household_consumption_expenditure'][i] - sums['gov_consumption_expenditure'][i] )")
        rhs = eval("1.000000")
        print ""
        print_equation_evaluation(lhs, rhs, "<", success)
        print ""

        maxintlen = 10
        vv = eval("sums['eurostat_gdp'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    eurostat_gdp                      = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['eurostat_investment_value'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    eurostat_investment_value         = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['household_consumption_expenditure'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    household_consumption_expenditure = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['gov_consumption_expenditure'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    gov_consumption_expenditure       = %s%f" % ((" " * spacer),vv)
    if not success: failed += 1


def test_rule_21_of_33():
    global failed
    success = True
    print ""    
    print " %s" % ("."*76)
    print ""
    print "RULE 21 : abs (  eurostat_active_firms  -  firm_active  -  igfirm_active )   <  PRECISION"
    for i in data.get_list_of_iterations():
        print ""
        print ""
        print "              ---- [ Iteration %d : " % i,
        if abs ( sums['eurostat_active_firms'][i] - sums['firm_active'][i] - sums['igfirm_active'][i] ) < 1.000000: 
            print "OK ] ----"
        else:
            success = False
            print "FAIL ] ----"
        lhs = eval("abs ( sums['eurostat_active_firms'][i] - sums['firm_active'][i] - sums['igfirm_active'][i] )")
        rhs = eval("1.000000")
        print ""
        print_equation_evaluation(lhs, rhs, "<", success)
        print ""

        maxintlen = 10
        vv = eval("sums['eurostat_active_firms'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    eurostat_active_firms             = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['firm_active'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    firm_active                       = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['igfirm_active'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    igfirm_active                     = %s%f" % ((" " * spacer),vv)
    if not success: failed += 1


def test_rule_22_of_33():
    global failed
    success = True
    print ""    
    print " %s" % ("."*76)
    print ""
    print "RULE 22 : abs (  eurostat_sold_quantity  -  firm_total_sold_quantity_volume  )   <  PRECISION"
    for i in data.get_list_of_iterations():
        print ""
        print ""
        print "              ---- [ Iteration %d : " % i,
        if abs ( sums['eurostat_sold_quantity'][i] - sums['firm_total_sold_quantity_volume'][i] ) < 1.000000: 
            print "OK ] ----"
        else:
            success = False
            print "FAIL ] ----"
        lhs = eval("abs ( sums['eurostat_sold_quantity'][i] - sums['firm_total_sold_quantity_volume'][i] )")
        rhs = eval("1.000000")
        print ""
        print_equation_evaluation(lhs, rhs, "<", success)
        print ""

        maxintlen = 10
        vv = eval("sums['eurostat_sold_quantity'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    eurostat_sold_quantity            = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['firm_total_sold_quantity_volume'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    firm_total_sold_quantity_volume   = %s%f" % ((" " * spacer),vv)
    if not success: failed += 1


def test_rule_23_of_33():
    global failed
    success = True
    print ""    
    print " %s" % ("."*76)
    print ""
    print "RULE 23 : abs (  eurostat_investment_value  -  igfirm_revenue  )   <  PRECISION"
    for i in data.get_list_of_iterations():
        print ""
        print ""
        print "              ---- [ Iteration %d : " % i,
        if abs ( sums['eurostat_investment_value'][i] - sums['igfirm_revenue'][i] ) < 1.000000: 
            print "OK ] ----"
        else:
            success = False
            print "FAIL ] ----"
        lhs = eval("abs ( sums['eurostat_investment_value'][i] - sums['igfirm_revenue'][i] )")
        rhs = eval("1.000000")
        print ""
        print_equation_evaluation(lhs, rhs, "<", success)
        print ""

        maxintlen = 10
        vv = eval("sums['eurostat_investment_value'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    eurostat_investment_value         = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['igfirm_revenue'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    igfirm_revenue                    = %s%f" % ((" " * spacer),vv)
    if not success: failed += 1


def test_rule_24_of_33():
    global failed
    success = True
    print ""    
    print " %s" % ("."*76)
    print ""
    print "RULE 24 : abs (  gov_tax_revenue  -  firm_tax_payment  -  igfirm_tax_payment  -  household_tax_payment  -  bank_tax_payment )   <  PRECISION"
    for i in data.get_list_of_iterations():
        print ""
        print ""
        print "              ---- [ Iteration %d : " % i,
        if abs ( sums['gov_tax_revenue'][i] - sums['firm_tax_payment'][i] - sums['igfirm_tax_payment'][i] - sums['household_tax_payment'][i] - sums['bank_tax_payment'][i] ) < 1.000000: 
            print "OK ] ----"
        else:
            success = False
            print "FAIL ] ----"
        lhs = eval("abs ( sums['gov_tax_revenue'][i] - sums['firm_tax_payment'][i] - sums['igfirm_tax_payment'][i] - sums['household_tax_payment'][i] - sums['bank_tax_payment'][i] )")
        rhs = eval("1.000000")
        print ""
        print_equation_evaluation(lhs, rhs, "<", success)
        print ""

        maxintlen = 10
        vv = eval("sums['gov_tax_revenue'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    gov_tax_revenue                   = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['firm_tax_payment'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    firm_tax_payment                  = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['igfirm_tax_payment'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    igfirm_tax_payment                = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['household_tax_payment'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    household_tax_payment             = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['bank_tax_payment'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    bank_tax_payment                  = %s%f" % ((" " * spacer),vv)
    if not success: failed += 1


def test_rule_25_of_33():
    global failed
    success = True
    print ""    
    print " %s" % ("."*76)
    print ""
    print "RULE 25 : abs (  gov_benefit_payment  -  gov_restitution_payment  -  household_unemployment_benefit  +  household_restitution_payment )  <  PRECISION"
    for i in data.get_list_of_iterations():
        print ""
        print ""
        print "              ---- [ Iteration %d : " % i,
        if abs ( sums['gov_benefit_payment'][i] - sums['gov_restitution_payment'][i] - sums['household_unemployment_benefit'][i] + sums['household_restitution_payment'][i] ) < 1.000000: 
            print "OK ] ----"
        else:
            success = False
            print "FAIL ] ----"
        lhs = eval("abs ( sums['gov_benefit_payment'][i] - sums['gov_restitution_payment'][i] - sums['household_unemployment_benefit'][i] + sums['household_restitution_payment'][i] )")
        rhs = eval("1.000000")
        print ""
        print_equation_evaluation(lhs, rhs, "<", success)
        print ""

        maxintlen = 10
        vv = eval("sums['gov_benefit_payment'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    gov_benefit_payment               = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['gov_restitution_payment'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    gov_restitution_payment           = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['household_unemployment_benefit'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    household_unemployment_benefit    = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['household_restitution_payment'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    household_restitution_payment     = %s%f" % ((" " * spacer),vv)
    if not success: failed += 1


def test_rule_26_of_33():
    global failed
    success = True
    print ""    
    print " %s" % ("."*76)
    print ""
    print "RULE 26 : abs (  firm_outstanding_shares  +  igfirm_outstanding_shares  +  bank_outstanding_shares  +  gov_nr_bonds_oustanding  -  household_nr_assets  -  ecb_nr_gov_bonds )   <  PRECISION"
    for i in data.get_list_of_iterations():
        print ""
        print ""
        print "              ---- [ Iteration %d : " % i,
        if abs ( sums['firm_outstanding_shares'][i] + sums['igfirm_outstanding_shares'][i] + sums['bank_outstanding_shares'][i] + sums['gov_nr_bonds_oustanding'][i] - sums['household_nr_assets'][i] - sums['ecb_nr_gov_bonds'][i] ) < 1.000000: 
            print "OK ] ----"
        else:
            success = False
            print "FAIL ] ----"
        lhs = eval("abs ( sums['firm_outstanding_shares'][i] + sums['igfirm_outstanding_shares'][i] + sums['bank_outstanding_shares'][i] + sums['gov_nr_bonds_oustanding'][i] - sums['household_nr_assets'][i] - sums['ecb_nr_gov_bonds'][i] )")
        rhs = eval("1.000000")
        print ""
        print_equation_evaluation(lhs, rhs, "<", success)
        print ""

        maxintlen = 10
        vv = eval("sums['firm_outstanding_shares'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    firm_outstanding_shares           = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['igfirm_outstanding_shares'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    igfirm_outstanding_shares         = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['bank_outstanding_shares'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    bank_outstanding_shares           = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['gov_nr_bonds_oustanding'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    gov_nr_bonds_oustanding           = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['household_nr_assets'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    household_nr_assets               = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['ecb_nr_gov_bonds'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    ecb_nr_gov_bonds                  = %s%f" % ((" " * spacer),vv)
    if not success: failed += 1


def test_rule_27_of_33():
    global failed
    success = True
    print ""    
    print " %s" % ("."*76)
    print ""
    print "RULE 27 : abs (  bank_cash  +  bank_reserves  +  gov_payment_account  -  ecb_payment_account_banks  -  ecb_payment_account_govs )  <  PRECISION"
    for i in data.get_list_of_iterations():
        print ""
        print ""
        print "              ---- [ Iteration %d : " % i,
        if abs ( sums['bank_cash'][i] + sums['bank_reserves'][i] + sums['gov_payment_account'][i] - sums['ecb_payment_account_banks'][i] - sums['ecb_payment_account_govs'][i] ) < 1.000000: 
            print "OK ] ----"
        else:
            success = False
            print "FAIL ] ----"
        lhs = eval("abs ( sums['bank_cash'][i] + sums['bank_reserves'][i] + sums['gov_payment_account'][i] - sums['ecb_payment_account_banks'][i] - sums['ecb_payment_account_govs'][i] )")
        rhs = eval("1.000000")
        print ""
        print_equation_evaluation(lhs, rhs, "<", success)
        print ""

        maxintlen = 10
        vv = eval("sums['bank_cash'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    bank_cash                         = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['bank_reserves'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    bank_reserves                     = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['gov_payment_account'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    gov_payment_account               = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['ecb_payment_account_banks'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    ecb_payment_account_banks         = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['ecb_payment_account_govs'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    ecb_payment_account_govs          = %s%f" % ((" " * spacer),vv)
    if not success: failed += 1


def test_rule_28_of_33():
    global failed
    success = True
    print ""    
    print " %s" % ("."*76)
    print ""
    print "RULE 28 : abs (  ecb_fiat_money  -  ecb_fiat_money_banks  -  ecb_fiat_money_govs )   <  PRECISION"
    for i in data.get_list_of_iterations():
        print ""
        print ""
        print "              ---- [ Iteration %d : " % i,
        if abs ( sums['ecb_fiat_money'][i] - sums['ecb_fiat_money_banks'][i] - sums['ecb_fiat_money_govs'][i] ) < 1.000000: 
            print "OK ] ----"
        else:
            success = False
            print "FAIL ] ----"
        lhs = eval("abs ( sums['ecb_fiat_money'][i] - sums['ecb_fiat_money_banks'][i] - sums['ecb_fiat_money_govs'][i] )")
        rhs = eval("1.000000")
        print ""
        print_equation_evaluation(lhs, rhs, "<", success)
        print ""

        maxintlen = 10
        vv = eval("sums['ecb_fiat_money'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    ecb_fiat_money                    = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['ecb_fiat_money_banks'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    ecb_fiat_money_banks              = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['ecb_fiat_money_govs'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    ecb_fiat_money_govs               = %s%f" % ((" " * spacer),vv)
    if not success: failed += 1


def test_rule_29_of_33():
    global failed
    success = True
    print ""    
    print " %s" % ("."*76)
    print ""
    print "RULE 29 : abs (  ecb_fiat_money_banks  -  bank_ecb_debt )   <  PRECISION"
    for i in data.get_list_of_iterations():
        print ""
        print ""
        print "              ---- [ Iteration %d : " % i,
        if abs ( sums['ecb_fiat_money_banks'][i] - sums['bank_ecb_debt'][i] ) < 1.000000: 
            print "OK ] ----"
        else:
            success = False
            print "FAIL ] ----"
        lhs = eval("abs ( sums['ecb_fiat_money_banks'][i] - sums['bank_ecb_debt'][i] )")
        rhs = eval("1.000000")
        print ""
        print_equation_evaluation(lhs, rhs, "<", success)
        print ""

        maxintlen = 10
        vv = eval("sums['ecb_fiat_money_banks'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    ecb_fiat_money_banks              = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['bank_ecb_debt'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    bank_ecb_debt                     = %s%f" % ((" " * spacer),vv)
    if not success: failed += 1


def test_rule_30_of_33():
    global failed
    success = True
    print ""    
    print " %s" % ("."*76)
    print ""
    print "RULE 30 : abs (  bank_ecb_interest_payment  -  ecb_bank_interest )   <  PRECISION"
    for i in data.get_list_of_iterations():
        print ""
        print ""
        print "              ---- [ Iteration %d : " % i,
        if abs ( sums['bank_ecb_interest_payment'][i] - sums['ecb_bank_interest'][i] ) < 1.000000: 
            print "OK ] ----"
        else:
            success = False
            print "FAIL ] ----"
        lhs = eval("abs ( sums['bank_ecb_interest_payment'][i] - sums['ecb_bank_interest'][i] )")
        rhs = eval("1.000000")
        print ""
        print_equation_evaluation(lhs, rhs, "<", success)
        print ""

        maxintlen = 10
        vv = eval("sums['bank_ecb_interest_payment'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    bank_ecb_interest_payment         = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['ecb_bank_interest'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    ecb_bank_interest                 = %s%f" % ((" " * spacer),vv)
    if not success: failed += 1


def test_rule_31_of_33():
    global failed
    success = True
    print ""    
    print " %s" % ("."*76)
    print ""
    print "RULE 31 : abs (  ecb_dividend_payment  -  gov_ecb_dividend )   <  PRECISION"
    for i in data.get_list_of_iterations():
        print ""
        print ""
        print "              ---- [ Iteration %d : " % i,
        if abs ( sums['ecb_dividend_payment'][i] - sums['gov_ecb_dividend'][i] ) < 1.000000: 
            print "OK ] ----"
        else:
            success = False
            print "FAIL ] ----"
        lhs = eval("abs ( sums['ecb_dividend_payment'][i] - sums['gov_ecb_dividend'][i] )")
        rhs = eval("1.000000")
        print ""
        print_equation_evaluation(lhs, rhs, "<", success)
        print ""

        maxintlen = 10
        vv = eval("sums['ecb_dividend_payment'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    ecb_dividend_payment              = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['gov_ecb_dividend'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    gov_ecb_dividend                  = %s%f" % ((" " * spacer),vv)
    if not success: failed += 1


def test_rule_32_of_33():
    global failed
    success = True
    print ""    
    print " %s" % ("."*76)
    print ""
    print "RULE 32 : abs (  bank_cash  +  bank_reserves  +  bank_deposits  +  bank_equity  +  bank_loan_loss_reserve  +  gov_payment_account  +  ecb_cash  -  bank_total_credit  -  ecb_fiat_money_banks  +  ecb_fiat_money_govs  )   <  PRECISION"
    for i in data.get_list_of_iterations():
        print ""
        print ""
        print "              ---- [ Iteration %d : " % i,
        if abs ( sums['bank_cash'][i] + sums['bank_reserves'][i] + sums['bank_deposits'][i] + sums['bank_equity'][i] + sums['bank_loan_loss_reserve'][i] + sums['gov_payment_account'][i] + sums['ecb_cash'][i] - sums['bank_total_credit'][i] - sums['ecb_fiat_money_banks'][i] + sums['ecb_fiat_money_govs'][i] ) < 1.000000: 
            print "OK ] ----"
        else:
            success = False
            print "FAIL ] ----"
        lhs = eval("abs ( sums['bank_cash'][i] + sums['bank_reserves'][i] + sums['bank_deposits'][i] + sums['bank_equity'][i] + sums['bank_loan_loss_reserve'][i] + sums['gov_payment_account'][i] + sums['ecb_cash'][i] - sums['bank_total_credit'][i] - sums['ecb_fiat_money_banks'][i] + sums['ecb_fiat_money_govs'][i] )")
        rhs = eval("1.000000")
        print ""
        print_equation_evaluation(lhs, rhs, "<", success)
        print ""

        maxintlen = 10
        vv = eval("sums['bank_cash'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    bank_cash                         = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['bank_reserves'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    bank_reserves                     = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['bank_deposits'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    bank_deposits                     = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['bank_equity'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    bank_equity                       = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['bank_loan_loss_reserve'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    bank_loan_loss_reserve            = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['gov_payment_account'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    gov_payment_account               = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['ecb_cash'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    ecb_cash                          = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['bank_total_credit'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    bank_total_credit                 = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['ecb_fiat_money_banks'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    ecb_fiat_money_banks              = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['ecb_fiat_money_govs'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    ecb_fiat_money_govs               = %s%f" % ((" " * spacer),vv)
    if not success: failed += 1


def test_rule_33_of_33():
    global failed
    success = True
    print ""    
    print " %s" % ("."*76)
    print ""
    print "RULE 33 : abs (  bank_cash  +  bank_reserves  +  gov_payment_account  -  ecb_cash  -  ecb_fiat_money )  <  PRECISION"
    for i in data.get_list_of_iterations():
        print ""
        print ""
        print "              ---- [ Iteration %d : " % i,
        if abs ( sums['bank_cash'][i] + sums['bank_reserves'][i] + sums['gov_payment_account'][i] - sums['ecb_cash'][i] - sums['ecb_fiat_money'][i] ) < 1.000000: 
            print "OK ] ----"
        else:
            success = False
            print "FAIL ] ----"
        lhs = eval("abs ( sums['bank_cash'][i] + sums['bank_reserves'][i] + sums['gov_payment_account'][i] - sums['ecb_cash'][i] - sums['ecb_fiat_money'][i] )")
        rhs = eval("1.000000")
        print ""
        print_equation_evaluation(lhs, rhs, "<", success)
        print ""

        maxintlen = 10
        vv = eval("sums['bank_cash'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    bank_cash                         = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['bank_reserves'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    bank_reserves                     = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['gov_payment_account'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    gov_payment_account               = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['ecb_cash'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    ecb_cash                          = %s%f" % ((" " * spacer),vv)
        maxintlen = 10
        vv = eval("sums['ecb_fiat_money'][i]")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    ecb_fiat_money                    = %s%f" % ((" " * spacer),vv)
    if not success: failed += 1

# run tests
print " * Running tests ..."
test_rule_1_of_33()
test_rule_2_of_33()
test_rule_3_of_33()
test_rule_4_of_33()
test_rule_5_of_33()
test_rule_6_of_33()
test_rule_7_of_33()
test_rule_8_of_33()
test_rule_9_of_33()
test_rule_10_of_33()
test_rule_11_of_33()
test_rule_12_of_33()
test_rule_13_of_33()
test_rule_14_of_33()
test_rule_15_of_33()
test_rule_16_of_33()
test_rule_17_of_33()
test_rule_18_of_33()
test_rule_19_of_33()
test_rule_20_of_33()
test_rule_21_of_33()
test_rule_22_of_33()
test_rule_23_of_33()
test_rule_24_of_33()
test_rule_25_of_33()
test_rule_26_of_33()
test_rule_27_of_33()
test_rule_28_of_33()
test_rule_29_of_33()
test_rule_30_of_33()
test_rule_31_of_33()
test_rule_32_of_33()
test_rule_33_of_33()


print ""
print ""
print " %s " % ("="*76)
print "  SUMMARY: %d rules tested, %d failed" % (total, failed)
print " %s " % ("="*76)

if failed == 0: sys.exit(0)
else: sys.exit(failed)
