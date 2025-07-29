-- MySQL dump 10.13  Distrib 8.0.42, for macos15 (x86_64)
--
-- Host: localhost    Database: university_db
-- ------------------------------------------------------
-- Server version	9.3.0

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
-- Table structure for table `AdvisingHistory`
--

DROP TABLE IF EXISTS `AdvisingHistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `AdvisingHistory` (
  `advising_id` int NOT NULL AUTO_INCREMENT,
  `student_id` int NOT NULL,
  `lecturer_id` int NOT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  PRIMARY KEY (`advising_id`),
  KEY `student_id` (`student_id`),
  KEY `lecturer_id` (`lecturer_id`),
  CONSTRAINT `advisinghistory_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `Students` (`student_id`) ON DELETE CASCADE,
  CONSTRAINT `advisinghistory_ibfk_2` FOREIGN KEY (`lecturer_id`) REFERENCES `Lecturers` (`lecturer_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=323 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AdvisingHistory`
--

LOCK TABLES `AdvisingHistory` WRITE;
/*!40000 ALTER TABLE `AdvisingHistory` DISABLE KEYS */;
INSERT INTO `AdvisingHistory` VALUES (1,1,1,'2022-09-01','2023-08-31'),(2,1,7,'2023-09-01',NULL),(3,2,3,'2021-09-01',NULL),(4,4,1,'2024-09-01',NULL),(5,1,2,'2024-09-01',NULL),(6,3,4,'2024-09-01',NULL),(7,8,9,'2024-09-01',NULL),(8,11,12,'2024-09-01',NULL),(9,15,16,'2024-09-01',NULL),(10,20,1,'2024-09-01',NULL),(11,23,4,'2024-09-01',NULL),(12,29,10,'2024-09-01',NULL),(13,35,16,'2024-09-01',NULL),(14,41,2,'2024-09-01',NULL),(15,47,8,'2024-09-01',NULL),(16,53,14,'2024-09-01',NULL),(17,59,20,'2024-09-01',NULL),(18,65,6,'2024-09-01',NULL),(19,71,12,'2024-09-01',NULL),(20,77,18,'2024-09-01',NULL),(21,83,4,'2024-09-01',NULL),(22,89,10,'2024-09-01',NULL),(23,95,16,'2024-09-01',NULL),(24,101,2,'2024-09-01',NULL),(25,107,8,'2024-09-01',NULL),(26,113,14,'2024-09-01',NULL),(27,119,20,'2024-09-01',NULL),(28,125,6,'2024-09-01',NULL),(29,131,12,'2024-09-01',NULL),(30,137,18,'2024-09-01',NULL),(31,143,4,'2024-09-01',NULL),(32,149,10,'2024-09-01',NULL),(33,155,16,'2024-09-01',NULL),(34,161,2,'2024-09-01',NULL),(35,167,8,'2024-09-01',NULL),(36,173,14,'2024-09-01',NULL),(37,179,20,'2024-09-01',NULL),(38,185,6,'2024-09-01',NULL),(39,191,12,'2024-09-01',NULL),(40,197,18,'2024-09-01',NULL),(41,4,5,'2024-09-01',NULL),(42,10,11,'2024-09-01',NULL),(43,16,17,'2024-09-01',NULL),(44,24,5,'2024-09-01',NULL),(45,30,11,'2024-09-01',NULL),(46,36,17,'2024-09-01',NULL),(47,42,3,'2024-09-01',NULL),(48,48,9,'2024-09-01',NULL),(49,54,15,'2024-09-01',NULL),(50,60,1,'2024-09-01',NULL),(51,66,7,'2024-09-01',NULL),(52,72,13,'2024-09-01',NULL),(53,78,19,'2024-09-01',NULL),(54,84,5,'2024-09-01',NULL),(55,90,11,'2024-09-01',NULL),(56,96,17,'2024-09-01',NULL),(57,102,3,'2024-09-01',NULL),(58,108,9,'2024-09-01',NULL),(59,114,15,'2024-09-01',NULL),(60,120,1,'2024-09-01',NULL),(61,126,7,'2024-09-01',NULL),(62,132,13,'2024-09-01',NULL),(63,138,19,'2024-09-01',NULL),(64,144,5,'2024-09-01',NULL),(65,150,11,'2024-09-01',NULL),(66,156,17,'2024-09-01',NULL),(67,162,3,'2024-09-01',NULL),(68,168,9,'2024-09-01',NULL),(69,174,15,'2024-09-01',NULL),(70,180,1,'2024-09-01',NULL),(71,186,7,'2024-09-01',NULL),(72,192,13,'2024-09-01',NULL),(73,198,19,'2024-09-01',NULL),(74,2,3,'2024-09-01',NULL),(75,9,10,'2024-09-01',NULL),(76,14,15,'2024-09-01',NULL),(77,21,2,'2024-09-01',NULL),(78,27,8,'2024-09-01',NULL),(79,33,14,'2024-09-01',NULL),(80,39,20,'2024-09-01',NULL),(81,45,6,'2024-09-01',NULL),(82,51,12,'2024-09-01',NULL),(83,57,18,'2024-09-01',NULL),(84,63,4,'2024-09-01',NULL),(85,69,10,'2024-09-01',NULL),(86,75,16,'2024-09-01',NULL),(87,81,2,'2024-09-01',NULL),(88,87,8,'2024-09-01',NULL),(89,93,14,'2024-09-01',NULL),(90,99,20,'2024-09-01',NULL),(91,105,6,'2024-09-01',NULL),(92,111,12,'2024-09-01',NULL),(93,117,18,'2024-09-01',NULL),(94,123,4,'2024-09-01',NULL),(95,129,10,'2024-09-01',NULL),(96,135,16,'2024-09-01',NULL),(97,141,2,'2024-09-01',NULL),(98,147,8,'2024-09-01',NULL),(99,153,14,'2024-09-01',NULL),(100,159,20,'2024-09-01',NULL),(101,165,6,'2024-09-01',NULL),(102,171,12,'2024-09-01',NULL),(103,177,18,'2024-09-01',NULL),(104,183,4,'2024-09-01',NULL),(105,189,10,'2024-09-01',NULL),(106,195,16,'2024-09-01',NULL),(107,5,6,'2024-09-01',NULL),(108,7,8,'2024-09-01',NULL),(109,17,18,'2024-09-01',NULL),(110,25,6,'2024-09-01',NULL),(111,31,12,'2024-09-01',NULL),(112,37,18,'2024-09-01',NULL),(113,43,4,'2024-09-01',NULL),(114,49,10,'2024-09-01',NULL),(115,55,16,'2024-09-01',NULL),(116,61,2,'2024-09-01',NULL),(117,67,8,'2024-09-01',NULL),(118,73,14,'2024-09-01',NULL),(119,79,20,'2024-09-01',NULL),(120,85,6,'2024-09-01',NULL),(121,91,12,'2024-09-01',NULL),(122,97,18,'2024-09-01',NULL),(123,103,4,'2024-09-01',NULL),(124,109,10,'2024-09-01',NULL),(125,115,16,'2024-09-01',NULL),(126,121,2,'2024-09-01',NULL),(127,127,8,'2024-09-01',NULL),(128,133,14,'2024-09-01',NULL),(129,139,20,'2024-09-01',NULL),(130,145,6,'2024-09-01',NULL),(131,151,12,'2024-09-01',NULL),(132,157,18,'2024-09-01',NULL),(133,163,4,'2024-09-01',NULL),(134,169,10,'2024-09-01',NULL),(135,175,16,'2024-09-01',NULL),(136,181,2,'2024-09-01',NULL),(137,187,8,'2024-09-01',NULL),(138,193,14,'2024-09-01',NULL),(139,199,20,'2024-09-01',NULL),(140,6,7,'2024-09-01',NULL),(141,12,13,'2024-09-01',NULL),(142,18,19,'2024-09-01',NULL),(143,22,3,'2024-09-01',NULL),(144,28,9,'2024-09-01',NULL),(145,34,15,'2024-09-01',NULL),(146,40,1,'2024-09-01',NULL),(147,46,7,'2024-09-01',NULL),(148,52,13,'2024-09-01',NULL),(149,58,19,'2024-09-01',NULL),(150,64,5,'2024-09-01',NULL),(151,70,11,'2024-09-01',NULL),(152,76,17,'2024-09-01',NULL),(153,82,3,'2024-09-01',NULL),(154,88,9,'2024-09-01',NULL),(155,94,15,'2024-09-01',NULL),(156,100,1,'2024-09-01',NULL),(157,106,7,'2024-09-01',NULL),(158,112,13,'2024-09-01',NULL),(159,118,19,'2024-09-01',NULL),(160,124,5,'2024-09-01',NULL),(161,130,11,'2024-09-01',NULL),(162,136,17,'2024-09-01',NULL),(163,142,3,'2024-09-01',NULL),(164,148,9,'2024-09-01',NULL),(165,154,15,'2024-09-01',NULL),(166,160,1,'2024-09-01',NULL),(167,166,7,'2024-09-01',NULL),(168,172,13,'2024-09-01',NULL),(169,178,19,'2024-09-01',NULL),(170,184,5,'2024-09-01',NULL),(171,190,11,'2024-09-01',NULL),(172,196,17,'2024-09-01',NULL),(173,13,14,'2024-09-01',NULL),(174,19,20,'2024-09-01',NULL),(175,26,7,'2024-09-01',NULL),(176,32,13,'2024-09-01',NULL),(177,38,19,'2024-09-01',NULL),(178,44,5,'2024-09-01',NULL),(179,50,11,'2024-09-01',NULL),(180,56,17,'2024-09-01',NULL),(181,62,3,'2024-09-01',NULL),(182,68,9,'2024-09-01',NULL),(183,74,15,'2024-09-01',NULL),(184,80,1,'2024-09-01',NULL),(185,86,7,'2024-09-01',NULL),(186,92,13,'2024-09-01',NULL),(187,98,19,'2024-09-01',NULL),(188,104,5,'2024-09-01',NULL),(189,110,11,'2024-09-01',NULL),(190,116,17,'2024-09-01',NULL),(191,122,3,'2024-09-01',NULL),(192,128,9,'2024-09-01',NULL),(193,134,15,'2024-09-01',NULL),(194,140,1,'2024-09-01',NULL),(195,146,7,'2024-09-01',NULL),(196,152,13,'2024-09-01',NULL),(197,158,19,'2024-09-01',NULL),(198,164,5,'2024-09-01',NULL),(199,170,11,'2024-09-01',NULL),(200,176,17,'2024-09-01',NULL),(201,182,3,'2024-09-01',NULL),(202,188,9,'2024-09-01',NULL),(203,194,15,'2024-09-01',NULL),(204,200,1,'2024-09-01',NULL),(260,8,14,'2023-09-01','2024-08-31'),(261,20,6,'2023-09-01','2024-08-31'),(262,4,10,'2023-09-01','2024-08-31'),(263,16,2,'2023-09-01','2024-08-31'),(264,24,10,'2023-09-01','2024-08-31'),(265,36,2,'2023-09-01','2024-08-31'),(266,48,14,'2023-09-01','2024-08-31'),(267,60,6,'2023-09-01','2024-08-31'),(268,72,18,'2023-09-01','2024-08-31'),(269,84,10,'2023-09-01','2024-08-31'),(270,96,2,'2023-09-01','2024-08-31'),(271,108,14,'2023-09-01','2024-08-31'),(272,120,6,'2023-09-01','2024-08-31'),(273,132,18,'2023-09-01','2024-08-31'),(274,144,10,'2023-09-01','2024-08-31'),(275,156,2,'2023-09-01','2024-08-31'),(276,168,14,'2023-09-01','2024-08-31'),(277,180,6,'2023-09-01','2024-08-31'),(278,192,18,'2023-09-01','2024-08-31'),(279,12,18,'2023-09-01','2024-08-31'),(280,28,14,'2023-09-01','2024-08-31'),(281,40,6,'2023-09-01','2024-08-31'),(282,52,18,'2023-09-01','2024-08-31'),(283,64,10,'2023-09-01','2024-08-31'),(284,76,2,'2023-09-01','2024-08-31'),(285,88,14,'2023-09-01','2024-08-31'),(286,100,6,'2023-09-01','2024-08-31'),(287,112,18,'2023-09-01','2024-08-31'),(288,124,10,'2023-09-01','2024-08-31'),(289,136,2,'2023-09-01','2024-08-31'),(290,148,14,'2023-09-01','2024-08-31'),(291,160,6,'2023-09-01','2024-08-31'),(292,172,18,'2023-09-01','2024-08-31'),(293,184,10,'2023-09-01','2024-08-31'),(294,196,2,'2023-09-01','2024-08-31'),(295,32,18,'2023-09-01','2024-08-31'),(296,44,10,'2023-09-01','2024-08-31'),(297,56,2,'2023-09-01','2024-08-31'),(298,68,14,'2023-09-01','2024-08-31'),(299,80,6,'2023-09-01','2024-08-31'),(300,92,18,'2023-09-01','2024-08-31'),(301,104,10,'2023-09-01','2024-08-31'),(302,116,2,'2023-09-01','2024-08-31'),(303,128,14,'2023-09-01','2024-08-31'),(304,140,6,'2023-09-01','2024-08-31'),(305,152,18,'2023-09-01','2024-08-31'),(306,164,10,'2023-09-01','2024-08-31'),(307,176,2,'2023-09-01','2024-08-31'),(308,188,14,'2023-09-01','2024-08-31'),(309,200,6,'2023-09-01','2024-08-31');
/*!40000 ALTER TABLE `AdvisingHistory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CommitteeMembers`
--

DROP TABLE IF EXISTS `CommitteeMembers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CommitteeMembers` (
  `committee_id` int NOT NULL,
  `lecturer_id` int NOT NULL,
  PRIMARY KEY (`committee_id`,`lecturer_id`),
  KEY `lecturer_id` (`lecturer_id`),
  CONSTRAINT `committeemembers_ibfk_1` FOREIGN KEY (`committee_id`) REFERENCES `Committees` (`committee_id`) ON DELETE CASCADE,
  CONSTRAINT `committeemembers_ibfk_2` FOREIGN KEY (`lecturer_id`) REFERENCES `Lecturers` (`lecturer_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CommitteeMembers`
--

LOCK TABLES `CommitteeMembers` WRITE;
/*!40000 ALTER TABLE `CommitteeMembers` DISABLE KEYS */;
INSERT INTO `CommitteeMembers` VALUES (1,1),(1,3),(2,7),(3,15);
/*!40000 ALTER TABLE `CommitteeMembers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Committees`
--

DROP TABLE IF EXISTS `Committees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Committees` (
  `committee_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` text,
  PRIMARY KEY (`committee_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Committees`
--

LOCK TABLES `Committees` WRITE;
/*!40000 ALTER TABLE `Committees` DISABLE KEYS */;
INSERT INTO `Committees` VALUES (1,'Academic Integrity Committee','Oversees academic honesty and policy.'),(2,'Curriculum Committee','Reviews and approves new courses and programs.'),(3,'Faculty Hiring Committee','Manages the process of hiring new faculty.');
/*!40000 ALTER TABLE `Committees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CourseMaterials`
--

DROP TABLE IF EXISTS `CourseMaterials`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CourseMaterials` (
  `material_id` int NOT NULL AUTO_INCREMENT,
  `offering_id` int NOT NULL,
  `material_type` varchar(100) DEFAULT NULL,
  `material_details` text,
  PRIMARY KEY (`material_id`),
  KEY `offering_id` (`offering_id`),
  CONSTRAINT `coursematerials_ibfk_1` FOREIGN KEY (`offering_id`) REFERENCES `CourseOfferings` (`offering_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CourseMaterials`
--

LOCK TABLES `CourseMaterials` WRITE;
/*!40000 ALTER TABLE `CourseMaterials` DISABLE KEYS */;
INSERT INTO `CourseMaterials` VALUES (1,7,'Book','Intro to DBs'),(2,8,'Movie','Brave Heart');
/*!40000 ALTER TABLE `CourseMaterials` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CourseOfferings`
--

DROP TABLE IF EXISTS `CourseOfferings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CourseOfferings` (
  `offering_id` int NOT NULL AUTO_INCREMENT,
  `course_id` int NOT NULL,
  `lecturer_id` int DEFAULT NULL,
  `semester` varchar(50) DEFAULT NULL,
  `year` int DEFAULT NULL,
  `schedule` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`offering_id`),
  KEY `course_id` (`course_id`),
  KEY `lecturer_id` (`lecturer_id`),
  CONSTRAINT `courseofferings_ibfk_1` FOREIGN KEY (`course_id`) REFERENCES `Courses` (`course_id`) ON DELETE CASCADE,
  CONSTRAINT `courseofferings_ibfk_2` FOREIGN KEY (`lecturer_id`) REFERENCES `Lecturers` (`lecturer_id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CourseOfferings`
--

LOCK TABLES `CourseOfferings` WRITE;
/*!40000 ALTER TABLE `CourseOfferings` DISABLE KEYS */;
INSERT INTO `CourseOfferings` VALUES (1,1,1,'Fall',2023,'MWF 10:00-11:00'),(2,2,7,'Fall',2023,'TTh 13:00-14:30'),(3,4,2,'Spring',2024,'MWF 09:00-10:00'),(4,1,9,'Fall',2024,'MWF 11:00-12:00'),(5,3,1,'Fall',2024,'TTh 10:00-11:30'),(6,5,8,'Fall',2024,'TTh 14:00-15:30'),(7,2,1,'Spring',2025,'MWF 10:00-11:00'),(8,6,3,'Spring',2025,'TTh 09:00-10:30'),(9,5,8,'Fall',2026,NULL);
/*!40000 ALTER TABLE `CourseOfferings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CoursePrerequisites`
--

DROP TABLE IF EXISTS `CoursePrerequisites`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CoursePrerequisites` (
  `course_id` int NOT NULL,
  `prerequisite_id` int NOT NULL,
  PRIMARY KEY (`course_id`,`prerequisite_id`),
  KEY `prerequisite_id` (`prerequisite_id`),
  CONSTRAINT `courseprerequisites_ibfk_1` FOREIGN KEY (`course_id`) REFERENCES `Courses` (`course_id`) ON DELETE CASCADE,
  CONSTRAINT `courseprerequisites_ibfk_2` FOREIGN KEY (`prerequisite_id`) REFERENCES `Courses` (`course_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CoursePrerequisites`
--

LOCK TABLES `CoursePrerequisites` WRITE;
/*!40000 ALTER TABLE `CoursePrerequisites` DISABLE KEYS */;
INSERT INTO `CoursePrerequisites` VALUES (2,1),(3,1),(5,4),(10,7),(11,9);
/*!40000 ALTER TABLE `CoursePrerequisites` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Courses`
--

DROP TABLE IF EXISTS `Courses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Courses` (
  `course_id` int NOT NULL AUTO_INCREMENT,
  `course_code` varchar(20) NOT NULL,
  `name` varchar(255) NOT NULL,
  `description` text,
  `department_id` int DEFAULT NULL,
  `credits` int DEFAULT NULL,
  `level` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`course_id`),
  UNIQUE KEY `course_code` (`course_code`),
  KEY `department_id` (`department_id`),
  CONSTRAINT `courses_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `Departments` (`department_id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Courses`
--

LOCK TABLES `Courses` WRITE;
/*!40000 ALTER TABLE `Courses` DISABLE KEYS */;
INSERT INTO `Courses` VALUES (1,'CS101','Introduction to Programming','Fundamentals of programming using Python.',1,3,'100'),(2,'CS301','Databases','Design and implementation of database systems.',1,4,'300'),(3,'CS450','Artificial Intelligence','Core concepts of AI and machine learning.',1,4,'400'),(4,'PHY101','Classical Mechanics','Introduction to Newtonian mechanics.',2,4,'100'),(5,'PHY350','Quantum Mechanics','Fundamentals of quantum theory.',2,4,'300'),(6,'HIS202','The Roman Empire','A survey of Roman history from Augustus to Constantine.',3,3,'200'),(7,'MTH210','Linear Algebra','Vectors, matrices, and linear transformations.',4,4,'200'),(8,'LIT401','Shakespeare','An in-depth study of Shakespeare\'s major works.',5,3,'400'),(9,'BIO110','Principles of Biology','Core concepts of modern biology.',6,4,'100'),(10,'MTH310','Advanced Algebra','Vectors, matrices, and linear transformations.',4,4,'300'),(11,'BIO320','Neurology','Neurology ..etc',6,4,'300');
/*!40000 ALTER TABLE `Courses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DepartmentResearchAreas`
--

DROP TABLE IF EXISTS `DepartmentResearchAreas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `DepartmentResearchAreas` (
  `department_id` int NOT NULL,
  `area_id` int NOT NULL,
  PRIMARY KEY (`department_id`,`area_id`),
  KEY `area_id` (`area_id`),
  CONSTRAINT `departmentresearchareas_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `Departments` (`department_id`) ON DELETE CASCADE,
  CONSTRAINT `departmentresearchareas_ibfk_2` FOREIGN KEY (`area_id`) REFERENCES `ResearchAreas` (`area_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DepartmentResearchAreas`
--

LOCK TABLES `DepartmentResearchAreas` WRITE;
/*!40000 ALTER TABLE `DepartmentResearchAreas` DISABLE KEYS */;
INSERT INTO `DepartmentResearchAreas` VALUES (1,1),(1,2),(3,3),(4,4),(5,5),(6,6),(2,7),(1,8),(6,9),(3,10),(2,11),(1,12);
/*!40000 ALTER TABLE `DepartmentResearchAreas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Departments`
--

DROP TABLE IF EXISTS `Departments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Departments` (
  `department_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`department_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Departments`
--

LOCK TABLES `Departments` WRITE;
/*!40000 ALTER TABLE `Departments` DISABLE KEYS */;
INSERT INTO `Departments` VALUES (1,'Computer Science'),(2,'Physics'),(3,'History'),(4,'Mathematics'),(5,'Literature'),(6,'Biology'),(7,'Administrative'),(8,'HR');
/*!40000 ALTER TABLE `Departments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DisciplinaryRecords`
--

DROP TABLE IF EXISTS `DisciplinaryRecords`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `DisciplinaryRecords` (
  `record_id` int NOT NULL AUTO_INCREMENT,
  `student_id` int NOT NULL,
  `date_of_incident` date DEFAULT NULL,
  `description` text,
  PRIMARY KEY (`record_id`),
  KEY `student_id` (`student_id`),
  CONSTRAINT `disciplinaryrecords_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `Students` (`student_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DisciplinaryRecords`
--

LOCK TABLES `DisciplinaryRecords` WRITE;
/*!40000 ALTER TABLE `DisciplinaryRecords` DISABLE KEYS */;
/*!40000 ALTER TABLE `DisciplinaryRecords` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `EmergencyContacts`
--

DROP TABLE IF EXISTS `EmergencyContacts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `EmergencyContacts` (
  `contact_id` int NOT NULL AUTO_INCREMENT,
  `staff_id` int NOT NULL,
  `name` varchar(200) NOT NULL,
  `relationship` varchar(100) DEFAULT NULL,
  `phone_number` varchar(20) NOT NULL,
  PRIMARY KEY (`contact_id`),
  KEY `staff_id` (`staff_id`),
  CONSTRAINT `emergencycontacts_ibfk_1` FOREIGN KEY (`staff_id`) REFERENCES `NonAcademicStaff` (`staff_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `EmergencyContacts`
--

LOCK TABLES `EmergencyContacts` WRITE;
/*!40000 ALTER TABLE `EmergencyContacts` DISABLE KEYS */;
INSERT INTO `EmergencyContacts` VALUES (1,1,'Mary Smith','Spouse','987-654-3210'),(2,2,'Robert Doe','Brother','987-654-3211'),(3,3,'Sarah Jones','Daughter','987-654-3212');
/*!40000 ALTER TABLE `EmergencyContacts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Enrollment`
--

DROP TABLE IF EXISTS `Enrollment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Enrollment` (
  `enrollment_id` int NOT NULL AUTO_INCREMENT,
  `student_id` int NOT NULL,
  `offering_id` int NOT NULL,
  PRIMARY KEY (`enrollment_id`),
  KEY `student_id` (`student_id`),
  KEY `offering_id` (`offering_id`),
  CONSTRAINT `enrollment_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `Students` (`student_id`) ON DELETE CASCADE,
  CONSTRAINT `enrollment_ibfk_2` FOREIGN KEY (`offering_id`) REFERENCES `CourseOfferings` (`offering_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=901 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Enrollment`
--

LOCK TABLES `Enrollment` WRITE;
/*!40000 ALTER TABLE `Enrollment` DISABLE KEYS */;
INSERT INTO `Enrollment` VALUES (1,1,1),(2,1,4),(3,2,2),(4,2,5),(5,3,1),(6,1,3),(7,1,2),(8,1,1),(9,2,3),(10,2,2),(11,2,1),(12,3,3),(13,3,2),(14,3,1),(15,4,2),(16,5,3),(17,5,2),(18,5,1),(19,6,3),(20,6,2),(21,6,1),(22,7,3),(23,7,1),(24,8,3),(25,8,2),(26,8,1),(27,9,3),(28,9,1),(29,10,3),(30,10,2),(31,10,1),(32,11,2),(33,11,1),(34,12,3),(35,13,3),(36,13,2),(37,13,1),(38,14,3),(39,14,2),(40,15,3),(41,15,1),(42,16,2),(43,16,1),(44,18,3),(45,18,2),(46,18,1),(47,19,2),(48,20,2),(49,20,1),(50,21,3),(51,21,2),(52,21,1),(53,22,3),(54,22,2),(55,22,1),(56,23,3),(57,23,1),(58,24,2),(59,25,3),(60,25,2),(61,25,1),(62,26,2),(63,26,1),(64,27,3),(65,27,2),(66,27,1),(67,28,3),(68,28,2),(69,29,3),(70,29,2),(71,29,1),(72,30,3),(73,31,3),(74,31,1),(75,32,3),(76,32,2),(77,32,1),(78,33,3),(79,33,2),(80,33,1),(81,34,3),(82,34,2),(83,34,1),(84,35,3),(85,35,2),(86,35,1),(87,36,3),(88,36,2),(89,36,1),(90,37,3),(91,37,1),(92,38,3),(93,38,2),(94,38,1),(95,39,3),(96,39,2),(97,39,1),(98,40,3),(99,40,2),(100,40,1),(101,41,2),(102,41,1),(103,42,3),(104,42,2),(105,43,3),(106,43,2),(107,44,2),(108,44,1),(109,45,3),(110,45,1),(111,46,2),(112,47,3),(113,47,2),(114,47,1),(115,48,3),(116,48,2),(117,48,1),(118,49,3),(119,49,2),(120,49,1),(121,50,1),(133,1,6),(134,1,5),(135,3,6),(136,3,5),(137,8,6),(138,8,4),(139,11,4),(140,15,6),(141,15,5),(142,15,4),(143,20,6),(144,20,5),(145,23,6),(146,23,4),(147,29,6),(148,35,5),(149,35,4),(150,41,6),(151,41,4),(152,47,6),(153,47,5),(154,47,4),(155,53,6),(156,53,4),(157,59,5),(158,59,4),(159,65,5),(160,71,6),(161,71,4),(162,77,6),(163,77,4),(164,83,5),(165,83,4),(166,89,6),(167,89,4),(168,95,6),(169,107,6),(170,107,5),(171,113,6),(172,113,4),(173,119,6),(174,119,4),(175,125,6),(176,125,4),(177,131,6),(178,131,4),(179,137,6),(180,137,5),(181,137,4),(182,143,5),(183,143,4),(184,149,6),(185,149,5),(186,155,5),(187,161,5),(188,167,6),(189,167,5),(190,173,6),(191,173,4),(192,179,6),(193,179,4),(194,185,6),(195,185,5),(196,191,5),(197,197,6),(198,197,5),(199,197,4),(200,4,6),(201,4,4),(202,10,6),(203,10,5),(204,10,4),(205,16,5),(206,24,6),(207,24,5),(208,24,4),(209,30,6),(210,30,4),(211,36,6),(212,42,5),(213,48,4),(214,54,5),(215,60,6),(216,60,4),(217,66,6),(218,66,5),(219,66,4),(220,72,5),(221,72,4),(222,78,4),(223,84,6),(224,84,5),(225,84,4),(226,90,6),(227,96,6),(228,96,5),(229,96,4),(230,102,6),(231,102,5),(232,102,4),(233,108,6),(234,108,4),(235,114,6),(236,114,5),(237,114,4),(238,120,5),(239,126,6),(240,126,5),(241,126,4),(242,132,4),(243,138,5),(244,138,4),(245,144,5),(246,150,6),(247,150,5),(248,150,4),(249,156,6),(250,156,5),(251,156,4),(252,162,6),(253,162,5),(254,168,5),(255,174,6),(256,174,5),(257,180,5),(258,180,4),(259,186,6),(260,186,4),(261,192,6),(262,192,4),(263,198,6),(264,198,4),(265,2,6),(266,2,5),(267,2,4),(268,9,6),(269,9,5),(270,9,4),(271,14,6),(272,14,5),(273,14,4),(274,21,6),(275,21,5),(276,21,4),(277,27,6),(278,33,6),(279,33,4),(280,39,6),(281,39,5),(282,39,4),(283,45,6),(284,45,5),(285,45,4),(286,51,6),(287,51,5),(288,57,6),(289,57,5),(290,57,4),(291,63,6),(292,69,6),(293,69,4),(294,75,6),(295,75,5),(296,75,4),(297,81,6),(298,81,5),(299,87,6),(300,87,4),(301,99,5),(302,99,4),(303,105,6),(304,105,5),(305,111,5),(306,117,5),(307,123,6),(308,129,5),(309,135,6),(310,135,4),(311,141,6),(312,141,5),(313,141,4),(314,147,6),(315,147,5),(316,147,4),(317,153,6),(318,153,5),(319,153,4),(320,159,6),(321,159,5),(322,159,4),(323,165,5),(324,165,4),(325,171,6),(326,171,5),(327,171,4),(328,177,5),(329,183,6),(330,183,5),(331,183,4),(332,189,5),(333,189,4),(334,195,6),(335,195,5),(336,195,4),(337,5,6),(338,5,5),(339,5,4),(340,7,6),(341,7,4),(342,17,6),(343,17,5),(344,17,4),(345,25,6),(346,25,5),(347,25,4),(348,31,6),(349,31,4),(350,37,6),(351,37,5),(352,37,4),(353,43,6),(354,43,5),(355,43,4),(356,49,6),(357,49,5),(358,55,6),(359,61,4),(360,67,6),(361,67,5),(362,67,4),(363,73,4),(364,79,6),(365,79,5),(366,85,6),(367,85,5),(368,91,6),(369,91,4),(370,97,5),(371,97,4),(372,103,6),(373,103,4),(374,109,6),(375,109,5),(376,115,6),(377,115,5),(378,115,4),(379,121,6),(380,121,5),(381,127,6),(382,127,5),(383,127,4),(384,133,5),(385,133,4),(386,139,6),(387,139,5),(388,139,4),(389,145,6),(390,145,5),(391,151,6),(392,157,6),(393,157,4),(394,163,6),(395,163,5),(396,163,4),(397,169,6),(398,169,5),(399,169,4),(400,175,6),(401,175,4),(402,187,4),(403,193,5),(404,193,4),(405,199,6),(406,199,5),(407,6,6),(408,6,5),(409,6,4),(410,12,5),(411,12,4),(412,18,6),(413,18,5),(414,18,4),(415,22,6),(416,22,5),(417,22,4),(418,34,5),(419,40,6),(420,40,5),(421,40,4),(422,46,6),(423,46,4),(424,52,6),(425,52,5),(426,52,4),(427,58,6),(428,58,5),(429,64,6),(430,64,5),(431,70,6),(432,70,4),(433,76,5),(434,82,6),(435,82,4),(436,88,6),(437,88,4),(438,94,6),(439,94,5),(440,94,4),(441,100,5),(442,100,4),(443,112,6),(444,112,5),(445,112,4),(446,118,6),(447,118,5),(448,124,6),(449,124,4),(450,130,4),(451,136,6),(452,136,5),(453,136,4),(454,142,6),(455,142,5),(456,142,4),(457,148,4),(458,154,5),(459,160,5),(460,160,4),(461,166,5),(462,172,6),(463,172,4),(464,178,6),(465,178,5),(466,178,4),(467,184,6),(468,184,4),(469,190,6),(470,190,5),(471,190,4),(472,196,6),(473,196,5),(474,196,4),(475,13,5),(476,13,4),(477,19,6),(478,19,4),(479,26,6),(480,26,5),(481,26,4),(482,32,6),(483,32,4),(484,38,6),(485,38,5),(486,38,4),(487,44,5),(488,50,5),(489,50,4),(490,56,6),(491,56,5),(492,56,4),(493,62,6),(494,62,4),(495,68,6),(496,68,5),(497,68,4),(498,74,6),(499,74,5),(500,74,4),(501,80,6),(502,80,4),(503,86,6),(504,86,5),(505,86,4),(506,92,5),(507,92,4),(508,98,6),(509,98,5),(510,104,6),(511,104,5),(512,104,4),(513,110,6),(514,110,5),(515,116,6),(516,116,4),(517,122,6),(518,122,5),(519,122,4),(520,128,6),(521,128,5),(522,128,4),(523,134,6),(524,134,5),(525,134,4),(526,140,6),(527,140,5),(528,140,4),(529,146,5),(530,152,5),(531,152,4),(532,158,6),(533,164,6),(534,164,5),(535,164,4),(536,170,6),(537,170,5),(538,176,6),(539,176,4),(540,182,6),(541,182,5),(542,182,4),(543,188,6),(544,188,4),(545,194,6),(546,194,4),(547,200,6),(548,200,5),(549,200,4),(644,100,8),(645,100,7),(646,101,8),(647,101,7),(648,102,7),(649,103,8),(650,103,7),(651,104,8),(652,104,7),(653,105,7),(654,106,8),(655,107,8),(656,109,8),(657,110,7),(658,111,7),(659,112,8),(660,112,7),(661,113,8),(662,113,7),(663,114,8),(664,114,7),(665,115,8),(666,115,7),(667,118,8),(668,119,8),(669,119,7),(670,120,8),(671,120,7),(672,121,8),(673,121,7),(674,122,8),(675,122,7),(676,123,7),(677,124,8),(678,124,7),(679,125,8),(680,125,7),(681,126,8),(682,126,7),(683,128,8),(684,128,7),(685,129,7),(686,130,7),(687,131,8),(688,132,7),(689,133,8),(690,133,7),(691,135,7),(692,136,8),(693,137,8),(694,138,8),(695,138,7),(696,139,7),(697,140,8),(698,141,8),(699,141,7),(700,142,7),(701,143,8),(702,144,7),(703,145,8),(704,145,7),(705,146,8),(706,146,7),(707,147,8),(708,147,7),(709,148,8),(710,149,7),(711,150,8),(712,150,7),(713,151,7),(714,153,8),(715,153,7),(716,154,7),(717,155,7),(718,156,8),(719,157,7),(720,158,7),(721,160,7),(722,161,8),(723,161,7),(724,162,8),(725,162,7),(726,163,8),(727,163,7),(728,164,7),(729,165,8),(730,165,7),(731,166,7),(732,167,8),(733,167,7),(734,168,8),(735,170,8),(736,170,7),(737,171,7),(738,172,8),(739,173,8),(740,173,7),(741,174,8),(742,174,7),(743,175,7),(744,176,8),(745,176,7),(746,177,8),(747,178,8),(748,179,8),(749,180,7),(750,181,8),(751,181,7),(752,182,8),(753,182,7),(754,183,7),(755,184,8),(756,184,7),(757,185,8),(758,185,7),(759,186,8),(760,186,7),(761,187,8),(762,187,7),(763,188,8),(764,188,7),(765,189,8),(766,189,7),(767,190,7),(768,194,8),(769,194,7),(770,195,8),(771,195,7),(772,196,8),(773,196,7),(774,197,8),(775,197,7),(776,198,8),(777,198,7),(778,199,7),(779,200,7),(899,1,8),(900,1,9);
/*!40000 ALTER TABLE `Enrollment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Grades`
--

DROP TABLE IF EXISTS `Grades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Grades` (
  `grade_id` int NOT NULL AUTO_INCREMENT,
  `enrollment_id` int NOT NULL,
  `grade_percentage` decimal(5,2) DEFAULT NULL,
  PRIMARY KEY (`grade_id`),
  KEY `enrollment_id` (`enrollment_id`),
  CONSTRAINT `grades_ibfk_1` FOREIGN KEY (`enrollment_id`) REFERENCES `Enrollment` (`enrollment_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=133 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Grades`
--

LOCK TABLES `Grades` WRITE;
/*!40000 ALTER TABLE `Grades` DISABLE KEYS */;
INSERT INTO `Grades` VALUES (1,1,88.50),(2,2,92.00),(3,3,75.00),(4,5,95.00),(5,1,64.52),(6,5,66.81),(7,8,80.46),(8,11,61.90),(9,14,88.12),(10,18,74.89),(11,21,90.07),(12,23,85.70),(13,26,98.31),(14,28,94.41),(15,31,77.15),(16,33,82.52),(17,37,81.16),(18,41,98.23),(19,43,67.66),(20,46,63.63),(21,49,95.17),(22,52,64.93),(23,55,99.17),(24,57,81.06),(25,61,87.79),(26,63,95.78),(27,66,75.50),(28,71,70.19),(29,74,64.45),(30,77,91.68),(31,80,85.05),(32,83,90.22),(33,86,95.94),(34,89,69.05),(35,91,77.41),(36,94,79.90),(37,97,67.27),(38,100,76.67),(39,102,81.51),(40,108,77.55),(41,110,83.23),(42,114,83.50),(43,117,67.82),(44,120,68.60),(45,121,79.55),(46,3,91.95),(47,7,81.11),(48,10,69.67),(49,13,85.03),(50,15,76.13),(51,17,65.57),(52,20,79.45),(53,25,60.55),(54,30,84.39),(55,32,60.30),(56,36,68.35),(57,39,60.84),(58,42,79.17),(59,45,73.30),(60,47,68.98),(61,48,65.02),(62,51,98.14),(63,54,75.65),(64,58,63.83),(65,60,72.19),(66,62,69.47),(67,65,70.76),(68,68,85.41),(69,70,74.78),(70,76,97.64),(71,79,83.87),(72,82,66.44),(73,85,60.58),(74,88,83.60),(75,93,96.26),(76,96,90.48),(77,99,63.64),(78,101,66.74),(79,104,82.77),(80,106,73.64),(81,107,99.91),(82,111,98.61),(83,113,93.31),(84,116,70.72),(85,119,93.69),(86,6,76.27),(87,9,80.30),(88,12,72.68),(89,16,62.50),(90,19,74.48),(91,22,84.87),(92,24,60.91),(93,27,69.94),(94,29,66.98),(95,34,65.06),(96,35,64.38),(97,38,66.72),(98,40,80.46),(99,44,62.12),(100,50,89.25),(101,53,79.86),(102,56,71.55),(103,59,98.20),(104,64,96.33),(105,67,87.07),(106,69,86.33),(107,72,70.45),(108,73,73.27),(109,75,94.99),(110,78,75.14),(111,81,70.73),(112,84,68.23),(113,87,68.95),(114,90,80.05),(115,92,93.40),(116,95,86.88),(117,98,94.17),(118,103,70.22),(119,105,88.60),(120,109,92.35),(121,112,95.96),(122,115,62.71),(123,118,85.70),(132,337,99.00);
/*!40000 ALTER TABLE `Grades` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `LecturerPublications`
--

DROP TABLE IF EXISTS `LecturerPublications`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `LecturerPublications` (
  `lecturer_id` int NOT NULL,
  `publication_id` int NOT NULL,
  PRIMARY KEY (`lecturer_id`,`publication_id`),
  KEY `publication_id` (`publication_id`),
  CONSTRAINT `lecturerpublications_ibfk_1` FOREIGN KEY (`lecturer_id`) REFERENCES `Lecturers` (`lecturer_id`) ON DELETE CASCADE,
  CONSTRAINT `lecturerpublications_ibfk_2` FOREIGN KEY (`publication_id`) REFERENCES `Publications` (`publication_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `LecturerPublications`
--

LOCK TABLES `LecturerPublications` WRITE;
/*!40000 ALTER TABLE `LecturerPublications` DISABLE KEYS */;
INSERT INTO `LecturerPublications` VALUES (1,1),(7,1),(9,1),(2,2),(3,3),(4,4),(3,5),(8,6),(10,6);
/*!40000 ALTER TABLE `LecturerPublications` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `LecturerQualifications`
--

DROP TABLE IF EXISTS `LecturerQualifications`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `LecturerQualifications` (
  `qualification_id` int NOT NULL AUTO_INCREMENT,
  `lecturer_id` int NOT NULL,
  `qualification_name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`qualification_id`),
  KEY `lecturer_id` (`lecturer_id`),
  CONSTRAINT `lecturerqualifications_ibfk_1` FOREIGN KEY (`lecturer_id`) REFERENCES `Lecturers` (`lecturer_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `LecturerQualifications`
--

LOCK TABLES `LecturerQualifications` WRITE;
/*!40000 ALTER TABLE `LecturerQualifications` DISABLE KEYS */;
INSERT INTO `LecturerQualifications` VALUES (1,1,'Ph.D. in Computer Science'),(2,1,'Certified Information Systems Security Professional (CISSP)'),(3,2,'Ph.D. in Physics'),(4,2,'Nobel Prize in Physics');
/*!40000 ALTER TABLE `LecturerQualifications` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `LecturerResearchAreas`
--

DROP TABLE IF EXISTS `LecturerResearchAreas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `LecturerResearchAreas` (
  `lecturer_id` int NOT NULL,
  `area_id` int NOT NULL,
  PRIMARY KEY (`lecturer_id`,`area_id`),
  KEY `area_id` (`area_id`),
  CONSTRAINT `lecturerresearchareas_ibfk_1` FOREIGN KEY (`lecturer_id`) REFERENCES `Lecturers` (`lecturer_id`) ON DELETE CASCADE,
  CONSTRAINT `lecturerresearchareas_ibfk_2` FOREIGN KEY (`area_id`) REFERENCES `ResearchAreas` (`area_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `LecturerResearchAreas`
--

LOCK TABLES `LecturerResearchAreas` WRITE;
/*!40000 ALTER TABLE `LecturerResearchAreas` DISABLE KEYS */;
INSERT INTO `LecturerResearchAreas` VALUES (1,1),(2,2),(3,3),(2,7),(1,8),(2,11),(1,12);
/*!40000 ALTER TABLE `LecturerResearchAreas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Lecturers`
--

DROP TABLE IF EXISTS `Lecturers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Lecturers` (
  `lecturer_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `department_id` int DEFAULT NULL,
  `phone_number` varchar(20) DEFAULT NULL,
  `work_email` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`lecturer_id`),
  UNIQUE KEY `work_email` (`work_email`),
  KEY `department_id` (`department_id`),
  CONSTRAINT `lecturers_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `Departments` (`department_id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Lecturers`
--

LOCK TABLES `Lecturers` WRITE;
/*!40000 ALTER TABLE `Lecturers` DISABLE KEYS */;
INSERT INTO `Lecturers` VALUES (1,'Alan','Turing',1,'123-456-7890','alan.turing@university.edu'),(2,'Marie','Curie',2,'123-456-7891','marie.curie@university.edu'),(3,'Herodotus','Halicarnassus',3,'123-456-7892','herodotus.h@university.edu'),(4,'Carl','Gauss',4,'123-456-7893','carl.gauss@university.edu'),(5,'Jane','Austen',5,'123-456-7894','jane.austen@university.edu'),(6,'Charles','Darwin',6,'123-456-7895','charles.darwin@university.edu'),(7,'Grace','Hopper',1,'123-456-7896','grace.hopper@university.edu'),(8,'Richard','Feynman',2,'123-456-7897','richard.feynman@university.edu'),(9,'Ada','Lovelace',1,'123-456-7898','ada.lovelace@university.edu'),(10,'Niels','Bohr',2,'123-456-7899','niels.bohr@university.edu'),(11,'Euclid','Alexandria',4,'123-456-7900','euclid.a@university.edu'),(12,'Mary','Shelley',5,'123-456-7901','mary.shelley@university.edu'),(13,'Gregor','Mendel',6,'123-456-7902','gregor.mendel@university.edu'),(14,'John','von Neumann',1,'123-456-7903','john.vonneumann@university.edu'),(15,'Isaac','Newton',2,'123-456-7904','isaac.newton@university.edu'),(16,'Thucydides','Olorus',3,'123-456-7905','thucydides.o@university.edu'),(17,'Emmy','Noether',4,'123-456-7906','emmy.noether@university.edu'),(18,'Virginia','Woolf',5,'123-456-7907','virginia.woolf@university.edu'),(19,'Rosalind','Franklin',6,'123-456-7908','rosalind.franklin@university.edu'),(20,'Tim','Berners-Lee',1,'123-456-7909','tim.berners-lee@university.edu');
/*!40000 ALTER TABLE `Lecturers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `NonAcademicStaff`
--

DROP TABLE IF EXISTS `NonAcademicStaff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `NonAcademicStaff` (
  `staff_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `job_title` varchar(100) DEFAULT NULL,
  `department_id` int DEFAULT NULL,
  `phone_number` varchar(20) DEFAULT NULL,
  `work_email` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`staff_id`),
  UNIQUE KEY `work_email` (`work_email`),
  KEY `department_id` (`department_id`),
  CONSTRAINT `nonacademicstaff_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `Departments` (`department_id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `NonAcademicStaff`
--

LOCK TABLES `NonAcademicStaff` WRITE;
/*!40000 ALTER TABLE `NonAcademicStaff` DISABLE KEYS */;
INSERT INTO `NonAcademicStaff` VALUES (1,'John','Smith','Administrator',1,'234-567-8901','john.smith@university.edu'),(2,'Jane','Doe','Lab Technician',2,'234-567-8902','jane.doe@university.edu'),(3,'Peter','Jones','Librarian',3,'234-567-8903','peter.jones@university.edu'),(4,'Mary','Williams','IT Support',1,'234-567-8904','mary.williams@university.edu'),(5,'David','Brown','Accountant',3,'234-567-8905','david.brown@university.edu'),(6,'Susan','Miller','HR Manager',8,'234-567-8906','susan.miller@university.edu'),(7,'Robert','Davis','Security Officer',5,'234-567-8907','robert.davis@university.edu'),(8,'Linda','Garcia','Admissions Officer',7,'234-567-8908','linda.garcia@university.edu'),(9,'Michael','Rodriguez','Janitor',7,'234-567-8909','michael.r@university.edu'),(10,'Karen','Martinez','Department Secretary',4,'234-567-8910','karen.martinez@university.edu'),(11,'James','Hernandez','Groundskeeper',7,'234-567-8911','james.h@university.edu'),(12,'Patricia','Lopez','Registrar',7,'234-567-8912','patricia.l@university.edu'),(13,'William','Gonzalez','Lab Manager',6,'234-567-8913','william.g@university.edu'),(14,'Jennifer','Wilson','Events Coordinator',7,'234-567-8914','jennifer.w@university.edu'),(15,'Richard','Anderson','Financial Aid Advisor',7,'234-567-8915','richard.a@university.edu');
/*!40000 ALTER TABLE `NonAcademicStaff` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `OrganizationMembers`
--

DROP TABLE IF EXISTS `OrganizationMembers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `OrganizationMembers` (
  `organization_id` int NOT NULL,
  `student_id` int NOT NULL,
  PRIMARY KEY (`organization_id`,`student_id`),
  KEY `student_id` (`student_id`),
  CONSTRAINT `organizationmembers_ibfk_1` FOREIGN KEY (`organization_id`) REFERENCES `StudentOrganizations` (`organization_id`) ON DELETE CASCADE,
  CONSTRAINT `organizationmembers_ibfk_2` FOREIGN KEY (`student_id`) REFERENCES `Students` (`student_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `OrganizationMembers`
--

LOCK TABLES `OrganizationMembers` WRITE;
/*!40000 ALTER TABLE `OrganizationMembers` DISABLE KEYS */;
INSERT INTO `OrganizationMembers` VALUES (1,1),(2,1),(2,2),(1,3),(1,4),(3,4),(3,5),(3,7),(3,8),(2,14),(2,17),(2,21),(2,22),(2,23),(2,24),(3,24),(3,25),(2,27),(3,29),(3,30),(2,31),(3,32),(2,36),(2,38),(3,38),(2,43),(2,44),(2,45),(3,47),(2,48),(2,52),(3,52),(3,56),(2,57),(3,57),(2,58),(2,65),(3,65),(2,68),(3,70),(2,73),(3,74),(3,76),(3,77),(3,78),(2,79),(3,83),(3,84),(3,85),(2,86),(2,87),(2,90),(2,91),(3,91),(3,92),(2,93),(3,93),(2,96),(3,97),(3,98),(2,100),(3,102),(2,107),(3,107),(2,108),(3,109),(2,111),(2,112),(2,113),(3,115),(2,116),(3,117),(3,118),(2,122),(3,124),(3,129),(2,130),(3,132),(2,133),(3,133),(2,134),(3,137),(2,139),(3,139),(3,142),(2,144),(2,145),(3,146),(3,147),(2,148),(3,148),(2,149),(3,149),(3,150),(3,153),(2,156),(3,156),(2,158),(3,158),(2,159),(2,160),(3,163),(2,164),(3,164),(2,166),(2,167),(3,169),(2,172),(3,173),(3,175),(2,176),(3,180),(2,185),(2,186),(3,186),(2,189),(3,190),(2,191),(3,191),(2,193),(2,195),(2,198);
/*!40000 ALTER TABLE `OrganizationMembers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ProgramRequirements`
--

DROP TABLE IF EXISTS `ProgramRequirements`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ProgramRequirements` (
  `program_id` int NOT NULL,
  `course_id` int NOT NULL,
  PRIMARY KEY (`program_id`,`course_id`),
  KEY `course_id` (`course_id`),
  CONSTRAINT `programrequirements_ibfk_1` FOREIGN KEY (`program_id`) REFERENCES `Programs` (`program_id`) ON DELETE CASCADE,
  CONSTRAINT `programrequirements_ibfk_2` FOREIGN KEY (`course_id`) REFERENCES `Courses` (`course_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ProgramRequirements`
--

LOCK TABLES `ProgramRequirements` WRITE;
/*!40000 ALTER TABLE `ProgramRequirements` DISABLE KEYS */;
INSERT INTO `ProgramRequirements` VALUES (1,1),(1,2),(1,3),(3,6);
/*!40000 ALTER TABLE `ProgramRequirements` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Programs`
--

DROP TABLE IF EXISTS `Programs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Programs` (
  `program_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `degree_awarded` varchar(100) DEFAULT NULL,
  `duration_years` int DEFAULT NULL,
  PRIMARY KEY (`program_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Programs`
--

LOCK TABLES `Programs` WRITE;
/*!40000 ALTER TABLE `Programs` DISABLE KEYS */;
INSERT INTO `Programs` VALUES (1,'B.Sc. in Computer Science','Bachelor of Science',4),(2,'M.Sc. in Data Science','Master of Science',2),(3,'B.A. in History','Bachelor of Arts',4),(4,'Ph.D. in Physics','Doctor of Philosophy',5),(5,'B.Sc. in Mathematics','Bachelor of Science',4),(6,'M.A. in English Literature','Master of Arts',2);
/*!40000 ALTER TABLE `Programs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ProjectMembers`
--

DROP TABLE IF EXISTS `ProjectMembers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ProjectMembers` (
  `member_id` int NOT NULL AUTO_INCREMENT,
  `project_id` int NOT NULL,
  `student_id` int NOT NULL,
  PRIMARY KEY (`member_id`),
  KEY `project_id` (`project_id`),
  KEY `student_id` (`student_id`),
  CONSTRAINT `projectmembers_ibfk_1` FOREIGN KEY (`project_id`) REFERENCES `ResearchProjects` (`project_id`) ON DELETE CASCADE,
  CONSTRAINT `projectmembers_ibfk_2` FOREIGN KEY (`student_id`) REFERENCES `Students` (`student_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ProjectMembers`
--

LOCK TABLES `ProjectMembers` WRITE;
/*!40000 ALTER TABLE `ProjectMembers` DISABLE KEYS */;
INSERT INTO `ProjectMembers` VALUES (1,1,1),(2,1,4),(3,2,2),(4,2,5),(5,3,2),(6,3,3),(7,4,1),(8,4,4),(9,1,5),(10,1,6),(11,1,9),(12,1,11),(13,1,12),(14,1,15),(15,1,17),(16,1,18),(24,2,21),(25,2,22),(26,2,23),(27,2,25),(28,2,27),(29,2,30),(30,2,31),(31,2,34),(32,2,36),(33,2,38),(34,2,39),(39,3,44),(40,3,45),(41,3,46),(42,3,47),(43,3,50),(44,3,52),(45,3,54),(46,3,55),(47,3,59),(48,3,60),(54,4,63),(55,4,65),(56,4,66),(57,4,69),(58,4,70),(59,4,71),(60,4,73),(61,4,74),(62,4,75),(63,4,77),(64,4,78),(65,4,80);
/*!40000 ALTER TABLE `ProjectMembers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ProjectPublications`
--

DROP TABLE IF EXISTS `ProjectPublications`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ProjectPublications` (
  `project_id` int NOT NULL,
  `publication_id` int NOT NULL,
  PRIMARY KEY (`project_id`,`publication_id`),
  KEY `publication_id` (`publication_id`),
  CONSTRAINT `projectpublications_ibfk_1` FOREIGN KEY (`project_id`) REFERENCES `ResearchProjects` (`project_id`) ON DELETE CASCADE,
  CONSTRAINT `projectpublications_ibfk_2` FOREIGN KEY (`publication_id`) REFERENCES `Publications` (`publication_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ProjectPublications`
--

LOCK TABLES `ProjectPublications` WRITE;
/*!40000 ALTER TABLE `ProjectPublications` DISABLE KEYS */;
INSERT INTO `ProjectPublications` VALUES (1,1),(3,5);
/*!40000 ALTER TABLE `ProjectPublications` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Publications`
--

DROP TABLE IF EXISTS `Publications`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Publications` (
  `publication_id` int NOT NULL AUTO_INCREMENT,
  `title` text NOT NULL,
  `year` int DEFAULT NULL,
  `publication_venue` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`publication_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Publications`
--

LOCK TABLES `Publications` WRITE;
/*!40000 ALTER TABLE `Publications` DISABLE KEYS */;
INSERT INTO `Publications` VALUES (1,'A Novel Approach to Neural Networks',2023,'Journal of AI Research'),(2,'Quantum Entanglement in Solid State Systems',2022,'Physical Review Letters'),(3,'Revisiting the Fall of Rome',2024,'Journal of Ancient History'),(4,'Advanced Matrix Decomposition Techniques',2021,'SIAM Journal on Matrix Analysis'),(5,'Digital Humanities and Ancient Texts',2024,'Journal of Digital History'),(6,'Advanced Topics in Quantum Field Theory',2025,'Annals of Physics');
/*!40000 ALTER TABLE `Publications` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ResearchAreas`
--

DROP TABLE IF EXISTS `ResearchAreas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ResearchAreas` (
  `area_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`area_id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ResearchAreas`
--

LOCK TABLES `ResearchAreas` WRITE;
/*!40000 ALTER TABLE `ResearchAreas` DISABLE KEYS */;
INSERT INTO `ResearchAreas` VALUES (1,'Artificial Intelligence'),(7,'Astrophysics'),(9,'Bioinformatics'),(12,'Cybersecurity'),(8,'Data Science'),(6,'Genetics'),(3,'Medieval History'),(4,'Number Theory'),(11,'Particle Physics'),(5,'Postmodern Literature'),(2,'Quantum Computing'),(10,'Renaissance Art'),(13,'Talent Acquisition Methods');
/*!40000 ALTER TABLE `ResearchAreas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ResearchProjects`
--

DROP TABLE IF EXISTS `ResearchProjects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ResearchProjects` (
  `project_id` int NOT NULL AUTO_INCREMENT,
  `title` text NOT NULL,
  `funding_source` varchar(255) DEFAULT NULL,
  `outcome_summary` text,
  `principal_investigator_id` int DEFAULT NULL,
  PRIMARY KEY (`project_id`),
  KEY `principal_investigator_id` (`principal_investigator_id`),
  CONSTRAINT `researchprojects_ibfk_1` FOREIGN KEY (`principal_investigator_id`) REFERENCES `Lecturers` (`lecturer_id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ResearchProjects`
--

LOCK TABLES `ResearchProjects` WRITE;
/*!40000 ALTER TABLE `ResearchProjects` DISABLE KEYS */;
INSERT INTO `ResearchProjects` VALUES (1,'Project DeepMind','Govt Grant','Developed a new learning algorithm.',1),(2,'Stellar Cartography Initiative','NASA','Mapped a new sector of the galaxy.',2),(3,'Historical Text Analysis using NLP','University Grant','Completed analysis of 500 ancient texts, identifying authorship patterns.',3),(4,'Graphene-based Superconductors','National Science Foundation','Ongoing research into high-temperature superconductivity.',2);
/*!40000 ALTER TABLE `ResearchProjects` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `StaffContracts`
--

DROP TABLE IF EXISTS `StaffContracts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `StaffContracts` (
  `contract_id` int NOT NULL AUTO_INCREMENT,
  `staff_id` int NOT NULL,
  `employment_type` varchar(100) DEFAULT NULL,
  `contract_details` text,
  `salary` decimal(10,2) DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  PRIMARY KEY (`contract_id`),
  KEY `staff_id` (`staff_id`),
  CONSTRAINT `staffcontracts_ibfk_1` FOREIGN KEY (`staff_id`) REFERENCES `NonAcademicStaff` (`staff_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `StaffContracts`
--

LOCK TABLES `StaffContracts` WRITE;
/*!40000 ALTER TABLE `StaffContracts` DISABLE KEYS */;
INSERT INTO `StaffContracts` VALUES (1,1,'Full-time','Standard 5-year contract',60000.00,'2022-08-01','2027-07-31'),(2,2,'Full-time','Permanent position',55000.00,'2021-09-15',NULL),(3,3,'Part-time','20 hours/week contract',30000.00,'2023-01-10','2025-12-31');
/*!40000 ALTER TABLE `StaffContracts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `StudentOrganizations`
--

DROP TABLE IF EXISTS `StudentOrganizations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `StudentOrganizations` (
  `organization_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` text,
  PRIMARY KEY (`organization_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `StudentOrganizations`
--

LOCK TABLES `StudentOrganizations` WRITE;
/*!40000 ALTER TABLE `StudentOrganizations` DISABLE KEYS */;
INSERT INTO `StudentOrganizations` VALUES (1,'Coding Club','A club for students interested in software development.'),(2,'History Society','Discussing historical events and figures.'),(3,'Physics and Astronomy Club','Exploring the wonders of the universe.');
/*!40000 ALTER TABLE `StudentOrganizations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Students`
--

DROP TABLE IF EXISTS `Students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Students` (
  `student_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `dob` date DEFAULT NULL,
  `phone_number` varchar(20) DEFAULT NULL,
  `student_email` varchar(255) NOT NULL,
  `program_id` int DEFAULT NULL,
  `year_of_study` int DEFAULT NULL,
  `graduation_status` varchar(50) DEFAULT 'Enrolled',
  PRIMARY KEY (`student_id`),
  UNIQUE KEY `student_email` (`student_email`),
  KEY `program_id` (`program_id`),
  CONSTRAINT `students_ibfk_1` FOREIGN KEY (`program_id`) REFERENCES `Programs` (`program_id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=202 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Students`
--

LOCK TABLES `Students` WRITE;
/*!40000 ALTER TABLE `Students` DISABLE KEYS */;
INSERT INTO `Students` VALUES (1,'Alice','Wonderland','2004-05-10','345-678-9012','alice.w@student.university.edu',1,3,'Enrolled'),(2,'Bob','Builder','2003-02-20','345-678-9013','bob.b@student.university.edu',3,4,'Enrolled'),(3,'Charlie','Chocolate','2002-11-30','345-678-3014','charlie.c@student.university.edu',1,4,'Graduated'),(4,'Diana','Prince','2005-08-15','345-678-9015','diana.p@student.university.edu',2,2,'Enrolled'),(5,'Eve','Online','2001-01-01','345-678-9016','eve.o@student.university.edu',4,5,'Graduated'),(6,'Oliver','Garcia','2004-03-22','555-0115-1234','oliver.garcia6@student.university.edu',5,3,'Enrolled'),(7,'John','Cena','1994-01-01','345-678-000','john.c@student.university.edu',4,5,'Enrolled'),(8,'Elijah','Davis','2003-12-18','555-0117-9012','elijah.davis8@student.university.edu',1,4,'Enrolled'),(9,'Sophia','Rodriguez','2002-06-25','555-0118-3456','sophia.rodriguez9@student.university.edu',3,4,'Graduated'),(10,'Mateo','Martinez','2004-10-10','555-0119-7890','mateo.martinez10@student.university.edu',2,2,'Enrolled'),(11,'Isabella','Hernandez','2004-01-12','555-0120-1111','isabella.hernandez11@student.university.edu',1,3,'Enrolled'),(12,'Lucas','Lopez','2004-02-13','555-0121-2222','lucas.lopez12@student.university.edu',5,3,'Enrolled'),(13,'Mia','Gonzalez','2005-04-18','555-0122-3333','mia.gonzalez13@student.university.edu',6,2,'Enrolled'),(14,'Levi','Wilson','2003-07-21','555-0123-4444','levi.wilson14@student.university.edu',3,4,'Enrolled'),(15,'Charlotte','Anderson','2002-09-14','555-0124-5555','charlotte.anderson15@student.university.edu',1,4,'Graduated'),(16,'Asher','Thomas','2005-11-03','555-0125-6666','asher.thomas16@student.university.edu',2,2,'Enrolled'),(17,'Luna','Taylor','2004-05-29','555-0126-7777','luna.taylor17@student.university.edu',4,3,'Enrolled'),(18,'James','Moore','2003-03-08','555-0127-8888','james.moore18@student.university.edu',5,4,'Enrolled'),(19,'Aurora','Jackson','2002-08-01','555-0128-9999','aurora.jackson19@student.university.edu',6,4,'Graduated'),(20,'Leo','Martin','2005-01-20','555-0129-1010','leo.martin20@student.university.edu',1,2,'Enrolled'),(21,'Zoe','Lee','2004-06-11','555-0130-1121','zoe.lee21@student.university.edu',3,3,'Enrolled'),(22,'Mila','Perez','2003-10-24','555-0131-2232','mila.perez22@student.university.edu',5,4,'Enrolled'),(23,'Jack','Thompson','2002-04-02','555-0132-3343','jack.thompson23@student.university.edu',1,4,'Graduated'),(24,'Eleanor','White','2005-07-19','555-0133-4454','eleanor.white24@student.university.edu',2,2,'Enrolled'),(25,'Hazel','Harris','2004-09-09','555-0134-5565','hazel.harris25@student.university.edu',4,3,'Enrolled'),(26,'Wyatt','Sanchez','2003-01-30','555-0135-6676','wyatt.sanchez26@student.university.edu',6,4,'Enrolled'),(27,'Aria','Clark','2002-05-16','555-0136-7787','aria.clark27@student.university.edu',3,4,'Graduated'),(28,'Luke','Ramirez','2005-02-07','555-0137-8898','luke.ramirez28@student.university.edu',5,2,'Enrolled'),(29,'Stella','Lewis','2004-11-23','555-0138-9909','stella.lewis29@student.university.edu',1,3,'Enrolled'),(30,'Owen','Robinson','2003-08-12','555-0139-1020','owen.robinson30@student.university.edu',2,4,'Enrolled'),(31,'Chloe','Walker','2002-12-04','555-0140-1131','chloe.walker31@student.university.edu',4,4,'Graduated'),(32,'Caleb','Young','2005-03-28','555-0141-2242','caleb.young32@student.university.edu',6,2,'Enrolled'),(33,'Lily','Allen','2004-08-19','555-0142-3353','lily.allen33@student.university.edu',3,3,'Enrolled'),(34,'Grayson','King','2003-05-01','555-0143-4464','grayson.king34@student.university.edu',5,4,'Enrolled'),(35,'Nora','Wright','2002-02-17','555-0144-5575','nora.wright35@student.university.edu',1,4,'Graduated'),(36,'Levi','Scott','2005-10-08','555-0145-6686','levi.scott36@student.university.edu',2,2,'Enrolled'),(37,'Penelope','Green','2004-04-14','555-0146-7797','penelope.green37@student.university.edu',4,3,'Enrolled'),(38,'Julian','Baker','2003-09-27','555-0147-8808','julian.baker38@student.university.edu',6,4,'Enrolled'),(39,'Addison','Adams','2002-07-06','555-0148-9919','addison.adams39@student.university.edu',3,4,'Graduated'),(40,'Lincoln','Nelson','2005-06-13','555-0149-1030','lincoln.nelson40@student.university.edu',5,2,'Enrolled'),(41,'Layla','Carter','2004-01-05','555-0150-1141','layla.carter41@student.university.edu',1,3,'Enrolled'),(42,'Ryan','Mitchell','2003-06-22','555-0151-2252','ryan.mitchell42@student.university.edu',2,4,'Enrolled'),(43,'Riley','Perez','2002-03-15','555-0152-3363','riley.perez43@student.university.edu',4,4,'Graduated'),(44,'Isaac','Roberts','2005-12-11','555-0153-4474','isaac.roberts44@student.university.edu',6,2,'Enrolled'),(45,'Ellie','Turner','2004-02-28','555-0154-5585','ellie.turner45@student.university.edu',3,3,'Enrolled'),(46,'Jayden','Phillips','2003-11-18','555-0155-6696','jayden.phillips46@student.university.edu',5,4,'Enrolled'),(47,'Aubrey','Campbell','2002-01-09','555-0156-7707','aubrey.campbell47@student.university.edu',1,4,'Graduated'),(48,'Carter','Parker','2005-08-25','555-0157-8818','carter.parker48@student.university.edu',2,2,'Enrolled'),(49,'Hannah','Evans','2004-12-26','555-0158-9929','hannah.evans49@student.university.edu',4,3,'Enrolled'),(50,'Isaiah','Edwards','2003-04-07','555-0159-1040','isaiah.edwards50@student.university.edu',6,4,'Enrolled'),(51,'Aaliyah','Collins','2002-10-17','555-0160-1151','aaliyah.collins51@student.university.edu',3,4,'Graduated'),(52,'Joshua','Stewart','2005-05-04','555-0161-2262','joshua.stewart52@student.university.edu',5,2,'Enrolled'),(53,'Brooklyn','Morris','2004-03-03','555-0162-3373','brooklyn.morris53@student.university.edu',1,3,'Enrolled'),(54,'Sebastian','Rogers','2003-07-14','555-0163-4484','sebastian.rogers54@student.university.edu',2,4,'Enrolled'),(55,'Zoe','Reed','2002-09-23','555-0164-5595','zoe.reed55@student.university.edu',4,4,'Graduated'),(56,'David','Cook','2005-06-02','555-0165-6606','david.cook56@student.university.edu',6,2,'Enrolled'),(57,'Leah','Morgan','2004-11-07','555-0166-7717','leah.morgan57@student.university.edu',3,3,'Enrolled'),(58,'Gabriel','Bell','2003-02-11','555-0167-8828','gabriel.bell58@student.university.edu',5,4,'Enrolled'),(59,'Lillian','Murphy','2002-08-29','555-0168-9939','lillian.murphy59@student.university.edu',1,4,'Graduated'),(60,'Anthony','Bailey','2005-01-15','555-0169-1050','anthony.bailey60@student.university.edu',2,2,'Enrolled'),(61,'Natalie','Rivera','2004-07-28','555-0170-1161','natalie.rivera61@student.university.edu',4,3,'Enrolled'),(62,'Samuel','Cooper','2003-12-09','555-0171-2272','samuel.cooper62@student.university.edu',6,4,'Enrolled'),(63,'Grace','Richardson','2002-06-05','555-0172-3383','grace.richardson63@student.university.edu',3,4,'Graduated'),(64,'Christopher','Cox','2005-09-19','555-0173-4494','christopher.cox64@student.university.edu',5,2,'Enrolled'),(65,'Audrey','Howard','2004-05-22','555-0174-5505','audrey.howard65@student.university.edu',1,3,'Enrolled'),(66,'John','Ward','2003-03-18','555-0175-6616','john.ward66@student.university.edu',2,4,'Enrolled'),(67,'Victoria','Torres','2002-02-21','555-0176-7727','victoria.torres67@student.university.edu',4,4,'Graduated'),(68,'Dylan','Peterson','2005-11-27','555-0177-8838','dylan.peterson68@student.university.edu',6,2,'Enrolled'),(69,'Claire','Gray','2004-10-31','555-0178-9949','claire.gray69@student.university.edu',3,3,'Enrolled'),(70,'Andrew','Ramirez','2003-08-04','555-0179-1060','andrew.ramirez70@student.university.edu',5,4,'Enrolled'),(71,'Bella','James','2002-04-26','555-0180-1171','bella.james71@student.university.edu',1,4,'Graduated'),(72,'Matthew','Watson','2005-07-13','555-0181-2282','matthew.watson72@student.university.edu',2,2,'Enrolled'),(73,'Savannah','Brooks','2004-09-03','555-0182-3393','savannah.brooks73@student.university.edu',4,3,'Enrolled'),(74,'Joseph','Kelly','2003-01-23','555-0183-4404','joseph.kelly74@student.university.edu',6,4,'Enrolled'),(75,'Skylar','Sanders','2002-05-10','555-0184-5515','skylar.sanders75@student.university.edu',3,4,'Graduated'),(76,'Christian','Price','2005-02-14','555-0185-6626','christian.price76@student.university.edu',5,2,'Enrolled'),(77,'Alexa','Bennett','2004-11-16','555-0186-7737','alexa.bennett77@student.university.edu',1,3,'Enrolled'),(78,'Jaxon','Wood','2003-08-22','555-0187-8848','jaxon.wood78@student.university.edu',2,4,'Enrolled'),(79,'Paisley','Barnes','2002-12-19','555-0188-9959','paisley.barnes79@student.university.edu',4,4,'Graduated'),(80,'Daniel','Ross','2005-03-21','555-0189-1070','daniel.ross80@student.university.edu',6,2,'Enrolled'),(81,'Scarlett','Henderson','2004-08-11','555-0190-1181','scarlett.henderson81@student.university.edu',3,3,'Enrolled'),(82,'William','Coleman','2003-05-25','555-0191-2292','william.coleman82@student.university.edu',5,4,'Enrolled'),(83,'Madison','Jenkins','2002-02-08','555-0192-3303','madison.jenkins83@student.university.edu',1,4,'Graduated'),(84,'Michael','Perry','2005-10-15','555-0193-4414','michael.perry84@student.university.edu',2,2,'Enrolled'),(85,'Camila','Powell','2004-04-22','555-0194-5525','camila.powell85@student.university.edu',4,3,'Enrolled'),(86,'Henry','Long','2003-09-17','555-0195-6636','henry.long86@student.university.edu',6,4,'Enrolled'),(87,'Ariana','Patterson','2002-07-24','555-0196-7747','ariana.patterson87@student.university.edu',3,4,'Graduated'),(88,'Alexander','Hughes','2005-06-30','555-0197-8858','alexander.hughes88@student.university.edu',5,2,'Enrolled'),(89,'Penelope','Flores','2004-01-18','555-0198-9969','penelope.flores89@student.university.edu',1,3,'Enrolled'),(90,'Benjamin','Washington','2003-06-09','555-0199-1080','benjamin.washington90@student.university.edu',2,4,'Enrolled'),(91,'Naomi','Butler','2002-03-04','555-0100-1191','naomi.butler91@student.university.edu',4,4,'Graduated'),(92,'Ethan','Simmons','2005-12-23','555-0101-2202','ethan.simmons92@student.university.edu',6,2,'Enrolled'),(93,'Riley','Foster','2004-02-19','555-0102-3313','riley.foster93@student.university.edu',3,3,'Enrolled'),(94,'Evelyn','Gonzales','2003-11-08','555-0103-4424','evelyn.gonzales94@student.university.edu',5,4,'Enrolled'),(95,'Logan','Bryant','2002-01-28','555-0104-5535','logan.bryant95@student.university.edu',1,4,'Graduated'),(96,'Abigail','Alexander','2005-08-14','555-0105-6646','abigail.alexander96@student.university.edu',2,2,'Enrolled'),(97,'Mason','Russell','2004-12-07','555-0106-7757','mason.russell97@student.university.edu',4,3,'Enrolled'),(98,'Harper','Griffin','2003-04-16','555-0107-8868','harper.griffin98@student.university.edu',6,4,'Enrolled'),(99,'Emily','Diaz','2002-10-29','555-0108-9979','emily.diaz99@student.university.edu',3,4,'Graduated'),(100,'Jacob','Hayes','2005-05-21','555-0109-1090','jacob.hayes100@student.university.edu',5,2,'Enrolled'),(101,'Avery','Myers','2004-03-11','555-0110-2101','avery.myers101@student.university.edu',1,3,'Enrolled'),(102,'Sofia','Ford','2003-07-02','555-0111-3212','sofia.ford102@student.university.edu',2,4,'Enrolled'),(103,'Jackson','Hamilton','2002-09-11','555-0112-4323','jackson.hamilton103@student.university.edu',4,4,'Graduated'),(104,'Ella','Graham','2005-06-19','555-0113-5434','ella.graham104@student.university.edu',6,2,'Enrolled'),(105,'Aiden','Sullivan','2004-11-12','555-0114-6545','aiden.sullivan105@student.university.edu',3,3,'Enrolled'),(106,'Scarlett','Wallace','2003-02-04','555-0115-7656','scarlett.wallace106@student.university.edu',5,4,'Enrolled'),(107,'Lucas','Woods','2002-08-08','555-0116-8767','lucas.woods107@student.university.edu',1,4,'Graduated'),(108,'Madison','Cole','2005-01-07','555-0117-9878','madison.cole108@student.university.edu',2,2,'Enrolled'),(109,'Liam','West','2004-07-22','555-0118-1989','liam.west109@student.university.edu',4,3,'Enrolled'),(110,'Chloe','Jordan','2003-12-14','555-0119-2090','chloe.jordan110@student.university.edu',6,4,'Enrolled'),(111,'Logan','Owens','2002-06-28','555-0120-3101','logan.owens111@student.university.edu',3,4,'Graduated'),(112,'Grace','Reynolds','2005-09-01','555-0121-4212','grace.reynolds112@student.university.edu',5,2,'Enrolled'),(113,'Caleb','Fisher','2004-05-15','555-0122-5323','caleb.fisher113@student.university.edu',1,3,'Enrolled'),(114,'Nora','Ellis','2003-03-25','555-0123-6434','nora.ellis114@student.university.edu',2,4,'Enrolled'),(115,'Ryan','Harrison','2002-02-01','555-0124-7545','ryan.harrison115@student.university.edu',4,4,'Graduated'),(116,'Zoey','Gibson','2005-11-11','555-0125-8656','zoey.gibson116@student.university.edu',6,2,'Enrolled'),(117,'Nathan','Mcdonald','2004-10-04','555-0126-9767','nathan.mcdonald117@student.university.edu',3,3,'Enrolled'),(118,'Lillian','Cruz','2003-08-30','555-0127-1878','lillian.cruz118@student.university.edu',5,4,'Enrolled'),(119,'Christian','Marshall','2002-04-19','555-0128-2989','christian.marshall119@student.university.edu',1,4,'Graduated'),(120,'Aubrey','Ortiz','2005-07-09','555-0129-3090','aubrey.ortiz120@student.university.edu',2,2,'Enrolled'),(121,'Isaac','Gomez','2004-09-26','555-0130-4101','isaac.gomez121@student.university.edu',4,3,'Enrolled'),(122,'Hannah','Murray','2003-01-03','555-0131-5212','hannah.murray122@student.university.edu',6,4,'Enrolled'),(123,'Owen','Freeman','2002-05-28','555-0132-6323','owen.freeman123@student.university.edu',3,4,'Graduated'),(124,'Addison','Wells','2005-02-24','555-0133-7434','addison.wells124@student.university.edu',5,2,'Enrolled'),(125,'Levi','Webb','2004-11-01','555-0134-8545','levi.webb125@student.university.edu',1,3,'Enrolled'),(126,'Stella','Simpson','2003-08-02','555-0135-9656','stella.simpson126@student.university.edu',2,4,'Enrolled'),(127,'Eli','Stevens','2002-12-28','555-0136-1767','eli.stevens127@student.university.edu',4,4,'Graduated'),(128,'Maya','Tucker','2005-03-14','555-0137-2878','maya.tucker128@student.university.edu',6,2,'Enrolled'),(129,'Aaron','Porter','2004-08-27','555-0138-3989','aaron.porter129@student.university.edu',3,3,'Enrolled'),(130,'Leah','Hunter','2003-05-13','555-0139-4090','leah.hunter130@student.university.edu',5,4,'Enrolled'),(131,'Wyatt','Hicks','2002-02-26','555-0140-5101','wyatt.hicks131@student.university.edu',1,4,'Graduated'),(132,'Audrey','Crawford','2005-10-22','555-0141-6212','audrey.crawford132@student.university.edu',2,2,'Enrolled'),(133,'Julian','Henry','2004-04-09','555-0142-7323','julian.henry133@student.university.edu',4,3,'Enrolled'),(134,'Bella','Boyd','2003-09-06','555-0143-8434','bella.boyd134@student.university.edu',6,4,'Enrolled'),(135,'Lincoln','Mason','2002-07-16','555-0144-9545','lincoln.mason135@student.university.edu',3,4,'Graduated'),(136,'Savannah','Morales','2005-06-23','555-0145-1656','savannah.morales136@student.university.edu',5,2,'Enrolled'),(137,'Jaxon','Kennedy','2004-01-02','555-0146-2767','jaxon.kennedy137@student.university.edu',1,3,'Enrolled'),(138,'Claire','Warren','2003-06-18','555-0147-3878','claire.warren138@student.university.edu',2,4,'Enrolled'),(139,'Skylar','Dixon','2002-03-24','555-0148-4989','skylar.dixon139@student.university.edu',4,4,'Graduated'),(140,'Paisley','Ramos','2005-12-01','555-0149-5090','paisley.ramos140@student.university.edu',6,2,'Enrolled'),(141,'Genesis','Reyes','2004-02-09','555-0150-6101','genesis.reyes141@student.university.edu',3,3,'Enrolled'),(142,'Josiah','Burns','2003-11-29','555-0151-7212','josiah.burns142@student.university.edu',5,4,'Enrolled'),(143,'Naomi','Gordon','2002-01-19','555-0152-8323','naomi.gordon143@student.university.edu',1,4,'Graduated'),(144,'Asher','Shaw','2005-08-05','555-0153-9434','asher.shaw144@student.university.edu',2,2,'Enrolled'),(145,'Ariana','Holmes','2004-12-16','555-0154-1545','ariana.holmes145@student.university.edu',4,3,'Enrolled'),(146,'Adam','Rice','2003-04-25','555-0155-2656','adam.rice146@student.university.edu',6,4,'Enrolled'),(147,'Gabriella','Robertson','2002-10-02','555-0156-3767','gabriella.robertson147@student.university.edu',3,4,'Graduated'),(148,'Leo','Hunt','2005-05-12','555-0157-4878','leo.hunt148@student.university.edu',5,2,'Enrolled'),(149,'Violet','Black','2004-03-29','555-0158-5989','violet.black149@student.university.edu',1,3,'Enrolled'),(150,'Jeremiah','Daniels','2003-07-23','555-0159-6090','jeremiah.daniels150@student.university.edu',2,4,'Enrolled'),(151,'Aurora','Palmer','2002-09-02','555-0160-7101','aurora.palmer151@student.university.edu',4,4,'Graduated'),(152,'Ezra','Mills','2005-06-08','555-0161-8212','ezra.mills152@student.university.edu',6,2,'Enrolled'),(153,'Hazel','Nichols','2004-11-20','555-0162-9323','hazel.nichols153@student.university.edu',3,3,'Enrolled'),(154,'Angel','Grant','2003-02-16','555-0163-1434','angel.grant154@student.university.edu',5,4,'Enrolled'),(155,'Everly','Knight','2002-08-18','555-0164-2545','everly.knight155@student.university.edu',1,4,'Graduated'),(156,'Maverick','Ferguson','2005-01-26','555-0165-3656','maverick.ferguson156@student.university.edu',2,2,'Enrolled'),(157,'Willow','Rose','2004-07-18','555-0166-4767','willow.rose157@student.university.edu',4,3,'Enrolled'),(158,'Elias','Stone','2003-12-25','555-0167-5878','elias.stone158@student.university.edu',6,4,'Enrolled'),(159,'Nova','Hawkins','2002-06-14','555-0168-6989','nova.hawkins159@student.university.edu',3,4,'Graduated'),(160,'Colton','Dunn','2005-09-28','555-0169-7090','colton.dunn160@student.university.edu',5,2,'Enrolled'),(161,'Emilia','Perkins','2004-05-08','555-0170-8101','emilia.perkins161@student.university.edu',1,3,'Enrolled'),(162,'Jameson','Hudson','2003-03-07','555-0171-9212','jameson.hudson162@student.university.edu',2,4,'Enrolled'),(163,'Isla','Spencer','2002-02-12','555-0172-1323','isla.spencer163@student.university.edu',4,4,'Graduated'),(164,'Ezekiel','Gardner','2005-11-04','555-0173-2434','ezekiel.gardner164@student.university.edu',6,2,'Enrolled'),(165,'Eliana','Stephens','2004-10-13','555-0174-3545','eliana.stephens165@student.university.edu',3,3,'Enrolled'),(166,'Jace','Payne','2003-08-09','555-0175-4656','jace.payne166@student.university.edu',5,4,'Enrolled'),(167,'Everleigh','Pierce','2002-04-08','555-0176-5767','everleigh.pierce167@student.university.edu',1,4,'Graduated'),(168,'Carson','Berry','2005-07-29','555-0177-6878','carson.berry168@student.university.edu',2,2,'Enrolled'),(169,'Adeline','Matthews','2004-09-15','555-0178-7989','adeline.matthews169@student.university.edu',4,3,'Enrolled'),(170,'Kai','Arnold','2003-01-14','555-0179-8090','kai.arnold170@student.university.edu',6,4,'Enrolled'),(171,'Gianna','Wagner','2002-05-02','555-0180-9101','gianna.wagner171@student.university.edu',3,4,'Graduated'),(172,'Cooper','Willis','2005-02-03','555-0181-1212','cooper.willis172@student.university.edu',5,2,'Enrolled'),(173,'Valentina','Ray','2004-11-25','555-0182-2323','valentina.ray173@student.university.edu',1,3,'Enrolled'),(174,'Xavier','Watkins','2003-08-17','555-0183-3434','xavier.watkins174@student.university.edu',2,4,'Enrolled'),(175,'Ruby','Olson','2002-12-08','555-0184-4545','ruby.olson175@student.university.edu',4,4,'Graduated'),(176,'Leonardo','Carroll','2005-03-02','555-0185-5656','leonardo.carroll176@student.university.edu',6,2,'Enrolled'),(177,'Serenity','Duncan','2004-08-20','555-0186-6767','serenity.duncan177@student.university.edu',3,3,'Enrolled'),(178,'Dominic','Snyder','2003-05-30','555-0187-7878','dominic.snyder178@student.university.edu',5,4,'Enrolled'),(179,'Kennedy','Hart','2002-02-18','555-0188-8989','kennedy.hart179@student.university.edu',1,4,'Graduated'),(180,'Josiah','Cunningham','2005-10-01','555-0189-9090','josiah.cunningham180@student.university.edu',2,2,'Enrolled'),(181,'Clara','Bradley','2004-04-13','555-0190-1101','clara.bradley181@student.university.edu',4,3,'Enrolled'),(182,'Ryder','Lane','2003-09-24','555-0191-2212','ryder.lane182@student.university.edu',6,4,'Enrolled'),(183,'Autumn','Andrews','2002-07-01','555-0192-3323','autumn.andrews183@student.university.edu',3,4,'Graduated'),(184,'Beau','Riley','2005-06-04','555-0193-4434','beau.riley184@student.university.edu',5,2,'Enrolled'),(185,'Arianna','Fox','2004-01-24','555-0194-5545','arianna.fox185@student.university.edu',1,3,'Enrolled'),(186,'Damian','Armstrong','2003-06-12','555-0195-6656','damian.armstrong186@student.university.edu',2,4,'Enrolled'),(187,'Eva','Carpenter','2002-03-31','555-0196-7767','eva.carpenter187@student.university.edu',4,4,'Graduated'),(188,'Miles','Weaver','2005-12-18','555-0197-8878','miles.weaver188@student.university.edu',6,2,'Enrolled'),(189,'Alice','Greene','2004-02-06','555-0198-9989','alice.greene189@student.university.edu',3,3,'Enrolled'),(190,'Silas','Lawrence','2003-11-14','555-0199-1090','silas.lawrence190@student.university.edu',5,4,'Enrolled'),(191,'Madelyn','Elliott','2002-01-04','555-0100-2101','madelyn.elliott191@student.university.edu',1,4,'Graduated'),(192,'Jason','Chavez','2005-08-23','555-0101-3212','jason.chavez192@student.university.edu',2,2,'Enrolled'),(193,'Cora','Sims','2004-12-03','555-0102-4323','cora.sims193@student.university.edu',4,3,'Enrolled'),(194,'Ian','Austin','2003-04-04','555-0103-5434','ian.austin194@student.university.edu',6,4,'Enrolled'),(195,'Kaylee','Peters','2002-10-09','555-0104-6545','kaylee.peters195@student.university.edu',3,4,'Graduated'),(196,'Axel','Kelley','2005-05-29','555-0105-7656','axel.kelley196@student.university.edu',5,2,'Enrolled'),(197,'Sadie','Franklin','2004-03-01','555-0106-8767','sadie.franklin197@student.university.edu',1,3,'Enrolled'),(198,'Camden','Lawson','2003-07-31','555-0107-9878','camden.lawson198@student.university.edu',2,4,'Enrolled'),(199,'Piper','Fields','2002-09-30','555-0108-1989','piper.fields199@student.university.edu',4,4,'Graduated'),(200,'Robert','Gutierrez','2005-06-16','555-0109-2090','robert.gutierrez200@student.university.edu',6,2,'Enrolled'),(201,'Johnny','Junior','2000-11-30','1111-222-3333','johnny.junio@student.university.edu',2,2,'Withdrawn');
/*!40000 ALTER TABLE `Students` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-07-23 18:49:25
