import csv
data = csv.DictReader(open('Resources/budget_data.csv'))

months = 0
total = 0
pre_rev = 0
change = 0
avg_ch = 0
inc = ['',0]
dec = ['',0]

for i,row in enumerate(data):
    months += 1
    
    rev = int(row['Profit/Losses'])
    total += rev

    change = rev - pre_rev
    pre_rev = rev

    if i == 0:
        change = 0
    avg_ch += change

    if change > inc[1]:
        inc[0] = row['Date']
        inc[1] = change

    if change < dec[1]:
        dec[0] = row['Date']
        dec[1] = change

output = (f'''Financial Analysis
----------------------------
Total Months: {months}
Total: $ {total:,.2f}
Average  Change: $ {avg_ch/(months-1):,.2f}
Greatest Increase in Profits: {inc[0]} ($ {inc[1]:,.2f})
Greatest Decrease in Profits: {dec[0]} ($ {dec[1]:,.2f})''')

open('analysis/report.txt', 'w').write(output)
print(output)