import os

token = os.getenv('YOUR_TOKEN_ENV_VARIABLE')

if __name__ == '__main__':
    # Your existing code here, but using 'token' where needed
    print('Token loaded from environment variable')