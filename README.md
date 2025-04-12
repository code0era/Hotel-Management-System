# 🏨 Hotel Management System

A comprehensive **Hotel Management System** built using **Python (Tkinter)** for the GUI and **MySQL** for database management. This project provides a complete digital solution for handling hotel operations such as customer registration, room booking, room inventory management, and billing.

## 📌 Features

### 💼 Customer Management
- Auto-generated reference number for each customer
- Full personal detail entry with ID proof handling
- Search, filter, update, and delete customer records

### 🛏️ Room Booking
- Integration with customer and room databases
- Automatic bill generation including tax
- Meal plan options (Breakfast, Lunch, Dinner)
- Real-time room availability check
- Stay duration calculation

### 🧾 Room Inventory Management
- Add, update, or remove rooms from inventory
- Categorize rooms by type (SINGLE, DOUBLE, LUXURY)
- Floor-based room management

### 🔍 Search System
- Multi-filter search across customer and booking records
- Instant, real-time result display

### 📇 Contact Module
- Displays hotel contact info with animated effects
- Company branding and logo display

---

## 🛠️ Tech Stack

- **Frontend**: Python `Tkinter` (GUI)
- **Backend**: Python
- **Database**: MySQL
- **Tools Used**: MySQL Workbench

---

## 📂 Project Structure


---

## 🗃️ Database Design

### Tables

#### `customer`
| Field        | Type        | Description               |
|--------------|-------------|---------------------------|
| Ref (PK)     | VARCHAR     | Unique customer ID        |
| Name         | VARCHAR     | Customer name             |
| Mother       | VARCHAR     | Mother's name             |
| Gender       | VARCHAR     | Gender                    |
| PostCode     | VARCHAR     | Postal code               |
| Mobile       | VARCHAR     | Mobile number             |
| Email        | VARCHAR     | Email address             |
| Nationality  | VARCHAR     | Nationality               |
| IdProof      | VARCHAR     | Type of ID provided       |
| IdNumber     | VARCHAR     | ID number                 |
| Address      | TEXT        | Full address              |

#### `details` (Room Details)
| Field        | Type        | Description               |
|--------------|-------------|---------------------------|
| floor        | INT         | Floor number              |
| roomno (PK)  | VARCHAR     | Unique room number        |
| roomType     | VARCHAR     | Room type (e.g. SINGLE)   |

#### `room` (Room Booking)
| Field        | Type        | Description               |
|--------------|-------------|---------------------------|
| contact (FK) | VARCHAR     | Linked to customer mobile |
| checkinDate  | DATE        | Check-in date             |
| checkoutDate | DATE        | Check-out date            |
| roomType     | VARCHAR     | Type of room              |
| room         | VARCHAR     | Room number               |
| meal         | VARCHAR     | Meal plan                 |
| noOfDays     | INT         | Number of stay days       |

---

## 🔐 Error Handling

- Input validation with user-friendly error messages
- Try-except blocks for database operations
- Graceful handling of unexpected errors
- Transaction management (commit/rollback)

---

## 🎯 Conclusion

This Hotel Management System demonstrates:
- Real-world business logic implementation
- Clean separation of concerns via a three-tier architecture
- Integration of GUI and database for an end-to-end software solution
- Scalable and user-friendly interface

---

## 🚀 Getting Started

### Requirements

- Python 3.x
- MySQL Server
- MySQL Connector (`pip install mysql-connector-python`)

### Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/hotel-management-system.git
   cd hotel-management-system
