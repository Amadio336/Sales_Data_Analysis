import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales_data = pd.read_csv("sales.csv", sep = ",")


# data section
print(sales_data.head())
print(sales_data.info())
print(sales_data.shape)


# adding revenue column
sales_data["incasso"] = sales_data["Quantità"] * sales_data["Prezzo_unitario"]

# total revenue
total_revenue = sales_data["incasso"].sum()
#print(total_revenue)


# average revenue per shop
group_shop = sales_data.groupby("Negozio")
#print(group_shop["incasso"].mean())

# top three product
sorted_df = sales_data.sort_values(["Quantità"], ascending=False)
#print(sorted_df.iloc[:3]["Prodotto"])


group_shop_product = sales_data.groupby(["Negozio", "Prodotto"])
averages_revenue = group_shop_product["incasso"].mean()
#print(averages_revenue)


#analysis on quantità field with numpy
q = sales_data["Quantità"].to_numpy()
average = np.mean(q)
maxi = np.max(q)
mini = np.min(q)
dev = np.std(q)

# product over average
for el in q:
    if el > average:
        print(el)



""" matplotlib """

#bar 
total_revenue_per_shop = group_shop["incasso"].sum()
print(total_revenue_per_shop)
plt.title("incasso totale per ogni negozio.")
plt.bar(total_revenue_per_shop.index, total_revenue_per_shop)
plt.savefig("mio_grafico.png")



# pie
revenue_per_product = sales_data.groupby("Prodotto")["incasso"].sum()
plt.figure(figsize=(8, 8))
plt.pie(revenue_per_product, 
        labels=revenue_per_product.index,  # I nomi dei prodotti
        autopct='%1.1f%%',                 # Aggiunge le percentuali (1 decimale)
        startangle=90)
plt.savefig("mio_grafico2.png")


# lines
sales_data["Data"] = pd.to_datetime(sales_data["Data"])
daily_revenue = sales_data.groupby("Data")["incasso"].sum()
plt.figure(figsize=(12, 6))
plt.plot(daily_revenue.index, daily_revenue, marker='o', linestyle='-', color='green')
plt.savefig("mio_grafico3.png")


mapping = {
    'Smartphone': 'Telefonia',
    'Laptop': 'Informatica',
    'Tablet': 'Informatica',
    'Monitor': 'Informatica',
    'Hard Disk': 'Informatica',
    'TV': 'Elettronica',
    'Console': 'Elettronica',
    'Smartwatch': 'Wearable',
    'Cuffie': 'Accessori',
    'Mouse': 'Accessori',
    'Tastiera': 'Accessori',
    'Stampante': 'Ufficio'
}

sales_data["Categoria"] = sales_data["Prodotto"].map(mapping)
sales_data['Categoria'] = sales_data['Categoria'].fillna('Altro')


# total revenue per category
revenue_group_category = sales_data.groupby("Categoria")["incasso"].sum()

# average products sold 
average_prodcuts_sold = sales_data.groupby("Categoria")["Quantità"].mean()


sales_data.to_csv("final_df.csv", index=False)