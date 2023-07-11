# Data Model
![ERD diagram](../docs/hcs-erd.png)

## Endpoints

### GET `/auth?access_token=...`
User authentication and authorization endpoint. Provided valid *access_token* returns the user.
- Loads from <span style="color:lightgray">**users**</span>

### GET `/users`
Returns all users.
- Loads from <span style="color:lightgray">**users**</span>

### GET `/users/{user_id}`
Provided *user_id* returns the user.
- Loads from <span style="color:lightgray">**users**</span>

### POST `/users/{user_id}/activity_records`
Provided *user_id* and *activity_id* creates an activity record for the user.
- Updates <span style="color:lightgreen">**raw_activity_records**</span>

### GET `/activity_records`
Returns activity records history organized by day (date).
- Loads from <span style="color:lightgray">**activity_records_daily**</span>

### GET `/activity_summary`
REturns activity records aggregations by user.
- Loads <span style="color:lightgray">**activity_records_summary**</span>