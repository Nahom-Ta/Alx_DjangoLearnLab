## POST /api/posts/{post_id}/comment/

- **Description**: Adds a comment to a post.
- **Request**:
  - **Method**: POST
  - **Body** (JSON):
    ```json
    {
        "comment_text": "This is a test comment"
    }
    ```
- **Response**:
  ```json
  {
      "id": 1,
      "post": 1,
      "text": "This is a test comment",
      "author": 1,
      "created_at": "2024-12-22T10:00:00Z"
  }
