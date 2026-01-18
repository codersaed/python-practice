-- -------------------------
-- SQL(Tables)
-- -------------------------

-- 1) SubscriptionPlan
CREATE TABLE SubscriptionPlan (
    plan_id        INT UNSIGNED NOT NULL AUTO_INCREMENT,
    plan_name      VARCHAR(50) NOT NULL,
    price          DECIMAL(10,2) NOT NULL,
    duration_days  INT UNSIGNED NOT NULL,
    features       TEXT,
    PRIMARY KEY (plan_id),
    UNIQUE KEY uq_plan_name (plan_name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 2) Vendor / SubscriptionPlan)
CREATE TABLE Vendor (
    vendor_id         INT UNSIGNED NOT NULL AUTO_INCREMENT,
    business_name     VARCHAR(120) NOT NULL,
    contact_person    VARCHAR(100) NOT NULL,
    email             VARCHAR(120) NOT NULL,
    phone             VARCHAR(30),
    business_address  VARCHAR(200),
    plan_id           INT UNSIGNED NOT NULL,
    PRIMARY KEY (vendor_id),
    UNIQUE KEY uq_vendor_email (email),
    KEY idx_vendor_plan (plan_id),
    CONSTRAINT fk_vendor_plan
        FOREIGN KEY (plan_id) REFERENCES SubscriptionPlan(plan_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 3) Product (FK -> Vendor)
CREATE TABLE Product (
    product_id     INT UNSIGNED NOT NULL AUTO_INCREMENT,
    vendor_id      INT UNSIGNED NOT NULL,
    product_name   VARCHAR(120) NOT NULL,
    description    TEXT,
    price          DECIMAL(12,2) NOT NULL,
    stock_qty      INT NOT NULL DEFAULT 0,
    status         ENUM('active','inactive') NOT NULL DEFAULT 'active',
    PRIMARY KEY (product_id),
    KEY idx_product_vendor (vendor_id),
    KEY idx_product_name (product_name),
    CONSTRAINT fk_product_vendor
        FOREIGN KEY (vendor_id) REFERENCES Vendor(vendor_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 4) Category
CREATE TABLE Category (
    category_id   INT UNSIGNED NOT NULL AUTO_INCREMENT,
    name          VARCHAR(80) NOT NULL,
    description   TEXT,
    PRIMARY KEY (category_id),
    UNIQUE KEY uq_category_name (name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 5) ProductCategory junction 
CREATE TABLE ProductCategory (
    product_id   INT UNSIGNED NOT NULL,
    category_id  INT UNSIGNED NOT NULL,
    PRIMARY KEY (product_id, category_id),
    KEY idx_pc_category (category_id),
    CONSTRAINT fk_pc_product
        FOREIGN KEY (product_id) REFERENCES Product(product_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT fk_pc_category
        FOREIGN KEY (category_id) REFERENCES Category(category_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 6) Customer
CREATE TABLE Customer (
    customer_id  INT UNSIGNED NOT NULL AUTO_INCREMENT,
    name         VARCHAR(120) NOT NULL,
    email        VARCHAR(120) NOT NULL,
    phone        VARCHAR(30),
    address      VARCHAR(200),
    PRIMARY KEY (customer_id),
    UNIQUE KEY uq_customer_email (email),
    KEY idx_customer_name (name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 7) Orders (FK -> Customer)
CREATE TABLE Orders (
    order_id      INT UNSIGNED NOT NULL AUTO_INCREMENT,
    customer_id   INT UNSIGNED NOT NULL,
    order_date    DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    total_amount  DECIMAL(12,2) NOT NULL DEFAULT 0,
    status        ENUM('pending','confirmed','shipped','delivered','cancelled') NOT NULL DEFAULT 'pending',
    PRIMARY KEY (order_id),
    KEY idx_orders_customer (customer_id),
    KEY idx_orders_date (order_date),
    CONSTRAINT fk_orders_customer
        FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 8) OrderItem 
CREATE TABLE OrderItem (
    order_item_id  INT UNSIGNED NOT NULL AUTO_INCREMENT,
    order_id       INT UNSIGNED NOT NULL,
    product_id     INT UNSIGNED NOT NULL,
    quantity       INT UNSIGNED NOT NULL,
    unit_price     DECIMAL(12,2) NOT NULL,
    subtotal       DECIMAL(12,2) NOT NULL,
    PRIMARY KEY (order_item_id),
    UNIQUE KEY uq_order_product (order_id, product_id),
    KEY idx_item_order (order_id),
    KEY idx_item_product (product_id),
    CONSTRAINT fk_item_order
        FOREIGN KEY (order_id) REFERENCES Orders(order_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT fk_item_product
        FOREIGN KEY (product_id) REFERENCES Product(product_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 9) Payment
CREATE TABLE Payment (
    payment_id    INT UNSIGNED NOT NULL AUTO_INCREMENT,
    order_id      INT UNSIGNED NOT NULL,
    method        ENUM('Card','Bkash','PayPal','CashOnDelivery') NOT NULL,
    amount        DECIMAL(12,2) NOT NULL,
    payment_date  DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    status        ENUM('pending','paid','failed','refunded') NOT NULL DEFAULT 'pending',
    PRIMARY KEY (payment_id),
    UNIQUE KEY uq_payment_order (order_id),
    CONSTRAINT fk_payment_order
        FOREIGN KEY (order_id) REFERENCES Orders(order_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- (Setup) 
INSERT INTO SubscriptionPlan (plan_name, price, duration_days, features)
VALUES ('Basic', 999.00, 30, 'Basic features')
ON DUPLICATE KEY UPDATE
    price = VALUES(price),
    duration_days = VALUES(duration_days),
    features = VALUES(features);

-- Q5:  Basic plan
INSERT INTO Vendor (business_name, contact_person, email, phone, business_address, plan_id)
SELECT
    'SmartTech Ltd.',
    'Rahim Khan',
    'rahim@smarttech.com',
    '017XXXXXXXX',
    'Dhaka, Bangladesh',
    sp.plan_id
FROM SubscriptionPlan sp
WHERE sp.plan_name = 'Basic';

--  Electronics category
INSERT INTO Category (name, description)
VALUES ('Electronics', 'Electronic items and gadgets')
ON DUPLICATE KEY UPDATE
    description = VALUES(description);

-- Q6: Insert product "Laptop" for SmartTech Ltd.
INSERT INTO Product (vendor_id, product_name, description, price, stock_qty, status)
SELECT
    v.vendor_id,
    'Laptop',
    'General purpose laptop',
    75000.00,
    10,
    'active'
FROM Vendor v
WHERE v.business_name = 'SmartTech Ltd.';

-- Link Laptop to Electronics category in junction table
INSERT INTO ProductCategory (product_id, category_id)
SELECT
    p.product_id,
    c.category_id
FROM Product p
JOIN Vendor v ON v.vendor_id = p.vendor_id
JOIN Category c ON c.name = 'Electronics'
WHERE p.product_name = 'Laptop'
  AND v.business_name = 'SmartTech Ltd.'
ON DUPLICATE KEY UPDATE
    category_id = category_id;

-- Q7: Update stock quantity of Laptop to 15
UPDATE Product p
JOIN Vendor v ON v.vendor_id = p.vendor_id
SET p.stock_qty = 15
WHERE p.product_name = 'Laptop'
  AND v.business_name = 'SmartTech Ltd.';

-- Q8: Delete customer whose email is oldcustomer@gmail.com
DELETE FROM Customer
WHERE email = 'oldcustomer@gmail.com';


-- Q9: All vendors with their plan name and price
SELECT
    v.vendor_id,
    v.business_name,
    v.contact_person,
    sp.plan_name,
    sp.price
FROM Vendor v
JOIN SubscriptionPlan sp ON sp.plan_id = v.plan_id
ORDER BY v.vendor_id;

-- Q10: Products under category "Electronics" (name, price, stock)
SELECT
    p.product_name,
    p.price,
    p.stock_qty
FROM Product p
JOIN ProductCategory pc ON pc.product_id = p.product_id
JOIN Category c ON c.category_id = pc.category_id
WHERE c.name = 'Electronics'
ORDER BY p.product_name;

-- Q11: Orders placed by customer "Karim Uddin"
SELECT
    o.order_id,
    o.order_date,
    o.total_amount,
    o.status
FROM Orders o
JOIN Customer cu ON cu.customer_id = o.customer_id
WHERE cu.name = 'Karim Uddin'
ORDER BY o.order_date DESC;

-- Q12: Payment details for order_id = 1
SELECT
    method,
    amount,
    status
FROM Payment
WHERE order_id = 1;

-- Q13: Top 5 best-selling products by total quantity sold
SELECT
    pr.product_id,
    pr.product_name,
    SUM(oi.quantity) AS total_qty_sold
FROM OrderItem oi
JOIN Product pr ON pr.product_id = oi.product_id
GROUP BY pr.product_id, pr.product_name
ORDER BY total_qty_sold DESC
LIMIT 5;
