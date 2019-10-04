import csv
import sys
import random
import time
import datetime
import socket
import StringIO
from datetime import datetime
from kafka import KafkaProducer

#HOST, PORT = "localhost", 9092

# Create a socket (SOCK_STREAM means a TCP socket)
producer = KafkaProducer(bootstrap_servers='127.0.0.1:9092')


try:
        writer = csv.writer(f)
        i = 0
        while True:
                t1 = time.time()
                newt1=t1*1000
                deviceReceiptTime1=int(newt1)

                art=random.randint(1000, 9999)
                amount=random.choice(["999889", "2399812", "1199700", "11154"])
                sourceId=random.randint(1, 4)
		        mcc=random.randint(1000, 2000)
		data1=random.randint(1000, 2300000)
                transactionType   = random.choice(["04", "05"])
		txnSubType   = random.choice(["U11", "U21", "U3", "U4"])
		channel   = random.choice(["UPI"])
		(dt, micro) = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f').split('.')
		dt = "%s.%03d" % (dt, int(micro) / 1000)
		terminalId = random.choice(["U1", "U2", "U3", "U4","U11", "U21", "U31", "U41"])
		transactionResponseCode = "224"
		channelTypeId="09"

                data = ",".join(["b0dd3f13-fbca-"+str(deviceReceiptTime1)+"-49790bc3bb04~#~1~#~"+str(sourceId)+"~#~3~#~4011~#~5~#~"+str(dt)+"~#~"+str(amount)+"~#~"+channel+"~#~9~#~"+terminalId+"~#~366~#~12~#~13~#~14~#~15~#~16~#~"+transactionResponseCode+"~#~"+transactionType+"~#~"+channelTypeId+"~#~00~#~SUCCESS"])

                # data = ",".join([ str(eventTime), str(receiptTime), device, logger, version,
                #                 deviceVendor, deviceProduct, deviceVersion, deviceEventClassId,agentSeverity,
                #                 cefVer, customerURI, deviceCustomString1, agentId, rawMessage,
                #                 deviceCustomString1Label, deviceProcessName, eventId, str(sourceAddress), deviceCustomString3Label,
                #                 str(endTime),customerName, str(baseEventCount), deviceAddress, deviceTimeZone,
                #                 deviceHostName, str(agentReceiptTime),agentType, agentVersion, agentTimeZone,
                #                 str(startTime), str(deviceReceiptTime), agentAddress, agentHostName, deviceCustomString2Label,
                #                 categoryBehavior, catdt,deviceFacility, categoryDeviceGroup, message,
                #                 deviceCustomString4, deviceCustomString2, categoryTechnique,deviceCustomNumber1Label, categoryObject,
                #                 categorySignificance, categoryOutcome, str(destinationAddress),str(sourcePort),destinationZoneURI])



                producer.send('stocks',(data + "\n").encode())
                #print(data)
                i = i + 1
                time.sleep(1)
finally:
		print ' '
