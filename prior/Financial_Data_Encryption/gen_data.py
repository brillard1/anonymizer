import pandas as pd
import numpy as np
from faker import Faker

# Set seed for reproducibility
np.random.seed(42)

# Generate some synthetic data
fake = Faker()

n = 1000
accounts = [fake.iban() for i in range(n)]
names = [fake.name() for i in range(n)]
ages = np.random.randint(18, 70, n)
incomes = np.random.normal(loc=50000, scale=10000, size=n)
expenses = np.random.normal(loc=40000, scale=10000, size=n)
balances = incomes - expenses

data = pd.DataFrame({
    'Account Number': accounts,
    'Name': names,
    'Age': ages,
    'Income': incomes,
    'Expenses': expenses,
    'Balance': balances
})

# Save data to CSV
data.to_csv('financial_data.csv', index=False)

