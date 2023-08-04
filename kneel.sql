
CREATE TABLE `Metal`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Order`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal_id` NVARCHAR(160) NOT NULL,
    `size_id` NVARCHAR(160) NOT NULL,
    `style_id` NUMERIC(160) NOT NULL,
    `timestamp` TIMESTAMP NOT NULL,
    FOREIGN KEY(`metal_id`) REFERENCES `Metal`(`id`),
    FOREIGN KEY(`size_id`) REFERENCES `Size`(`id`),
    FOREIGN KEY(`style_id`) REFERENCES `Style`(`id`)
);

CREATE TABLE `Size`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `carets` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(160) NOT NULL
);

CREATE TABLE `Style`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `style` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(160) NOT NULL
);

INSERT INTO `Metal` VALUES (null, 'Sterling Silver', 12.42);
INSERT INTO `Metal` VALUES (null, '14K Gold', 736.4);
INSERT INTO `Metal` VALUES (null, '24K Gold', 1258.9);
INSERT INTO `Metal` VALUES (null, 'Platinum', 795.45);
INSERT INTO `Metal` VALUES (null, 'Palladium', 1241);

INSERT INTO `Size` VALUES (null, 0.5, 405);
INSERT INTO `Size` VALUES (null, 0.75, 782);
INSERT INTO `Size` VALUES (null, 1, 1470);
INSERT INTO `Size` VALUES (null, 1.5, 1997);
INSERT INTO `Size` VALUES (null, 2, 3638);

INSERT INTO `Style`VALUES(NULL,'Classic', 500 );
INSERT INTO `Style`VALUES(NULL,'Modern', 710 );
INSERT INTO `Style`VALUES(NULL,'Vintage', 965 );

INSERT INTO `Order`VALUES (NULL, 3,2, 3, 1614659931693);
INSERT INTO `Order`VALUES (NULL, 1,1, 1, 1614659931694);
INSERT INTO `Order`VALUES (NULL, 2,3, 3, 1614659931695);
INSERT INTO `Order`VALUES (NULL, 3,2, 2, 1614659931696);


SELECT
    o.id,
    o.metal_id,
    o.size_id,
    o.style_id,
    o.timestamp,
    m.metal,
    m.price metal_price,
    st.style,
    st.price style_price,
    si.carets,
    si.price size_price
        -- You select the rest of the columns from the joined tables here
FROM `Order` o
JOIN Metal m ON m.id = o.metal_id
JOIN Style st ON st.id = o.style_id
JOIN Size si ON si.id = o.size_id