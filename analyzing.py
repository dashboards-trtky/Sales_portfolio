import pandas as pd

def products_amount(df):

    top_products = df["Product Name"].value_counts().reset_index()

    return top_products



def products_revenue(df):

    b = df.groupby(by = ["Product Name"])["Sales"].agg(["sum","count"]).reset_index()

    b = b.rename(columns={"sum": 'Sales_revenue',
                          "count":"amount"})


    b["revenue_per_product"] = b["Sales_revenue"]/b["amount"]


    b = b.sort_values(by = ["Sales_revenue"], ascending = False)


    return b



def sales_by_region(df):

    c =  df.groupby(by = ["Country","Region","City"])["Sales"].agg("sum").reset_index()

    c = c.rename(columns={"Sales": 'Sales_revenue'})

    c = c.sort_values(by = ["Sales_revenue"], ascending = False)

    return c



def sales_by_segment(df):

    d =  df.groupby(by = ["Segment"])["Sales"].agg(["sum","count"]).reset_index()


    d = d.rename(columns={"sum": 'Sales_revenue',
                          "count":"amount"})

    d["average_revenue_per_segment"] = d["Sales_revenue"] / d["amount"]


    d  =  d.sort_values(by = ["average_revenue_per_segment"], ascending = False)

    return d



def sales_by_month(df):

    df["Order Date"] = pd.to_datetime(df["Order Date"],format = "%d/%m/%Y")
    df["Order Month"] = df["Order Date"].dt.to_period("M")

    m = df.groupby("Order Month")["Sales"].sum().reset_index()
    m = m.rename(columns={"Sales": "Sales_revenue"})

    m = m.sort_values("Order Month")

    return m


def sales_by_category(df):

    e = df.groupby(by=["Category"])["Sales"].agg(["sum", "count"]).reset_index()

    e = e.rename(columns={"sum": 'Sales_revenue',
                          "count": "amount"})


    return e

