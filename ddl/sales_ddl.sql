create table if not exists sales (
    product_key integer
    , order_date date
    , customer_key integer
    , sales_territory_key integer
    , sales_order_number char(7)
    , sales_order_line_number integer
    , order_quantity integer
    , unit_price decimal(7, 2)
    , extended_amount decimal(7, 2)
    , product_standard_cost decimal(7,2)
    , total_product_cost decimal(7,2)
    , sales_amount decimal(7,2)
    , tax_amt decimal(7,2)
    , freight decimal(7,2)
    , foreign key (product_key) references products(product_key)
    , foreign key (customer_key) references customers(customer_key)
    , foreign key (sales_territory_key) references territory(territory_key)
)