create table if not exists territory (
    territory_key integer not null unique
    , region varchar(14)
    , country varchar(14)
    , continent varchar(14)
    , primary key (territory_key)
)