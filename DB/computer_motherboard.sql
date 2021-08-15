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
-- Table structure for table `motherboard`
--

DROP TABLE IF EXISTS `motherboard`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `motherboard` (
  `name` varchar(30) NOT NULL,
  `manufacturer` varchar(45) NOT NULL,
  `socket` varchar(45) NOT NULL,
  `chipset` varchar(45) NOT NULL,
  `price` int NOT NULL,
  `formfactor` varchar(45) NOT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `motherboard`
--

LOCK TABLES `motherboard` WRITE;
/*!40000 ALTER TABLE `motherboard` DISABLE KEYS */;
INSERT INTO `motherboard` VALUES ('a320m-hdv','Asrock','AM4','a320',4150,'M-ATX'),('a520m ds3h','gigabyte','AM4','b520',6700,'M-ATX'),('a520m-hdv','Asrock','AM4','a520',5350,'M-ATX'),('aorus elite','gigabyte','AM4','b450',11000,'ATX'),('aorus pro wifi','gigabyte','AM4','b450',13000,'ATX'),('b450 gaming pro carbon','msi','AM4','b450',13000,'ATX'),('b450 mortar','msi','AM4','b450',11000,'ATX'),('b450 steel legend','Asrock','AM4','b450',9500,'ATX'),('b450 tomahawk','msi','AM4','b450',10000,'ATX'),('b450m pro 4','Asrock','AM4','b40',7500,'M-ATX'),('b460 phantom gaming 4','Asrock','LGA 1200','b460',9600,'ATX'),('b460 steel legend','Asrock','LGA 1200','b460',11200,'ATX'),('b460m gaming hd','gigabyte','AM4','b460',12000,'M-ATX'),('b550 phantom gaming 4','Asrock','AM4','b550',11900,'ATX'),('h410 vd-h','MSI','LGA 1200','h410',3500,'M-ATX'),('h410m elite','gigabyte','lga 1200','h410',5200,'M-ATX'),('H410M pro-vh','MSI','LGA 1200','h410',4500,'ATX'),('meg x570 ace','msi','am4','x570',35000,'ATX'),('mps b550 gaming','msi','am4','b550',21000,'ATX'),('n7 z490','nzxt','lga 1200','z490',26000,'ATX'),('prime a320 k','asus','am4','b450',4200,'M-ATX'),('prime h410 plus','asus','lga 1200','h410',10000,'ATX'),('rog strix b450 gaming-e','asus','AM4','b450',15000,'ATX'),('rog strix b450 gaming-f','asus','AM4','b450',13000,'ATX'),('tuf gaming b450m plus','asus','AM4','b450',10000,'M-ATX'),('z490 extreme','asrock','LGA 1200','z490',18999,'ATX');
/*!40000 ALTER TABLE `motherboard` ENABLE KEYS */;
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
