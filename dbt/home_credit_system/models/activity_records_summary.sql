with activity_statistics as (
    select 
        users.id as user_id,
        {# users.name as user_name,
        users.color as user_color,
        activities.name as activity_name,
        activities.icon as activity_icon, #}
        activities.id as activity_id,
        sum(activities.value) as activity_value,
        count(activities.value) as activity_count
    from {{ source('raw', 'activity_records_new') }} records
    inner join {{ source('raw', 'users_new') }} users
        on records.user_id = users.id
    inner join {{ source('raw', 'activities') }} activities
        on records.activity_icon = activities.icon 
        and records.create_timestamp >= activities.start_date
        and records.create_timestamp < activities.end_date
    group by
        users.id, activities.id
)

select
    user_id,
    activity_id,
    activity_value,
    activity_count,
    sum(activity_value) over (partition by user_id) as user_total_score
from
    activity_statistics
order by
    user_total_score desc, activity_value desc
