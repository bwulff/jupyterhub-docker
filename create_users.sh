#!/bin/bash

# Create admin user if it doesn't exist
if ! id -u admin > /dev/null 2>&1; then
    useradd -m -s /bin/bash admin
    echo "admin:admin" | chpasswd
    echo "Admin user created"
fi

NUM_USERS=20  
for i in $(seq 1 "$NUM_USERS"); do
    USERNAME="group${i}"
    #PASSWORD=$(openssl rand -base64 16 | tr -dc 'a-zA-Z0-9' | head -c 5)
    PASSWORD="pass${i}"
    useradd -m -s /bin/bash "$USERNAME"
    echo "${USERNAME}:${PASSWORD}" | chpasswd
    echo "Created user: $USERNAME | Password: $PASSWORD"
done
echo "$NUM_USERS user(s) created."
