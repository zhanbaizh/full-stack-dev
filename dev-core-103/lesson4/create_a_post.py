import requests

def create_post(title, body, user_id):
    """Creates a new post by sending a POST request."""
    url = "https://jsonplaceholder.typicode.com/posts"
    data = {
        "title": title,
        "body": body,
        "userId": user_id
    }

    try:
        # Send POST request
        response = requests.post(url, json=data)

        # Check if the request was successful
        if response.status_code == 201:  # HTTP 201 Created
            post = response.json()  # Parse the response JSON
            print("Post created successfully!")
            print(f"Post ID: {post['id']}")
            print(f"Title: {post['title']}")
            print(f"Body: {post['body']}")
            print(f"User ID: {post['userId']}")
        else:
            print(f"Failed to create post. Status code: {response.status_code}")
            print(f"Response: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Create a New Post")
    title = input("Enter the title: ").strip()
    body = input("Enter the body: ").strip()

    try:
        user_id = int(input("Enter the user ID: "))
        create_post(title, body, user_id)
    except ValueError:
        print("Invalid input. User ID must be a number.")
