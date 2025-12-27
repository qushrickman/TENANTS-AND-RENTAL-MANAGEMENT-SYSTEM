	# TENANTS-AND-RENTAL-MANAGEMENT-SYSTEM

this is a system that will be used by both landlords and tenants to access the personal rent status and statements

Tenants and Rental Management System (API)
This is a secure django API for managing tenants, rent, payments, and late fees.
This project is designed for landlords to manage rental operations and for tenants to securely view their rent status and payment history.

Main Features
Authentication & Authorization
JWT-based authentication 
User registration and login
Role-based access control: Landlord ,Tenant

Tenant Management (Landlord Only)
Create, view, update, and delete tenants
View tenant details

Rent Management
Assign rent to tenants
Track rent amount, due dates, and status
Tenants can only view their own rent records

Payment Tracking
Record rent payments
View payment history
Tenants are restricted to their own payments
Late Fees
Track late fees for overdue rent
Restricted to landlord access
Project Structure
accounts = Authentication, profiles, permissions
tenants = Tenant management
billing = Rent, payments, late fees
README.md

Project Models
Profile: LANDLORD | TENANT
Rent - amount, due date, status
Payment - amount, payment date
Late Fee - amount, applied date
Authentication

POST /api/auth/register/ - Register a landlord or tenant

POST /api/auth/login/ - Obtain JWT tokens

POST /api/auth/refresh/ - Refresh access token
	Tenants (Landlord Only)

GET /api/tenants/ - List all tenants

POST /api/tenants/ - Create a new tenant

GET /api/tenants/{id}/ - Retrieve tenant details

PUT /api/tenants/{id}/ - Update tenant information

DELETE /api/tenants/{id}/ - Delete a tenant
	Rent

GET /api/rents/
Landlord: View all rents
Tenant: View own rent only

POST /api/rents/
Landlord only: Create rent records

Payments
GET /api/payments/ - landlord View all payments
Tenant: View own payments only

POST /api/payments/
Landlord only: Record a payment
	Late Fees
GET /api/late-fees/ - Landlord only: View late fees

POST /api/late-fees/ - Landlord only: Create late fees
	















 Security
•	All protected endpoints require JWT authentication
•	Default permission: IsAuthenticated
•	Custom permissions enforce role-based access
•	Tenants are restricted to their own records only
Future Enhancements
•	Automated late fee calculation
•	Rent statements & financial reports
•	Email notifications
•	Front end
