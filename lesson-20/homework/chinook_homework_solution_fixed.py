import pandas as pd
import sqlite3

# Подключение к базе данных
conn = sqlite3.connect("chinook.db")

# Задание 1: Анализ покупок клиентов
invoices = pd.read_sql_query("SELECT InvoiceId, CustomerId, Total FROM Invoice", conn)
customers = pd.read_sql_query("SELECT CustomerId, FirstName, LastName FROM Customer", conn)

total_spent = invoices.groupby("CustomerId")["Total"].sum().reset_index()
top_customers = total_spent.sort_values(by="Total", ascending=False).head(5)
top_customers = top_customers.merge(customers, on="CustomerId")[["CustomerId", "FirstName", "LastName", "Total"]]

# Задание 2: Покупка альбомов против отдельных треков
invoice_lines = pd.read_sql_query("SELECT InvoiceLineId, InvoiceId, TrackId FROM InvoiceLine", conn)
tracks = pd.read_sql_query("SELECT TrackId, AlbumId FROM Track", conn)

invoice_album = invoice_lines.merge(tracks, on="TrackId")
album_track_counts = tracks.groupby("AlbumId")["TrackId"].count().reset_index()
invoice_album = invoice_album.merge(album_track_counts, on="AlbumId", suffixes=("", "_Total"))
invoice_album["PurchaseCount"] = invoice_album.groupby(["InvoiceId", "AlbumId"])["TrackId"].transform("count")
invoice_album["IsFullAlbum"] = invoice_album["TrackId_Total"] == invoice_album["PurchaseCount"]
invoice_album_per_invoice = invoice_album.groupby("InvoiceId")["IsFullAlbum"].any().reset_index()
invoice_album_per_invoice["CustomerId"] = invoice_album_per_invoice["InvoiceId"].map(
    invoices.set_index("InvoiceId")["CustomerId"]
)
customer_album_pref = invoice_album_per_invoice.groupby("CustomerId")["IsFullAlbum"].any().reset_index()
customer_album_pref["Preference"] = customer_album_pref["IsFullAlbum"].replace({True: "Full Album", False: "Tracks"})
summary = customer_album_pref["Preference"].value_counts(normalize=True) * 100
summary = summary.reset_index().rename(columns={"index": "PurchaseType", "Preference": "Percentage"})

# Вывод результатов
print("Top 5 Customers by Total Purchase:")
print(top_customers)

print("\nPercentage of Customers by Purchase Preference:")
print(summary)
