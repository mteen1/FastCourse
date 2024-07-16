
## API Endpoints

Below is an image showing all available API endpoints:

![API Endpoints](./path/to/image.png)

### Users

- **GET /users**: Read Users
- **POST /users**: Create New User
- **GET /users/{user_id}**: Read User
- **GET /users/{user_id}/courses**: Read User Courses

### Courses

- **GET /courses**: Read Courses
- **POST /courses**: Create New Course
- **GET /courses/{course_id}**: Read Course
- **PATCH /courses/{course_id}**: Alter Course
- **DELETE /courses/{course_id}**: Remove Course
- **GET /courses/{course_id}/sections**: Read Course Sections

### Sections

- **GET /sections/{id}**: Read Section
- **PATCH /sections/{id}**: Update Section Endpoint
- **DELETE /sections/{id}**: Delete Section Endpoint
- **POST /sections**: Create New Section
- **GET /sections/{section_id}/content-blocks**: Read Section Content Blocks

### Content Blocks

- **GET /content-blocks/{id}**: Read Content Block
- **PATCH /content-blocks/{id}**: Update Content Block Endpoint
- **DELETE /content-blocks/{id}**: Delete Content Block Endpoint
- **POST /content-blocks**: Create New Content Block

## Example Usage

### Creating a New Course

To create a new course, use the following endpoint:

```http
POST /courses
Content-Type: application/json

{
  "title": "Introduction to AI",
  "description": "A beginner's course on AI.",
  "user_id": 1
}
```

### Reading All Courses

To read all courses, use the following endpoint:

```http
GET /courses
```

### Updating a Course

To update a course, use the following endpoint:

```http
PATCH /courses/{course_id}
Content-Type: application/json

{
  "title": "Introduction to AI - Updated",
  "description": "An updated beginner's course on AI."
}
```

### Deleting a Course

To delete a course, use the following endpoint:

```http
DELETE /courses/{course_id}
```
