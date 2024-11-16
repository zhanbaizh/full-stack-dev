import requests

def fetch_post_by_id(post_id):
    """Fetches a post by its ID."""
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    
    try:
        # Send GET request
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            post = response.json()  # Parse JSON response
            print("Post Details:")
            print(f"ID: {post['id']}")
            print(f"Title: {post['title']}")
            print(f"Body: {post['body']}")
        elif response.status_code == 404:
            print("Post not found. Please check the ID and try again.")
        else:
            print(f"Failed to fetch post. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Ask the user for the post ID
    try:
        post_id = int(input("Enter the post ID: "))
        fetch_post_by_id(post_id)
    except ValueError:
        print("Invalid input. Please enter a numeric ID.")
