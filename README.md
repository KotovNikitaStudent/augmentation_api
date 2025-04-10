# Image Augmentation API

This API provides functionality for image augmentation (transformations within the framework of services related to storing multiple versions of processed images).  
Users can register, authenticate, upload images for processing, and view their operation history.

### Available image transformations:

- 90-degree rotation
- RGB to grayscale conversion
- 2x resizing with aspect ratio preservation

## Project Deployment Guide

### 1. Clone the Repository

Run the to get the source code:

```sh
git clone git@github.com:KotovNikitaStudent/augmentation_api.git
cd augmentation_api
```

### 2. Run with Docker Compose

Build and launch services in detached mode:

```sh
docker-compose up -d --build
```

### 3. Apply Database Migrations

To set up the database, execute:

```sh
docker-compose exec api sh
alembic upgrade head
```
