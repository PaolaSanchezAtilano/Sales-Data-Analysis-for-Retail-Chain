import pandas as pd
import plotly.express as px

data = pd.read_excel("ventas.xlsx")


print("\n=== primeras filas ===")
print(data.head())

print("\n=== últimas filas ===")
print(data.tail())

print("\n=== dimensiones ===")
print(data.shape)

print("\n=== información general ===")
data.info()

print("\n=== estadísticas ===")
print(data.describe())


ventas_por_tienda = data.groupby("tienda")["precio"].sum()

print("\n=== tienda con mayor facturación ===")
tienda_top = ventas_por_tienda.idxmax()
monto_top = ventas_por_tienda.max()
print(f"la tienda con mayor facturación es {tienda_top} con ${monto_top:,.2f}")

print("\n=== tienda con menor facturación ===")
tienda_menor = ventas_por_tienda.idxmin()
monto_menor = ventas_por_tienda.min()
print(f"la tienda con menor facturación es {tienda_menor} con ${monto_menor:,.2f}")

print("\n=== forma de pago más utilizada ===")
forma_pago_top = data["forma_pago"].value_counts().idxmax()
print(f"la forma de pago más usada es {forma_pago_top}")

print("\n=== ranking de tiendas ===")
ranking = ventas_por_tienda.sort_values(ascending=False)
print(ranking)

grafico = px.histogram(
    data,
    x="tienda",
    y="precio",
    title="retail sales performance by store",
    text_auto=True,
    color="forma_pago"
)

grafico.show()
