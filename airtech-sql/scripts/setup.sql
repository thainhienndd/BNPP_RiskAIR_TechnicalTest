-- Schéma
CREATE TABLE IF NOT EXISTS countries (
  country_id   VARCHAR(2) PRIMARY KEY,
  country_name VARCHAR(40) DEFAULT NULL,
  region       VARCHAR(10) NOT NULL
);

CREATE TABLE IF NOT EXISTS employees (
  employee_id   SERIAL PRIMARY KEY,
  first_name    VARCHAR(20) DEFAULT NULL,
  last_name     VARCHAR(25) NOT NULL,
  email         VARCHAR(100) NOT NULL,
  phone_number  VARCHAR(20) DEFAULT NULL,
  manager_id    INT DEFAULT NULL REFERENCES employees(employee_id),
  department    VARCHAR(20) DEFAULT NULL,
  country_id    VARCHAR(2) REFERENCES countries(country_id)
);

-- Données
INSERT INTO countries VALUES ('AR','ARGENTINA', 'lamr');
INSERT INTO countries VALUES ('BR','BRAZIL', 'lamr');
INSERT INTO countries VALUES ('ES','SPAIN', 'euro');
INSERT INTO countries VALUES ('FR','FRANCE', 'euro');
INSERT INTO countries VALUES ('GB','UNITED KINGDOM', 'euro');
INSERT INTO countries VALUES ('HK','HONG KONG', 'asia');
INSERT INTO countries VALUES ('IT','ITALY', 'euro');
INSERT INTO countries VALUES ('US','UNITED STATES', 'namr');

INSERT INTO employees (first_name,last_name,email,phone_number,manager_id,department,country_id) VALUES
('Jean','AAA','jean.aaa@mycompany.fr','32359949',NULL,'Sales','FR'),
('Michel','BBB','michel.bbb@mycompany.es','81945947','1','HR','ES'),
('Juliane','CCC','juliane.ccc@mycompany.br','87622749','1','Sales','BR'),
('Patrice','DDD','patrice.ddd@mycompany.hk','13931578','1','HR','HK'),
('Louis','EEE','louis.eee@mycompany.fr','68154273','1','Sales','FR'),
('Albert','FFF','albert.fff@mycompany.hk','63142944',NULL,'IT','HK'),
('Ludivine','GGG','ludivine.ggg@mycompany.fr','63280299','6','IT','FR'),
('Sophie','HHH','sophie.hhh@mycompany.br','66811818','6','IT','BR'),
('Camille','III','camille.iii@mycompany.gb','24205021','6','Sales','GB'),
('Frank','JJJ','frank.jjj@mycompany.it','83318015',NULL,'Sales','IT'),
('Thomas','KKK','thomas.kkk@mycompany.ar','20430282','9','Sales','AR'),
('Eric','LLL','eric.lll@mycompany.us','86227391','9','HR','US'),
('Thierry','MMM','thierry.mmm@mycompany.gb','93130273','9','Sales','GB'),
('Nathalie','NNN','nathalie.nnn@mycompany.es','41576574','9','IT','ES');
