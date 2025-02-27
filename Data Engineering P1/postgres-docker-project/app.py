import psycopg2
from psycopg2 import sql

#Database connection parameters
conn_params ={
    'dbname':'pdb1',
    'user':'admin',
    'password':'admin',
    'host':'localhost',
    'port':'5432'
}

#Connect to the PostgreSQL database
conn = psycopg2.connect(**conn_params)
cursor = conn.cursor()

#Create a Hotel Table
create_table_query_Hotel = """
CREATE TABLE IF NOT EXISTS Hotel (
    HotelID INT PRIMARY KEY,
    Name VARCHAR(255),
    Address VARCHAR(255),
    Phone VARCHAR(15),
    Email VARCHAR(255),
    Stars INT,
    CheckinTime TIME,
    CheckoutTime TIME
)
"""
cursor.execute(create_table_query_Hotel)
conn.commit()

#Insert Hotel data
insert_query_Hotel = sql.SQL("""
INSERT INTO Hotel (HotelID, Name, Address, Phone, Email, Stars, CheckinTime, CheckoutTime) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
""")

data_Hotel = [
    (1, 'Ocean Breeze Hotel', '123 Beach Road, Miami, FL', '+1-305-555-1234','info@oceanbreeze.com', 5, '3:00 PM', '11:00 AM'),
    (2, 'Grand Skyline Inn', '456 Main St, New York, NY', '+1-212-555-5678', 'contact@skylineinn.com', 4, '2:00 PM', '12:00 PM'),
    (3, 'Mountain View Lodge', '789 Hiltop Ave, Denver, CO', '+1-720-555-9012', 'booking@mv-lodge.com', 3, '4:00 PM', '10:00 AM'),
    (4, 'Sunset Paradise', '101 Sunset Blvd, Los Angeles, CA', '+1-213-555-3426', 'stay@sunsetparadise.com', 5, '3:30 PM', '11:30 AM'),
    (5, 'Green Leaf Resort', '222 Forest Lane, Seattle, WA', '+1-206-555-7890', 'reservations@greenleaf.com', 4, '2:30 PM', '12:00 PM')
]

cursor.executemany(insert_query_Hotel,data_Hotel)
conn.commit()

# Create a RoomType table
create_table_query_RoomType = """
CREATE TABLE IF NOT EXISTS RoomType (
    TypeID INT PRIMARY KEY,
    Name VARCHAR(50),
    Description VARCHAR(255),
    PricePerNight DECIMAL(10, 2),
    Capacity INT
);
"""
cursor.execute(create_table_query_RoomType)
conn.commit()

# Insert RoomType data
insert_query_RoomType = sql.SQL("""
INSERT INTO RoomType (TypeID, Name, Description, PricePerNight, Capacity) VALUES (%s, %s, %s, %s, %s);
""")

data_RoomType = [
    (1, 'Deluxe Suite', 'Spacious suite with ocean view and king-sized bed', 250.00, 2),
    (2, 'Standard Room', 'Cozy room with modern amenities and queen-sized bed', 150.00, 2),
    (3, 'Family Room', 'Large room with two double beds, perfect for families', 200.00, 4),
    (4, 'Penthouse Suite', 'Luxury suite with private balcony and hot tub', 500.00, 2),
    (5, 'Dormitory', 'Budget-friendly shared room with bunk beds', 50.00, 6),
    (6, 'Deluxe Suite', 'Spacious suite with ocean view and king-sized bed', 250.00, 2),
    (7, 'Standard Room', 'Cozy room with modern amenities and queen-sized bed', 150.00, 2),
    (8, 'Family Room', 'Large room with two double beds, perfect for families', 200.00, 4),
    (9, 'Penthouse Suite', 'Luxury suite with private balcony and hot tub', 500.00, 2),
    (10, 'Dormitory', 'Budget-friendly shared room with bunk beds', 50.00, 6)
]

cursor.executemany(insert_query_RoomType, data_RoomType)
conn.commit()

#Create a Room table
create_table_query_Room = """
CREATE TABLE IF NOT EXISTS Room (
    RoomNumber INT PRIMARY KEY,
    HotelID INT,
    TypeID INT,
    Status VARCHAR(20),
    FOREIGN KEY (HotelID) REFERENCES Hotel(HotelID),
    FOREIGN KEY (TypeID) REFERENCES RoomType(TypeID)
);
"""
cursor.execute(create_table_query_Room)
conn.commit()

# Insert Room data
insert_query_Room = sql.SQL("""
INSERT INTO Room (RoomNumber, HotelID, TypeID, Status) VALUES (%s, %s, %s, %s);
""")

data_Room = [
    (101, 1, 1, 'Available'),
    (102, 1, 2, 'Occupied'),
    (201, 2, 3, 'Available'),
    (202, 2, 4, 'Under Maintenance'),
    (301, 3, 5, 'Available'),
    (103, 1, 6, 'Available'),
    (104, 1, 7, 'Occupied'),
    (203, 2, 8, 'Available'),
    (204, 4, 9, 'Under Maintenance'),
    (302, 5, 10, 'Available')
]

cursor.executemany(insert_query_Room, data_Room)
conn.commit()



#Create a Guest table
create_table_query_Guest = """
CREATE TABLE IF NOT EXISTS Guest (
    GuestID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    DateOfBirth DATE,
    Address VARCHAR(255),
    Phone VARCHAR(15),
    Email VARCHAR(255)
);
"""
cursor.execute(create_table_query_Guest)
conn.commit()

# Insert Guest data
insert_query_Guest = sql.SQL("""
INSERT INTO Guest (GuestID, FirstName, LastName, DateOfBirth, Address, Phone, Email) VALUES (%s, %s, %s, %s, %s, %s, %s);
""")

data_Guest = [
    (1, 'John', 'Doe', '1985-06-15', '123 Maple St, New York, NY', '+1-212-555-7890', 'john.doe@example.com'),
    (2, 'Emma', 'Smith', '1992-09-23', '456 Oak Ave, Los Angeles, CA', '+1-310-555-1234', 'emma.smith@example.com'),
    (3, 'Michael', 'Brown', '1988-12-05', '789 Pine Rd, Chicago, IL', '+1-312-555-5678', 'michael.brown@example.com'),
    (4, 'Sophia', 'Johnson', '1995-04-18', '321 Cedar Blvd, Miami, FL', '+1-305-555-9012', 'sophia.johnson@example.com'),
    (5, 'David', 'Williams', '1980-07-30', '654 Birch Ln, Seattle, WA', '+1-206-555-3456', 'david.williams@example.com'),
    (6, 'Johnny', 'Doe', '1985-06-15', '123 Maple St, New York, NY', '+1-212-555-7890', 'john.doe@example.com'),
    (7, 'Emmily', 'Smith', '1992-09-23', '456 Oak Ave, Los Angeles, CA', '+1-310-555-1234', 'emma.smith@example.com'),
    (8, 'Mike', 'Brown', '1988-12-05', '789 Pine Rd, Chicago, IL', '+1-312-555-5678', 'michael.brown@example.com'),
    (9, 'Sophi', 'Johnson', '1995-04-18', '321 Cedar Blvd, Miami, FL', '+1-305-555-9012', 'sophia.johnson@example.com'),
    (10, 'Dave', 'Williams', '1980-07-30', '654 Birch Ln, Seattle, WA', '+1-206-555-3456', 'david.williams@example.com')
]


cursor.executemany(insert_query_Guest, data_Guest)
conn.commit()


#Create a Booking table
create_table_query_Booking = """
CREATE TABLE IF NOT EXISTS Booking (
    BookingID INT PRIMARY KEY,
    GuestID INT,
    RoomNumber INT,
    CheckinDate DATE,
    CheckoutDate DATE,
    TotalPrice DECIMAL(10, 2),
    FOREIGN KEY (GuestID) REFERENCES Guest(GuestID),
    FOREIGN KEY (RoomNumber) REFERENCES Room(RoomNumber)
);
"""
cursor.execute(create_table_query_Booking)
conn.commit()

# Insert Booking data
insert_query_Booking = sql.SQL("""
INSERT INTO Booking (BookingID, GuestID, RoomNumber, CheckinDate, CheckoutDate, TotalPrice) VALUES (%s, %s, %s, %s, %s, %s);
""")

data_Booking = [
    (1, 1, 101, '2025-03-10', '2025-03-15', 1250.00),
    (2, 2, 102, '2025-03-12', '2025-03-14', 300.00),
    (3, 3, 201, '2025-03-15', '2025-03-20', 1000.00),
    (4, 4, 202, '2025-03-18', '2025-03-22', 2000.00),
    (5, 5, 301, '2025-03-20', '2025-03-25', 250.00),
    (6, 6, 103, '2025-03-10', '2025-03-15', 12500.00),
    (7, 7, 104, '2025-03-12', '2025-03-14', 3000.00),
    (8, 8, 203, '2025-03-15', '2025-03-20', 10000.00),
    (9, 9, 204, '2025-03-18', '2025-03-22', 20000.00),
    (10, 10, 302, '2025-03-20', '2025-03-25', 2500.00)
]

cursor.executemany(insert_query_Booking, data_Booking)
conn.commit()



#Create a Payment table
create_table_query_Payment = """
CREATE TABLE IF NOT EXISTS Payment (
    PaymentID INT PRIMARY KEY,
    BookingID INT,
    Amount DECIMAL(10, 2),
    PaymentDate DATE,
    PaymentMethod VARCHAR(50),
    FOREIGN KEY (BookingID) REFERENCES Booking(BookingID)
);
"""
cursor.execute(create_table_query_Payment)
conn.commit()

# Insert Payment data
insert_query_Payment = sql.SQL("""
INSERT INTO Payment (PaymentID, BookingID, Amount, PaymentDate, PaymentMethod) VALUES (%s, %s, %s, %s, %s);
""")

data_Payment = [
    (1, 1, 1250.00, '2025-03-10', 'Credit Card'),
    (2, 2, 300.00, '2025-03-12', 'PayPal'),
    (3, 3, 1000.00, '2025-03-15', 'Debit Card'),
    (4, 4, 2000.00, '2025-03-18', 'Bank Transfer'),
    (5, 5, 250.00, '2025-03-20', 'Cash')
]


cursor.executemany(insert_query_Payment, data_Payment)
conn.commit()

#Retrieve some data 
select_query = "SELECT * FROM Payment;"
cursor.execute(select_query)
rows = cursor.fetchall()

print("Data in the Payment Table: ")
for row in rows:
    print(row)


#close the cursor and connection
cursor.close()
conn.close()