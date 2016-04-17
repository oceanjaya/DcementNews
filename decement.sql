
CREATE TABLE `dcement_news`.`industry_news`
( `news_id` INT UNSIGNED NOT NULL AUTO_INCREMENT , `url` VARCHAR(100) NOT NULL , `time` VARCHAR(20) NULL , `title` VARCHAR(200) NOT NULL , `content` TEXT NOT NULL , PRIMARY KEY (`news_id`)) ENGINE = InnoDB;