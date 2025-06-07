echo "Testing Redis..."
REDIS_PASSWORD=${REDIS_PASSWORD:-"StrongRedisPassword123!"}

if redis-cli -h redis -p 6379 -a "$REDIS_PASSWORD" ping; then
    echo "Connected to Redis!"
    redis-cli -h redis -p 6379 -a "$REDIS_PASSWORD" set test_key "Hello from Docker!"
    redis-cli -h redis -p 6379 -a "$REDIS_PASSWORD" get test_key
else
    echo "Redis connection failed."
    exit 1
fi