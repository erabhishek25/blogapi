# Blog Post API

This project is a Django REST Framework based API for managing blog posts. It includes functionalities for creating, retrieving, updating, and deleting blog posts, along with features for categorizing and tagging posts and commenting.

## Features

- **Create, Read, Update, Delete (CRUD) Operations** for blog posts.
- **Categories and Tags** for organizing and filtering posts.
- **Custom Validation** for ensuring unique titles and slugs.
- **Status Management** for post states such as draft, publish, and pending.

## Installation

### Prerequisites

- Python 3.8 or higher
- Django 4.x
- Django REST Framework
- Django Filter

### Setup

1. **Clone the repository**

    ```bash
    git clone https://github.com/erabhishek25/blogapi
    cd your-repository
    ```

2. **Create and activate a virtual environment**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply database migrations**

    ```bash
    python manage.py migrate
    ```

5. **Run the development server**

    ```bash
    python manage.py runserver
    ```

## API Endpoints

### Blog Posts

- **List Blog Posts**
  - `GET /posts/`
  - Retrieves a list of all blog posts.

- **Create Blog Post**
  - `POST /posts/`
  - Creates a new blog post.
  - **Request Body:**

    ```json
    {
      "title": "How to Use Django REST Framework",
      "content": "Detailed guide on Django REST Framework...",
      "categories": [{"name": "Technology"}],
      "tags": [{"name": "Django"}],
      "status": "publish"
    }
    ```

- **Retrieve Blog Post**
  - `GET /posts/{id}/`
  - Retrieves a single blog post by ID.

- **Update Blog Post**
  - `PUT /posts/{id}/`
  - Updates an existing blog post.
  - **Request Body:**

    ```json
    {
      "title": "Updated Title",
      "content": "Updated content...",
      "categories": [{"name": "Technology"}],
      "tags": [{"name": "Django"}],
      "status": "draft"
    }
    ```

- **Delete Blog Post**
  - `DELETE /posts/{id}/`
  - Deletes a blog post by ID.

### Categories Comming soon code

- **List Categories**
  - `GET /categories/`
  - Retrieves a list of all categories.

- **Create Category**
  - `POST /categories/`
  - Creates a new category.
  - **Request Body:**

    ```json
    {
      "name": "Programming",
      "description": "Posts related to programming and development."
    }
    ```

- **Retrieve Category**
  - `GET /categories/{id}/`
  - Retrieves a single category by ID.

- **Update Category**
  - `PUT /categories/{id}/`
  - Updates an existing category.
  - **Request Body:**

    ```json
    {
      "name": "Updated Category Name",
      "description": "Updated description."
    }
    ```

- **Delete Category**
  - `DELETE /categories/{id}/`
  - Deletes a category by ID.

### Tags

- **List Tags**
  - `GET /tags/`
  - Retrieves a list of all tags.

- **Create Tag**
  - `POST /tags/`
  - Creates a new tag.
  - **Request Body:**

    ```json
    {
      "name": "Django"
    }
    ```

- **Retrieve Tag**
  - `GET /api/tags/{id}/`
  - Retrieves a single tag by ID.

- **Update Tag**
  - `PUT /api/tags/{id}/`
  - Updates an existing tag.
  - **Request Body:**

    ```json
    {
      "name": "Updated Tag Name"
    }
    ```

- **Delete Tag**
  - `DELETE /api/tags/{id}/`
  - Deletes a tag by ID.

## Testing

To run the tests, use the following command:

```bash
python manage.py test
