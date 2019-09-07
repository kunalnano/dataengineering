def getInputs():
    gross = float (input('Enter gross pay => '))
    exemptions = int (input('Enter the number of exemptions => '))

    return (gross, exemptions)

def getExemptionValue(exemptions):
    if exemptions == 1:
        exvalue = 2500
    elif exemptions == 2:
        exvalue = 5000
    else:
        exvalue = 7500
    return exvalue

def getAdjustedGross(gross, exemptionValue):
    return gross - exemptionValue

def calculateTaxes(adjustedGross):
    # calculate tax for the adjusted gross
    fede_tax = adjustedGross * 0.200
    net_pay = adjustedGross - fede_tax

    return (fede_tax, net_pay)

def printResults(grossPay, federalTax, net):
    # print the tax and payment
    print ()
    print ("PAYCHECK STUB")
    print ("  Gross Pay: ${:>10.2f}".format (grossPay))
    print ("Federal Tax: ${:>10.2f}".format (federalTax))
    print ("-------------------")
    print ("    Net Pay: ${:>10.2f}".format (net))

def main():

    grossPay, exemptions = getInputs()
    exemptionValue = getExemptionValue(exemptions)
    adjustedGross = getAdjustedGross(grossPay,exemptionValue)
    #call calculate taxes
    fede, net = calculateTaxes(adjustedGross)
    #call print results
    printResults(grossPay, fede, net)

if __name__ == '__main__':
    main()
