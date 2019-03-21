create table if not exists tb_customer_account (
    id_customer int unsigned not null auto_increment,
    cpf_cnpj varchar(14) not null,
    nm_customer varchar(45) not null,
    is_active ENUM('Actived', 'Is not actived') not null,
    vl_total int unsigned not null,
    unique key (id_customer),
    primary key (cpf_cnpj)
)
