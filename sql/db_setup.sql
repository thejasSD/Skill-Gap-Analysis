-- MySQL dump 10.13  Distrib 8.0.36, for macos14 (x86_64)
--
-- Host: 127.0.0.1    Database: skill_based_analysis
-- ------------------------------------------------------
-- Server version	8.3.0

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
-- Table structure for table `domain_role`
--

DROP TABLE IF EXISTS `domain_role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `domain_role` (
  `id` int NOT NULL AUTO_INCREMENT,
  `role_id` int DEFAULT NULL,
  `domain_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `role_id` (`role_id`),
  KEY `domain_id` (`domain_id`),
  CONSTRAINT `domain_role_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `ms_role` (`role_id`),
  CONSTRAINT `domain_role_ibfk_2` FOREIGN KEY (`domain_id`) REFERENCES `ms_domain` (`domain_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `domain_role`
--

LOCK TABLES `domain_role` WRITE;
/*!40000 ALTER TABLE `domain_role` DISABLE KEYS */;
INSERT INTO `domain_role` VALUES (1,1,1),(2,2,1),(3,3,2),(4,4,3),(5,5,1),(6,3,4);
/*!40000 ALTER TABLE `domain_role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ms_domain`
--

DROP TABLE IF EXISTS `ms_domain`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ms_domain` (
  `domain_id` int NOT NULL AUTO_INCREMENT,
  `domain_name` varchar(255) NOT NULL,
  PRIMARY KEY (`domain_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ms_domain`
--

LOCK TABLES `ms_domain` WRITE;
/*!40000 ALTER TABLE `ms_domain` DISABLE KEYS */;
INSERT INTO `ms_domain` VALUES (1,'IT'),(2,'Sales'),(3,'Finance'),(4,'Operations');
/*!40000 ALTER TABLE `ms_domain` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ms_role`
--

DROP TABLE IF EXISTS `ms_role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ms_role` (
  `role_id` int NOT NULL AUTO_INCREMENT,
  `role_name` varchar(255) NOT NULL,
  PRIMARY KEY (`role_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ms_role`
--

LOCK TABLES `ms_role` WRITE;
/*!40000 ALTER TABLE `ms_role` DISABLE KEYS */;
INSERT INTO `ms_role` VALUES (1,'Python Developer'),(2,'Junior System Engineer'),(3,'Sales Executive'),(4,'Data Analyst'),(5,'Network Administrator');
/*!40000 ALTER TABLE `ms_role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'skill_based_analysis'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-09-27 19:15:28
