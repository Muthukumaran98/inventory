-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Oct 11, 2020 at 05:29 AM
-- Server version: 10.4.10-MariaDB
-- PHP Version: 7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `inventory`
--

-- --------------------------------------------------------

--
-- Table structure for table `location`
--

DROP TABLE IF EXISTS `location`;
CREATE TABLE IF NOT EXISTS `location` (
  `loc_id` int(255) NOT NULL,
  `loc_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `location`
--

INSERT INTO `location` (`loc_id`, `loc_name`) VALUES
(1011, 'India'),
(1012, 'China'),
(1013, 'United State'),
(1014, 'Singapore');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

DROP TABLE IF EXISTS `login`;
CREATE TABLE IF NOT EXISTS `login` (
  `id` int(255) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`id`, `username`, `email`, `password`) VALUES
(4, 'muthukumaran', 'muthukumaran2026@gmail.com', 'Muthu'),
(5, 'xotevey773', 'muthukumaran2026@gmail.com', 'Muthu77');

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
CREATE TABLE IF NOT EXISTS `product` (
  `prod_id` int(255) NOT NULL,
  `prod_name` varchar(255) NOT NULL,
  `place` varchar(255) NOT NULL,
  `qty` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`prod_id`, `prod_name`, `place`, `qty`) VALUES
(101, 'Laptop', 'Singapore ', 1145),
(102, 'Mobile', 'China ', 558),
(103, 'Printer', 'United State ', 440),
(104, 'PC', 'India ', 1785),
(104, 'PC', 'China ', 60),
(101, 'Laptop', 'India ', 230),
(102, 'Mobile', 'India ', 150),
(103, 'Printer', 'India ', 150),
(101, 'Laptop', 'China ', 100),
(103, 'Printer', 'China ', 60),
(102, 'Mobile', 'Singapore ', 12),
(103, 'Printer', 'Singapore ', 50),
(104, 'PC', 'Singapore ', 155),
(101, 'Laptop', 'United State ', 25),
(102, 'Mobile', 'United State ', 30);

-- --------------------------------------------------------

--
-- Table structure for table `product_movement`
--

DROP TABLE IF EXISTS `product_movement`;
CREATE TABLE IF NOT EXISTS `product_movement` (
  `movementid` int(255) NOT NULL AUTO_INCREMENT,
  `timestamp` date NOT NULL,
  `from_location` varchar(255) NOT NULL,
  `to_location` varchar(255) NOT NULL,
  `product_id` int(255) NOT NULL,
  `qty` int(255) NOT NULL,
  PRIMARY KEY (`movementid`)
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `product_movement`
--

INSERT INTO `product_movement` (`movementid`, `timestamp`, `from_location`, `to_location`, `product_id`, `qty`) VALUES
(57, '2020-10-11', 'India ', 'China ', 104, 60),
(58, '2020-10-11', 'Singapore ', 'India ', 101, 250),
(59, '2020-10-11', 'China ', 'India ', 102, 150),
(60, '2020-10-11', 'United State ', 'India ', 103, 150),
(61, '2020-10-11', 'Singapore ', 'China ', 101, 100),
(62, '2020-10-11', 'United State ', 'China ', 103, 60),
(63, '2020-10-11', 'India ', 'Singapore ', 101, 20),
(64, '2020-10-11', 'China ', 'Singapore ', 102, 12),
(65, '2020-10-11', 'United State ', 'Singapore ', 103, 50),
(66, '2020-10-11', 'India ', 'Singapore ', 104, 155),
(67, '2020-10-11', 'Singapore ', 'United State ', 101, 25),
(68, '2020-10-11', 'China ', 'United State ', 102, 30);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
