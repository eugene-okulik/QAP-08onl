INITIAL = DEPOSIT = 1000
PERCENT = 10/100
print(f'начальный депозит: {INITIAL}, годовой процент: {PERCENT*100}')

for month in range(12):
    INCOME = DEPOSIT * PERCENT / 12
    DEPOSIT += INCOME
    print(f'месяц: {month+1}, доход: {INCOME}, вклад: {DEPOSIT}')

YEAR_PERCENT = (DEPOSIT - INITIAL) / INITIAL
print(f'годовой процент с учётом капитализации составил: {YEAR_PERCENT*100}')
