import pandas as pd
from analyzing import (products_amount,
                       products_revenue,
                       sales_by_region,
                       sales_by_month,
                       sales_by_category)





if __name__ == '__main__':

    df = pd.read_csv('train.csv')

    df.to_excel("data.xlsx",index = False)


    df_amount = products_amount(df)

    df_revenue = products_revenue(df)

    df_sales_by_region = sales_by_region(df)

    df_sales_by_month = sales_by_month(df)

    df_sales_by_category= sales_by_category(df)


    df_amount.to_excel(f"./output/product_amount.xlsx",index = False)
    df_revenue.to_excel("./output/products_revenue.xlsx",index = False)
    df_sales_by_region.to_excel(f"./output/sales_by_region.xlsx",index = False)
    df_sales_by_month.to_excel(f"./output/sales_by_segment.xlsx",index = False)
    df_sales_by_category.to_excel(f"./output/df_sales_by_category.xlsx",index = False)

