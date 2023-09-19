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
/*!40000 ALTER TABLE `itemConsumo` ENABLE KEYS */;
UNLOCK TABLES;

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
/*!40000 ALTER TABLE `pedido` ENABLE KEYS */;
UNLOCK TABLES;

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
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-19  7:29:53
