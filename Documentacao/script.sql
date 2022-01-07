create database Dividas;

use Dividas;

CREATE TABLE Usuario (
    UsuarioId int primary key NOT NULL AUTO_INCREMENT,
    Cpf varchar(11) NOT NULL,
    Nome varchar(20) NOT NULL,
    DataNascimento date NOT NULL,
    DataCriacao date NOT NULL,     
    DataAtualizacao date
);

CREATE TABLE Divida (
    DividaId int primary key NOT NULL AUTO_INCREMENT,
    Produto varchar(20) NOT NULL,
    DataVencimento date NOT NULL,
    IdExterno int,
    Valor decimal,
	DevedorId int,
    DataCriacao date NOT NULL,     
    DataAtualizacao date ,
    
	FOREIGN KEY (DevedorId) REFERENCES Usuario(UsuarioId)

);

CREATE TABLE Teste (
    testeId int primary key NOT NULL AUTO_INCREMENT,
	Nome varchar(20) NOT NULL
);


INSERT INTO Teste (Nome)
VALUES ("tetse2");

select * from teste;

select * from Usuario;

select * from Divida;

delete from Divida
where DividaId = 2;


-- drop table Teste;

-- drop table Divida;


UPDATE Usuario 
    SET Cpf = "12345678900", Nome = "teste", DataNascimento = "1995-02-16", DataAtualizacao = "1995-02-16"
    WHERE UsuarioId = 2;
    
DELETE FROM Usuario 
    WHERE UsuarioId = 3

SET PASSWORD FOR 'root'@'localhost' = PASSWORD('teste');
FLUSH PRIVILEGES;