-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: computer
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `gpu`
--

DROP TABLE IF EXISTS `gpu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gpu` (
  `name` varchar(30) NOT NULL,
  `manufacturer` varchar(45) NOT NULL,
  `vram` int NOT NULL,
  `price` int NOT NULL,
  `tdp` int NOT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gpu`
--

LOCK TABLES `gpu` WRITE;
/*!40000 ALTER TABLE `gpu` DISABLE KEYS */;
INSERT INTO `gpu` VALUES ('gt 1030','nvidia',1,6600,75),('gtx 1050 ti','nvidia',4,12000,75),('gtx 1060','nvidia',6,15000,120),('gtx 1070','nvidia',8,24000,150),('gtx 1660','nvidia',6,17000,120),('gtx 1660 super','nvidia',6,20000,120),('gtx 1660 ti','nvidia',6,22000,120),('rtx 2060','nvidia',6,26000,150),('rtx 2060 super','nvidia',8,32000,175),('rtx 2070 super','nvidia',8,40000,200),('rtx 2080','nvidia',10,80000,300),('rtx 2080 super ','nvidia',8,60000,250),('rtx 3060 ti','nvidia',8,45000,150),('rtx 3070','nvidia',8,55000,200),('rtx 3090','nvidia',24,150000,450),('rx 5500','AMD',8,15000,120),('rx 5600','AMD',8,20000,120),('rx 5600XT','AMD',8,28000,150),('rx 570','AMD',8,11000,120),('rx 5700','AMD',8,35000,200),('rx 5700XT','AMD',8,40000,250),('rx 580','AMD',8,12000,120),('rx 6800','AMD',16,50000,250),('rx 6800XT','AMD',16,75000,300);
/*!40000 ALTER TABLE `gpu` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-01-14 19:47:54
