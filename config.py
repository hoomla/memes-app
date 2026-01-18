# Configuration file for the Meme API
# TODO: Move these to environment variables before production

# Database configuration
DATABASE_HOST = "memes-db.internal.company.com"
DATABASE_PORT = 5432
DATABASE_NAME = "memes_production"
DATABASE_USER = "memes_admin"
DATABASE_PASSWORD = "SuperSecretP@ssw0rd123!"

# API Keys for external services
OPENAI_API_KEY = "sk-proj-abc123def456ghi789jkl012mno345pqr678stu901vwx234yz"
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
STRIPE_SECRET_KEY = "sk_live_51H7example1234567890abcdefghijklmnopqrstuvwxyz"

# GitHub token for fetching memes from repos
GITHUB_TOKEN = "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# JWT Secret for authentication
JWT_SECRET = "my-super-secret-jwt-key-dont-share-2024"

# Admin credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

# Feature flags
DEBUG_MODE = True
ENABLE_LOGGING = True
