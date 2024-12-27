-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8889
-- Erstellungszeit: 25. Dez 2024 um 11:54
-- Server-Version: 10.11.6-MariaDB
-- PHP-Version: 8.2.20

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

-- Sicherstellen, dass alle SET-Variablen mit MariaDB kompatibel sind
/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Datenbank: `Vino`
--

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `Kategorie`
--

CREATE DATABASE Vino;
USE Vino;

CREATE TABLE `Kategorie` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(265) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Daten für Tabelle `Kategorie`
--

INSERT INTO `Kategorie` (`ID`, `Name`) VALUES
(1, 'Example');

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `Produkt`
--

CREATE TABLE `Produkt` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `K_ID` int NOT NULL,
  `Name` varchar(256) NOT NULL,
  `MinTotal` int NOT NULL DEFAULT '0',
  `CurrentTotal` int NOT NULL DEFAULT '0',
  `ProductURL` varchar(256) NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `fk_produkt_kategorie` (`K_ID`),
  CONSTRAINT `fk_produkt_kategorie` FOREIGN KEY (`K_ID`) REFERENCES `Kategorie` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Daten für Tabelle `Produkt`
--

INSERT INTO `Produkt` (`ID`, `K_ID`, `Name`, `MinTotal`, `CurrentTotal`, `ProductURL`) VALUES
(2, 1, 'Example', 0, 3, 'product/example.jpg');

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `Spezifikation`
--

CREATE TABLE `Spezifikation` (
  `P_ID` int NOT NULL,
  PRIMARY KEY (`P_ID`),
  CONSTRAINT `fk_spezifikation_produkt` FOREIGN KEY (`P_ID`) REFERENCES `Produkt` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `Vorschlag`
--

CREATE TABLE `Vorschlag` (
  `P_ID` int NOT NULL,
  PRIMARY KEY (`P_ID`),
  CONSTRAINT `fk_vorschlag_produkt` FOREIGN KEY (`P_ID`) REFERENCES `Produkt` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
