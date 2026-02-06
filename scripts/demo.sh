#!/usr/bin/env bash
set -euo pipefail

IP="${1:-<EC2_PUBLIC_IP>}"
BASE="http://${IP}:8000/v1"
HDR="Content-Type: application/json"

echo "=== Bike Sharing — Assignment Service (2-minute demo) ==="
echo "BASE: $BASE"
echo

echo "1) Health"
curl -s "$BASE/health"; echo; echo

echo "2) Assign B1 -> U1"
ASSIGN_RESP=$(curl -s -X POST "$BASE/assign" -H "$HDR" \
  -d '{"user_id":"U1","bicycle_id":"B1"}')
echo "$ASSIGN_RESP"
ASSIGN_ID=$(echo "$ASSIGN_RESP" | sed -n 's/.*"assignment_id":"\([^"]*\)".*/\1/p')
echo "assignment_id=$ASSIGN_ID"
echo

echo "3) Conflict (same bike)"
curl -i -s -X POST "$BASE/assign" -H "$HDR" \
  -d '{"user_id":"U2","bicycle_id":"B1"}' | head -n 12
echo

echo "4) Bikes in use"
curl -s "$BASE/bikes-in-use"; echo; echo

echo "5) User bike"
curl -s "$BASE/user-bike/U1"; echo; echo

echo "6) Release"
curl -s -X POST "$BASE/release" -H "$HDR" \
  -d "{\"assignment_id\":\"$ASSIGN_ID\"}"; echo; echo

echo "7) Bikes in use (after release)"
curl -s "$BASE/bikes-in-use"; echo; echo

echo "=== Demo completed ==="
