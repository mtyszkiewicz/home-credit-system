select 
    row_number() over () as id,
    date(records.create_timestamp) as "date",
    to_char(records.create_timestamp, 'HH24:MI') as "time",
    users.id as user_id,
    activities.id as activity_id
    {# users.name as user_name,
    users.color as user_color,
    activities.name as activity_name,
    activities.icon as activity_icon,
    activities.value as activity_value #}
from {{ source('raw', 'activity_records') }} records
inner join {{ source('raw', 'users') }} users
    on records.user_id = users.id
inner join {{ source('raw', 'activities') }} activities
    on records.activity_icon = activities.icon 
    and records.create_timestamp >= activities.start_date
    and records.create_timestamp < activities.end_date
order by
    records.create_timestamp desc