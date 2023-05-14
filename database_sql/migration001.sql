-- Initial table creation

-- Users table
CREATE TABLE `user` (
    `id` BIGINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    `email` VARCHAR(50) UNIQUE NOT NULL,
    `password` VARCHAR(500),
    `otp_secret` CHAR(16),
    `is_admin` BOOL NOT NULL DEFAULT FALSE,
	-- personal info (i.e. that of school)
	`name` VARCHAR(50),
	`qualification` VARCHAR(50)
);

-- Schools table
CREATE TABLE `school` (
	`id` BIGINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
	`name` VARCHAR(50) NOT NULL,
	`aff_no` INT UNIQUE NOT NULL,
	`schoolcode` INT UNIQUE NOT NULL,
	`address` VARCHAR(75) NOT NULL,
	`phone` VARCHAR(15) NOT NULL,
	`principal` BIGINT UNSIGNED NOT NULL UNIQUE,
	CONSTRAINT FK_School_User FOREIGN KEY (`principal`)
	REFERENCES `user`(`id`)
);

-- Exams TABLE
CREATE TABLE `board_ay` (
	`id` BIGINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
	`exam_yr` YEAR NOT NULL,
	`std` TINYINT(2) NOT NULL,
	`parse_engine` VARCHAR(100)
);

-- CBSE subjects
CREATE TABLE `subject` (
	`id` BIGINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
	`subcode` SMALLINT(3) UNSIGNED ZEROFILL NOT NULL,
	`subname` VARCHAR(50) NOT NULL,
	`std` TINYINT(2) NOT NULL
);

-- CBSE Board Exam Students TABLE
CREATE TABLE `student` (
	`id` BIGINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
	`board_ay` BIGINT UNSIGNED NOT NULL,
	`school` BIGINT UNSIGNED NOT NULL,
	`gender` ENUM("M", "F"),
	`name` VARCHAR(50) NOT NULL,
	`passcode` VARCHAR(500), -- optional
	`result` VARCHAR(5),
	`cache_total` INT,
	`cache_rank` INT,
	CONSTRAINT FK_Student_BoardAY FOREIGN KEY (`board_ay`)
	REFERENCES `board_ay`(`id`) 
	ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT FK_Student_School FOREIGN KEY (`school`)
	REFERENCES `school`(`id`) 
	ON UPDATE CASCADE ON DELETE CASCADE	
);

-- CBSE Board exam Subject Mark table
CREATE TABLE `subject_mark` (
	`id` BIGINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
	`student` BIGINT UNSIGNED NOT NULL,
	`subject` BIGINT UNSIGNED NOT NULL,
	`marks` TINYINT(3) UNSIGNED,
	CHECK(0 <= `marks` AND `marks` <= 100),
	CONSTRAINT FK_SubjectMark_Student FOREIGN KEY (`student`)
	REFERENCES `student`(`id`),
	CONSTRAINT FK_SubjectMark_Subject FOREIGN KEY (`subject`)
	REFERENCES `subject`(`id`) 
);

-- File
CREATE TABLE `file` (
	`id` BIGINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
	`filename` VARCHAR(50),
	`mimetype` VARCHAR(50) NOT NULL,
	`created` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	`modified` TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	`user` BIGINT UNSIGNED,
	CONSTRAINT FK_File_User FOREIGN KEY (`user`)
	REFERENCES `user`(`id`)
);