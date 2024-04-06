#! /bin/bash
curl -X POST -H "Content-Type: application/json" -d '{
  "type": "win"
}' http://localhost:5000/create
