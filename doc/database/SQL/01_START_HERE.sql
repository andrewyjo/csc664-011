/**
Here is the DDL to create and use: the db, the File Table, Event, Event Hierarchy
and other db initialzation code



**/




CREATE DATABASE `smartmediainterface` 
USE `smartmediainterface` 

-- File is for storing all raw multimedia files
-- smartmediainterface.File definition

CREATE TABLE `File` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `filename` varchar(100) DEFAULT NULL,
  `extension` varchar(100) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  `filesize` decimal(10,0) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  `latitude` decimal(10,0) DEFAULT NULL,
  `longitude` decimal(10,0) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=219 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- Move onto 02_IMPORT_FILE_DATA.sql