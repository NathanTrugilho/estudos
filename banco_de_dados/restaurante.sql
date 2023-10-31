-- MySQL dump 10.13  Distrib 8.0.34, for Linux (x86_64)
--
-- Host: localhost    Database: restaurante
-- ------------------------------------------------------
-- Server version	8.0.34-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cliente`
--

DROP TABLE IF EXISTS `cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cliente` (
  `idCliente` tinyint NOT NULL,
  `nomeCliente` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`idCliente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente`
--

LOCK TABLES `cliente` WRITE;
/*!40000 ALTER TABLE `cliente` DISABLE KEYS */;
INSERT INTO `cliente` VALUES (1,'Nathan'),(2,'Camila'),(3,'Babi'),(4,'Layla'),(5,'Messi'),(6,'Tiquinho'),(7,'Lucas'),(8,'Eduardo'),(9,'Segovia'),(10,'Adryelson'),(11,'Giselle');
/*!40000 ALTER TABLE `cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contem`
--

DROP TABLE IF EXISTS `contem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contem` (
  `idPedido` tinyint NOT NULL,
  `idItem` tinyint NOT NULL,
  `quantidade` tinyint DEFAULT NULL,
  PRIMARY KEY (`idPedido`,`idItem`),
  KEY `idItem` (`idItem`),
  CONSTRAINT `contem_ibfk_1` FOREIGN KEY (`idPedido`) REFERENCES `pedido` (`idPedido`),
  CONSTRAINT `contem_ibfk_2` FOREIGN KEY (`idItem`) REFERENCES `itemConsumo` (`idItem`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contem`
--

LOCK TABLES `contem` WRITE;
/*!40000 ALTER TABLE `contem` DISABLE KEYS */;
INSERT INTO `contem` VALUES (1,5,2),(1,9,1),(1,10,1),(2,1,1),(2,15,2),(3,8,1),(4,1,2),(4,12,3),(5,11,2);
/*!40000 ALTER TABLE `contem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `itemConsumo`
--

DROP TABLE IF EXISTS `itemConsumo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `itemConsumo` (
  `idItem` tinyint NOT NULL,
  `nomeItem` varchar(30) DEFAULT NULL,
  `precoUnit` float(8,2) DEFAULT NULL,
  `descricao` varchar(200) DEFAULT NULL,
  `categoria` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`idItem`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `itemConsumo`
--

LOCK TABLES `itemConsumo` WRITE;
/*!40000 ALTER TABLE `itemConsumo` DISABLE KEYS */;
INSERT INTO `itemConsumo` VALUES (1,'agua',2.00,'muito refrescante','bebida'),(2,'guaravita',3.00,'doce como mel','bebida'),(3,'coca-cola',6.50,'inimiga dos diabeticos','bebida'),(4,'suco de caju',9.99,'bom pra dor de barriga','bebida'),(5,'vinho',20.00,'para um jantar romantico','bebida'),(6,'suco de uva',9.99,'vinho para criancas','bebida'),(7,'cafe',4.00,'para quem vive cansado','bebida'),(8,'pizza',42.00,'nao pode faltar','massa'),(9,'macarrao',17.00,'amigo do marombeiro','massa'),(10,'lasanha',15.00,'bem recheada','massa'),(11,'nhoque',22.00,'amarelo como o sol','massa'),(12,'bolo de chocolate',5.00,'vem com morango','sobremesa'),(13,'pudim',14.00,'cheio de calda','sobremesa'),(14,'pave',14.00,'ou pra comer ?','sobremesa'),(15,'brownie',6.20,'vale cada moeda','sobremesa'),(16,'picole',1.50,'fica mais caro no verao','sobremesa'),(17,'fandangos',5.00,'milho','comida');
/*!40000 ALTER TABLE `itemConsumo` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `preco_novo_produto` AFTER INSERT ON `itemConsumo` FOR EACH ROW begin insert into cliente values(11, "Giselle") ; end */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `mesa`
--

DROP TABLE IF EXISTS `mesa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mesa` (
  `idMesa` tinyint NOT NULL,
  `numeroMesas` tinyint DEFAULT NULL,
  PRIMARY KEY (`idMesa`),
  UNIQUE KEY `numeroMesas` (`numeroMesas`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mesa`
--

LOCK TABLES `mesa` WRITE;
/*!40000 ALTER TABLE `mesa` DISABLE KEYS */;
INSERT INTO `mesa` VALUES (1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10);
/*!40000 ALTER TABLE `mesa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nota`
--

DROP TABLE IF EXISTS `nota`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nota` (
  `numeroNota` tinyint NOT NULL,
  `dtPagamento` date NOT NULL,
  `idPedido` tinyint DEFAULT NULL,
  PRIMARY KEY (`numeroNota`,`dtPagamento`),
  KEY `idPedido` (`idPedido`),
  CONSTRAINT `nota_ibfk_1` FOREIGN KEY (`idPedido`) REFERENCES `pedido` (`idPedido`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nota`
--

LOCK TABLES `nota` WRITE;
/*!40000 ALTER TABLE `nota` DISABLE KEYS */;
INSERT INTO `nota` VALUES (10,'2023-02-05',1);
/*!40000 ALTER TABLE `nota` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pedido`
--

DROP TABLE IF EXISTS `pedido`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pedido` (
  `idPedido` tinyint NOT NULL,
  `idCliente` tinyint DEFAULT NULL,
  `idMesa` tinyint DEFAULT NULL,
  `dtPedido` date DEFAULT NULL,
  `motivoCancel` varchar(100) DEFAULT NULL,
  `situacao` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`idPedido`),
  KEY `idCliente` (`idCliente`),
  KEY `idMesa` (`idMesa`),
  CONSTRAINT `pedido_ibfk_1` FOREIGN KEY (`idCliente`) REFERENCES `cliente` (`idCliente`),
  CONSTRAINT `pedido_ibfk_2` FOREIGN KEY (`idMesa`) REFERENCES `mesa` (`idMesa`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pedido`
--

LOCK TABLES `pedido` WRITE;
/*!40000 ALTER TABLE `pedido` DISABLE KEYS */;
INSERT INTO `pedido` VALUES (1,1,1,'2023-02-05',NULL,'aprovado'),(2,2,1,'2023-02-05',NULL,'aprovado'),(3,4,2,'2023-02-05',NULL,'aprovado'),(4,5,3,'2023-03-11',NULL,'aprovado'),(5,10,9,'2023-02-09',NULL,'aprovado');
/*!40000 ALTER TABLE `pedido` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `pedidosCliente`
--

DROP TABLE IF EXISTS `pedidosCliente`;
/*!50001 DROP VIEW IF EXISTS `pedidosCliente`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `pedidosCliente` AS SELECT 
 1 AS `idPedido`,
 1 AS `nomeCliente`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `telCliente`
--

DROP TABLE IF EXISTS `telCliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `telCliente` (
  `idCliente` tinyint NOT NULL,
  `telCliente` char(9) NOT NULL,
  PRIMARY KEY (`idCliente`,`telCliente`),
  CONSTRAINT `telCliente_ibfk_1` FOREIGN KEY (`idCliente`) REFERENCES `cliente` (`idCliente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `telCliente`
--

LOCK TABLES `telCliente` WRITE;
/*!40000 ALTER TABLE `telCliente` DISABLE KEYS */;
/*!40000 ALTER TABLE `telCliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `pedidosCliente`
--

/*!50001 DROP VIEW IF EXISTS `pedidosCliente`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `pedidosCliente` (`idPedido`,`nomeCliente`) AS select `pedido`.`idPedido` AS `idPedido`,`cliente`.`nomeCliente` AS `nomeCliente` from (`pedido` join `cliente` on((`pedido`.`idCliente` = `cliente`.`idCliente`))) where (`cliente`.`nomeCliente` = 'Nathan') */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-30  8:43:07
