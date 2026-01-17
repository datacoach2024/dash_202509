select
    customer_key
    , name
    , birth_date
    , case marital_status
        when 'M' then 'Married'
        when 'S' then 'Single'
        else 'N/A'
    end as marital_status
    , case gender
        when 'F' then 'Female'
        when 'M' then 'Male'
        else 'N/A'
    end as gender
    , yearly_income
    , number_children_at_home
    , occupation
    , house_owner_flag
    , number_cars_owned
    , phone
    , date_first_purchase
from customers