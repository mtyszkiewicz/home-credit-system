select 
    records.create_timestamp,
    users.image as user_image,
    users.color as user_color,
    activities.icon as activity_icon,
    activities.value as activity_value,
    sum(activities.value) over (
        partition by users.id 
        order by records.create_timestamp 
        rows between unbounded preceding and current row) as cumulative_score
from raw.activity_records records
inner join raw.users users
    on records.user_id = users.id
inner join raw.activities activities
    on records.activity_icon = activities.icon 
    and records.create_timestamp >= activities.start_date
    and records.create_timestamp < activities.end_date
order by
    records.create_timestamp desc