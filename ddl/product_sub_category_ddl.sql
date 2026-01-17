create table if not exists product_sub_category (
    product_subcategory_key integer not null unique
    , english_product_subcategory_name varchar(17)
    , product_category_key integer
    , primary key (product_subcategory_key)
    , foreign key (product_category_key) references product_category(product_category_key)
)