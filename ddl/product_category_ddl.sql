create table if not exists product_category(
    product_category_key integer not null unique
    , english_product_category_name varchar(11)
    , primary key (product_category_key)
)