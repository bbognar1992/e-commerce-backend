# E-commerce Backend Application

Welcome to the E-commerce Backend Application! This project prototype project to show how I write code. Below, you will find details on the available API endpoints and how to interact with them.

## Table of Contents

- [Introduction](#introduction)
- [APIs](#apis)
  - [User Endpoints](#user-endpoints)
    - [Register a User](#post-userregistration)
    - [Login a User](#post-userlogin)
    - [Get User Information](#get-userme)
    - [Delete User Account](#delete-userme)
  - [Product Endpoints](#product-endpoints)
    - [Create a Product](#post-product)
    - [Get Product Details](#get-productsid)
    - [Update Product Details](#patch-productsid)
    - [Delete a Product](#delete-productsid)
- [Getting Started](#getting-started)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The E-commerce Backend Application is designed to handle user authentication and product management for an e-commerce platform. It includes endpoints for user registration, login, retrieving user details, and CRUD operations for products.

## APIs

### User Endpoints

![apis.png](assets%2Fapis.png)

#### POST /api/v1/user/registration

Register a new user.

**Request Body:**
```json
{
  "email": "string",
  "username": "string",
  "is_superuser": false,
  "is_active": true,
  "password": "string"
}
```

**Response:**
```json
{
  "email": "string",
  "username": "string",
  "is_superuser": false,
  "is_active": true,
  "id": "string"
}
```

#### POST /api/v1/user/login

Authenticate a user.

**Request Body:**
```json
{
  "username": "string",
  "password": "string"
}
```

**Response:**
```json
{
  "access_token": "string", "token_type": "bearer"
}
```

#### GET /api/v1/user/me

Retrieve authenticated user's information.

**Headers:**
```json
{
  "Authorization": "Bearer token"
}
```

**Response:**
```json
{
  "userId": "string",
  "username": "string",
  "email": "string"
}
```

#### DELETE /api/v1/user/me

Delete the authenticated user's account.

**Headers:**
```json
{
  "Authorization": "Bearer token"
}
```

**Response:**
```json
{
  "message": "User account deleted successfully"
}
```

### Product Endpoints

#### POST /api/v1/product

Create a new product.

**Request Body:**
```json
{
  "name": "string",
  "description": "string",
  "price": "number",
  "stock": "number"
}
```

**Response:**
```json
{
  "message": "Product created successfully",
  "productId": "string"
}
```

#### GET /api/v1/products/{id}

Get details of a specific product.

**Path Parameters:**
- `id`: The unique identifier of the product.

**Response:**
```json
{
  "productId": "string",
  "name": "string",
  "description": "string",
  "price": "number",
  "stock": "number"
}
```

#### PATCH /api/v1/products/{id}

Update details of a specific product.

**Path Parameters:**
- `id`: The unique identifier of the product.

**Request Body:**
```json
{
  "name": "string",
  "description": "string",
  "price": "number",
  "stock": "number"
}
```

**Response:**
```json
{
  "message": "Product updated successfully"
}
```

#### DELETE /api/v1/products/{id}

Delete a specific product.

**Path Parameters:**
- `id`: The unique identifier of the product.

**Response:**
```json
{
  "message": "Product deleted successfully"
}
```

## Getting Started

To get started with the E-commerce Backend Application, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/bbognar1992/e-commerce-backend.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ecommerce-backend
   ```
3. Set up a virtual environment:
   ```bash
   docker compose up -d
   ```

## Technologies Used
- Postgres
- Python
- FastAPI
- SQLAlchemy (or your preferred ORM)
- JWT for authentication

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to reach out if you have any questions or need further assistance. Happy coding! 🚀
<a href="mailto:bbognar0209©gmail.com">bbognar0209©gmail.com</a>