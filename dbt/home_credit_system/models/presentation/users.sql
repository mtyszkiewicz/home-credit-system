select 
    users.id as id,
    users.name as name,
    users.image as image,
    users.color as color,
    users.access_token,
    sum(activities.value) as score
from {{ source('raw', 'activity_records') }} records
inner join {{ source('raw', 'users') }} users
    on records.user_id = users.id
inner join {{ source('raw', 'activities') }} activities
    on records.activity_icon = activities.icon 
    and records.create_timestamp >= activities.start_date
    and records.create_timestamp < activities.end_date
group by
    users.id, users.name, users.image, users.color, users.access_token