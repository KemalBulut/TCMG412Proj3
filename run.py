t = open ('http_access_log.txt', 'r')
q1 = 0
q2 = 0

for line in t:
        if '/199' in line:
                q2 += 1
		
		if '/1995' in line:
			q1 += 1

print ("The number of transactions documented in 1995 is " , q1)
print ("The total number of transactions documented for this period is ", q2)
